#Use: $python count_nodes_edges.py --input network_file.txt

import argparse
import networkx as nx

parser = argparse.ArgumentParser(description='count nodes and edges in a network')
parser.add_argument('--input', type=argparse.FileType('r'), required=True, 
                   help='text file "node,interaction(w),node" undirected')
#parser.and_argument('--newnet', type=argparse.FileType('w'), required=True,
#                   help='clean new network file')

args = parser.parse_args()
#writer = csv.writer(args.newnetwork)

G = nx.Graph()
edges = [l.strip().split() for l in margs.input.readlines()]

for e in edges:
    G.add_edge(e[0],e[2],weight=float(e[1]))

G.remove_edges_from(G.selfloop_edges())

print "edges = %s \nnodes = %s" % (G.number_of_edges(), G.number_of_nodes())

#    writer.writerows(args.newnet)
#args.salida.close()
