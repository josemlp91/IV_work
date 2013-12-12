#Una introducción ligera al lenguaje Ruby
================================================


###Ejercicio 1:
_Instalar Ruby y usar ```ruby --version``` para comprobar la versión instalada.
A la vez, conviene instalar también irb, rubygems y rdoc._


~~~
sudo apt-get install ruby1.9.3
~~~

###Ejercicio 2:
_Crear un programa en Ruby que imprima los números desde el 1 hasta otro contenido en una variable._

~~~
#!/usr/bin/env ruby

$i = 0
$num = 5
begin
   puts("Valor de la variable #$i" )
   $i +=1;
end until $i > $num
~~~

###Ejercicio 3:
¿Se pueden crear estructuras de datos mixtas en Ruby? Crear un array de hashes de arrays e imprimirlo.

