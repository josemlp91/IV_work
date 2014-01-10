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


![ubuntu_server](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/virtual@josemlpVirtual:%20~_014.png?raw=true)


Añadimos el usuario al grupo fuse de la maquina virtual:

~~~
sudo gpasswd -a $USER fuse
~~~

Y ya lo tenemos todo listo para crear nuestro disco duro virtual:


Ejecutamos:

~~~
sshfs virtual@192.168.1.15:/home ~/DiscoVirtual
~~~

![sshfs](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/josemlp@josemlp-ubuntu:%20~_016.png?raw=true)

No informa que el punto de montaje no esta vacio.

Como vemos el disco virtual va a tener el contenido de /home de la maquina virtual.

![nautilus](https://github.com/josemlp91/IV_work/blob/master/capturas_T4/virtual_017.png?raw=true)


Ademas probamos a editar los archivos y vemos como las escrituras tambien se producen de forma correcta.

###Ejercicio 3
*Crear imágenes con estos formatos (y otros que se encuentren tales como VMDK) y manipularlas a base de montarlas o con cualquier otra utilidad que se encuentre.*

Para crear imagenes en formato raw uso:
	
    fallocate -l 100M imagenfallocate.img 
    
Para crear imagenes de forma facil en distintos formatos voy a usar ```gemu-img```

Estas son las caracteristicas de los formatos que soporta gemu-img.

-  raw: 
> El formato de imagen del disco crudo (predeterminado). Este formato tiene la ventaja de ser sencillo y de fácil exportación a los demás emuladores. Si su sistema de archivos admite huecos (por ejemplo en ext2 o ext3 en Linux o NTFS en Windows), entonces sólo los sectores escritos reservarán espacio. _Tal como se dice en los apuntes_. Use qemu-img info para concocer el tamaño real utilizado por la imagen o ls -ls en Unix/Linux. 

- qcow2:
>El formato de imagen QEMU, el formato más versatil. Utilícelo para imágenes más pequeñas (útil si su sistema de archivos no admite huecos, por ejemplo: en Windows), encriptación opcional AES, compresión basada en zlib y soporte de múltiples instantáneas de VM.

- qcow: 
>Formato anterior de imagen QEMU. Sólo se incluye para compatibilidad con versiones anteriores.

- cow
>El formato de imagen User Mode Linux Copy On Write. El formato cow se incluye sólo por compatibilidad con versiones anteriores. No funciona con Windows.

- vmdk
>Formato de imagen compatible de VMware 3 y 4.

- cloop
>Imagen Linux Compressed Loop, útil únicamente para reutilizar directamente imágenes comprimidas de CD-ROM, presentes por ejemplo, en los Knoppix CD-ROM.


	qemu-img create -f qcow2 qcowImage.qcow2 5M 
    qemu-img create -f vdi vdiImage.vdi 5M    
    qemu-img create -f vmdk vmdkImage.vmdk 100M
    
    
![qemu-img](http://pix.toile-libre.org/upload/original/1389347480.png)

Voy a montar la última imagen creada en ```VMWare Player```.

![vmware](http://pix.toile-libre.org/upload/original/1389348369.png)

###Ejercicio 4
*Crear uno o varios sistema de ficheros en bucle usando un formato que no sea habitual (xfs o btrfs) y comparar las prestaciones de entrada/salida entre sí y entre ellos y el sistema de ficheros en el que se encuentra, para comprobar el overhead que se añade mediante este sistema.*

Primeramente creamos las imagenes:

	qemu-img create -f raw btrfs.img 200M
	qemu-img create -f raw xfs.img 200M
    
![](http://pix.toile-libre.org/upload/original/1389349646.png)

Ahora tenemos que convertirlas en dispositivos loop usando losetup.

	sudo losetup -v -f btrfs.img
    	"El dispositivo de bucle es /dev/loop0"
        
    sudo losetup -v -f xfs.img
    	"El dispositivo de bucle es /dev/loop1"

![](http://pix.toile-libre.org/upload/original/1389349816.png)

Formateamos las unidades.

Hay que instalar ```sudo apt-get install xfsprogs``` y ```sudo apt-get install btrfs-tools``

	sudo mkfs.xfs /dev/loop0
	sudo mkfs.btrfs /dev/loop1
    
    ![](http://pix.toile-libre.org/upload/original/1389350365.png)
    
    
    
    
    



    
    
