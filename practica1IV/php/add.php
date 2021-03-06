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
	//ini_set('display_errors', true);
	//error_reporting(E_ALL);
	
			    
	$user= getenv('OPENSHIFT_MYSQL_DB_USERNAME');
        $clave= getenv('OPENSHIFT_MYSQL_DB_PASSWORD');
	$h=getenv('OPENSHIFT_MYSQL_DB_HOST');
	$db=getenv('OPENSHIFT_APP_NAME');
	$puerto=getenv('OPENSHIFT_MYSQL_DB_PORT');
	$host = 'mysql:host='.$h.';port:'.$puerto.';dbname='.$db;
	$enlace = new PDO( $host, $user, $clave );

	
	
	$autor=$_POST['autor'];
	$titulo=$_POST['titulo'];
	$mensaje=$_POST['mensaje'];
	$respuesta=$_POST['respuestas'];
	$identificador=$_POST['identificador'];
  
	$fecha=time();

	if(empty($identificador)) {$identificador=0;}
	if(empty($respuesta)) {$respuesta=0;}
	
	$respuesta=$respuestas+1;
	
	$sql = "INSERT INTO foroivirtuales2 . foro1(
	    autor,
            titulo,
            mensaje,
            fecha,
            identificador) VALUES (
            :filmautor, 
            :filmtitulo, 
            :filmmensaje, 
            :filmfecha, 
            :filmidentificador)";


	$stmt = $enlace->prepare($sql);
	$stmt->bindParam(':filmautor', $autor, PDO::PARAM_STR);       
	$stmt->bindParam(':filmtitulo', $titulo, PDO::PARAM_STR); 
	$stmt->bindParam(':filmmensaje', $mensaje, PDO::PARAM_STR);
	$stmt->bindParam(':filmfecha', $fecha, PDO::PARAM_STR);
	$stmt->bindParam(':filmidentificador', $identificador, PDO::PARAM_STR);
	$stmt->execute(); 

	$sql2 = "UPDATE foroivirtuales2 . foro1 SET 
            respuesta = :filmrespuesta, 
            WHERE id = :filmID";

	$stmt2 = $enlace->prepare($sql2);                                  
	$stmt2->bindParam(':filmrespuesta', $respuesta, PDO::PARAM_STR);       
	$stmt2->bindParam(':filmID', $identificador, PDO::PARAM_STR);

	$stmt2->execute();

	$resultado='SELECT '. $mensaje.' FROM `foroivirtuales2` . `foro1` WHERE `mensaje`='. $mensaje;

	foreach ($enlace->query($resultado) as $registro) {

		echo"<tr>";
		foreach($registro as $cl){
			echo"<td>",$cl,"</td>";
		}
	}

	echo "<br />
	<br />";

	echo '<a href="index.php">volver al foro</a>';
?>
</div>
</html>
