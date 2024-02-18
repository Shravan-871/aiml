import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def rmse_metric(actual, predicted):
    return sqrt(sum((p - a)**2 for a, p in zip(actual, predicted)) / len(actual))

def evaluate_algorithm(dataset, algorithm):
    test_set = [row[:-1] + [None] for row in dataset]
    predicted = algorithm(dataset, test_set)
    print(predicted)
    actual = [row[-1] for row in dataset]
    rmse = rmse_metric(actual, predicted)
    return rmse

def mean(values):
    return sum(values) / len(values)

def covariance(x, mean_x, y, mean_y):
    return sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (len(x) - 1)

def variance(values, mean):
    return sum((x - mean)**2 for x in values) / (len(values) - 1)

def coefficients(dataset):
    x_values, y_values = zip(*dataset)
    x_mean, y_mean = mean(x_values), mean(y_values)
    x_variance, y_variance = variance(x_values, x_mean), variance(y_values, y_mean)
    b1 = covariance(x_values, x_mean, y_values, y_mean) / x_variance
    b0 = y_mean - b1 * x_mean
    return b0, b1

def simple_linear_regression(train, test):
    b0, b1 = coefficients(train)
    return [b0 + b1 * row[0] for row in test]

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

# Print statistics
x_values, y_values = zip(*dataset)
x_mean, y_mean = mean(x_values), mean(y_values)
x_variance, y_variance = variance(x_values, x_mean), variance(y_values, y_mean)
print('X stats: mean=%3f variance=%3f' % (x_mean, x_variance))
print('Y stats: mean=%3f variance=%3f' % (y_mean, y_variance))
covar = covariance(x_values, x_mean, y_values, y_mean) / (x_variance * y_variance)
print('covariance: %3f' % covar)
rmse = evaluate_algorithm(dataset, simple_linear_regression)
print('RMSE: %3f' % rmse)
b0, b1 = coefficients(dataset)
print('coefficient: B0=%3f, B1=%3f' % (b0, b1))

# Plot the data and regression line
plt.scatter(x_values, y_values, label='Actual data')
plt.plot(x_values, [b0 + b1 * x for x in x_values], color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
