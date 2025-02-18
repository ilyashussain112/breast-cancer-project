from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import joblib as j
from .dataclean import Clean


clean = Clean()
df = clean.df_clean()


class Transform:
    def __init__(self):
        pass 

    
    def transform(self):
        le = LabelEncoder()
        df['diagnosis'] = le.fit_transform(df['diagnosis'] )

        x = df.drop('diagnosis', axis=1)
        y = df['diagnosis']

        sc = StandardScaler()
        sc.fit(x)
        j.dump(sc, "models/scaler.pkl")
        x = sc.transform(x)
        


        return x,y
    