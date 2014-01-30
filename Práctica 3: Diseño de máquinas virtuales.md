#Práctica 3: Diseño de máquinas virtuales
________________


##Motivación.

Durante los  temas anterior hemos visto las distintas posibilidades que tenemos para crear maquinas virtuales, segun la necesidades que tengamos, pudiendolo hacer de forma local o utilizando servicios en la nuve como el que nos proporciona Windows Azure.

Lo que me empuja a  utilizar  máquinas virtuales en la nube para realizar esta practica, ha sido que tras mi experiencia en los ejercicios de creación de maquinas virutales locales, he visto que mis recursos de almacenamiento son muy reducidos y  me da para instalar pocas máquinas.
Los recursos de CPU  y RAM tambien me son  limitado y cuando inicio varias máquinas virtuales simultaneamente, tengo problemas para poder seguir trabajando de forma cómoda.

Tambien creo que seria muy interesante habituarme ha realizar configuraciones de forma remota, así como realizar script que lo automaticen.

##Introdución.

Mi idea consiste en montar varias máquinas virtuales con distintas distribuciones linux, (ubuntu, centOS ), y instalarlos cada uno usando 2 configuraciones distintas, de entre las que me permite Azure. (Small, Large ).

Una vez que esten instaladas voy a desplegar una aplicación web que he desarrollado en la asignatura de DAI, programada en python utilizando el micro-framework ```Web.py``` y utiliza bases de datso noSql ```mongoDB```.

Por tanto tengo que realizar toda la instalación y configuración de python junto con todas las librerias que  se  utilizan (rss, twitter, maku, anydb, feedparser), ademas voy a crear un servidor MongoDB en la propia máquina por lo cual, tambien hay que configurarlo.

La aplicación web esta alojada en este propio repositorio por tanto tambien debemos instalar ```git``` y clonar de [https://github.com/josemlp91/practica3IV](https://github.com/josemlp91/practica3IV)

Tabien deberemos instalar y configurar el servidor MongoDB.

##Instalación de una de las máquinas Virtuales Azure.

Voy a explicar el proceso que sigo para crear y instalar  las máquinas virtuales en Azure, la instalación de la aplicación web que he comentado.

###Crear la maquina virtual.

Vamos ha hacer la instalación desde la interfaz web que nos ofrece Azure.

####**1. Seleccionar crear una máquina desde galeria.**
![](http://pix.toile-libre.org/upload/original/1389535129.png)

####**2. Seleccionamos la distribución que nos interese.**

![](http://pix.toile-libre.org/upload/original/1389535260.png)

####**3. Seleccionar la configuración

![](http://pix.toile-libre.org/upload/original/1389535519.png)

####**4. Configuración 2**

![](http://pix.toile-libre.org/upload/original/1389535703.png)


####**5. Abrimos la "puerta"**

Puersto que ahora mismo el servidor web va a funcionar desde el puerto 8080 asi lo tenemos que configurar.

![](http://pix.toile-libre.org/upload/original/1389540672.png)

###**5. Entrar e la maquina mediante SSH**

![](http://pix.toile-libre.org/upload/original/1389538997.png)


####**6. Vemos la información de la CPU y la memoria.

![](http://pix.toile-libre.org/upload/original/1389539073.png)
![](http://pix.toile-libre.org/upload/original/1389539205.png)

####**7. Intalación aplicación web.

- Instalamos git 
		sudo apt-get install git
- Clonamos el repositorio
		git clone https://github.com/josemlp91/practica3IV
        
- Instalamos librerias:
       	sudo apt-get install  python-dev
        sudo apt-get install python-pip
        
       	pip install web.py
        pip install mako
        pip install pymongo
        pip install lxml
        pip install tweepy
        pip install feedparser

- Intalamos MongoDB
		wget http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz
        tar xzvf mongodb-linux-x86_64-2.4.9.tgz
        
        
- En funcionamiento:

![](http://pix.toile-libre.org/upload/original/1389540556.png)


## Evaluar prestaciones servidor web

Para evaluar las prestaciones de un servidor web existen distintas herramienas.

- Apache Beckmark
- httperf
- OpenWebLoad
- ApacheJMeter.

Voy a utilizar apache beckmark que es una de las más populares y es potente.


	ab -n $N -c $C ${maquina}

- $N:  el numero de periciones que hacemos en el test.

- $C:  la concurrencia de las peticiones
 
- ${maquina}: Dirección de la máquina, IP o dominio.

Adicionalemte podemos añadir el parametro ```-g``` para que nos guarde el resultado en un fichero.

###Carga de trabajo.

Como nos indica [antonioguirola](https://github.com/antonioguirola/practica3IV#carga-de-trabajo) Azure limita las peticiones que se le pueden hacer, y si ponemos una carga demasiada alta, las pruebas nos se realizaran de forma correcta.

- 1900 peticiones con una concurrencia de 100 simultáneas
- 2500 peticiones sin concurrencia

Voy a utilizar una carga un poco inferior para no hacer el proceso tan pesado.

 - 300 peticiones con una concurrencia de 30 simultáneas

### Ejecucion de los tests

	ab -n 300 -c 30 http://ubuntupeque.cloudapp.net:8080/ | grep -e  'Time per request:' -e 'Transfer rate: '
	
![](http://pix.toile-libre.org/upload/original/1389547331.png)

####Hacer grafica

	ab -c 20 -n 300 -g ab.txt http://ubuntupeque.cloudapp.net:8080/
	gnuplot -e 'set terminal png; set output "ab.png"; set xlabel "Petición"; set ylabel "ms"; plot "ab.txt" using 10 with lines title "Tiempo de respuesta"'


## Automatización del proceso.

Al arrancar acceder a nuestro servidor via SSH, lo primero que hacemos es:

	 sudo apt-get install -y git
     git clone https://github.com/josemlp91/practica3IV

Una vez esto ya podemos acceder a este  pequeño script: 

El script funciona tal cual tanto en Ubuntu como en CentOS.

~~~
		#!/bin/bash     
       
        sudo easy_install pip
        sudo pip install setuptools --no-use-wheel --upgrade
        
        sudo pip install web.py
        sudo pip install mako
        sudo pip install pymongo
        sudo pip install lxml
        sudo pip install tweepy
        sudo pip install feedparser
   
        wget http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz
        tar xzvf mongodb-linux-x86_64-2.4.9.tgz

~~~

###Resultados.

- ### Configuración (peque) Ubuntu Server 13.10 - Pequeño  1 core 1,75GB
~~~
Time per request:       40684.792 [ms] 
Transfer rate:             4.62 [Kbytes/sec] received
~~~
![](http://pix.toile-libre.org/upload/original/1389553055.png)



- ### Configuración (media) Ubuntu Server 13.10 - Media  3 core 3,5GB

~~~
Time per request:       28354.491 [ms]
Transfer rate: 			   6.92KB/s
~~~


![](http://pix.toile-libre.org/upload/original/1389550958.png)

-   ###Configuracion (centos peque) CentOS - Pequeño 1 core 1,75GB

Recordemos de CentOS usa el gestro de paquetes yum

- Instalamos git: ```yum install git```
- Instalamos pip:    ```sudo easy_install pip``` y ```sudo pip install setuptools --no-use-wheel --upgrade```
- Clonamos repositorio : ``` git clone https://github.com/josemlp91/practica3IV```
- Ejecutamos script ```configuraWeb.sh```



~~~
Time per request:       8509.565 [ms] (mean)
Transfer rate:          22.07 [Kbytes/sec] received
~~~
![](http://pix.toile-libre.org/upload/original/1389558027.png)




- ###Configuracion (centos medio) CentOS - Media 1 core 3,5GB

~~~
Time per request:       6840.236 [ms] (mean)
Transfer rate:          27.45 [Kbytes/sec] received
~~~

![](http://pix.toile-libre.org/upload/original/1389555949.png)


![](http://pix.toile-libre.org/upload/original/1389562641.png)

##Conclusión

Como conclusión puedo expresar la sorprendenter mejora en la respuesta utilizando CentOS, reduciendo el tiempo de respues en mas de la mitad, respesto al la diferencia entre maquinas con la misma distribución podemos ver una diferencia sustancial entre la de menor y mayor recurso.











