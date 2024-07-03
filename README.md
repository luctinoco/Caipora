# Pylands-Learn-Apply

## Landscape Metrics Analysis Tool for Public Health Applications

Pylands-Learn-Apply is a Python script designed for postgraduate students in public health applications. It facilitates the analysis of landscape metrics from raster data, enabling interactive visualizations and saving outputs for further analysis.

## Overview

This script leverages various Python libraries to manage raster data, compute landscape metrics, create interactive maps, and handle data formats:

### Libraries Used:

- **[pylandstats](https://pylandstats.readthedocs.io/en/latest/landscape.html):** Computes landscape metrics such as class area, edge density, and shape index.
- **[openpyxl](https://openpyxl.readthedocs.io/en/stable/):** Reads Excel files to define colors for raster classes.
- **[rasterio](https://rasterio.readthedocs.io/en/latest/):** Handles raster data by loading arrays and transforming coordinates.
- **[folium](https://python-visualization.github.io/folium/):** Generates interactive maps in HTML format.
- **[numpy](https://numpy.org/):** Supports numerical operations on arrays.
- **[geopandas](https://geopandas.org/):** Provides spatial operations and data structures.
- **[matplotlib](https://matplotlib.org/):** Generates plots and visualizations.
- **[shapely](https://shapely.readthedocs.io/en/stable/):** Manipulates and analyzes geometric objects.
- **[IPython](https://ipython.org/), [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/):** Enables interactive computing and widgets for data visualization.

## Functions Implemented:

### `setup_environment()`

Ensures all required Python packages are installed, simplifying setup for new users.

### `calculate_save_metrics_and_plot(input_raster, output_folder, output_base_name, color_excel, nodata_value=0)`

- Loads raster data using rasterio and computes landscape metrics via pylandstats.
- Saves metrics to a CSV file (`{output_base_name}_metrics_output.csv`).
- Reads a color legend from an Excel file (`color_excel`) to assign colors to raster classes.
- Generates a raster plot using `matplotlib` and `GeoPandas`, allowing interactive legend customization.
- Creates an interactive pie chart based on selected metrics using `ipywidgets`.
- Generates an interactive map using folium, saved as an HTML file (`{output_base_name}_map_output.html`).

## Compatibility and Adaptation

While originally designed for land use and land cover rasters from platforms like MapBiomas, this script is modular and adaptable. It can process other raster types with appropriate adjustments to input parameters and data handling.

## Color Data File Requirements

To properly assign colors to raster classes, ensure your color data file (`color_data.xlsx`) meets these requirements:

1. **Excel File Format**: Provide color data in an Excel (.xlsx) format.
   
2. **Sheet Structure**: The Excel file should have:
   - A sheet with columns containing headers.
   - A `Class_ID` column specifying unique identifiers for raster classes.
   - A `Color` column with hexadecimal color codes (e.g., `#RRGGBB`).

### Example of Color Data Sheet Structure:

| Class_ID | Color     |
|----------|-----------|
| 1        | #FF0000   |
| 2        | #00FF00   |
| 3        | #0000FF   |
| ...      | ...       |

For detailed legend codes from MapBiomas, you can visit their [legend code page](https://brasil.mapbiomas.org/codigos-de-legenda/).

## Running the Script

### Setup Instructions

1. **Clone Repository**: Clone the Pylands-Learn-Apply repository to your local machine or Google Colab.
   
2. **Run the Script**: Execute the script and follow prompts to input necessary file paths and parameters.

### Example Usage in Google Colab

To use this script in Google Colab, run this command in your Colab environment:

```bash
import os

# Check if the directory exists
if not os.path.exists("Pylands-Learn-Apply"):
    # Clone the repository if it doesn't exist
    !git clone https://github.com/luctinoco/Pylands-Learn-Apply.git

# Change into the directory
%cd Pylands-Learn-Apply

# Run the notebook
%run Pylands-Learn-Apply.ipynb
```
## This command does the following steps:

The command `git clone https://github.com/luctinoco/Pylands-Learn-Apply.git` downloads a repository from GitHub with the URL provided. Here's what each part does:

- `git clone`: This Git command is used to make a copy of a repository from a remote source (in this case, GitHub).
- `https://github.com/luctinoco/Pylands-Learn-Apply.git`: This is the URL of the repository you want to clone.

After cloning the repository, `%cd Pylands-Learn-Apply` changes the current directory to `Pylands-Learn-Apply`, assuming it exists in your current working directory.

Finally, `%run Pylands-Learn-Apply.ipynb` executes the Google Colab file `Pylands-Learn-Apply.ipynb`.

### Or click in this banner:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luctinoco/Pylands-Learn-Apply/blob/main/Clone_learn.ipynb)

### Follow these examples steps to execute the Pylands-Learn-Apply script:

1. **Path to Output Folder:**
   - Enter the path to the output folder where results will be saved: `/content/drive/My Drive/Output`
   - Provide the path to the folder where you want the results to be saved. If the folder does not exist, the script will create it automatically.

2. **Path to Raster File (`*.tif`):**
   - Enter the path to the input raster (.tif) file: `/content/drive/My Drive/raster_data.tif`
   - Provide the path to the raster file in `*.tif` format. The script will check if the file exists and has the correct extension.

3. **Path to Color Legend Excel File (`color_data.xlsx`):**
   - Input the path to the color legend Excel file in `*.xlsx` format.
   - The script will verify if the file exists and has the correct extension.

4. **Base Name for Output Files (without extension):**
   - Enter the base name for output files (without extension): `output_results`
   - Type a base name for the output files that will be generated by the script. This name will be used for the CSV metrics files and the HTML interactive map file.
  
## Example Usage:

If you specify `output_results` as your base name, your script might produce files like:
- `output_results_plot.png` (for the raster plot)
- `output_results_metrics.csv` (for metrics data)
- `output_results_map.html` (for an interactive map)

This naming convention makes it clear which files belong together and simplifies management and interpretation of your script’s outputs.

## Here is an example of a folder structure on Google Drive for use in Google Colab:

### Without outputs
```bash
/MyDrive/
    ├── MAPBIOMAS-EXPORT/
    │   ├── Legend-collection-8.xlsx
    │   ├── mapbiomas-brazil-collection-80-2022.tif
```


### With outputs
```bash
/MyDrive/
    ├── MAPBIOMAS-EXPORT/
    │   ├── Legend-collection-8.xlsx
    │   ├── mapbiomas-brazil-collection-80-2022.tif
    │   ├── base_Name_metrics_output.csv
    │   ├── base_name_raster_plot.png
    │   ├── base_name_raster_plot.png
    │   ├── base_name_map_output.html
```
    
## Base Name for Output Files (without extension):

When you provide a base name, such as `output_results`, it serves as a prefix for naming various output files generated by your script. Here’s how it applies:

1. **Raster Plot Title:**
   - The raster plot or map generated from your script might include a title or caption. This title could be automatically generated using the base name you provide. For example, if your base name is `output_results`, the title of the raster plot might be something like "Output Results".

2. **Other Output Files:**
   - Besides the raster plot, your script might generate other output files such as CSV files containing metrics or an HTML interactive map. These files could also use the base name to distinguish them. For instance, `output_results_metrics.csv` or `output_results_map.html`.

### Why Use a Base Name?

- **Consistency:** Using a base name ensures that all related output files are easily identifiable as belonging to the same run or batch of your script.
  
- **Automation:** It allows your script to generate output files without requiring manual naming each time, which can be error-prone and time-consuming.

- **Organizational:** Helps in organizing multiple runs or versions of your script, especially if you're running it multiple times with different inputs or parameters.

## Explain the Plots

The Pylands-Learn-Apply script generates several plots and visualizations based on the input raster data and color legend. Here’s an explanation of each plot:

### 1. Raster Plot

The raster plot visualizes the input raster data, where each pixel represents a different land cover or land use class. The plot uses colors specified in the color legend to differentiate between classes. Here’s what you can observe from the raster plot:

- **Color Representation:** Each class from the raster data is represented by a specific color, as defined in the `color_data.xlsx` file.
  
- **Spatial Distribution:** You can visually interpret the spatial distribution of different land cover types across the study area.
  
- **Legend:** The legend accompanying the plot explains the correspondence between colors and land cover classes, aiding in interpretation.

### 2. Interactive Map

The interactive map generated using folium provides an interactive visualization of landscape metrics computed from the raster data. Key features of the interactive map include:

- **Layer Control:** Users can toggle different layers to visualize specific metrics such as class area, edge density, or shape index.
  
- **Tooltip Information:** Hovering over map elements provides additional information such as metric values or class identifiers.
  
- **Export Functionality:** The map can be exported as an HTML file (`{output_base_name}_map_output.html`), allowing for easy sharing and integration into reports or presentations.

### 3. Pie Chart (Interactive)

An interactive pie chart generated using ipywidgets complements the raster plot by illustrating the distribution of selected landscape metrics across different land cover classes. Features of the pie chart include:

- **Metric Selection:** Users can select different metrics (e.g., class area, edge density) from a dropdown menu to visualize.
  
- **Dynamic Updates:** As metrics are selected or changed, the pie chart dynamically updates to reflect the proportion of each class contributing to the selected metric.

### 4. Metrics Output (CSV)

Metrics computed from the raster data are saved into a CSV file (`{output_base_name}_metrics_output.csv`). This file includes quantitative data such as:

- **Class Areas:** Area covered by each land cover class.
  
- **Edge Density:** Density of edges between different land cover classes.
  
- **Shape Index:** Measures of landscape shape complexity for each class.

### 5. Additional Plots (if applicable)

Depending on the metrics computed and the specific configuration of the script, additional plots such as histograms or scatter plots may be generated. These plots can provide further insights into the spatial patterns and characteristics of the landscape metrics.

### Interpretation and Application

- **Public Health Applications:** Understanding landscape metrics is crucial for assessing environmental factors that impact public health, such as urban heat islands or biodiversity conservation.
  
- **Policy and Planning:** Plots generated by Pylands-Learn-Apply aid policymakers and planners in making informed decisions regarding land use management and conservation strategies.
  
- **Research and Education:** These visualizations support research endeavors and educational purposes by providing clear, interpretable data representations.

By leveraging these plots and visualizations, users can gain valuable insights into landscape metrics derived from raster data, enhancing their understanding and decision-making processes in public health and environmental research.

## Handling Errors

### Error Messages for Incorrect Files

When running the script, you may encounter specific error messages if the files provided are incorrect or cannot be found:

1. **File Not Found Error:**
   - If the script cannot find the specified raster file (*.tif) or color data file (color_data.xlsx) in your Google Drive, it will raise a FileNotFoundError.
   - Example: 
     
FileNotFoundError: No .tif file found at the specified path: /content/drive/My Drive/incorrect_raster.tif


2. **Incorrect File Type Error:**
   - If the provided files do not match the expected file types (*.tif for raster and color_data.xlsx for color data), the script will raise an appropriate error.
   - Example:
     
ValueError: Incorrect file type provided. Expected *.tif raster file or color_data.xlsx Excel file.


3. **Other Errors:**
   - For any other unforeseen errors related to file reading, parsing, or processing, the script will raise informative error messages to guide troubleshooting.
   - Example:
     
IOError: Unable to read color data from color_data.xlsx. Please check the file format and contents.

### Troubleshooting Tips

- **Double-check File Paths:** Ensure that the paths provided to the raster file and color data file are correct and accessible in your Google Drive.
  
- **Verify File Formats:** Confirm that the raster file is in *.tif format and the color data file is in *.xlsx format with the required structure (Class_ID and Color columns).

- **Check File Permissions:** Make sure you have the necessary permissions to access and read the files from your Google Drive.

By following these guidelines and paying attention to error messages, you can effectively troubleshoot and resolve issues when using the Pylands-Learn-Apply script.

## Acknowledgments

We extend our gratitude to all contributors, past, present, and future, who help make this project a valuable resource for learners around the world. Together, we can empower the next generation of programmers and creators.

Don't forget to cite this repository if you use its code in your project.

Happy analyzing!

Lucas F. T. Leonardo
