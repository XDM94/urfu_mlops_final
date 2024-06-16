#!/bin/sh

curl -X POST -H "Content-Type: application/json" -d '{"Pclass": 1, "Sex": 0, "Age": 20.0, "SibSp": 0, "Parch": 0, "Fare": 15, "Embarked": 0}' http://127.0.0.1:8091/predict

curl -X POST -H "Content-Type: application/json" -d '{"Pclass": 2, "Sex": 1, "Age": 40.0, "SibSp": 1, "Parch": 0, "Fare": 30, "Embarked": 0}' http://127.0.0.1:8091/predict
