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





