import os
import sys
from src.exception import CustomException
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models, parameter):
    try:
        report = {}
        # best_models = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = parameter[list(models.keys())[i]]

            gs = GridSearchCV(model, param, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            #model.fit(X_train, y_train)  # Train model

            # best_model = gs.best_estimator_
            
            # y_train_predictions = best_model.predict(X_train)
            # y_test_predictions = best_model.predict(X_test)
            y_train_predictions = model.predict(X_train)
            y_test_predictions = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_predictions)
            test_model_score = r2_score(y_test, y_test_predictions)

            report[list(models.keys())[i]] = test_model_score
            # best_models[model_name] = best_model

        # return report, best_models
        return report

    except Exception as e:
        raise CustomException(e, sys)
