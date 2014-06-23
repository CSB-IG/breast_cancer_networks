import csv
import sys 

#abrimos el archivo en donde estan los Affy_id y geneSymbol
id_gene = csv.reader(open("id_gene_HG.csv", 'rb'), delimiter = ',')
dict = {}
aff_id = []

#metemos en un diccionario todas la entradas del archivo y en arreglo auxiliar solo los Affy_id para posteriormente iterar en el diccionario las entradas 
for row in id_gene:
	dict[row[0]] = row[1]	
	aff_id.append(row[0])

#borramos la primera entrada del diccionario que son los encabezados
aff_id.remove("Probe Set ID")
del dict["Probe Set ID"]

#abrimos el archivo donde estan los p.value y loads lo pasamos a arreglos
name_pvalue = open("name_pvalue_1191.txt", 'rb')
name = []
pv = []
loads = []
for row in name_pvalue:
	p = row.split("\t")
	name.append(p[0])
	pv.append(p[2])
	loads.append(p[1].strip())
#cerramos el archivo
name_pvalue.close()


#y abrimos un nuevo archivo para escribir las salidas:
salida = open("id_loads.txt", "w") #sera mejor escribirlo con cvs?????
#escribimos el encabezado
salida.writelines(["Affy_id","\t\t", "gene_symbol", "\n"])

#hago split por cada entrada del diccionario
for entry in aff_id:
	#print (entry, "--->" ,dict[entry])
	sp = dict[entry].split(" /// ")
	aux = []
	#ahora por cada entrada de sp busco en el archivo y extraigo su p_value para compararlos
	for chunk in sp:
		for i in range(len(name)):
			#print (name[i].replace("\"",""), chunk)
			if name[i].replace("\"","") == chunk :
				aux.append([name[i],pv[i],loads[i]])
				break

	#comparo los p_values y me quedo con el mas chico
	if len(aux) == 0:
		salida.writelines([entry,"\t\t"," NF ", "\n"])	
		print "paso 0"
	elif len(aux) == 1:		
		salida.writelines([entry,"\t\t", aux[0][0], "\n"])
		print "paso 1"
	else:
		
		m = 0
		for i in range(len(aux)-1):
			if aux[i][2] < aux[i+1][2]:
				m = i
			else:
				m = i+1
		
		'''
		val, idx = min((val, idx) for (idx, val) in enumerate(aux))
		'''
		print "paso 2"
		print m
		salida.writelines([entry,"\t\t", aux[m][0], "\n"])
		
#cerramos el archivo de salida
salida.close()

