import argparse
import os, stat
from math import log
from jinja2 import Environment, FileSystemLoader

parser = argparse.ArgumentParser(description='Prune interaction below given threshold.')
parser.add_argument('--adj',  type=argparse.FileType('r'), required=True, help='one or more adjacency files')
parser.add_argument('--outdir',  required=True, help="directory to place condor scripts" )
parser.add_argument('--p',  required=True, help="P-value: e.g. 1e-7" )
parser.add_argument('--n',  required=True, help="sample size" )

args    = parser.parse_args()

# compute mi value, from bootstrap Aldo Huerta 2014
alfa  = 1.062
beta  = -48.7
gamma = -0.634
p     = float(args.p)
n     = int(args.n)
mi = (alfa - log(p)) / ((-beta) + (-gamma)*n)
print "will generate prune scripts for mi=%f" % mi


# use same dir as this file's as environment, load template
env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.realpath(__file__))))
template = env.get_template('prune_adj.tt')




# create output dir
if not os.path.exists(args.outdir):
    os.makedirs(args.outdir)
os.chdir(args.outdir)


# create one prune script per line
lineas = args.adj.readlines()

for linea in lineas:
    if not linea.startswith('>'):
        gene_line = linea.strip()
        gene_list = gene_line.split()
        gene_id = gene_list[0]

        with open("condor_%s_prune.py" % gene_id, 'w') as f:
            f.write( template.render( gene_line = gene_line,
                                      p         = args.p,
                                      mi        = "%f" % mi ) )


        
