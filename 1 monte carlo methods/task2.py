import numpy as np
import random
from store_data import store_data

def func(x):
	return pow(x, 3)

times = 100
Ns = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 100])
integral_result = np.zeros([10, 103])
integral_result[:, 0] = Ns.T

b = 1
a = 0

for i in range(times):
	for j in range(10):
		f_points = []
		for k in range(Ns[j]):
 			x = random.uniform(a, b)
 			f_points.append(func(x))	
		integral_result[j, i+1] = round((b-a)*np.sum(f_points)/Ns[j], 5)

for i in range(10):
	integral_result[i, times + 1] = round(np.mean(integral_result[i, 1:times+1]), 5)
	integral_result[i, times + 2] = round(np.var(integral_result[i, 1:times+1]), 5)

store_data(integral_result, Ns, 100, "task2.txt")
	