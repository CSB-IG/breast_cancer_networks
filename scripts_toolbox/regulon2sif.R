# usage: Rscript regulon2sif.R regulon.RData salida.sif
# regulon.RData es un rdata que contiene un regulon, salida de viper

args <- commandArgs(trailingOnly = TRUE);

rdata = args[1];
outfile = args[2]
print(outfile);

load(rdata);
regulon = get(ls()[2]);

for (name in names(regulon)) {
	sif <- cbind(rep(name, length(regulon[[name]]$tfmod)), 
		names(regulon[[name]]$tfmod), 
		as.vector(regulon[[name]]$tfmod))
	write.table(sif, file = outfile, append = TRUE, quote = FALSE, sep = "\t", col.names=FALSE, row.names=FALSE);
}

