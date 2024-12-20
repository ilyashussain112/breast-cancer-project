from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

from typing_extensions import ParamSpec
from sklearn.model_selection import GridSearchCV
class Model:
    def __init__(self):
        pass

    def model (self):
        params ={
        'n_estimators' :[100],
    'criterion' :['gini', 'entropy'],
        "max_depth" :[None, 10, 20],
    "min_samples_split" :[2, 5, 10],
    "min_samples_leaf" :[1, 2, 4],

        }


        grid = GridSearchCV(estimator=rf , cv=5 ,scoring='accuracy' , param_grid=params)
        return grid 