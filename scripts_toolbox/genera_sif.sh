#! /bin/bash

# Uso  
# sh genera_sif.sh nombre.sif

tail -n 1 *.adj | grep -v '>' > $1_all.adj
awk '{for(i=2;i<=NF;i+=2) print $1"\t"$(i+1)"\t"$i}' $1_all.adj > $1_all.sif
