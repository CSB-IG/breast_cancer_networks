import argparse
import csv


parser = argparse.ArgumentParser(description='Create network of pathways connected by genes, add enrichment levels')

parser.add_argument('--network',         type=argparse.FileType('r'), required=True, help="CSV file with pw, gene, 1")
#parser.add_argument('--gene_enrichment', type=argparse.FileType('r'), required=True, help="CSV file with genes and their enrichments")
#parser.add_argument('--pw_enrichment',   type=argparse.FileType('r'), required=True, help="CSV file with pathways and their enrichments")

args = parser.parse_args()




pw_gen = {}
gen_pw = {}
nw_reader = csv.reader(args.network, delimiter="\t")
for l in nw_reader:
    pw  = l[0]
    gen = l[1]

    if pw in pw_gen:
        pw_gen[pw].append(gen)
    else:
        pw_gen[pw] = [gen, ]

    if gen in gen_pw:
        gen_pw[gen].append(pw)
    else:
        gen_pw[gen] = [pw, ]
    

for pw in pw_gen:
    pw1 = pw
    for gen in pw_gen[pw]:
        connection = gen
        for pw2 in gen_pw[gen]:
            if pw1 != pw2:
                print pw1, connection, pw2
        




# from pprint import pprint
# pprint(gen_pw)
# pprint(pw_gen)
