from pyveplot import *
import networkx as nx
import random

from pprint import pprint

h = Hiveplot( 'regulon085.svg')


axis0 = Axis( (1000,1000), (950,0), stroke="black", stroke_width=3)   # Transcription Factor
axis1 = Axis( (1200,1000), (1250,0), stroke="black", stroke_width=3) # Transcription Factor again, to show inner interactions

ms_axis = Axis( (1200, 1000),
                (2200, 1618),
                stroke="black", stroke_width=3) # Molecular Signature, Gene Onthology Cell Division

axis3 = Axis( (1000,1000), (0,1618), stroke="black", stroke_width=3)    # etc.

h.axes = [ axis0, axis1, ms_axis, axis3]

# Load sets from files
tf  = [f.strip() for f in open('tf_k_sorted.csv').readlines()]
ms  = [f.strip() for f in open('ms_k_sorted.csv').readlines()]
etc = [f.strip() for f in open('etc_k_sorted.csv').readlines()]

#division = [f.strip() for f in open('GeneOntology_CellDivision.csv').readlines()]
#death    = [f.strip() for f in open('GeneOntology_CellDeath.csv').readlines()]



# load sif file to networkx graph
g = nx.Graph()
for line in open('regulon_2WsC_cy40.sif').readlines():
    (s, t, mi) = line.strip().split()
    g.add_edge(s, t, mi=float(mi))

# remove self-loops
g.remove_edges_from(g.selfloop_edges())


topten= { 'HIF3A' : '9',
          'KAT7'  : '8',
          'TFDP3' : '7',
          'TBR1'  : '6',
          'ZIC3'  : '5',
          'FOXJ2' : '4',
          'IKZF3' : '3',
          'ZNF3'  : '2',
          'ZNF132': '1',
          'AGTR2' : '0', }

#####################
# Add nodes to axes #
#####################

# an even distribution, from first to last node on both tf axes
delta = 0.98 / float(len(tf))
offset = 0.01
for t in tf:
    nd = Node(t)
    axis0.add_node(nd, offset)

    if t in topten:
        nd.dwg.add(nd.dwg.circle(center=(nd.x, nd.y), r=10, stroke="black", stroke_width=1, fill="white", opacity=1))
        nd.dwg.add(nd.dwg.text(topten[t], insert=(nd.x-4, nd.y+4)))

    
    nd1 = Node(t)
    axis1.add_node(nd1, offset)

    if t in topten:
        nd1.dwg.add(nd1.dwg.circle(center=(nd1.x, nd1.y), r=10, stroke="black", stroke_width=1, fill="white", opacity=1))
        nd1.dwg.add(nd1.dwg.text(topten[t], insert=(nd1.x-4, nd1.y+4)))
    
    offset += delta


# Molecular Signature
delta = 0.98 / float(len(ms))
offset = 0.01
for n in ms:
    nd1 = Node(n)
    ms_axis.add_node(nd1, offset)

    if n in topten:
        nd1.dwg.add(nd1.dwg.circle(center=(nd1.x, nd1.y), r=10, stroke="black", stroke_width=1, fill="white", opacity=1))
        nd1.dwg.add(nd1.dwg.text(topten[n], insert=(nd1.x-4, nd1.y+4)))
    
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


    if abs(g.get_edge_data(*e)['mi']) < 0.85:
        continue

    
    # TF to TF
    if (e[0] in axis0.nodes) and (e[1] in axis1.nodes):
        h.connect(axis0, e[0],
                  10,  # source angle
                  axis1, e[1], 
                  -10, # target angle
                  stroke_width=0.5,
                  stroke_opacity=0.3,
                  stroke='limegreen',
                  fill='none')

    # TF to MS
    if (e[0] in axis1.nodes) and (e[1] in ms_axis.nodes):
        if not ((e[0] in tf) and (e[1] in tf)):
            color = 'crimson'
            h.connect(axis1, e[0],  45,
                      ms_axis, e[1], -45,
                      stroke_width=0.5,
                      stroke_opacity=0.3,
                      stroke=color,
                      fill='none')

        

    if (e[0] in ms_axis.nodes) and (e[1] in axis3.nodes):
        if (e[0] in tf) and (e[1] in tf):
            color = 'limegreen'
        else:
            color = 'royalblue'

        h.connect(ms_axis, e[0], 15,
                  axis3, e[1], -15,
                  stroke_width=0.5,
                  stroke_opacity=0.3,
                  stroke=color,
                  fill='none')

        
    if (e[0] in axis3.nodes) and (e[1] in axis0.nodes):
        if (e[0] in tf) and (e[1] in tf):
            color = 'limegreen'
        else:
            color = 'purple'

        h.connect(axis0, e[1], -45,
                  axis3, e[0], 45,
                  stroke_width=0.5,
                  stroke_opacity=0.3,
                  stroke=color,
                  fill='none')




for e in g.edges():

    if abs(g.get_edge_data(*e)['mi']) < 0.85:
        continue

    # TF to MS
    if (e[0] in axis1.nodes) and (e[1] in ms_axis.nodes):
        if (e[0] in tf) and (e[1] in tf):
            color = 'limegreen'
            h.connect(axis1, e[0],  45,
                      ms_axis, e[1], -45,
                      stroke_width=0.5,
                      stroke_opacity=0.9,
                      stroke=color,
                      fill='none')
        



        
h.save()
