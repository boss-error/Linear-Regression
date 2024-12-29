import numpy as np

def calculate_linear_regression(x, y, predict_value):
    """Calculate linear regression and return the results"""
    # Calculate required values
    x_sq = np.square(x)
    y_sq = np.square(y)
    x_y = x * y
    
    # Calculate sums
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_sq = np.sum(x_sq)
    sum_y_sq = np.sum(y_sq)
    sum_x_y = np.sum(x_y)
    
    # Calculate constants
    n = len(x)
    a = (n * sum_x_y - sum_x * sum_y) / (n * sum_x_sq - sum_x**2)
    b = (sum_y - a * sum_x) / n
    
    # Calculate predicted value
    predicted_y = a * predict_value + b
    
    return {
        'x': x,
        'y': y,
        'x_sq': x_sq,
        'y_sq': y_sq,
        'x_y': x_y,
        'sum_x': sum_x,
        'sum_y': sum_y,
        'sum_x_sq': sum_x_sq,
        'sum_y_sq': sum_y_sq,
        'sum_x_y': sum_x_y,
        'n': n,
        'a': a,
        'b': b,
        'predict_value': predict_value,
        'predicted_y': predicted_y
    }