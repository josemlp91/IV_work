~~~

# Copyright (C) 2013 - Jose Miguel Lopez (josemlp@correo.ugr.es)
#    
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#   
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

~~~



Práctica 2: Aislamiento de una aplicación web.
===============================================

####Crear una mini-aplicación web y aislarlo en una jaula chroot.

En esta practica vamos a asentar muchos de lo ya trabajado en los ejercicios del tema, en particular
vamos a tratar de desplegar una jaula asignar la politica de  seguridad pertinentes a los usuarios de la jaula, 
preparar el entorno para por último instalar una aplicación web relacionada con la asignatura.


Tenemos que instalar antes el paquete debootstrap
~~~
sudo apt-get install debootstrap
~~~

~~~
sudo debootstrap --arch=i386 saucy /home/jaulas/quantal/ http://archive.ubuntu.com/ubuntu
~~~

![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/cap3b.png?raw=true)


Una vez creada la jaula. ya podemos entrar a ella con:```sudo chroot /jaulas/quantal``` y
instalar todos los recursos necesarios.

![](https://github.com/josemlp91/IV_work/blob/master/capturas_T2/ej4_b.png?raw=true)

Mi practica la voy a desarrollar utilzando un framework de python que actualmente estamos aprendiendo en otra asignatura,
se llama webpy y lo encontramos en [webpy](http://webpy.org/), este framework destaca por ser simple a la par de potente.

Ademas webpy arranca directamente un servidor web, lo que nos evita tener que configurar otro servidor web, independiente.

Lo primero que instalamos es el interprete de python

###Intalacion recursos imprescindibles

Python
~~~~
sudo apt-get install python
~~~

Intalamos el framework propiamente.

Webpy
~~~
$ wget http://webpy.org/static/web.py-0.37.tar.gz
$ tar xvzf web.py-0.37.tar.gz
$ cd web.py-0.37
$ sudo python setup.py install
~~~

![](https://github.com/josemlp91/practica2/blob/master/cap_practica/instalando_webpy.png?raw=true)

Para instalar otras librerias distintas es interesante tener instalado ```easy_install``` y ```pip```

Pip
~~~
sudo apt-get install python-setuptools python-dev build-essential 
sudo easy_install pip 
~~~

Libreria que maneja los templates.

Mako
~~~
pip install Mako
~~~

Comprobar que todo funciona:

![](https://github.com/josemlp91/practica2/blob/master/cap_practica/mako_web_funcionado.png?raw=true)


###Usuarios:

Ahora nos vamos a ocupar de los usuarios que van a trabajar en la jaula.

Creamos el usuario:
~~~
useradd -s /bin/bash -m -d /home/jaulas/quantal/./home/user_limit -c "Usuario limitado" -g users user_limit
~~~
conectamos por ssh y vemos que se puede "escapar"

~~~
ssh user_limit@localhost
~~~

![](https://github.com/josemlp91/practica2/blob/master/cap_practica/usuario_se_escapa.png?raw=true)

El usuario "enjaulado" puede acceder a todo el sistema


//captura

###Configuramos ssh para evitar que el usuario enjaulado, al conectarse por ssh, pueda acceder a todo el sistema.


~~~
Editamos /etc/ssh/sshd_conf

Match User user_limit
	ChrootDirectory /home/jaulas/quantal
	X11Forwarding no
	AllowTcpForwarding no
~~~
~~~
sudo service ssh restart
~~~

![](https://github.com/josemlp91/practica2/blob/master/cap_practica/usuario_bien_enjaulado.png?raw=true)

Para llevar a cabo esta última configuración me he apollado en la experiencia de algunos compañeros, y tambien el 
siguiente enlace [restrict ssh users](http://unix.stackexchange.com/questions/53409/how-to-restrict-ssh-users-to-browse-only-home-u-contents)

###Movemos la aplicacion a la jaula.

Movemos el proyecto a la jaula.
~~~
scp -r iv user_limit@localhost:/
~~~

Nos encontramos con un poroblema y es que el usuario "user_limit" no tiene permiso para ejecutar.
¿Como ejecutamos nuestra aplicacion python? Como dice nuestro compañero [oskyar](https://github.com/oskyar)¡¡¡ADIVINA ADIVINANZA!!!

Pues le hacemos caso y ejecutamos:

~~~
sudo chown -R root:root /home/jaulas/quantal/
~~~

~~~

~~~
###Arrancamos aplicación

~~~
python practica.py
~~~
Nos lanza el servidor web, con la aplicación corriendo.

![](https://github.com/josemlp91/practica2/blob/master/cap_practica/funcionando.png?raw=true)


###Enlaces:

[Enlace repositorio Git](https://github.com/josemlp91/practica2/)

