# Breast cancer studies

## Objetive

<p>The main objective of this work is to generate a wide range of transcriptional genetic networks that help us to understand the dynamics of genetic interaction in primary stages of breast cancer. This proyect focuses on the information generated from a database of 880 breast tissue microarrays (Affymetrix HGU133-A), 61 healthy tissue and diseased tissue in 819 primary stage.</p>

## Tools

<p>We use <a href="http://wiki.c2b2.columbia.edu/califanolab/index.php/Software/ARACNE">ARACNE</a> algoritm from <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> thats estimate Mutual Information for Gene Network reconstruction.</p>

<p>We wrote a script to prune the networks generated with a value of p / MI we desire in parallel with HTCondor.</p>

### ARACNE whit HT Condor

<p>For generate the Condor_submit File:</p>

```
python ~/breast_cancer_networks/parallel_aracne/genera_condor.py \
	--path_to_aracne2 /home/hachepunto/ARACNE/aracne2 \
	--expfile /home/hachepunto/data/Expression_Matrix_genesym_todos_sin_duplicados_colapsed.txt \
	--probes /home/hachepunto/transfac_network/human_transfacs.txt \
	--run_id transfac_all_10 \
	--outdir /home/hachepunto/transfac_network/transfac_all_10 \
	--kernel_width 0.10 \
	--p 1e-10
```

<p>For submit the run_id.condor script:</p>

<pre><code>cd $outdir
condor_submit run_id.condor
</code></pre>

<p> The kernel width must be calculate based on the number of samples and can be estimate with the formula:</p>

k = 0.525 × n^-0.24

<p>Where n is the number of samples (see more in <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> suplementary material)</p>

### Prune whit HT Condor

<p>For generate the Condor_submit File:</p>

```
python ~/breast_cancer_networks/parallel_aracne/genera_prune_condor.py \
	--adj ~/transfac_network/p1_adjs/AnimalTFDB_1.adj \
	--outdir ~/transfac_network/pruned_AnimalTFDB_1exp-10/ \
	--p 1e-10 \
	--n 880
```


<p>where:
	<p>--adj = one or more adjacency files
	<p>--outdir = directory to place condor scripts
	<p>--p = P-value: e.g. 1e-7
	<p>--n = sample size</p>


<p>In the console, a message return the value of MI which will be pruned network. For example:</p>

<pre><code>$ will generate prune scripts for mi=0.039708</code></pre>

<p>For submit the run_id.condor script:</p>

```
cd $outdir
condor_submit run_id.condor
```
