import requests
import pandas as pd
from io import BytesIO
from xlrd import XLRDError

def id_from_link(link):
    
    if 'google.com' not in link:
        id = link
    
    elif '/d/' in link:
        split = link.split('/')
        i = split.index('d')
        id = split[i+1]
    
    elif 'id=' in link:
        split1 = link.split('id=')[1]
        id = split1.split('/')[0]
        
    return id


def read_excel(link, 
               sheet_name=0,
               header=0,
               names=None,
               index_col=None,
               parse_cols=None,
               usecols=None,
               squeeze=False,
               dtype=None,
               engine=None,
               converters=None,
               true_values=None,
               false_values=None,
               skiprows=None,
               nrows=None,
               na_values=None,
               keep_default_na=True,
               verbose=False,
               parse_dates=False,
               date_parser=None,
               thousands=None,
               comment=None,
               skip_footer=0,
               skipfooter=0,
               convert_float=True,
               mangle_dupe_cols=True,
               **kwds):
    '''
    Read Google Sheets worksheet as pandas dataframe.
    '''
    
    excel_data = ExcelFile(link)
    
    return pd.read_excel(
        excel_data=excel_data,
        sheet_name=sheet_name,
        header=header,
        names=names,
        index_col=index_col,
        parse_cols=parse_cols,
        usecols=usecols,
        squeeze=squeeze,
        dtype=dtype,
        engine=engine,
        converters=converters,
        true_values=true_values,
        false_values=false_values,
        skiprows=skiprows,
        nrows=nrows,
        na_values=na_values,
        keep_default_na=keep_default_na,
        verbose=verbose,
        parse_dates=parse_dates,
        date_parser=date_parser,
        thousands=thousands,
        comment=comment,
        skip_footer=skip_footer,
        skipfooter=skipfooter,
        convert_float=convert_float,
        mangle_dupe_cols=mangle_dupe_cols,
        **kwds)


def ExcelFile(link):
    '''
    Read Google Sheets workbook as pandas ExcelFile.
    '''
    
    id = id_from_link(link)
    
    dl = f'https://docs.google.com/spreadsheets/d/{id}/export?format=xlsx&id={id}'
    
    r = requests.get(dl)

    try:
        excel_data = pd.ExcelFile(BytesIO(r.content))
        
    except XLRDError:
        raise Exception("Can't access spreadsheet, check sharing configuration. Spreadsheet must be public.")

    return excel_data