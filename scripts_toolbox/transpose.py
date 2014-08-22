import argparse
import numpy as np

parser = argparse.ArgumentParser(description='print to stdout transposed file')
parser.add_argument('--input', type=argparse.FileType('r'), required=True, 
                   help='file to transpose')

args = parser.parse_args()

lineas = args.input.readlines()

arreglote = []
for i in range(0,len(lineas)):
    columnas = lineas[i].split()
    arreglote.append([])
    for j in range(0,len(columnas)):
        arreglote[i].append(columnas[j])
        

t = np.array(arreglote)


for renglon in t.swapaxes(0,1):
    print "\t".join(renglon)

