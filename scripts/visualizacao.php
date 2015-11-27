<head>
<script src="js/jquery.js"></script>
</head>

<script>
$(document).ready(function(){

function doStuff(){
  //do some things
	  setInterval(continueExecution, 3000);
}

function continueExecution() {
	console.log("esso");
	// refazer a query php,
	// acho que chamando um arquivo externo

  $.ajax({
            url: "getData.php",
		dataType: 'json'
        })
        .done(function(resultt) {
		mdata=resultt;
        });
	
}
continueExecution();
doStuff();
});
// dar um pulso periódico
// depois disso fazer a query no servidor e devolver periodicamente
</script>
BANANA!
