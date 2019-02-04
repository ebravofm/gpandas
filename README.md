# Gpandas

Utilities for working with Google Sheets on pandas and python.

# read_gexcel

Use pandas' read_excel function on a google drive workbook. Get sharing link and update permissions as public. No need to authenticate.
```python
from Gpandas import read_gexcel

df = read_gexcel('https://drive.google.com/open?id=18ID3C6mhTMgISlqkd6L1NOfWRdxiEwdMqAWvSKkvcd8')

#    Countries Code
# 0      Chile   CL
# 1  Argentina  ARG
# 2   Colombia   CO
# 3       Perú   PE
```
You can use any of pandas.read_excel() original arguments (such as sheet_name to select sheet to parse, usecols, converters, etc)
