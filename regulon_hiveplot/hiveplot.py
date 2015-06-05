from pyveplot import *
import networkx as nx
import random

from pprint import pprint

h = Hiveplot( 'regulon_sans_FOXN3.svg')


axis0 = Axis( (900,900), (900,10), stroke="black", stroke_width=1)   # Transcription Factor
axis1 = Axis( (1100,900), (1100,10), stroke="black", stroke_width=1) # Transcription Factor again, to show inner interactions

ms_axis = Axis( (1100, 900),
                (1900, 1200),
                stroke="black", stroke_width=1) # Molecular Signature, Gene Onthology Cell Division

axis3 = Axis( (900,900), (10,1200), stroke="black", stroke_width=1)    # etc.

h.axes = [ axis0, axis1, ms_axis, axis3]

# Load sets from files
tf  = [f.strip() for f in open('tf_k_sorted_sans_FOXN3.csv').readlines()]
ms  = [f.strip() for f in open('ms_k_sorted_sans_FOXN3.csv').readlines()]
etc = [f.strip() for f in open('etc_k_sorted.csv').readlines()]

division = [f.strip() for f in open('GeneOntology_CellDivision.csv').readlines()]
death    = [f.strip() for f in open('GeneOntology_CellDeath.csv').readlines()]



# load sif file to networkx graph
g = nx.Graph()
for line in open('regulon_100.sif').readlines():
    (s, t, mi) = line.strip().split()
    g.add_edge(s, t, mi=float(mi))

# remove self-loops
g.remove_edges_from(g.selfloop_edges())





#####################
# Add nodes to axes #
#####################

# an even distribution, from first to last node on both tf axes
delta = 0.98 / float(len(tf))
offset = 0.01
for t in tf:
    nd = Node(t)
    axis0.add_node(nd, offset)
    nd1 = Node(t)
    axis1.add_node(nd1, offset)    
    offset += delta


# Molecular Signature
delta = 0.98 / float(len(ms))
offset = 0.01
for n in ms:
    ms_axis.add_node(Node(n), offset)
    offset += delta

        

# add the rest of the nodes
delta = 0.98 / float(len(etc))
offset = 0.01
for n in etc:
    axis3.add_node(Node(n), offset)
    offset += delta



    

#####################
# Add edges to plot #
#####################

for e in g.edges():
    if g.get_edge_data(*e)['mi'] < 0:
        print g.get_edge_data(*e)['mi']
        
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        h.connect(axis0, e[0],
                  10,  # source angle
                  axis1, e[1], 
                  -10, # target angle
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke='purple',
                  fill='none')

    if (e[0] in axis1.nodes) and (e[1] in ms_axis.nodes):
        color = 'red'
        h.connect(axis1, e[0],  45,
                  ms_axis, e[1], -45,
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke=color,
                  fill='none')

        

    if (e[0] in ms_axis.nodes) and (e[1] in axis3.nodes):

        h.connect(ms_axis, e[0], 15,
                  axis3, e[1], -15,
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke='grey',
                  fill='none')

        
    if (e[0] in axis3.nodes) and (e[1] in axis0.nodes):
        color = 'blue'
        h.connect(axis0, e[1], -45,
                  axis3, e[0], 45,
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke=color,
                  fill='none')




        
h.save()
