import argparse
import csv


parser = argparse.ArgumentParser(description='Create network of pathways connected by genes, add enrichment levels')

parser.add_argument('--network',         type=argparse.FileType('r'), required=True, help="CSV file with pw, gene, 1")
parser.add_argument('--gene_enrichment', type=argparse.FileType('r'), required=True, help="CSV file with genes and their enrichments")
parser.add_argument('--pw_enrichment',   type=argparse.FileType('r'), required=True, help="CSV file with pathways and their enrichments")

args = parser.parse_args()



# load gene enrichment into a dictionary
gene_enrichment = {}
gene_reader = csv.reader(args.gene_enrichment, delimiter=",")
gene_reader.next() # pop header
for l in gene_reader:
    gene_enrichment[l[0]] = l[1]



# load pathway enrichment into a dictionary
pw_enrichment = {}
pw_reader = csv.reader(args.pw_enrichment, delimiter=",")
pw_reader.next() # pop header
for l in pw_reader:
    pw_enrichment[l[0]] = l[1]



pw_gene = {}
gene_pw = {}
nw_reader = csv.reader(args.network, delimiter="\t")
for l in nw_reader:
    pw  = l[0]
    gene = l[1]

    if pw in pw_gene:
        pw_gene[pw].append(gene)
    else:
        pw_gene[pw] = [gene, ]

    if gene in gene_pw:
        gene_pw[gene].append(pw)
    else:
        gene_pw[gene] = [pw, ]
    

bipartite_nw = []

for pw in pw_gene:
    pw1 = pw
    for gene in pw_gene[pw]:
        connection = gene
        for pw2 in gene_pw[gene]:
            if pw1 != pw2:

                if pw1 in pw_enrichment:
                    pw1_enr = pw_enrichment[pw1]
                else:
                    pw1_enr = 0

                if pw2 in pw_enrichment:
                    pw2_enr = pw_enrichment[pw2]
                else:
                    pw2_enr = 0


                if connection in gene_enrichment:
                    bipartite_nw.append( (pw1, pw1_enr,
                                          connection, gene_enrichment[connection],
                                          pw2, pw2_enr ))
        


for l in bipartite_nw:
    print "\t".join([str(j) for j in l])

#from pprint import pprint
#pprint(bipartite_nw)
