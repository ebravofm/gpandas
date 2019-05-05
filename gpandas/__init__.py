import requests
import pandas as pd
from io import BytesIO

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

def read_gexcel(link, **pd_read_excel_args):
    '''
    Read Google Sheets worksheet as pandas dataframe.
    '''
    
    excel_data = gExcelFile(link)
    
    return pd.read_excel(excel_data, **pd_read_excel_args)


def gExcelFile(link):
    '''
    Read Google Sheets workbook as pandas ExcelFile.
    '''
    
    id = id_from_link(link)
    
    dl = f'https://docs.google.com/spreadsheets/d/{id}/export?format=xlsx&id={id}'
    r = requests.get(dl) 
    excel_data = pd.ExcelFile(BytesIO(r.content))

    return excel_data