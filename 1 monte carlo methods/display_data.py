from prettytable import PrettyTable
import numpy as np

def store_data(data, Ns, times, path):

	file = open(path, "w")
	# file.write(result)

	for i in range(int(times/10)):
		titles = []
		tmp = ["N\\Times"]
		
		for j in range(10):
			tmp.append(str(i*10+(j+1)))

		tmp_table = PrettyTable(tmp)
		for j in range(len(Ns)):
			row = np.zeros(11)
			row[0] = Ns[j]
			row[1:11] = data[j, i*10+1:i*10+11]
			tmp_table.add_row(row)
		
		file.write(str(tmp_table)+"\n")
		# file.write(str(tmp_table))
		mv_table = PrettyTable(["N\\Times", "Mean", "Variance"])

	for i in range(len(Ns)):
		mv_table.add_row([Ns[i], round(np.mean(data[i, 1:times+1]), 5), round(np.var(data[i, 1:times+1]), 5)])
	# print(mv_table)	
	file.write(str(mv_table))
	file.close();
