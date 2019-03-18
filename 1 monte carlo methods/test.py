import numpy as np
import random
from math import exp
from display_data import display_data

def func(x, y):
	return (pow(y, 3)*exp(-pow(y, 2))+pow(x, 4)*exp(-pow(x, 2)))/(x*exp(-pow(x, 2)))