Breast cancer studies
=====================

__Objetive__

<p>The main objective of this work is to generate a wide range of transcriptional genetic networks that help us to understand the dynamics of genetic interaction in primary stages of breast cancer. This proyect focuses on the information generated from a database of 880 breast tissue microarrays (Affymetrix HGU133-A), 61 healthy tissue and diseased tissue in 819 primary stage.</p>

__Tools__

<p>We use <a href="http://wiki.c2b2.columbia.edu/califanolab/index.php/Software/ARACNE">ARACNE</a> algoritm from <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> thats estimate Mutual Information for Gene Network reconstruction.</p>



__HT Condor__

<p>For generate the Condor_submit File:</p>

<pre><code>
python ~/breast_cancer_networks/parallel_aracne/genera_condor.py \
	--path_to_aracne2 /home/hachepunto/ARACNE/aracne2 \
	--expfile /home/hachepunto/data/Expression_Matrix_genesym_todos_sin_duplicados_colapsed.txt \
	--probes /home/hachepunto/transfac_network/human_transfacs.txt \
	--run_id transfac_all_10 \
	--outdir /home/hachepunto/transfac_network/transfac_all_10 \
	--kernel_width 0.10 \
	--p 1e-10
</code></pre>

For submit the run_id.condor script:

<pre><code>
cd $outdir
condor_submit run_id.condor
</code></pre>

<p> The kernel width must be calculate based on the number of samples and can be estimate with the formula:</p>

k=0.525 × n^-0.24

<p>Where n is the number of samples (see more in <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> suplementary material)</p>
