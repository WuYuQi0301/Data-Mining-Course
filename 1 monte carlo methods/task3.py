import numpy as np
import random
from math import exp
from store_data import store_data

def func(x, y):
	return (pow(y, 2)*exp(-pow(y, 2))+pow(x, 4)*exp(-pow(x, 2)))/(x*exp(-pow(x, 2)))

times = 100
Ns = np.array([10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500])
integral_result = np.zeros([len(Ns), times+3])
integral_result[:, 0] = Ns.T

upper_x = 4
lower_x = 2
upper_y = 1
lower_y = -1

for i in range(times):
	for j in range(len(Ns)):

		integral_y = []
		for m in range(Ns[j]):

 			x = random.uniform(lower_x, upper_x)
 			points = []

 			for n in range(Ns[j]):           # （固定x）将A(x0)投影到yOz平面上
 				y = random.uniform(lower_y, upper_y)
 				points.append(func(x, y))
 			if np.mean(points) == 0:
 				print("error")
 			# integral_y[0,m] = round((upper_y - lower_y)*np.mean(points), 5)
 			integral_y.append(round((upper_y - lower_y)*np.mean(points), 5))# 用一重积分计算截面面积

		integral_result[j, i+1] = round((upper_x - lower_x)*np.mean(integral_y), 2)
	if i%10 == 0:
		print(i)

for i in range(len(Ns)):
	integral_result[i, times + 1] = round(np.mean(integral_result[i, 1:times+1]), 2)
	integral_result[i, times + 2] = round(np.var(integral_result[i, 1:times+1]), 2)

store_data(integral_result, Ns, times, "task3.txt")