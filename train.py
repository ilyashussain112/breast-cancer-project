from pipeline.model import Model
from src.datasplit import Splitter
import joblib as j 
split = Splitter()
models = Model()

x_train, x_test, y_train, y_test = split.splitter()
grid = models.model()
print("Trainig Start.. ")

grid.fit(x_train, y_train)
print ("model train")

model = grid.best_estimator_
j.dump(model , 'models/model.pkl')

print ("Model save")
