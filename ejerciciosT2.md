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

![Puentes red](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/mostrarPuentes.png?raw=true)

###Ejercicio 3:

#####Usar debootstrap (o herramienta similar en otra distro)
para crear un sistema mínimo que se pueda ejecutar más adelante

Tenemos que instalar antes el paquete debootstrap
~~~
sudo apt-get install debootstrap
~~~

![Instalar debbotstrp](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej3.png?raw=true)

Vamos a crear un sistema Ubuntu 13.10 (Saucy Salamander), para ello, especificamos la arquitectura,
la distribución, el directorio de instalación y la url donde se encuentra la distribución 

~~~
sudo debootstrap --arch=amd64 saucy /home/jaulas/saucy/ http://archive.ubuntu.com/ubuntu
~~~

![1](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/cap3c.png?raw=true)
![2](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/cap3b.png?raw=true)

#####Experimentar con la creación de un sistema Fedora dentro de Debian usando Rinse.

Instalamos rince: 
~~~
sudo apt-get install rince
~~~

Descargamos la distribucion de fedora:
~~~
sudo rinse --arch=i386 --distribution fedora-core-7 --directory /home/jaulas/fedora/
~~~
![3](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/fedora_con%20rince.png?raw=true)

//captura
###Ejercicio 4:
#####Instalar alguna sistema debianita y configurarlo para su uso. 
#####Trabajando desde terminal, probar a ejecutar alguna aplicación o instalar las herramientas necesarias para compilar una y ejecutarla.

Del ejercicio donde utilizabamos "debootstrap" tengo instaladas varias jaulas con ubuntu  (saucy y quantal), por tanto voy a utilizar una de ellas.

1. Entramos en la jaula.

~~~
sudo chroot /home/jaulas/quantal
~~~
![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_a.png?raw=true)

2. Debemos montar /proc para que funcione procesos tales como top.

~~~
mount -t proc proc /proc
~~~
![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_b.png?raw=true)


![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_c.png?raw=true)


3. Una vez esto ya podemos instalar aplicaciones tal como estamos acostumbrados, 
como voy a crear un programita en c++, instalo un editor simple, para crear el fuente.

~~~
sudo apt-get install nano
~~~

![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_d.png?raw=true)
![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_e.png?raw=true)

4. Instalamos compilador de c++, gcc

~~~
sudo apt-get install gcc
~~~

5. Compilamos el codigo.

![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_f.png?raw=true)


Ya vemos que es simple la instalacion de aplicaciones en la jaula.



###Ejercicio 5:
##### Instalar una jaula chroot para ejecutar el servidor web de altas prestaciones nginx.

Sigueindo los paso de : 

[Instalar nginx](https://www.digitalocean.com/community/articles/how-to-install-the-latest-version-of-nginx-on-ubuntu-12-10)

~~~
sudo apt-get install python-software-properties
sudo apt-get install software-properties-common

sudo add-apt-repository ppa:nginx/stable
sudo apt-get update
sudo apt-get install nginx
~~~

sudo service nginx start

Puede que al arrancar nginx de error:
Esto tener otra aplicacion utilizando el puerto 80, para solucionarlo utilizar

~~~
netstat -tulpn
~~~
Observamos la aplicacion que usa el puerto 80 y la detenemos

![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej5.png?raw=true)



###Ejercicio 6:
#####Crear una jaula y enjaular un usuario usando `jailkit`, que previamente se habrá tenido que instalar. 

1. Primero descargar jailkit….

~~~
wget http://olivier.sessink.nl/jailkit/jailkit-2.14.tar.gz
~~~

Despues de descargar, instalar…
~~~
tar -zxvf jailkit-2.14.tar.gz
cd jailkit-2.14
./configure
make
sudo make install
~~~
Decir que con este proceso, make me daba errores, y no era capaz de completarse la instalación.
Para solucionarlo he usado la aplicación ```alien``` que es un convertidor de paquetes de Linux.

Se instala usando: ```sudo apt-get install alien```

y lo uso para combertir el paquete a .deb dado que estoy en ubuntu:

~~~
sudo alien jailkit-2.14.tar.gz
~~~

Una vez creado ```jailkit-2.14.dev```, lo instalo directamente haciendo doble click en él, y aceptando la instalación.

Crear el directorio que contendrá el sistema enjaulado…

~~~
sudo mkdir /seguro/jaulas/dorada
sudo chown root:root:root /seguro
~~~

2. Crear el entorno

~~~
sudo jk_init -v /seguro/jaulas/dorada basicshell
sudo jk_init -v /seguro/jaulas/dorada editors
sudo jk_init -v /seguro/jaulas/dorada extendedshell
sudo jk_init -v /seguro/jaulas/dorada netutils
sudo jk_init -v /seguro/jaulas/dorada ssh
sudo jk_init -v /seguro/jaulas/dorada sftp
sudo jk_init -v /seguro/jaulas/dorada sftp

~~~

Crear el usuario y enjaularlo

~~~
adduser pardillo
sudo jk_jailuser -m -j /seguro/jaulas/dorada pardillo
~~~

Comprobar que el fichero ```/etc/passwd``` tiene la siguiente linea
~~~
pardillo:x:1001:500::/home/jail/./home/jail_user:/bin/bash
~~~
Asignar una contraseña al usuario
~~~
sudo passwd pardillo
~~~


![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/pardillo.png?raw=true)




