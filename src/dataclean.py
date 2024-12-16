from .dataloading import loader
import pandas as pd
PATH = r'artifacts\breast cancer.csv'
load = loader()
df = load.df_loader(PATH)

class Clean:
    def __init__(self):
        pass
    
    def df_clean(self):
        df = df.dropna()
        df = df.drop_duplicates()

        return df
     