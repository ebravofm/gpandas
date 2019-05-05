# Gpandas

Utilities for working with Google Sheets on pandas and python.

# Installation

```
python3 -m pip install git+https://github.com/ebravofm/Gpandas.git
```
# read_gexcel

Use pandas' read_excel function on a google drive workbook. Get sharing link and update permissions as public. No need to authenticate.
```python
import gpandas as gpd

df = gpd.read_gexcel('https://drive.google.com/open?id=18ID3C6mhTMgISlqkd6L1NOfWRdxiEwdMqAWvSKkvcd8')

#    Countries Code
# 0      Chile   CL
# 1  Argentina  ARG
# 2   Colombia   CO
# 3       Perú   PE
```
You can use any of pandas.read_excel() original arguments (such as sheet_name to select sheet to parse, usecols, converters, etc)
