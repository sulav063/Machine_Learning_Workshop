import math
import numpy as np 
import pandas as pd

def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))
#hlo
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)

#day 11
