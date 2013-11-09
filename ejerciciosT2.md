###Ejercicio 1:

#####Crear un espacio de nombres y montar en él una imagen ISO de un CD de forma que no se pueda leer más que desde él.

Lo primero es crear el espacio de nombres, indicando -m para montajes:

~~~
sudo unshare -m /bin/bash
~~~

Creamos el directorio para el punto de montaje:

~~~
mkdir -p /mnt/disk
~~~

~~~
mount -o loop ubuntu-13.04-desktop-amd64.iso /mnt/disk
~~~

[Ejecucion](http://showterm.io/02307b2ba934177373f99#fast)


###Ejercicio 2:

#####Mostrar los puentes configurados en el sistema operativo.

Capturaa

#####Crear un interfaz virtual y asignarlo al interfaz de la tarjeta wifi, si se tiene, o del fijo, si no se tiene.

Necesitatamos tener instalado el siguiente paquete:

~~~
sudo apt-get install bridge-utils
~~~

Creamos el puente:

~~~
sudo brctl addbr wifivirtual
~~~

Asignamos interfaz al puente:

~~~
brctl addif wifivirtual wlan1
~~~

###Ejercicio 3:

#####Usar debootstrap (o herramienta similar en otra distro)
para crear un sistema mínimo que se pueda ejecutar más adelante

Tenemos que instalar antes el paquete debootstrap
~~~
sudo apt-get install debootstrap
~~~

Vamos a crear un sistema Ubuntu 13.10 (Saucy Salamander), para ello, especificamos la arquitectura,
la distribución, el directorio de instalación y la url donde se encuentra la distribución 

~~~
sudo debootstrap --arch=amd64 saucy /home/jaulas/saucy/ http://archive.ubuntu.com/ubuntu
~~~

#####Experimentar con la creación de un sistema Fedora dentro de Debian usando Rinse.

Instalamos rince: 
~~~
sudo apt-get install rince
~~~

Descargamos la distribucion de fedora:
~~~
sudo rinse --arch=i386 --distribution fedora-core-7 --directory /home/jaulas/fedora/
~~~

//captura
###Ejercicio 4:
#####Instalar alguna sistema debianita y configurarlo para su uso. 
#####Trabajando desde terminal, probar a ejecutar alguna aplicación o instalar las herramientas necesarias para compilar una y ejecutarla.

Del ejercicio donde utilizabamos "debootstrap" tengo instaladas varias jaulas con ubuntu  (saucy y quantal), por tanto voy a utilizar una de ellas.

1. Entramos en la jaula.

~~~
sudo chroot /home/jaulas/quantal
~~~

2. Debemos montar /proc para que funcione procesos tales como top.

~~~
mount -t proc proc /proc
~~~

Captura top


3. Una vez esto ya podemos instalar aplicaciones tal como estamos acostumbrados, 
como voy a crear un programita en c++, instalo un editor simple, para crear el fuente.

~~~
sudo apt-get install nano
~~~

//captura nano.

4. Instalamos compilador de c++, gcc

~~~
sudo apt-get install gcc
~~~

5. Compilamos el codigo.

//captura

Ya vemos que es simple la instalacion de aplicaciones en la jaula.
















