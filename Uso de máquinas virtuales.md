#Uso de máquinas virtuales
____________
###Ejercicio 1:
*Instalar los paquetes necesarios para usar KVM. Se pueden seguir estas instrucciones. Ya lo hicimos en el primer tema, pero volver a comprobar si nuestro sistema está preparado para ejecutarlo o hay que conformarse con la paravirtualización.*

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
*Crear varias máquinas virtuales con algún sistema operativo libre, Linux o BSD. Si se quieren distribuciones que ocupen poco espacio con el objetivo principalmente de hacer pruebas se puede usar CoreOS (que sirve como soporte para Docker) GALPon Minino, hecha en Galicia para el mundo, Damn Small Linux, SliTaz (que cabe en 35 megas) y ttylinux (basado en línea de órdenes solo).*

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


###Hacer un ejercicio equivalente usando otro hipervisor como Xen, VirtualBox o Parallels

Como ya comente  en un issue VirtualBox me ha dejado de funcionar mostrandome este error:

Por tanto voy a utilizar VMWare Player ya que se encuntra instalado en mi sistema:

![](http://pix.toile-libre.org/upload/original/1389447371.png)

![](http://pix.toile-libre.org/upload/original/1389446932.png)

![](http://pix.toile-libre.org/upload/original/1389447018.png)

![](http://pix.toile-libre.org/upload/original/1389447718.png)






