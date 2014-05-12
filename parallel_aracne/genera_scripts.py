import argparse
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('/home/hachepunto/parallel_ARACNe'))
template = env.get_template('aracne.tt')

parser = argparse.ArgumentParser(description='Prepares paralel run of aracne from a template.')
parser.add_argument('--expfile',  type=argparse.FileType('r'), required=True, help='expression file')
parser.add_argument('--affyids',  type=argparse.FileType('r'), required=True, help='gene ids, one in every line' )
parser.add_argument('--prefix',  required=True, help="prefix for scripts" )
parser.add_argument('--outdir',  required=True, help="outdir for adj matrices" )
parser.add_argument('--p',  required=True, help="P-value: e.g. 1e-7" )
parser.add_argument('--e',  required=False, help="DPIs" )

args    = parser.parse_args()
expfile = args.expfile.name
affyids = args.affyids.readlines()
prefix  = args.prefix
p       = args.p
outdir  = args.outdir

for id in affyids:

    affyid=id.strip().replace('/','_')

    scriptname = "%s_%s_%s.sh" % (prefix, affyid, p )
    with open(scriptname, 'w') as f:
        f.write( template.render( expfile = expfile,
                                  affyid = id.strip(),
                                  p = p,
                                  outdir = outdir ) )
