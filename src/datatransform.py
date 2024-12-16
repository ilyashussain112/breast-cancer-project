from sklearn import labelEncoder
from sklearn.preprocessing import StandardScaler
from .dataclean import Clean
le = labelEncoder()

clean = Clean()
df = clean.df_clean()


class transform:
    def __init__(self):
        pass 
    def transform(self):
        df['diagnosis'] = le.fit_transform(df['diagnosis'] )
        

        x = df.drop('diagnosis', axis=1)
        y = df['diagnosis']

        sc = StandardScaler()
        x = sc.fit_transform(x)

        return x,y
    