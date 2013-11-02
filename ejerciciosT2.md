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
mount -o loop ubuntu-13.04-desktop-amd64.iso /mnt/disk
~~~

http://showterm.io/02307b2ba934177373f99
