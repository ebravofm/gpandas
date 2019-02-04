import requests
import pandas as pd
from io import BytesIO

def read_gexcel(id, **pd_read_excel_args):

    if 'id=' in id:
        id = id.split('id=')[1]
    
    dl = 'https://docs.google.com/spreadsheets/d/{0}/export?format=xlsx&id={0}'.format(id)
    r = requests.get(dl) 
    excel_data = pd.ExcelFile(BytesIO(r.content))

    return pd.read_excel(excel_data, **pd_read_excel_args)