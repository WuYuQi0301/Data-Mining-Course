from prettytable import PrettyTable
import numpy as np
from math import floor

def store_data(data, Ns, times, path):

	file = open(path, "w")
	# file.write(result)
	sp = 10
	for i in range(int(times/sp)):
		titles = []
		tmp = ["N\\Times"]
		
		for j in range(sp):
			tmp.append(str(i*sp+j+1))

		tmp_table = PrettyTable(tmp)
		for j in range(len(Ns)):
			row = np.zeros(sp+1)
			row[0] = Ns[j]
			row[1:sp+1] = data[j, i*sp+1:i*sp+sp+1]
			tmp_table.add_row(row)
		
		file.write(str(tmp_table)+"\n")
		# file.write(str(tmp_table))
		
	mv_table = PrettyTable(["N\\Times", "Mean", "Variance"])
	for i in range(len(Ns)):
		mv_table.add_row([Ns[i], round(np.mean(data[i, 1:times+1]), 2), round(np.var(data[i, 1:times+1]), 2)])
	# print(mv_table)	
	file.write(str(mv_table))
	file.close();
