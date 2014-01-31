
#Gestión de infraestructuras virtuales
_____________

##Ejercicio 1
###Instalar chef en la máquina virtual que vayamos a usar.

	sudo apt-get install ruby1.9.1 ruby1.9.1-dev rubygems
    sudo gem install ohai chef
    sudo su
    curl -L https://www.opscode.com/chef/install.sh | bash
    exit
    
    
![](http://pix.toile-libre.org/upload/original/1391033801.png)
    
 
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



  