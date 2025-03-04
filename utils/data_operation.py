import math
import numpy as np 
import pandas as pd

def distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))