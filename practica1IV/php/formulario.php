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
	$id=0;
	$id=$_GET['id'];
	$respuestas=$_GET['respuestas'];
?>


	<h2>Bienvenido </h2>
	<form action="add.php" method="post" target="" style="padding:5px;">
	<input name="respuestas" type="hidden" value="<?php echo $respuestas;?>" />
	<input name="identificador" type="hidden" value="<?php echo $id;?>" />
	
	Autor:<br />
	<input name="autor" type="text" size="32"/><br />
	<br />
	
	Titulo:<br />
	<input name="titulo" type="text" size="32"/>
	<br />
	<br />
	
	Mensaje:<br /><textarea name="mensaje" cols="40"  rows="7"/></textarea>
	<input name="" value="Iniciar" type="submit" />
	</form>
	</div>

</html>
