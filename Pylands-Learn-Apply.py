import subprocess  # Import subprocess module to run shell commands
import pylandstats as pls  # Import pylandstats for landscape analysis
import pandas as pd  # Import pandas for data manipulation
import rasterio  # Import rasterio for raster data handling
import folium  # Import folium for interactive maps
import numpy as np  # Import numpy for numerical operations
from matplotlib.colors import ListedColormap  # Import ListedColormap for custom colormaps


# Function to check and install necessary packages
def setup_environment():
    def check_install(package):
        try:
            __import__(package)  # Try to import the package
            print(f'{package} already installed.')  # Print message if already installed
        except ImportError:
            print(f'{package} not installed. Installing {package}...')  # Print message if not installed
            subprocess.check_call(['pip', 'install', package])  # Use subprocess to install package

    # List of necessary packages
    packages = ['pylandstats', 'openpyxl', 'rasterio', 'folium']

    # Check and install each package
    for package in packages:
        check_install(package)


# Function to calculate and save landscape metrics and plot the raster interactively
def calculate_save_metrics_and_plot(input_file, output_file, color_excel, nodata_value=0):
    # Load raster data and calculate metrics using pylandstats
    ls = pls.Landscape(input_file, nodata=nodata_value)
    metrics_df = ls.compute_class_metrics_df().to_csv(output_file, sep='\t', encoding='utf-8')

    # Read color legend Excel file using pandas
    color_df = pd.read_excel(color_excel)
    color_map = {row['Class_ID']: row['Color'] for _, row in color_df.iterrows()}

    # Load raster data using rasterio
    with rasterio.open(input_file) as src:
        bounds = src.bounds
        raster_array = src.read(1)
        transform = src.transform

    # Create a custom colormap based on colors from the legend
    unique_classes = np.unique(raster_array)
    colormap = np.zeros((256, 4), dtype=int)
    for class_id, color in color_map.items():
        hex_color = color.lstrip('#')
        rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        colormap[class_id] = (*rgb, 255)  # Add alpha channel

    colormap = ListedColormap([tuple(c / 255 for c in colormap[i]) for i in range(256)])

    # Create folium map centered on raster data bounds
    m = folium.Map([((bounds.top + bounds.bottom) / 2), ((bounds.left + bounds.right) / 2)], zoom_start=10)

    # Add raster data overlay to the map
    folium.raster_layers.ImageOverlay(
        image=raster_array,
        bounds=[[bounds.bottom, bounds.left], [bounds.top, bounds.right]],
        colormap=lambda x: colormap.colors[x],
        opacity=0.6
    ).add_to(m)

    # Add zoom control to the map
    folium.LayerControl().add_to(m)

    # Display the map
    return m


# Execute setup_environment function to ensure required packages are installed
setup_environment()

# Example usage:
input_raster = 'your_raster.tif'
output_file = 'metrics_output.csv'
color_excel = 'color_data.xlsx'  # Assumes this is an Excel file with required format

# Call the function to perform calculations, save metrics, and plot raster
m = calculate_save_metrics_and_plot(input_raster, output_file, color_excel)

# Save the interactive map as HTML
html_output = 'map_output.html'
m.save(html_output)
print(f'Map saved to {html_output}')

# Print success message after saving metrics to CSV
print(f'Metrics saved to {output_file}')

# Print completion message
print('Process completed successfully.')

# Display the interactive map in Jupyter Notebook or Google Colab
m