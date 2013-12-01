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

![modificando nubecilla](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/Una-caja%20-%20LXC%20Web%20Panel%20-%20Chromium_037.png?raw=true)

**Ejercicio 5** : 
_Comparar las prestaciones de un servidor web en una jaula y el mismo servidor en un contenedor. Usar nginx._

Recordamos como creabamos la jaula:
~~~
sudo debootstrap --arch=amd64 saucy /home/jaulas/saucy/ http://archive.ubuntu.com/ubuntu
~~~

Instalamos nginx en la jaula:
[TEMA_2_ej5](https://github.com/josemlp91/IV_work/blob/master/ejerciciosT2.md#ejercicio-5)

Entramos:
~~~
sudo chroot /jaulas/saucy
~~~

