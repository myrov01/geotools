# Geotools

Geotools - this is a set of scripts for solving three educational tasks.

`geom_calc` from [myrov01](https://github.com/myrov01)

`geom_cut` from [myrov01](https://github.com/myrov01)

`geom_lim` from [myrov01](https://github.com/myrov01)

## Installation

```bash
git clone git@github.com:myrov01/geotools.git
cd ./geotools
python -m venv ./env
. ./env/Scripts/activate
pip install -r ./requirements.txt
```

## Usage

Script *geom_calc* uses the library `geopandas` for reading geographical data and calculating the total number of coordinates of points (including outer and inner rings) in polygons and multipolygons from the GeoPackage file.

Script *geom_cut* uses the libraries `geopandas`, `shapely`, `argparse`, `os` for dividing polygonal objects into parts, based on the condition of the boundary number of points in a polygonal object, with further output of the result of the processed polygon layer in GeoPackage format.

Script *geom_lim* uses the library `geopandas` for reading geographical data and calculating the maximum number of coordinates of points (including outer and inner rings) in polygons and multipolygons from the GeoPackage file.

## Test data for `geom_calc`, `geom_cut`, `geom_lim`

The test data set can be downloaded from the link: https://drive.google.com/file/d/1Kw0IEnFqZeUvVoZDGsmkwkSozPMp2G2B/view?usp=drive_link
