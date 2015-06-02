from pyveplot import *
import networkx as nx
import random

from pprint import pprint

h = Hiveplot( 'regulon.svg')


axis0 = Axis( (900,900), (900,10), stroke="black", stroke_width=1)   # Transcription Factor
axis1 = Axis( (1100,900), (1100,10), stroke="black", stroke_width=1) # Transcription Factor again, to show inner interactions

ms_start_x = 1100
ms_start_y = 900
ms_division = Axis( (ms_start_x, ms_start_y),
                    (ms_start_x+300, ms_start_y+300),
                    stroke="green", stroke_width=1) # Molecular Signature, Gene Onthology Cell Division
ms_death    = Axis( (ms_start_x+300, ms_start_y+300),
                    (ms_start_x+600, ms_start_y+600),
                    stroke="red", stroke_width=1) # Molecular Signature, Gene Onthology Cell Death
ms_other    = Axis( (ms_start_x+600, ms_start_y+600),
                    (ms_start_x+900, ms_start_y+900),
                    stroke="black", stroke_width=1) # Molecular Signature, other GO categories

axis3 = Axis( (900,900), (10,1200), stroke="black", stroke_width=1)    # etc.

h.axes.append( [axis0, axis1] )
h.axes.append( [ms_division, ms_death, ms_other] )
h.axes.append( axis3 )

# Load sets from files
TF       = [tf.strip() for tf in open('factores_de_transcripcion.txt').readlines()]
FM       = [tf.strip() for tf in open('firma_molecular_filtrada_zscore20.csv').readlines()]
resto    = [tf.strip() for tf in open('resto.csv').readlines()]

division = [tf.strip() for tf in open('GeneOntology_CellDivision.csv').readlines()]
death    = [tf.strip() for tf in open('GeneOntology_CellDeath.csv').readlines()]



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
# TF are ordered by degree
# an even distribution, from first to last node on both TF axes
delta = 0.98 / float(len(TF))
offset = 0.01
for t in TF:
    nd = Node(t)
    axis0.add_node(nd, offset)
    nd1 = Node(t)
    axis1.add_node(nd1, offset)    
    offset += delta



    
# add nodes to molecular signature axis
# order by betweeness
btwness = nx.centrality.betweenness.betweenness_centrality(g)    

delta = 0.98 / float(len(FM))
offset = 0.01
for key, value in sorted(btwness.iteritems(), key=lambda (k,v): (v,k)):
    if key in FM:
        axis2.add_node(Node(key), offset)
        offset += delta


# add the rest of the nodes
delta = 0.98 / float(len(resto))
offset = 0.01
#for key, value in sorted(btwness.iteritems(), key=lambda (k,v): (v,k)):
for key in resto:
    if key in resto:
        axis3.add_node(Node(key), offset)
        print key, offset
        offset += delta



    

#####################
# Add edges to plot #
#####################

for e in g.edges():
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        h.connect(axis0, e[0],
                  10,  # source angle
                  axis1, e[1], 
                  -10, # target angle
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke='purple',
                  fill='none')

    if (e[0] in axis1.nodes) and (e[1] in axis2.nodes):
        h.connect(axis1, e[0],  45,
                  axis2, e[1], -45,
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke='red',
                  fill='none')
        

    if (e[0] in axis2.nodes) and (e[1] in axis3.nodes):

        h.connect(axis2, e[0], 15,
                  axis3, e[1], -15,
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke='grey',
                  fill='none')

        
    if (e[0] in axis3.nodes) and (e[1] in axis0.nodes):
        h.connect(axis0, e[1], -45,
                  axis3, e[0], 45,
                  stroke_width=g.get_edge_data(*e)['mi'],
                  stroke_opacity=g.get_edge_data(*e)['mi'],
                  stroke='blue',
                  fill='none')




        
h.save()
