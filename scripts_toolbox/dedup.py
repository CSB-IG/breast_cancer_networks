import argparse
import numpy as np
import pprint

parser = argparse.ArgumentParser(description='will remove lines with duplicate data regardless of key')
parser.add_argument('--input', type=argparse.FileType('r'), required=True, help='file to process')

args = parser.parse_args()

lineas = args.input.readlines()

arreglote = []
for l in lineas:
    columnas = l.split()
    arreglote.append(columnas)


swapped = np.array(arreglote).swapaxes(1,0)

# count duplicate keys for same sets of values
p = {}
for campos in swapped:
    sample = campos[0]
    data  = tuple(campos[1:])
    if data in p:
        p[data].append(sample)
    else:
        p[data]=[sample,]


redundantes = []
for datos in p:
    if len(p[datos])>1:
        redundantes+=p[datos][1:]


tmp = []
for l in swapped:
    sample = l[0]
    if not sample in redundantes:
        tmp.append(l)
    
unswapped = np.array(tmp).swapaxes(1,0)

for l in unswapped:
    print '\t'.join(l)
