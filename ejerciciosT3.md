###Ejercicios tema 3

**Ejercicio 1** : _Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo_

> ![Clonando LXC](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~-lxc-lxc_038.png?raw=true)

Intento instalarlo directamente desde el repositorio usando:

~~~
./autogen.sh;
./configure;
make;
make install'
~~~
Pero me da error el primer script ``./autogen.sh;`` 
[Ver error](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~-lxc-lxc_039.png?raw=true)

**Instalo LXC directamente con el gestor de paquetes ``synaptic``**

> ![Instalar LXC](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~-Escritorio_027.png?raw=true)

Comprobamos que nuestro nucleo tiene soporte para este contenedor
~~~ 
lxc-checkconfig
~~~
>![Check LXC](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~-Escritorio_028.png?raw=true)

**Vemos que nuestro nucleo está preparado.**


**Ejercicio 2** : _Comprobar qué interfaces puente se han creado y explicarlos._

Vemos que efectivamente se crea el interfaz ``lxcbr0``
Podemos usar la orden:
~~~
brctl show
~~~
Que nos muestra únicamente los interfaces puente.

O directamente ``ifconfig``, que nos muestra todos los interfaces.


![interfaz red lxc](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~_032.png?raw=true)

**Ejercicio 2** :
_Crear y ejecutar un contenedor basado en Debian._

__Creamos un nuevo contenedor, en este caso con la misma arquitectura que el sistema anfitrion__

~~~
sudo lxc-create -t ubuntu-cloud -n una-caja
~~~

![creando contenedor_ubuntu](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~-Escritorio_030.png?raw=true)


__Ya podemos arrancarlo__

~~~
sudo lxc-start -n una-caja
~~~

![arrancando contenedor ubuntu](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~_031.png?raw=true)

~~~
sudo lxc-stop -n una-caja
~~~
**Ejercicio 4** : 
_Instalar lxc-webpanel y usarlo para arrancar, parar y visualizar las máquinas virtuales que se tengan instaladas._

Siguiendo el manual: [xc-with-lxc-web-pannel-in-ubuntu](http://www.computersnyou.com/2123/2013/07/installing-lxc-with-lxc-web-pannel-in-ubuntu/)
~~~
$ sudo apt-get install lxc debootstrap bridge-utils -y
$ sudo su
$ wget http://lxc-webpanel.github.com/tools/install.sh -O - | bash
~~~

~~~
open broswer 

http://localhost:5000  
username :  admin 
password admin
~~~


![ASCII ART](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/Selecci%C3%B3n_040.png?raw=true)

Arrancamos web panel:
![lxc web panel](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/Overview%20-%20LXC%20Web%20Panel%20-%20Chromium_033.png?raw=true)

_Desde el panel restringir los recursos que pueden usar: CPU shares, CPUs que se pueden usar (en sistemas multinúcleo) o cantidad de memoria._
Modificamos la nubecilla:

![modificando nubecilla](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/jaula_vs_LXC__nginx__.png?raw=true)

**Ejercicio 5** : 
_Comparar las prestaciones de un servidor web en una jaula y el mismo servidor en un contenedor. Usar nginx._

Recordamos como creabamos la jaula:
~~~
sudo debootstrap --arch=amd64 saucy /home/jaulas/saucy/ http://archive.ubuntu.com/ubuntu
~~~

Instalamos nginx en la jaula:
[TEMA_2_ej5](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/jaula_vs_LXC__nginx__.png?raw=true)

En este caso me ha dado error y e necesitado modificar
el puerto de escucha de nginx:

~~~
Editar:
nano /etc/nginx/sites-enabled/default
listen $puertoX;
~~~

Entramos:

~~~
sudo chroot /jaulas/saucy
~~~

![arrancamos nginx en LXC](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/LXC_nginx.png?raw=true)
![arrancamos nginx en JAULA](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/nginx_jaula.png?raw=true)

Usando el siguiente manual grafico resultado Apache Benchmark [enlace](http://www.fjordan.es/graficar-resultados-de-apachebench-con-gnuplot.html)

Optenemos la siguiente grafica
![Grafica](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/benchmark.png?raw=true)


___Vemos que nginx es un poco más rápido en la jaula que en LXC container.___


**Ejercicio 6** : 
_Instalar juju._
_Usándolo, instalar MySql en un táper._


La isntalación la realizo segun nos indica los apuntes de la asignatura:

~~~
sudo add-apt-repository ppa:juju/stable
sudo apt-get update 
sudo apt-get install juju-core
~~~

Una vez ya podemos comenzar a trabajar con el:

~~~
juju init
~~~

![juju_init](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/juju_init.png?raw=true)

Para trabajar con contenedores LXC locales:

![default_local](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/juju_local.png?raw=true)



~~~
juju switch local
~~~

Es requisito para trabajar en local tener instalado MongDB

Comporbamos que efectivamente esta intalada y arrancada.

![mongo_db](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/mongoArrancado.png?raw=true)

Ya podemos crear nuestro táper y desplegar mediawiki:

~~~
juju bootstrap
juju deploy mediawiki
juju deploy mysql
juju add-relation mediawiki mysql
juju expose mediawiki
juju status
~~~

![jujustatus](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/juju_status_mediawiki.png?raw=true)


![mediawiki_juju](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/mediaWiki_funcionando.png?raw=true)

**Ejercicio 7** : 

+ Destruir toda la configuración creada anteriormente
+ Volver a crear la máquina anterior y añadirle mediawiki y una relación entre ellos.
+ Crear un script en shell para reproducir la configuración usada en las máquinas que hagan falta

Destruimos toda la configuración anterior.

~~~
sudo juju destroy-unit mysql/0
sudo juju destroy-unit mediawiki/0
~~~

o 

~~~
juju remove-unit  mysql/0 mediawiki/0
~~~

Desrtruir la máquina

~~~
juju destory-machine 2
~~~

Tambien se da la opcion de destruir todo el entorno:

~~~
juju destroy-environment -e local
~~~


Una vez que lo elinamos se nos pide volver a crear la misma configuración
pues repetimos los mismo pasos:


~~~
juju bootstrap
juju deploy mediawiki
juju deploy mysql
juju add-relation mediawiki mysql
juju expose mediawiki
juju status
~~~

__Script para automatizarlo todo__

~~~
 #!/bin/bash

if [ $# == 1 ]; then

	if [ $1 == "crear" ]; then
		juju switch local
		sudo juju bootstrap
		juju add-machine
		juju deploy mediawiki
		juju deploy mysql 
		juju add-relation mediawiki:slave mysql:db 
		juju expose mediawiki 
		juju status
		echo "[Mediawiki desplegada]"

	elif [ $1 == "destruir" ]; then

		juju unexpose mediawiki
                juju destroy-relation mediawiki:db mysql
                juju destroy-service mysql
                juju destroy-service mediawiki
		echo "[Entorno mediawiki eliminado]"

	elif [ $1 == "destruir" ]; then
		echo "[Parametro incorrecto, juju.sh <crear> | <destruit>]"
	fi

elif [ $# != 1 ]; then

	echo "[Parametro incorrecto, juju.sh <crear> | <destruit>]"
	

fi
~~~ 



**Ejercicio 8** : 
_Instalar libvirt. Te puede ayudar esta guía para Ubuntu._

~~~
sudo apt-get install kvm libvirt-bin
~~~

Añado mi usuario al grupo de libvirtd

~~~
sudo adduser josemlp libvirtd
~~~

**Ejercicio 9** :

+ Instalar un contenedor usando virt-install.

Necesitamos instalar tanto ``` virtinst``` como ```virt-viewer```
~~~
sudo apt-get install virtinst
sudo apt-get install virt-viewer
~~~

Creamos una maquina virtual Fedora19 en modo livecd
~~~
virt-install --name Fedora19_2  --ram 2048  --livecd --cdrom=./Escritorio/Fedora-Live-Desktop-x86_64-19-1.iso  --noautoconsole --nodisk
~~~

Mostamos la maquina
~~~
virt-viewer Fedora19_2
~~~

Mostamos la máquina arrancada
![virt-viewer](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/virt_viewer.png?raw=true)


[Ejemplos de virt-install](http://www.adminso.es/index.php/Creaci%C3%B3n_de_m%C3%A1quinas_virtuales_con_virt-install)