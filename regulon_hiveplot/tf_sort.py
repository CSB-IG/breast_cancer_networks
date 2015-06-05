import networkx as nx


TF    = [tf.strip() for tf in open('factores_de_transcripcion.txt').readlines()]
FM    = [tf.strip() for tf in open('firma_molecular_filtrada_zscore20.csv').readlines()]
resto = [tf.strip() for tf in open('resto.csv').readlines()]

# load sif file to networkx graph
H = nx.Graph()
for line in open('regulon_2WsC_cy40.sif').readlines():
    (s, t, mi) = line.strip().split()
    H.add_edge(s, t, mi=mi)

# remove self-loops
H.remove_edges_from(H.selfloop_edges())

degrees = H.degree(H.nodes())



tf  = open('tf_k_sorted.csv', 'w')
ms  = open('ms_k_sorted.csv', 'w')
etc = open('etc_k_sorted.csv', 'w')

# sort by value
for key, value in sorted(degrees.iteritems(), key=lambda (k,v): (v,k)):
    if key in TF:
        tf.write(key+"\n")

    if key in FM:
        ms.write(key+"\n")

    if key in resto:
        etc.write(key+"\n")

