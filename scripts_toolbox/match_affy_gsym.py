'''
How to run:

python match_affy_gsym.py input_file.sif
output: input_file_sif_output.txt

example: 
match_affy_gsym.py apoptosis_sanos_ADJ_output_20.sif
output: apoptosis_sanos_ADJ_output_20_sif_output.txt
'''


import sys
import csv


'''
First gets the gene symbols with them load values from name_pvalue_1191.txt
'''
name_pvalue = open("name_pvalue_1191.txt", 'rb')
next(name_pvalue)
dict1 = {}

for row in name_pvalue:
	p = row.split("\t")
	p0 = p[0].replace("\"","")
	if p0 in dict1:
	    val = p[1].strip()
	    #take the biggest load value
	    if val > dict1[p0]:  
	        dict1[p0] = val
	else:
	    dict1 [p0] = p[1].strip()
name_pvalue.close()



'''
Then gets the affy_ids with gene symbol that has the biggest load value among all gene symbols
'''

id_gene = csv.reader(open("id_gene_HG.csv", 'rb'), delimiter = ',')
next(id_gene)
dict2 = {}

for row in id_gene:
	sp = row[1].split(" /// ")
	aux = -sys.maxint - 1
	for chunk in sp:
	    if chunk in dict1:
		    if dict1[chunk] > aux:
		        dict2[row[0]] = chunk


'''
At last translates the affy_id from the input file into gene symbol
'''
input_file = open(sys.argv[1], 'rb')
output_file = open(sys.argv[1].replace(".sif", "", 1)+"_genesym.txt", "w")
for row in input_file:
    p = row.split("\t")
    str1 = ""
    str2 = ""
    if p[0] in dict2:
        str1 = dict2[p[0]]
    else:
        str1 = p[0]
    
    if p[1] in dict2:
        str2 = dict2[p[1]]
    else:
        str2 = p[1]
    
    output_file.writelines([str1,"\t",str2,"\t",p[2]])
	
input_file.close()
output_file.close()






