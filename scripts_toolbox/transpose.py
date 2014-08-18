import argparse

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
        



for i in range(0,len(arreglote)):
    filas = arreglote[i]
    renglon = []
    for j in range(0,len(filas)):
        try:
            renglon.append(arreglote[j][i])
        except:
            pass
    if renglon:
        print "\t".join(renglon)


