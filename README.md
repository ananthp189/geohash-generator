# Geohash Generator - Shortest unique code

## Overview

This Python script generates geohashes for each latitude and longitude coordinates and stores the shortest unique geohash prefixes in a CSV file. The generated geohashes can be used for spatial indexing and location-based applications.

## Prerequisites

- Python 3.x
- Required Python libraries: pandas,numpy and geohash (install using `pip install pandas python-geohash numpy`)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ananthp189/geohash-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd geohash-generator
    ```

3. Place your input file (`coordinates.csv.gz`) in the project directory.

4. Run the script:

    ```bash
    python geohash_generator.py
    ```

5. The script will generate a new CSV file (`geohash.csv`) containing only the geohash column.

## Configuration

- Modify the file_path in case of change in the name of the file or path. 
- Adjust the precision parameter in the `generate_geohash` function in the script for desired geohash precision.



## Author

- Ananth
- ananthpadakannaya93@gmail.com
