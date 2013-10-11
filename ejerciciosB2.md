### Ejercicio 7

1. Crear diferentes grupos de control sobre un sistema operativo Linux. 
   
	Para crear los grupos de control me resulta más cómodo usar libcgroup, para evitarnos
	tener que trabajar directamente con los sitemas de ficheros virtuales.


Instalar cgroup en ubuntu

~~~	
sudo apt-get install cgroup-bin 
~~~

Podemos consultar que efectivamente exites el directorio 

~~~
ls -l /sys/fs/cgroup/cpuacct
~~~


Creamos los subgrupos para cada una de los distintos tipos de aplicaciones:

~~~
sudo cgcreate -g memory,cpu,cpuacct:ejer7IV/navegado	 
sudo cgcreate -g memory,cpu,cpuacct:ejer7IV/editor	 
sudo cgcreate -g memory,cpu,cpuacct:ejer7IV/apliInten
~~~
     
Ejecutamos los programas de cada tipo en el subgrupo.

~~~
sudo cgexec -g memory,cpu,cpuacct:ejer7IV/navegador chromium-browser --user-data-dir /home &
sudo cgexec -g memory,cpu,cpuacct:ejer7IV/editor /home/josemlp//Sublime\ Text\ 2/sublime_text &
sudo cgexec -g memory,cpu,cpuacct:ejer7IV/apliInten  /home/josemlp/Escritorio/ejer_python/m.py & 
~~~

Podemos consultar los resultados en:
~~~
ls -l/sys/fs/cgroup/cpuacct/ejer7IV
~~~
------------------------------------------------
**Ejecucion en el siguiente enlace:**

Paso 1:
<http://showterm.io/290927702e253143ef3c0#fast>

Paso 2:
<http://showterm.io/8b826266caa48b5a66bd1#fast>


Paso 3:
<http://showterm.io/9d4def54f06cd45b49c70#fast>

##### Tabla consumo de recursos distintas aplicaciones#####

| Recuros             | Chromium | Sublime Text   | Mandelbrot.py
| :-------            | :------: | -----:         |-----:         
|cpuacct.usage_percpu | 13181653556 6499539992 11944331085 6010034198 | 1491227726 794997556 830199868 652466764 | 125306944410 169694806577 246520653233 110845284318
|cpuacct.stat         | user 121 system 19    | user 120 system 13         | user 65357  system 15
|cpuacct.usage        | 39537256881    | 4569691585  |  654111370098
|memory.max_usage_in_bytes  | 470978560     | 63188992 | 107446272


> pendiente segundo apartado

2 .Calcular el coste real de uso de recursos de un ordenador teniendo en cuenta sus costes de amortización.
Añadir los costes eléctricos correspondientes.

### Ejercicio 8
___Discutir diferentes escenarios de limitación de uso de recursos o de asignación de los mismos a una u otra CPU.___

>> Mi idea es hacer una aproximación de los recursos de un dispositivo con recursos limitados, (como un smartphone),
un ejemplo seria que estamos desarrollando una aplicación web responsive, destina a una empresa 
donde sabemos que el 70% de los empleados que la van a usar, van interactuar con ella desde sus smartphones, 
(con una cpu y una ram muy por debajo de las maquinas del entorno de producción), podemos tomar la decisión de limitar el entorno de producción
para que se adapte mejor, y ahorrar costes al tener solo los recursos justos a lo que se nos requiere.

>>Otra idea que se me ocurre, es limitar los recursos para tener una reserva,
para situaciones donde sabemos que se va a requerir de más recursos. Un ejemplo el servidor de "una tienda virtual"
donde sabemos que en verano se usa muy poco, podemos disminuir el porcentaje de CPU y la RAM,
y en la época de navidad hacer una asignacion de recursos máxima.


