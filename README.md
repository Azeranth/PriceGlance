# PriceGlance
PriceGlance is a python utility for quickly retrieving data for Market Quick Views

## Usage
```
usage: PriceGlance.py [-h] [--database DATABASE] file [file ...]

PriceGlance is a python utility for quickly retrieving data for Market Quick Views

positional arguments:
  file                 File containing Market Quick View config

options:
  -h, --help           show this help message and exit
  --database DATABASE  Item ID and display name database file. Defaults to 'ItemTypeDatabase' in install directory

https://github.com/Azeranth/PriceGlance
```
### Error Codes
* 129 - HTTP Connection Error

## Market Quick View
A Market Quick View is a comma delimted list of index for the desired fields followed by comma delimited list of item ids to retrieve data for. Lists may not exceed 200 ids.
|Index|Field|
|---|---|
|0|Volume|
|1|Average|
|2|Max Price|
|3|Min Price|
|4|Std Dev|
|5|Median Price|
|6|Percentile|
