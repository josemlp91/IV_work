<!--
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
-->


<!DOCTYPE html>
<html>

    <meta name="author" content="José Miguel López Pérez">
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <link type="text/css" rel="stylesheet" href="style.css"/>

<?php 
	$id=$_GET['id'];
	//ini_set('display_errors', true);
	//error_reporting(E_ALL);
	
				    
	$user= getenv('OPENSHIFT_MYSQL_DB_USERNAME');
	$clave= getenv('OPENSHIFT_MYSQL_DB_PASSWORD');
	$h=getenv('OPENSHIFT_MYSQL_DB_HOST');
	$db=getenv('OPENSHIFT_APP_NAME');
	$puerto=getenv('OPENSHIFT_MYSQL_DB_PORT');

	$host = 'mysql:host='.$h.';port:'.$puerto.';dbname='.$db.'';
	$enlace = new PDO( $host, $user, $clave );
	$consulta='SELECT * FROM `foroivirtuales2` . `foro1`  WHERE `id`='.$id.' ORDER BY `fecha` DESC';


 	foreach ($enlace->query($consulta) as $row){

	  $titulo=$row['titulo'];
	  $autor=$row['autor'];
	  $mensaje=$row['mensaje'];
	  $id=$row['id'];
	  $fecha=$row['fecha'];
	  $respuestas=$row['respuestas'];

	  echo"<h2> <tr>
	      <td> $titulo</td>
	    </tr></h2><table>
	    <tr>
	      <td>Autor: $autor</td>
	    </tr>
	    <tr>
	      <td>$mensaje</td>
	    </tr>
	  </table>
	  ";
	  echo"<br /><br /><a href=formulario.php?id=$id&respuestas=$respuestas>Responder</a><br />
	  <br />";
}

	$consulta2='SELECT * FROM `foroivirtuales2`. `foro1` WHERE `identificador` ='.$id.' ORDER by `fecha` DESC';


	echo"RESPUESTAS:<br /> <br /> ";

	foreach ($enlace->query($consulta2) as $row){
		  $titulo=$row['titulo'];
		  $autor=$row['autor'];
		  $mensaje=$row['mensaje'];
		  $id=$row['id'];
		  $fecha=$row['fecha'];
		  $respuestas=$row['respuestas'];
		  echo"
		  <div width='40%' style='background-color:#CCCCCC;'>
		  <table>
		      <tr><strong>Titulo: </strong>$titulo</tr><br />
		      <tr><strong>Autor: </strong>$autor</tr><br />
		      <tr>$mensaje</tr><br />
		  <br />
		  </table>
		  </div><br />";
	}
?>
</div>

</html>
