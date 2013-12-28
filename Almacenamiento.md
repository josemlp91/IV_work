#Virtualización del almacenamiento
===========================================

###Ejercicio 1:
_¿Cómo tienes instalado tu disco duro? ¿Usas particiones? ¿Volúmenes lógicos?_

Para consultar todos los datos de mi HDD y de sus  particiones he utilizado los siguiente comandos:

Consulto discos duros:

~~~
cat /proc/scsi/scsi
~~~

![cap1](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/josemlp@josemlp-ubuntu:%20~_006.png?raw=true)

Vemos que cuento con "tres discos duros" el primero es el disco duro original del portatil, de 500GB.

El segundo es un disco SSD de 120GB.

El tercero hace referencia al lector de targetas SD.


Usando:
~~~
sudo lsblk -fm
~~~

![cap2](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/josemlp@josemlp-ubuntu:%20~_007.png?raw=true)


Podemos ver la gerarquia de las particiones de cada disco duro.

>```sda```: es el primer disco de los anteriores, este contien 4 particiones  primarias ("que es el maximo de las posibles.") y esta destinado principalmente a __datos__.
>>```sda1```: contiene la grub de mi linux.
>>```sda2 y sda3```: son  particiones para datos personales, aislada de los sitemas operativos.
>>```sda4``` es una partición de recuperación que trae por defecto el portatil.

>> Tambien veo que tengo 2MB sin asignar.

>```sdb```:hace referencia al disco SSD, destinado principalmente a SO y programas.

>>```sdb1```: Particion primaria para Windows

>>```sdb2```: Particion extendida para Linux


>>>```sdb6```: Montaje ubuntu

>>>```sdb5```:swap ubuntu

![cap3](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/josemlp@josemlp-ubuntu:%20~_008.png?raw=true)


Podemos verlo más graficamente utilizando gparted

![cap4](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/-dev-sda%20-%20GParted_010.png?raw=true)
![cap5](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/-dev-sdb%20-%20GParted_009.png?raw=true)

_Si tienes acceso en tu escuela o facultad a un ordenador común para las prácticas, ¿qué almacenamiento físico utiliza?_

Completar cuando este en la escuela.


_Buscar ofertas SAN comerciales y comparar su precio con ofertas locales (en el propio ordenador) equivalentes._

<<<<<<< HEAD
###Ejercicio 2
Usar FUSE para acceder a recursos remotos como si fueran ficheros locales. Por ejemplo, sshfs para acceder a ficheros de una máquina virtual invitada o de la invitada al anfitrión.

Dispongo de Ubuntu Server preinstalado en una máquina virtual VirtualBox, ademas ya tiene configurado el servicio SSH, y comparto mi clave pública con dicho servidor.


Lo primero que tenemos que hacer es intalar ```sshfs``` tanto en el cliente como en el servidor, usando la orden ```sudo apt-get install sshfs```


Añadir el usuario al grupo fuse:

~~~
sudo gpasswd -a $USER fuse
~~~

Lo siguiente es consultar la ip de mi máquina virtual ```ip -s route```
~~~
192.168.1.0/24 dev eth0  proto kernel  scope link  src 192.168.1.15 
~~~

Sabemos que el usuario de la maquina virtual es ```virtual```.

Es necesario crear en el cliente un directorio que va a servirnos como punto de montaje de la unidad virtual.

~~~
mkdir DiscoVirtual
~~~

Primero probar que la conexion ssh funciona correctamente y que se identifican bien cliente y servidor.
(No es requisito que se compartan las claves RSA, pero es interesante para no tener que introducir claves cada vez que montemos la unidad.)

~~~
ssh virtual@192.168.1.15
~~~

Añadimos el usuario al grupo fuse de la maquina virtual:

~~~
sudo gpasswd -a $USER fuse
~~~

Y ya lo tenemos todo listo para crear nuestro disco duro virtual:


Ejecutamos:

~~~
sshfs virtual@192.168.1.15:/home ~/DiscoVirtual
~~~

Como vemos el disco virtual va a tener el contenido de /home de la maquina virtual.



Ademas probamos a editar los archivos y vemos como las escrituras tambien se producen de forma correcta.


=======
...
>>>>>>> 89c1543e39d2434916e04ee973836bc567156c14


