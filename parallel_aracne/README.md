# ARACNE whit HTCondor

<p>For generate the Condor_submit File:</p>

```
python /home/hachepunto/breast_cancer_networks/parallel_aracne/genera_condor.py \
	--aracne_tgz /home/hachepunto/ARACNE/ARACNE.src.tar.gz \
	--expfile_bz2 /home/hachepunto/rauldb/subclasificacion/her2_exp_matrix.txt.bz2 \
	--probes /home/hachepunto/rauldb/vaquerizas_plus2.txt \
	--run_id her2_1 \
	--outdir /home/hachepunto/rauldb/subclasificacion/her2_1 \
	--p 1
```

<p>For submit the run_id.condor script:</p>

<pre><code>cd $outdir
condor_submit run_id.condor
</code></pre>

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
