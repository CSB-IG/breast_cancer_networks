import argparse
import csv


parser = argparse.ArgumentParser(description='find synergistic interactions')

parser.add_argument('--bi_enriched_network',         type=argparse.FileType('r'), required=True, help="CSV file with bipartite enriched network")

args = parser.parse_args()



i_reader = csv.reader(args.bi_enriched_network, delimiter="\t")
for l in i_reader:
    if float(l[1]) >= 0 and float(l[3]) >= 0 and float(l[5]) >= 0:
        status = "A"
    elif float(l[1]) >= 0 and float(l[3]) >= 0 and float(l[5]) < 0:
        status = "B"
    elif float(l[1]) >= 0 and float(l[3]) < 0 and float(l[5]) >= 0:
        status = "C"
    elif float(l[1]) < 0 and float(l[3]) < 0 and float(l[5]) < 0:
        status = "D"
    elif float(l[1]) < 0 and float(l[3]) < 0 and float(l[5]) >= 0:
        status = "E"
    elif float(l[1]) < 0 and float(l[3]) >= 0 and float(l[5]) < 0:
        status = "F"
    elif float(l[1]) >= 0 and float(l[3]) < 0 and float(l[5]) < 0:
        status = "E"
    elif float(l[1]) < 0 and float(l[3]) >= 0 and float(l[5]) >= 0:
        status = "B"

    l.append(status)
    print "\t".join(l)
