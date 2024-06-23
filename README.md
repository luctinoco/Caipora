# Pylands-Learn-Apply

## Landscape Metrics Analysis Tool for Public Health Applications

This Python script serves as a comprehensive toolset designed for postgraduate students in geoprocessing, specifically tailored for public health applications. It facilitates the analysis of landscape metrics from raster data, providing interactive visualizations and saving outputs for further analysis.

## Overview

The script leverages various Python libraries to manage raster data, compute landscape metrics, create interactive maps, and handle data formats:

### Packages Used:

- **pylandstats:** Computes landscape metrics like class area, edge density, and shape index.
- **openpyxl:** Reads Excel files to define colors for raster classes.
- **rasterio:** Manipulates raster data by loading arrays and transforming coordinates.
- **folium:** Generates interactive maps in HTML format.
- **numpy:** Facilitates numerical operations on arrays.
- **matplotlib:** Specifically uses ListedColormap for customizing plot colors.

### Functions Defined:

- **setup_environment():** Ensures all required Python packages are installed, making the script easy to set up for newcomers.
  
- **calculate_save_metrics_and_plot(input_file, output_file, color_excel, nodata_value=0):**
  - Loads raster data using rasterio and computes landscape metrics via pylandstats.
  - Saves metrics to a CSV file ('metrics_output.csv').
  - Reads a color legend from an Excel file ('color_data.xlsx') to assign colors to raster classes.
  - Creates a custom colormap based on the defined colors.
  - Generates an interactive map using folium, saved as an HTML file ('map_output.html').

### Example Usage:

To use the script:

1. Replace 'your_raster.tif' with your raster file path.
2. Ensure 'color_data.xlsx' follows the required format (Class ID and Color columns).
3. Execute the script to compute metrics, save outputs, and create an interactive map.

### Outputs:

- **Metrics Output ('metrics_output.csv'):** Contains calculated landscape metrics.
- **Interactive Map Output ('map_output.html'):** Visualizes raster data with assigned colors.

## Usage

### Setup:

- Ensure Python and required packages (pylandstats, openpyxl, rasterio, folium) are installed.
- Run setup_environment() to install any missing packages.

### Running the Script:

1. Adjust `input_file`, `output_file`, and `color_excel` variables according to your data.
2. Execute the script (`python script_name.py`).

### Viewing Outputs:

- Check 'metrics_output.csv' for metrics data.
- Open 'map_output.html' in a web browser to interact with the map.

## Notes:

- This script emphasizes simplicity and educational value, aiming to be accessible for students new to Python.
- As the author, I welcome discussions on improving the script while preserving its educational intent.
- This script provides foundational tools for landscape analysis relevant to public health, facilitating rapid and meaningful exploration of landscape metrics. For detailed guidance on customization or further functionality, refer to the documentation of each Python package used.

Happy coding!

Lucas F. T. Leonardo
