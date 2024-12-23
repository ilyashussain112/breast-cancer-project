from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from .dataclean import Clean
le = LabelEncoder()

clean = Clean()
df = clean.df_clean()


class Transform:
    def __init__(self):
        pass 
    def transform(self):
        df['diagnosis'] = le.fit_transform(df['diagnosis'] )

        x = df.drop('diagnosis', axis=1)
        y = df['diagnosis']

        sc = StandardScaler()
        x = sc.fit_transform(x)

        return x,y
    