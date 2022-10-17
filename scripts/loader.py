
import json
import sys
from git import Object
import pandas as pd

class LoadData:


    def __init__(self) -> None:
    """
    def read_json(self, json_file: str, dfExtractFunc: Object) -> pd.DataFrame:
        data_list = []
        for item in open(json_file, "r"):
            data_list.append(json.loads(item))

        df = dfExtractFunc(data_list)
        return df
    """
    def read_excel(self, excel_file, startRow=0) -> pd.DataFrame:
        
        df = pd.read_excel(excel_file, engine="openpyxl")
        return df

    def read_csv(self, csv_file) -> pd.DataFrame:
        
        return pd.read_csv(csv_file)
