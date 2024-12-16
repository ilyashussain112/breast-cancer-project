import pandas as pd 

class loader:
    def __init__(self):
        pass
    def df_loader(self , path):
        df = pd.read_csv(path)
        return df