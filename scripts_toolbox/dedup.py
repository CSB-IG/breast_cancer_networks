import argparse

parser = argparse.ArgumentParser(description='will remove lines with duplicate data regardless of key')
parser.add_argument('--input', type=argparse.FileType('r'), required=True, 
                   help='file to transpose')

args = parser.parse_args()

lineas = args.input.readlines()


p = {}
for l in lineas:
    campos = l.split()
    sample = campos[0]
    datos  = tuple(campos[1:])
    if datos in p:
        p[datos].append(sample)
    else:
        p[datos]=[sample,]


redundantes = []
for datos in p:
    if len(p[datos])>1:
        redundantes+=p[datos][1:]

for l in redundantes:
    print l
