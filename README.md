# Breast cancer studies

## Objetive

<p>The main objective of this work is to generate a wide range of transcriptional genetic networks that help us to understand the dynamics of genetic interaction in primary stages of breast cancer. This proyect focuses on the information generated from a database of 880 breast tissue microarrays (Affymetrix HGU133-A), 61 healthy tissue and diseased tissue in 819 primary stage.</p>

## Tools

<p>We use <a href="http://wiki.c2b2.columbia.edu/califanolab/index.php/Software/ARACNE">ARACNE</a> algoritm from <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> thats estimate Mutual Information for Gene Network reconstruction.</p>

<p>We wrote a script to prune the networks generated with a value of p / MI we desire in parallel with HTCondor.</p>