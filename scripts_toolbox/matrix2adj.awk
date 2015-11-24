#! /usr/bin/awk -f

BEGIN{
	FS = "\t"}
# registra el encabezado en la primera linea 
NR==1{
	split($0,head,FS) #separa el primer rengl\'on y guarda en head, usando tab.
	} 


# a partir de la segunda linea encuentra el valor mayor que cero y lo imprime frente a su nombre de encabezado
NR>1{
	printf("%s\t", $1);
	for (i = 2; i <= NF; i++) if($i > 0 ) printf("%s\t%s\t", head[i],$i);
	printf(RS) # Salto de linea por default
	}
