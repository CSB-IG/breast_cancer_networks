1191
====

Breast cancer studies
---------------------

__Objetivo General__

<p>El objetivo central de este trabajo es generar una amplia gama de redes genéticas transcripcionales que nos ayuden a comprender la dinámica de interaccion genético en estadíos primarios de cancer de mama. Este trabajo se centra en la información generada de una base de datos de 1191 microarreglos de tejido de mama (Affymetrix HGU133-A), 61 de tejido sano y 1130 de tejido enfermo en etapa primaria.</p>

__Herramientas__

<p>Usamos el software <a href="http://wiki.c2b2.columbia.edu/califanolab/index.php/Software/ARACNE">ARACNe</a> de <a href="http://www.nature.com/nprot/journal/v1/n2/full/nprot.2006.106.html">Magnoli et al. 2006</a> que básicamente estima la información mutua (MI) entre pares de genes a lo largo de todas las muestras y con ello genera una matriz de adyacencia con el valor de MI obtenido.
</p>



__HT Condor__

Ejemplo para generar el condor submit file:

<pre><code>
python ~/breast_cancer_networks/parallel_aracne/genera_condor.py \
       --expfile /media/c/breast_cancer_networks_main/data/Expression_Matrix_22283_affyid_sanos.txt \
       --affyids /home/hachepunto/all_network/all_affyid.txt \
       --run_id sanos_10 \
       --outdir /home/hachepunto/all_network/sanos_10 \
       --p 1e-10
</code></pre>
Ejecutar este comando genera un script sanos_10.condor en $outdir. Luego hay que someterlo asi:

<pre><code>
cd $outdir
condor_submit sanos_10.condor
</code></pre>

__Optimización de sofware para el equipo de cómputo__

<p>Contamos con una computadora con 32 CPUs y 380 GB de RAM. Como cada comando de ARACNe ocupa un solo CPU y el cálculo por gen es independiente, se desarrolló una técnica para generar scripts que corrieran un gen por proceso de ARACNe a partir de una lista de genes de tal forma que pudieramos usar tantos CPUs como desearamos al mismo tiempo. Por tanto se desarrolló un script de Phyton (genera_scripts.py) que genera el script con el comando de ARACNe para un gen a la vez a partir de una lista deseada usando una plantilla (aracne.tt)
</p>
<p>Como ya se mencionó, el script "genera\_scripts.py" por si solo genera todos los scripts individuales a partir de la lista de genes a explorar. Pero como en este trabajo se requería de una gama de convinaciones de parámetros se usa un script intermedio (genera_todos.sh) que sirve para controlar las convinaciones de parametros y muestras que se van a usar.
</p>
<p>Una vez hechos todos los scripts con "genera_todos.sh" se crea una carpeta donde guardaremos los scripts que llamarán cada una de las comaladas. Dentro de el se crea este archivo "todos" que contiene la lista de todos los .sh (uno por gen)</p>

<pre><code>ls ../*sh | sort | awk '{print $1" &"}' > todos
</code></pre>

<p>Se enlistan solo los scripts. El comando "sort" es opcional y puede ayudarnos a ordenar de alguna forma particular lo sscripts. Invocamos a "awk" para añadir un "&" al final de cada renglón.

Se corta "todos" en tantos archivos como sea necesario para que cada lote tenga 24 scripts. La opción -d da contadores con número en vez de letras, la opción -a da el número de dígitos del contador y la opción -l los scripts por lote.</p>

<pre><code>split -d -a 3 -l 24 todos comalada_
</code></pre>

<p>Se genera un archivo (metacomal) que administrará el lanzamiento de los lotes con la siguiente estructura:</p>

<pre><code>date >> meta.log #genera el archivo meta.log que informa el desarrollo del proceso y le pone la fecha
echo comalada_000 >> meta.log #informa en pantalla que lote se está procesando
sh comalada_000 # echa a andar el lote
sleep 1777 # tiempo que espera antes de mandar el resto de los lotes

date >> meta.log
echo comalada_001 >> meta.log
sh comalada_001
sleep 1777

date >> meta.log
echo comalada_002 >> meta.log
sh comalada_002
sleep 1777
</code></pre>
