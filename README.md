# Geotools

Geotools - this is a set of scripts for solving two educational tasks.

`geom_calc` from [myrov01](github.com/myrov01)

`track_length` from [deisnau](github.com/deisnau)

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

Script *track_length* uses the library `geopandas` for reading *.gpx file and calculating track's lengths.

<!-- кажется, то, что в этом разделе нужно под первый заголовок, а здесь описать что принимается на входе, что получается на выходе -->

## Test data for `geom_calc`

The test data set can be downloaded from the link: https://youtrack.nextgis.net/issue/ILB-81/Sozdanie-skripta-geomcalc-i-geomsut-dlya-osnovnogo-instrumenta-konvertacii-gpkgsxf

## Test data for `track_length`

The test data set can be downloaded from the link: https://drive.google.com/file/d/1kzwrBtGKJvTfH-aRzoBY2p9av3golpNe/view?usp=drive_link 