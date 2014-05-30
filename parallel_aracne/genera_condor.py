import argparse
import os
from shutil import copy
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('/home/hachepunto/parallel_ARACNe'))
template = env.get_template('condor_aracne.tt')

parser = argparse.ArgumentParser(description='Generates condor submit file for aracne runs.')
parser.add_argument('--expfile',  type=argparse.FileType('r'), required=True, help='expression file')
parser.add_argument('--affyids',  type=argparse.FileType('r'), required=True, help='gene ids, one in every line' )
parser.add_argument('--run_id',  required=True, help="name of condor run" )
parser.add_argument('--outdir',  required=True, help="outdir for adj matrices" )
parser.add_argument('--p',  required=True, help="P-value: e.g. 1e-7" )

args    = parser.parse_args()
expfile = args.expfile.name
p       = args.p
outdir  = args.outdir

affyids = []
for id in args.affyids.readlines():
    affyids.append( id.strip() )
    
if not os.path.exists(outdir):
    os.makedirs(outdir)

copy('/home/hachepunto/parallel_ARACNe/aracne.sh', outdir)

scriptname = "%s/%s.condor" % (outdir, args.run_id)
with open(scriptname, 'w') as f:
    f.write( template.render( expfile = expfile,
                              affyids = affyids,
                              p       = p,
                              outdir  = outdir,
                              run_id  = args.run_id ) )



