#Uso de máquinas virtuales
____________
###Ejercicio 1:
####*Instalar los paquetes necesarios para usar KVM. Se pueden seguir estas instrucciones. Ya lo hicimos en el primer tema, pero volver a comprobar si nuestro sistema está preparado para ejecutarlo o hay que conformarse con la paravirtualización.*

	egrep '^flags.*(vmx|svm)' /proc/cpuinfo
 o
 
    egrep -c '(vmx|svm)' /proc/cpuinfo

![](http://pix.toile-libre.org/upload/original/1389384987.png)

    josemlp@josemlp-ubuntu:~$ kvm-ok
    INFO: /dev/kvm exists
    KVM acceleration can be used

Una buena referencia es: [http://www.sismonda.com.ar/166-2012-11-20-virtualizacion-en-ubuntu-12-04-con-kvm-](http://www.sismonda.com.ar/166-2012-11-20-virtualizacion-en-ubuntu-12-04-con-kvm-)

Actualizamos el sistema:

	
	sudo apt-get update
	sudo apt-get  install kvm libvirt-bin ubuntu-vm-builder bridge-utils virt-manager virt-viewer

	sudo usermod josemlp -a -G libvirtd
    
    

###Ejercicio 2:
#####*Crear varias máquinas virtuales con algún sistema operativo libre, Linux o BSD. Si se quieren distribuciones que ocupen poco espacio con el objetivo principalmente de hacer pruebas se puede usar CoreOS (que sirve como soporte para Docker) GALPon Minino, hecha en Galicia para el mundo, Damn Small Linux, SliTaz (que cabe en 35 megas) y ttylinux (basado en línea de órdenes solo).*

	sudo modprobe kvm-intel
    
Uso dos distribuciones ligeras:
    
    http://www.slitaz.org/en/get/#stable
    http://ttylinux.net/docs.html

Creamos un ```disco duro virtual```

	qemu-img create -f raw SliTar-hdd.img 100M
.

	qemu-system-x86_64 -hda ./SliTar-hdd.img -cdrom ../Descargas/slitaz-4.0.iso -show-cursor

 ![](http://pix.toile-libre.org/upload/original/1389433505.png)
 
 
 	qemu-system-x86_64 -hda ./SliTar-hdd.img -cdrom ../Descargas/ttylinux-virtio_x86_64-16.1.iso -show-cursor
    
 ![](http://pix.toile-libre.org/upload/original/1389435158.png)
 
 Vamos a instalar una distribución más completa como es ```ElementaryOS```:
 
 
 http://elpuig.xeill.net/Members/vcarceler/articulos/qemu
 
 	qemu-img create -f qcow2 -o preallocation=metadata ElementaryOS-hdd.img 8G	
 	qemu-system-x86_64 -hda ./ElementaryOS-hdd.img -cdrom ../Escritorio/elementaryos-stable-i386.20130810.iso -show-cursor -m 2048 -smp 3

Con ``` -m 2048 -smp 3```: configuramos la memoria ram y el numero de procesadores.
 
![](http://pix.toile-libre.org/upload/original/1389437867.png)

A pesar de arrancar con esta configuración el sistema es demasiado lento como para realizar una isntalación, así que voy a probar 

 ####Configurar VMM
 
 ![](http://pix.toile-libre.org/upload/original/1389438285.png)
 
 ![](http://pix.toile-libre.org/upload/original/1389438520.png)
 
 
He de decir que es muy importante tener un minimo de espacio adicional en el disco duro anfitrion, si nó la  instalación se pausará.

Podemos ver la instalación completada.

![](http://pix.toile-libre.org/upload/original/1389442282.png)

Ya podemos arrancar directamente usnado una orden tal cual:

	sudo qemu-system-x86_64 -boot order=c -drive file=./VirtualMachines/ElementaryOS-hdd.img,if=virtio


- ####Hacer un ejercicio equivalente usando otro hipervisor como Xen, VirtualBox o Parallels

Como ya comente  en un issue VirtualBox me ha dejado de funcionar mostrandome este error:

Por tanto voy a utilizar VMWare Player ya que se encuntra instalado en mi sistema:

![](http://pix.toile-libre.org/upload/original/1389447371.png)

![](http://pix.toile-libre.org/upload/original/1389446932.png)

![](http://pix.toile-libre.org/upload/original/1389447018.png)

![](http://pix.toile-libre.org/upload/original/1389447718.png)


###Ejercicio 3:
####*Crear un benchmark de velocidad de entrada salida y comprobar la diferencia entre usar paravirtualización y arrancar la máquina virtual*

#####Por terminar


###Ejercicio 4:
####*Crear una máquina virtual Linux con 512 megas de RAM y entorno gráfico LXDE a la que se pueda acceder mediante VNC y ssh.*

Existe una distribución de Ubuntu que ya incorpora el entorno LXDE, se puede descargar de:

[http://cdimage.ubuntu.com/lubuntu/releases/13.10/release/lubuntu-13.10-desktop-amd64.iso](http://cdimage.ubuntu.com/lubuntu/releases/13.10/release/lubuntu-13.10-desktop-amd64.iso)

	qemu-img create -f qcow2 -o preallocation=metadata Lubuntu-hdd.img 8G

Una vez creado el disco duro virtual procedo como en el _ejercicio 2_, utilizando **VMM**

Aqui vemos la maquina funcionando y una terminal que muestra una conexion ssh hacia ella.

![](http://pix.toile-libre.org/upload/original/1389460604.png)



###Ejercicio 5:
#####*Crear una máquina virtual ubuntu e instalar en ella un servidor nginx para poder acceder mediante web.*

	azure vm image list

![](http://pix.toile-libre.org/upload/original/1389464081.png)

Podeis consultar todas las imagenes en:   [Documento Imagenes Azure](enlace)

Vamos a instalar Ubuntu 14.04 Server de 30 GB, que esta recien publicado:

	azure vm image show b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu_DAILY_BUILD-trusty-14_04-LTS-amd64-server-20140111-en-us-30GB

![](http://pix.toile-libre.org/upload/original/1389465360.png)

![](http://pix.toile-libre.org/upload/original/1389466503.png)

####Instalamos nginx

	sudo apt-get install nginx

Recorgemos que los html nginx los almacena por defecto en:
	
    /usr/share/nginx/html
    
 ![](http://pix.toile-libre.org/upload/original/1389468804.png)
 
 ###Ejercicio 6:
 #####*Usar juju para hacer el ejercicio anterior.*
 
 Siguiendo los pasos del siguiente manual, no consigo terminar la configuración de forma correcta.
 [https://juju.ubuntu.com/docs/config-azure.html](https://juju.ubuntu.com/docs/config-azure.html)


###Ejercicio 7:
#####*Instalar una máquina virtual Ubuntu 12.04 para el hipervisor que tengas instalado.*

	sudo vmbuilder kvm ubuntu --suite precise --flavour server -o ./virtmanager/ --hostname josemlp --domain josemlp

![](http://pix.toile-libre.org/upload/original/1389519197.png)

	sudo qemu-system-x86_64 -hda /home/josemlp/ubuntu-kvm/tmpO2zm3N.qcow2
    
  ![](http://pix.toile-libre.org/upload/original/1389519377.png)
  
  Para conectar con vinagre tal como se decia en [Problema con VNC y KVM/QEMU (#97)](Problema con VNC y KVM/QEMU (#97)), debemos conectarnos con la ip del interfaz ```virbr0 ``` en mi caso  192.168.122.1:5901"

