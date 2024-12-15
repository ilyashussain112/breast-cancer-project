from .dataloading import loader
import pandas as pd
PATH = r'artifacts\breast cancer.csv'
loader = loader()
data = data.data_loader(PATH)

class clean:
    def __init__(self):
        pass
    
    def drop_missing(self):
        self.data = self.data.dropna()
        return self.data
     
    def drop_duplicates(self):
        self.data = self.data.drop_duplicates()
        return self.data 
    
    def reset_indux(self):
        self.data = self.data.reset_indux(drop = True)
        return self.data