'''
NOTA: Antes de ejecutar este script recuerda haber generado el archivo id_loads.txt con el script id_genes2id_pvalue.txt

Despues de eso en el mismo lugar donde se genero el archivo correr este script de la siguiente forma:
$ python match_process_id.py "nombre del archivo del procesos a traducir" "nombre del archivo salida", un ejemplo:

$ python match_process_id.py proceso1.txt salida_proceso

y la salida sera un archivo salida_proceso.txt


'''

import sys
import csv


id_loads = csv.reader(open("id_loads.txt", 'rb'), delimiter = '\t')
gene_p=[]
gene_aff_id=[]
gene_sym=[]


process_file = open(sys.argv[1], 'rb')
for row in process_file:
	gene_p.append(row.replace("\"","").strip())
process_file.close()

for r in id_loads:
	gene_aff_id.append(r[0])
	gene_sym.append(r[2])

gene_aff_id.remove("Affy_id")
gene_sym.remove("gene_symbol")

#abrimos el archivo salida
salida = open(sys.argv[2]+".txt", "w")
salida.writelines(["aff_id","\t\t","gene_symbol", "\n"])

for genes in gene_p:
	for i in range (len(gene_aff_id)):
		if gene_sym[i].replace("\"","") == genes.replace("\"",""):
			salida.writelines([genes,"\t\t", gene_aff_id[i], "\n"])

salida.close()

