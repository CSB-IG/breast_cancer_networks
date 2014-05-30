#!/bin/bash
#Prepara al bash para el ambiente de Python
source ~/environments/paracne/bin/activate

#El que sigue es el comando básico que usa el script "genera_scripts.py" para generar los scripts por gene de una lista de genes para ARACNe:
#Phyton compila el script y dile: --expfile = donde está el archido con los datos de expresión, --affyids = Donde la lista de Affy IDs que corresponden a los genes, --prefix = como se va a etiquetar el análisis, --p con que valores de p va hacer ARACNe el corte, --outdir = Donde lo va a guardar 
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix sanos10 --p 1e-10 --outdir /home/hachepunto/autofagia/sanos10
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix sanos20 --p 1e-20 --outdir /home/hachepunto/autofagia/sanos20
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix sanos40 --p 1e-40 --outdir /home/hachepunto/autofagia/sanos40
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix sanos60 --p 1e-60 --outdir /home/hachepunto/autofagia/sanos60
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix sanos80 --p 1e-80 --outdir /home/hachepunto/autofagia/sanos80
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix sanos100 --p 1e-100 --outdir /home/hachepunto/autofagia/sanos100

python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix sanos10 --p 1e-10 --outdir /home/hachepunto/apoptosis/sanos10
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix sanos20 --p 1e-20 --outdir /home/hachepunto/apoptosis/sanos20
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix sanos40 --p 1e-40 --outdir /home/hachepunto/apoptosis/sanos40
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix sanos60 --p 1e-60 --outdir /home/hachepunto/apoptosis/sanos60
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix sanos80 --p 1e-80 --outdir /home/hachepunto/apoptosis/sanos80
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_sanos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix sanos100 --p 1e-100 --outdir /home/hachepunto/apoptosis/sanos100


python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix enfermos10 --p 1e-10 --outdir /home/hachepunto/autofagia/enfermos10
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix enfermos20 --p 1e-20 --outdir /home/hachepunto/autofagia/enfermos20
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix enfermos40 --p 1e-40 --outdir /home/hachepunto/autofagia/enfermos40
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix enfermos60 --p 1e-60 --outdir /home/hachepunto/autofagia/enfermos60
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix enfermos80 --p 1e-80 --outdir /home/hachepunto/autofagia/enfermos80
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/autofagia/autofagia_genes_affyid.txt --prefix enfermos100 --p 1e-100 --outdir /home/hachepunto/autofagia/enfermos100

python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix enfermos10 --p 1e-10 --outdir /home/hachepunto/apoptosis/enfermos10
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix enfermos20 --p 1e-20 --outdir /home/hachepunto/apoptosis/enfermos20
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix enfermos40 --p 1e-40 --outdir /home/hachepunto/apoptosis/enfermos40
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix enfermos60 --p 1e-60 --outdir /home/hachepunto/apoptosis/enfermos60
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix enfermos80 --p 1e-80 --outdir /home/hachepunto/apoptosis/enfermos80
python ~/parallel_ARACNe/genera_scripts.py --expfile /home/hachepunto/1191/Expression_Matrix_22283_affyid_enfermos.txt --affyids /home/hachepunto/apoptosis/apoptosis_genes_affyid.txt --prefix enfermos100 --p 1e-100 --outdir /home/hachepunto/apoptosis/enfermos100

#Dar permisos de ejecusión a los scripts
chmod +x *
