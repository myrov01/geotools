# Geotools

Description

## Installation

```bash
git clone git@github.com:myrov01/geotools.git
cd ./geotools
python -m venv ./env
. ./evn/Scripts/activate
pip install -r ./requirements.txt
```

## Usage

This script uses the library `geopandas` for reading geographical data and calculating the total number of coordinates of points (including outer and inner rings) in polygons and multipolygons from the GeoPackage file.

### Installation

Make sure you have the library installed before using it `geopandas`:
```bash
pip install geopandas
```
The test data set can be downloaded from the link: https://youtrack.nextgis.net/issue/ILB-81/Sozdanie-skripta-geomcalc-i-geomsut-dlya-osnovnogo-instrumenta-konvertacii-gpkgsxf

Copy the vegetation-polygon file.gpkg to the same folder where the script is located, or specify the path to another GeoPackage file containing polygonal data.

Run the script from the command line:
```bash
python script_name.py
```
The result of the script will show the total number of coordinates of points in polygons and multipolygons from the specified file.

After running the script, you will see the output in the format:
```bash
Total points: <число>
```
The script loads geometric data from the vegetation-polygon.gpkg file.

The geo_calc function counts the number of points (coordinates) in each polygon and multipolygon.

The outer rings and inner rings (nested polygons) are counted in the total score.

Make sure that the geometry column is present in the Getpackage file, otherwise the script will not be able to process the data.

Only Polygon and MultiPolygon geometries are supported.

Replace `script_name.py ` to the actual name of your script.