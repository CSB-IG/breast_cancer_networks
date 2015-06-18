import networkx as nx
import csv
from pprint import pprint

TF  = set()
ETC = set()
MS  = set()
with open('molecular.signature', 'r') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        zscore = float(row[1])
        if zscore >= 7 or zscore <= -7:
            MS.add(row[0])


# load sif file to networkx graph
g = nx.Graph()
for line in open('regulon_TCGA30.sif').readlines():
    (s, t, mi) = line.strip().split()
    g.add_edge(s, t, mi=float(mi))
    TF.add(s)
    ETC.add(t)
    
# remove self-loops
g.remove_edges_from(g.selfloop_edges())


# remove molecular signature from ETC
ETC = ETC - set(MS)

tf  = open('tf_k_sorted.csv', 'w')
ms  = open('ms_k_sorted.csv', 'w')
etc = open('etc_k_sorted.csv', 'w')

degrees = g.degree(g.nodes())
# sort by value
for key, value in sorted(degrees.iteritems(), key=lambda (k,v): (v,k)):
    if key in TF:
        tf.write(key+"\n")

    if key in MS:
        ms.write(key+"\n")

    if key in ETC:
        etc.write(key+"\n")

