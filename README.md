# Pylands-Learn-Apply

## Landscape Metrics Analysis Tool for Public Health Applications

This Python script provides a comprehensive toolset designed for postgraduate students in public health applications. It facilitates the analysis of landscape metrics from raster data, enabling interactive visualizations and saving outputs for further analysis.

## Overview

The script leverages various Python libraries to manage raster data, compute landscape metrics, create interactive maps, and handle data formats:

### Libraries Used:

- **pylandstats:** Computes landscape metrics such as class area, edge density, and shape index.
- **openpyxl:** Reads Excel files to define colors for raster classes.
- **rasterio:** Handles raster data by loading arrays and transforming coordinates.
- **folium:** Generates interactive maps in HTML format.
- **numpy:** Supports numerical operations on arrays.
- **matplotlib:** Specifically uses ListedColormap for customizing plot colors.

### Functions Implemented:

- **setup_environment():** Ensures all required Python packages are installed, simplifying setup for new users.
  
- **calculate_save_metrics_and_plot(input_file, output_file, color_excel, nodata_value=0):**
  - Loads raster data using rasterio and computes landscape metrics via pylandstats.
  - Saves metrics to a CSV file ('metrics_output.csv').
  - Reads a color legend from an Excel file ('color_data.xlsx') to assign colors to raster classes.
  - Creates a custom colormap based on the defined colors.
  - Generates an interactive map using folium, saved as an HTML file ('map_output.html').

### Example Usage:

To use the script:

1. Ensure your raster file ('.tif') and color data file ('.xlsx') are in the same directory as the script.
2. Execute the script to automatically detect and analyze the files.

## Color Data File Requirements

For the script to properly assign colors to raster classes, ensure your color data file (`color_data.xlsx`) meets the following requirements:

1. **Excel File Format**: The color data should be provided in an Excel (.xlsx) format.
   
2. **Sheet Structure**: The Excel file should contain a sheet with the necessary data. Ensure:
   - The sheet contains columns with headers.
   - One column should be named **"Class_ID"**: This column specifies the unique identifier for each raster class.
   - Another column should be named **"Color"**: This column specifies the color assigned to each raster class, represented in hexadecimal format (e.g., `#RRGGBB`).

3. **Color Format**: Colors in the "Color" column must be in hexadecimal format to ensure compatibility with plotting functions.

### Example of Color Data Sheet Structure:

| Class_ID | Color     |
|----------|-----------|
| 1        | #FF0000   |
| 2        | #00FF00   |
| 3        | #0000FF   |
| ...      | ...       |

### Notes:
- Ensure the `Class_ID` matches the class identifiers used in your raster data.
- `Color` are specified in hexadecimal format (e.g., `#RRGGBB`).

## Compatibility and Adaptation

While originally designed for land use and land cover rasters from the MapBiomas platform, this script is modular and adaptable. It can process other raster types with appropriate adjustments to input parameters and data handling.

### Usage on Google Colab

To use this project on Google Colab, click the badge below to open the notebook in Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luctinoco/Pylands-Learn-Apply/blob/main/notebooks/Pylands-Learn-Apply.ipynb)

### Getting Started in Google Colab

1. Open the notebook in Colab using the badge above.
2. Configure the environment by running the following cells at the beginning of the notebook:

   ```python
   !git clone https://github.com/luctinoco/Pylands-Learn-Apply.git
   %cd Pylands-Learn-Apply
   !pip install -r requirements.txt
   
3.Follow the examples provided in the notebook to analyze your raster data and visualize results.

## Acknowledgments
We extend our gratitude to all contributors, past, present, and future, who help make this project a valuable resource for learners around the world. Together, we can empower the next generation of programmers and creators.

Happy coding!

Lucas F. T. Leonardo
