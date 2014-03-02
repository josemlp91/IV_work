/*
  Esta archivo pertenece a la aplicación "foroivirtuales2" bajo licencia GPLv2.
  Copyright (C) 2013 José Miguel López Pérez.

  Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los términos 
  de la Licencia Pública General de GNU según es publicada por la Free Software Foundation, 
  bien de la versión 2 de dicha Licencia o bien (según su elección) de cualquier versión 
  posterior.

  Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA, 
  incluso sin la garantía MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN 
  PROPÓSITO PARTICULAR. Véase la Licencia Pública General de GNU para más detalles.

  Debería haber recibido una copia de la Licencia Pública General junto con este programa. 
  Si no ha sido así, escriba a la Free Software Foundation, Inc., en 675 Mass Ave, Cambridge, 
  MA 02139, EEUU.
*/




### PRÁCTICA 1 : Creación y despliegue de una aplicación en un PaaS

He decidido implementar la practica usando el lenguaje PHP, por tanto y dado que ya estoy 
familiarizado de ejercicios anteriores con OpenShift opto por elegirlo como PaaS.

### Utilidad y funcionamiento de la aplicación.
El funcionamiento se asemeja a un foro de debates, con funcionalidades reducidas.
La aplicación permite, abrir hebras para un tema determinado y ademas hacer comentarios en la hebra.
Mi motivación a implementar este tipo de aplicaciones viene dada por la forma de interactuar en la asignatura, pues la mayoría de las veces es mediante los "_issues_" o foros propios de github, también buscaba una aplicación diferente del resto y que ademas pueda tener algo de utilidad aunque como he dicho ahora mismo la funcionalidad es reducida.

El funcionamiento es sencillo, utilizar el boton "Nuevo Tema" para crear una hebra.
Introducir en los campos, el nombre, el titulo, y el mensaje, pulsar "Iniciar".

Para responder, pulsar sobre el enlace "Ver" de la hebra que te interese, rellenar los mismos campos,
pues he aprovechado el mismo formulario para crear hebras que para responder a la hebra.

### Preparar PaaS, OpenShift
Lo primero de debemos hacer es registrarnos en la plataforma, si aun no estamos.
Una vez registrados ya se nos permite crear hasta un máximo de 3 aplicaciones, 
pulsamos sobre "ADD APLICATION" y nos da la opción tanto de instalar una aplicación, Jenkins Server 
Drupal 7, WordPress 3.x directamente o implementarla nosotros mismo utilizando Java, Python, PHP, Ruby o otros.

Le asignamos un nombre, y seleccionamos PHP 5.3, continuamos los pasos y por ultimo obtenemos un enlace ssh a nuestro repositorio git.

![openshift git](https://github.com/josemlp91/practica1/blob/master/capturas/cap1.png?raw=true)

Ya tenemos clonado el repositorio en nuestra máquina, ahora cuando desarrollemos para solo tenemos que ir haciendo: git add . ; git commit -m "comentario" ; git push


Dado que nuestra aplicación va a necesitar conectar con una BD de mysql, debemos instalar MySQL 5.1, esto se encuentra en "cartridge" se sigue el proceso de instalación y por último se nos proporcionan las credenciales de acceso a sistema de bases de datos.
Podemos consultar desde consola la configuracion usando rhc apps

![consola](https://github.com/josemlp91/practica1/blob/master/capturas/cap4.png?raw=true)

Una herramienta interesante y muy útil es phpmyadmin, que se instala de igual manera, al finalizar se nos da la url para acceder a nuestro phpmyadmin.

![phpmyadmin](https://github.com/josemlp91/practica1/blob/master/capturas/cap2.png?raw=true)

Una vez configurado esto ya podemos ir a la carpeta php de nuestro repositorio y comenzar a implementar comenzando por modificar "index.php".

### Implementacion foroivirtuales2

He de decir que mucho código lo reutilizo del curso anterior. 
Pero en esencia puedo explicar que contamos con cuatro ficheros de código php.
El principal index.php, es la primera vista, y se ocupa de mostrar el titulo, una imagen que cojo de
"http://openclipart.org/" por tener licencia sin restricciones.

A continuación, tengo un boton "Nuevo Tema" que enlaza enlaza con "add.php",
Por ultimo muestra una tabla, que muestra las hebras del foro, y estas son leídas desde la base de datos, para esto debemos hacer la conexión, (para conocer los datos de conexion utilizo _getenv('OPENSHIFT_MYSQL_DB_HOST');_ y demás métodos).

Una vez abierta la conexión podemos general las consultas y ejecutarlas en mi caso utilizo la intefaz PDO.

El fichero "add.php" se encarga generar las inserciones y las actualizaciones de la BD.
formulario.php se encarga de generar el formulario que recoge los datos, y pasarselos a add.php.
foro.php hace la consulta de las respuestas asignadas a una hebra. 

Tambien uso una hoja de estilo "style.css".

![captura](https://github.com/josemlp91/practica1/blob/master/capturas/cap3.png?raw=true)

### Liberar aplicación foroivirtuales2
Por ultimo voy a liberar el código de mi aplicación y ponerlo público en la GitHub, para eso me creo un nuevo repositorio y enlazo todos los ficheros.
No hay que olvidad declarar el tipo de licencia que va a llevar el software, en mi caso uso GPL v2 y así lo detallo en cada uno de los fuentes.

### Bibliográfica.
[1]   [OpenShift Get Started](https://www.openshift.com/get-started)

[2] [Mysql PDO](http://wiki.hashphp.org/PDO_Tutorial_for_MySQL_Developers)

[3] [openshift-php-mysql](http://undeploying.blogspot.com.es/2012/08/openshift-php-mysql.html)

[4] [w3schools](http://www.w3schools.com/)

### Enlaces

####Aplicación:
[http://foroivirtuales2-josemlp.rhcloud.com/](http://foroivirtuales2-josemlp.rhcloud.com/)