<?php
  include_once('dbconfig.php');
  $result=mysqli_query($conn, "SELECT * from transacoes_caixamagica;");
  //$result2=mysqli_fetch_array($conn, $result);
  $result2=mysqli_fetch_all( $result,MYSQLI_ASSOC);
	echo json_encode($result2);
?>

