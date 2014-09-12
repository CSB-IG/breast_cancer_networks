Breast cancer studies
=====================

__Objetive__

<p>The main objective of this work is to generate a wide range of transcriptional genetic networks that help us to understand the dynamics of genetic interaction in primary stages of breast cancer. This proyect focuses on the information generated from a database of 880 breast tissue microarrays (Affymetrix HGU133-A), 61 healthy tissue and diseased tissue in 819 primary stage.</p>

__Tools__

<p>We use <a href="http://wiki.c2b2.columbia.edu/califanolab/index.php/Software/ARACNE">ARACNE</a> algoritm from <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> thats estimate Mutual Information for Gene Network reconstruction.</p>



__HT Condor__

<<<<<<< HEAD
For generate the Condor_submit File:

<pre><code>
python ~/parallel_ARACNe/genera_condor.py \
	   --path_to_aracne2 /home/hachepunto/ARACNE/aracne2
       --expfile /home/hachepunto/1191/Expression_Matrix_genesym_sanos.txt \
       --affyids /home/hachepunto/all_network/all_genesym.txt \
=======
Ejemplo para generar el condor submit file:

<pre><code>
python ~/breast_cancer_networks/parallel_aracne/genera_condor.py \
       --path_to_aracne2 ~/ARACNE/aracne2 \
       --expfile /media/c/breast_cancer_networks_main/data/Expression_Matrix_22283_affyid_sanos.txt \
       --affyids /home/hachepunto/all_network/all_affyid.txt \
>>>>>>> e5adc16cea9b6ecab2fc486cad29da98150db3e2
       --run_id sanos_10 \
       --outdir /home/hachepunto/all_network/sanos_10 \
	   --kernel_width 0.10 \
       --p 1e-10
</code></pre>

For submit the run_id.condor script:

<pre><code>
cd $outdir
condor_submit run_id.condor
</code></pre>

<p> The kernel width must be calculate based on the number of samples and can be estimate with the formula:</p>

![equation](http://www.sciweavers.org/tex2img.php?eq=k%3D0.525%20%5Ctimes%20n%5E%7B-024%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

<p>Where n is the number of samples (see more in <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> suplementary material)</p>
