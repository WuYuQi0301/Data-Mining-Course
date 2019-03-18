import numpy as np
import random
from store_data import store_data

def DropPoint():
	x = random.random()
	y = random.random()
	if (np.sqrt(x*x + y*y)) < 1:
		return True
	return False

times = 100
Ns = np.array([20, 50, 100, 200, 300, 500, 1000, 5000])
result = np.zeros([8, times+3])
result[:, 0] = Ns.T

for i in range(times):   # process times
	for j in range(8):   # number of points
		counter_in = 0
		for k in range(Ns[j]):
			if DropPoint() == True:
				counter_in += 1

		result[j, i+1] = round(counter_in/Ns[j], 5)

for i in range(8):
	result[i, times + 1] = round(np.mean(result[i, 1:times+1]), 5)
	result[i, times + 2] = round(np.var(result[i, 1:times+1]), 5)

store_data(result, Ns, 100, "task1.txt")
