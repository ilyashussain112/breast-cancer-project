from pipeline.model import Model
from src.datasplit import Splitter

split = Splitter()
models = Model()

x_train, x_test, y_train, y_test = split.spliter()
grid = models.sv_model()
grid.fit(x_train, y_train)
model = grid.best_estimator_
grid.best_estimator_