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

~~~
sudo lxc-create -t ubuntu-cloud -n nubecilla
~~~

![creando contenedor_ubuntu](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~-Escritorio_030.png?raw=true)


![arrancando contenedor ubuntu](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/josemlp@josemlp-ubuntu:%20~_031.png?raw=true)

![ASCII ART](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/Selecci%C3%B3n_040.png?raw=true)

![lxc web panel](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/Overview%20-%20LXC%20Web%20Panel%20-%20Chromium_033.png?raw=true)


![modificando nubecilla](https://github.com/josemlp91/IV_work/blob/master/capturas_T3/Una-caja%20-%20LXC%20Web%20Panel%20-%20Chromium_037.png?raw=true)
