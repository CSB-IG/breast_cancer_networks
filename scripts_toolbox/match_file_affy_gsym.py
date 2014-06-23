

'''
README!!!!

How to run: python match_file_affy_gsym.py example.txt
output file: example_genesym.txt

needs all_list_gsym_affy.txt and example.txt at the same level of this script in the file system

example:
python match_file_affy_gsym.py autofagia_sanos.txt
output file: autofagia_sanos_output.txt

'''


import sys
import csv


'''
translates the affy_id from the input file into gene symbol
'''

list_file = csv.reader(open("all_list_gsym_affy.txt", 'rb'), delimiter = '\t')
dict1 = {}

for row in list_file:
    dict1[row[0]] = row[1]
   

input_file = open(sys.argv[1], 'rb')
name=sys.argv[1].replace(".txt", "", 1)+"_genesym.txt"
output_file = open(name, "w")

for row in input_file:
    p = row.split(" ")
    
    str1 = ""
    str2 = ""

    p0 = p[0].replace("\n", "").replace("\t", "")
    p1 = p[1].replace("\n", "").replace("\t", "")
    p2 = p[2].replace("\n", "").replace("\t", "")

    if p0 in dict1:
        str1 = dict1[p0].replace("\n", "").replace("\t", "")
    else:
        str1 = p0
    
    if p2 in dict1:
        str2 = dict1[p2].replace("\n", "").replace("\t", "")
    else:
        str2 = p2
    
    output_file.writelines([str1,"\t",p1,"\t",str2,"\n"])

print "output file: ", name
output_file.close()
input_file.close()






