import joblib as j
import pandas as pd

#scaler load
sc = j.load("models\\scaler.pkl")

#model load
model = j.load("models\\model.pkl")

#user data 
df = pd.read_csv("artifacts\\data.csv")
data = df.drop(['diagnosis', 'id'], axis=1)
data = data.head(1).values

def prediction(data, scaler=sc, model=model):
    data = scaler.transform(data)
    predict = model.predict(data)
    return predict

