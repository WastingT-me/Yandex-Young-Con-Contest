# -*- coding: utf-8 -*-

import sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().split('\n')

    # Extract training data
    train_data = []
    for line in input_data[:1000]:
        train_data.append(list(map(float, line.strip().split('\t'))))
    train_data = np.array(train_data)
    X_train = train_data[:, :-1]
    y_train = train_data[:, -1]

    # Extract test data
    test_data = []
    for line in input_data[1000:]:
        test_data.append(list(map(float, line.strip().split('\t'))))
    X_test = np.array(test_data)

    # Create a pipeline that combines PolynomialFeatures and LinearRegression
    model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())

    # Train the model
    model.fit(X_train, y_train)

    # Predict the test data
    predictions = model.predict(X_test)

    # Print the predictions
    for pred in predictions:
        print(pred)

if __name__ == "__main__":
    main()