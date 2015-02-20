#Author: Daniel Teran
'''
This script removes genes and their respective MI in a .adj file.

How run:
python delete_gene.py file.adj target_1 target_2 .... target_n
python delete_gene.py example.adj YY1 CYP2A6

output: example_updated.adj
'''

import sys
 
 
 
exp_file = open(sys.argv[1], 'rb')
salida = open(sys.argv[1].replace(".adj", "", 1)+"_updated.adj", "w")

 
for line in exp_file :
	line.replace("\\n","")
	inter = line.split("\t")
	str_out = ""
	str_out += inter[0]
	for i in range(1,len(inter),2):#por cada gen en el renglon
		bandera = 0
		for j in range(2,len(sys.argv)):#por cada gen en la lista que quieres eliminar
			if i==j:
				bandera = 1
				break
		if bandera == 0:
			add = "\t"+inter[i]+"\t"+inter[i+1]	
			str_out += add
	salida.write(str_out)
				

exp_file.close()
salida.close()  



