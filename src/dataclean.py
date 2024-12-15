from .dataloading import loader
import pandas as pd
PATH = r'artifacts\breast cancer.csv'
loader = loader()
data = data.data_loader(PATH)

class clean:
    def __init__(self):
        pass
    