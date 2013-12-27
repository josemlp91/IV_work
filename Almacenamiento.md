#Virtualización del almacenamiento
===========================================

###Ejercicio 1:
_¿Cómo tienes instalado tu disco duro? ¿Usas particiones? ¿Volúmenes lógicos?_

Para consultar todos los datos de mi HDD y de sus  particiones he utilizado los siguiente comandos:

Consulto discos duros:

~~~
cat /proc/scsi/scsi
~~~

Vemos que cuento con "tres discos duros" el primero es el disco duro original del portatil, de 500GB.

El segundo es un disco SSD de 120GB.

El tercero hace referencia al lector de targetas SD.


Usando:
~~~
sudo lsblk -fm
~~~

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


Podemos verlo más graficamente utilizando gparted


_Si tienes acceso en tu escuela o facultad a un ordenador común para las prácticas, ¿qué almacenamiento físico utiliza?_

Completar cuando este en la escuela.


_Buscar ofertas SAN comerciales y comparar su precio con ofertas locales (en el propio ordenador) equivalentes._




