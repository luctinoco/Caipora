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

### Functions Implemented:

- **setup_environment():** Ensures all required Python packages are installed, simplifying setup for new users.
  
- **calculate_save_metrics_and_plot(input_file, output_file, color_excel, nodata_value=0):**
  - Loads raster data using rasterio and computes landscape metrics via pylandstats.
  - Saves metrics to a CSV file ('metrics_output.csv').
  - Reads a color legend from an Excel file ('color_data.xlsx') to assign colors to raster classes.
  - Generates an interactive map using folium, saved as an HTML file ('map_output.html').

## Compatibility and Adaptation

While originally designed for land use and land cover rasters from the MapBiomas platform, this script is modular and adaptable. It can process other raster types with appropriate adjustments to input parameters and data handling.

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

## Straight to the point

### Running the Script:

Make sure your `*.tif` raster file and `color_data.xlsx` are accessible in your Google Drive.

### Input Prompts

When running the script, you will be prompted to provide the following information in the specified order:

1. **Path to Output Folder:**
   - Enter the path to the folder where you want the results to be saved. If the folder does not exist, the script will create it automatically.
   -Example:
    ```
   Enter the path to the output folder where results will be saved: /content/drive/My Drive/Output
    ```
3. **Path to Raster File (`*.tif`):**
- Provide the path to the raster file in `*.tif` format. The script will check if the file exists and has the correct extension.
-Example:
 ```
Enter the path to the input raster (.tif) file: /content/drive/My Drive/raster_data.tif
 ```
3. **Path to Color Legend Excel File (`color_data.xlsx`):**
- Input the path to the color legend Excel file in `*.xlsx` format. The script will verify if the file exists and has the correct extension.
-Example:
 ```
Enter the path to the color legend Excel (.xlsx) file: /content/drive/My Drive/color_data.xlsx
 ```

4. **Base Name for Output Files (without extension):**
- Type a base name for the output files that will be generated by the script. This name will be used for the CSV metrics files and the HTML interactive map file.
-Example:
 ```
Enter the base name for output files (without extension): output_results
 ```
### Usage on Google Colab

To use this project on Google Colab, click the badge below to open the notebook directly:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luctinoco/Pylands-Learn-Apply/blob/main/notebooks/Pylands-Learn-Apply.ipynb)

## Handling Errors

### Error Messages for Incorrect Files

When running the script, you may encounter specific error messages if the files provided are incorrect or cannot be found:

1. **File Not Found Error:**
   - If the script cannot find the specified raster file (`*.tif`) or color data file (`color_data.xlsx`) in your Google Drive, it will raise a `FileNotFoundError`.
   - Example: 
     ```
     FileNotFoundError: No .tif file found at the specified path: /content/drive/My Drive/incorrect_raster.tif
     ```

2. **Incorrect File Type Error:**
   - If the provided files do not match the expected file types (`*.tif` for raster and `color_data.xlsx` for color data), the script will raise an appropriate error.
   - Example:
     ```
     ValueError: Incorrect file type provided. Expected *.tif raster file or color_data.xlsx Excel file.
     ```

3. **Other Errors:**
   - For any other unforeseen errors related to file reading, parsing, or processing, the script will raise informative error messages to guide troubleshooting.
   - Example:
     ```
     IOError: Unable to read color data from color_data.xlsx. Please check the file format and contents.
     ```

### Troubleshooting Tips

- **Double-check File Paths:** Ensure that the paths provided to the raster file and color data file are correct and accessible in your Google Drive.
  
- **Verify File Formats:** Confirm that the raster file is in `*.tif` format and the color data file is in `*.xlsx` format with the required structure (Class_ID and Color columns).

- **Check File Permissions:** Make sure you have the necessary permissions to access and read the files from your Google Drive.

By following these guidelines and paying attention to error messages, you can effectively troubleshoot and resolve issues when using the Pylands-Learn-Apply script.

## Acknowledgments
We extend our gratitude to all contributors, past, present, and future, who help make this project a valuable resource for learners around the world. Together, we can empower the next generation of programmers and creators.

Don't forget to cite this repository if you use its code in your project.

Happy coding!

Lucas F. T. Leonardo
