<head>
<script src="js/jquery.js"></script>
</head>

<?php
  include_once('dbconfig.php');
  $result=mysqli_query($conn, "SELECT * from transacoes_caixamagica;");
  //$result2=mysqli_fetch_array($conn, $result);
  $result2=mysqli_fetch_all( $result,MYSQLI_ASSOC);
print_r($result2);
?>
<script>
$(document).ready(function(){
    myArray = <?php print(json_encode($result2)); ?>;
//    console.log(myArray);
	bona=56;
for (i=0;i<myArray.length;i++){
console.log(myArray[i].metodo);
}
});
</script>
BANANA!
