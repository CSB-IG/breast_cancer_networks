1191
====

Breast cancer studies
---------------------

<p>Una vez hechos todos los scripts con "genera_todos" se crea una carpeta donde guardaremos los scripts que llamarán cada una de las comaladas. Dentro de el se crea este archivo "todos" que contiene la lista de todos los .sh (uno por gen)</p>

<pre><code>ls ../*sh | sort | awk '{print $1" &"}' > todos
</code></pre>

<p>Se corta "todos" en tantos archivos como sea necesario para que cada lote tenga 24 scripts. La opción -d da contadores con número en vez de letras, la opción -a da el número de dígitos del contador y la opción -l los scripts por lote.</p>

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
