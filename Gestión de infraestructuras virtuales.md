
#Gestión de infraestructuras virtuales
_____________

##Ejercicio 1
###Instalar chef en la máquina virtual que vayamos a usar.

	sudo apt-get install ruby1.9.1 ruby1.9.1-dev rubygems
    sudo gem install ohai chef
    sudo su
    curl -L https://www.opscode.com/chef/install.sh | bash
    exit
    
    

    
 
##Ejercicio 2
###Crear una receta para instalar nginx, tu editor favorito y algún directorio y fichero que uses de forma habitual.

	
	mkdir -p chef/cookbooks/nginx/recipes
    mkdir -p chef/cookbooks/nano/recipes
    mkdir -p chef/cookbooks/doc/recipes
    
    echo package \'nginx\' >  ./cookbooks/nginx/recipes/default.rb
	echo package \'nano\' >  ./cookbooks/nano/recipes/default.rb

	nano ./cookbooks/doc/recipes/default.rb
--

    directory 'home/datos'
	file "home/datos/holachef.txt" do
        owner "josemlp"
        group "josemlp"
        mode 00777
        action :create
        content "texto"
	end
--    

	nano ./cookbooks/nginx/metadata.rb
	
--  

	maintainer       "Jose Miguel Lopez"
	maintainer_email "josemlp@correo.ugr.es"
	description      "Instala servidor web nginx"
	version          "0.1"

	recipe "nginx", "Despliegue servidor web"    
--    
Repetir con:

	nano ./cookbooks/nano/metadata.rb
	nano ./cookbooks/doc/metadata.rb

--

	nano   ./node.json
    
--


    {

        "nginx": {
            "version"   : "1.5.9",
            "user"      : "www-data",
            "port"      : "80"
         },


         "nano": {
            "version"   : "2.2.6"
        },


        "doc": {
            "name"      : "doc"
        },



        "run_list": [
                   "recipe[nginx]",
                   "recipe[nano]",
                   "recipe[doc]"
        ]

	}

Optenemos la siguiente estructura:

![](http://pix.toile-libre.org/upload/original/1391039448.png)

Ejecutamos:

	sudo chef-solo -c ./solo.rb -j ./node.json
    
![](http://pix.toile-libre.org/upload/original/1391039372.png)
    

##Ejercicio 3
###Escribir en YAML la siguiente estructura de datos en JSON

    { uno: "dos", tres: [ 4, 5, "Seis", { siete: 8, nueve: [ 10, 11 ] } ] }

	-
    uno:"dos"
	tres:
    - 4
    - 5 
    -"Seis"
    -
        - siete:8
        - nueve:[10,11]
        

##Ejercicio 4
###Desplegar los fuentes de la aplicación de DAI o cualquier otra aplicación que se encuentre en un servidor git público en la máquina virtual Azure (o una máquina virtual local) usando ansible.

Ya tenemos una maquina virtual creada en Azure.
![](http://pix.toile-libre.org/upload/original/1391183401.png)

Entramos en ella usando ssh:

	ssh ubuntu-dai-iv.cloudapp.net
    
####Configuramos claves rsa para ssh:

Escribimos en la máquina de Azure:

	ssh-keygen -t rsa -C "josemlp.montefrio@gmail.com"
    
Compartimos clave rsa publica con máquina anfitrion:

	ssh-copy-id josemlp@ubuntu-dai-iv.cloudapp.net

.

Creamos fichero inventario con los host que vamos a controlar
    
	echo -e "[azure] \n ubuntu-dai-iv.cloudapp.net" > ~/ansible_hosts
	export ANSIBLE_HOSTS=~/ansible_hosts
    


	
	
![](http://pix.toile-libre.org/upload/original/1391184871.png)

Desplegamos fuentes desde git:

	ansible azure -m git -a "repo=https://github.com/josemlp91/practica3IV.git dest=~/dai version=HEAD"


![](http://pix.toile-libre.org/upload/original/1391186144.png)

Verificamos que todas las fuentes han sido descargadas en las máquinas remotas:

![](http://pix.toile-libre.org/upload/original/1391186254.png)

##Ejercicio 5
###Desplegar la aplicación de DAI con todos los módulos necesarios usando un playbook de Ansible.

Necesitamos crear un playbooks por ejemplo ```ansibledai.yml```
~~~
---
- hosts: azure
  sudo: yes
  tasks:
    - name: Python python-pip y build-essential EasyInstall
      apt: name=build-essential state=present
      apt: name=python-dev state=present
      apt: name=python-setuptools state=present
      apt: name=python-pip state=present
    - name: MongoDB
      apt: name=mongodb-server state=present
    - name: Módulos de Python 
      command: pip install web.py mako pymongo lxml feedparser tweepy
    - name: Desplegar aplicación
      command: chdir=/home/josemlp/dai/App_dai nohup 
               python practica.py 8080 &
      async: 50
      poll: 0
~~~
Ejecutamos playbook: ```ansible-playbook ansibledai.yml```


![](http://pix.toile-libre.org/upload/original/1391191240.png)

Ya esta la aplicación funcionando y podemos acceder:

![](http://pix.toile-libre.org/upload/original/1391191439.png)
  
##Ejercicio 5  
###Instalar una máquina virtual Debian usando Vagrant y conectar con ella.  

Instalamos vagrant:

	sudo apt-get install vagrant

Descargamos una maquina vagrat, en mi caso uso un Debian 7 minimal:  
[http://www.vagrantbox.es/](http://www.vagrantbox.es/)    

    vagrant box add debian7 https://www.dropbox.com/s/23gupgb0xompvkm/Wheezy64.box?dl=1
	
    vagrant init debian7
    
    vagrant up
    
    vagrant ssh
    
    
    http://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box
    
![](http://pix.toile-libre.org/upload/original/1391440679.png)

![](http://pix.toile-libre.org/upload/original/1391441119.png)

![](http://pix.toile-libre.org/upload/original/1391441162.png)

Realizo un ejemplo de instalación personalizada:

~~~    
    # -*- mode: ruby -*-
    # vi: set ft=ruby :
    
    Vagrant.configure("2") do |config|
    
    
      config.vm.box = "ubuntu"
    
      config.vm.provision "shell",
        inline:"sudo apt-get install htop"    
    end
~~~

Vemos que efectivamente se ha instalado correctamente:

![](http://pix.toile-libre.org/upload/original/1391594531.png)


##Ejercicio 6
###Crear un script para provisionar `nginx` o cualquier otro servidor web que pueda ser útil para alguna otra práctica

~~~    
    # -*- mode: ruby -*-
    # vi: set ft=ruby :
    
    Vagrant.configure("2") do |config|
    
    
      config.vm.box = "ubuntu"
    
      config.vm.provision "shell",
        inline: "sudo apt-get update && sudo apt-get install -y nginx && sudo service nginx restart
        && sudo service nginx status"
    end
~~~

![](http://pix.toile-libre.org/upload/original/1391595653.png)

##Ejercicio 7
###Configurar tu máquina virtual usando vagrant con el provisionador ansible

Lo primero que tenemos que hacer es hacer una configuración de red que nos permita el acceso ssh desde el exterior,  y esta es la parte del ejercicio que más problemas me ha dado, utilizo una intezfaz puente.

Configuramos nuestro vagrantfile:

~~~
		# -*- mode: ruby -*-
        # vi: set ft=ruby :
        
        Vagrant.configure("2") do |config|
        
          
        
          config.vm.box = "ubuntu"
        
          config.vm.network :public_network,:bridge=>"eth0"
        
        
        end
        
~~~

Entramos en la máquina via ``vagrant ssh`` 

![](http://pix.toile-libre.org/upload/original/1391603407.png)

Vemos todas las IP de los adaptadores que tiene nuestra máquina virtual:
En mi caso la que puedo utilizar para conexiones ssh es la 192.168.1.188

Despues otro paso importante es cambiar la contraseña del usuario vagrant, puesto que no la conozco, y la necesitamos para hacer la conexion ssh del modo usual:

	passwd vagrant

Y ponemos la que nos de la gana.

En la máquina anfitriona:

Añadimos dicha IP a nuestro inventario:

	echo -e "[vagrant] \n  vagrant@192.168.1.188 " > ~/ansible_hosts
	export ANSIBLE_HOSTS=~/ansible_hosts
    
 Creamos nuestro playbook
 
 ~~~
 ---
- hosts: vagrant
  sudo: yes
  tasks:
    - name: Actualizar lista de paquetes
      apt: update_cache=yes
    - name: Instalar Nginx
      apt: name=nginx state=present
~~~

Lo ejecutamos:

	ansible-playbook playbook.yml


Ya podemos ver que todo funciona perfectamente:


![](http://pix.toile-libre.org/upload/original/1391603088.png)

![](http://pix.toile-libre.org/upload/original/1391603113.png)










    
