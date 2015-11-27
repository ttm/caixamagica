<head>
<script src="js/jquery.js"></script>
<script src="js/underscore-min.js"></script>
<script src="js/d3.min.js"></script>
<style>
.mcentered {
    margin: 0 auto;
    text-align: center;
}
</style>

</head>

<script>
function mNormalize(dataset){
ds=[];
dataset.forEach(function(md){
	limit=Math.pow(10,md.toString().length);
	md_=(md/limit)*hmax;
	ds.push(md_)
});
return ds;
}
function tDraw(mdata){
	// primeiro: pegamos numero de ips, de problemas, de solucoes e de votos
	ips=[]
	nprobs= 0;
	nsols = 0;
	nvots = 0;
	mdata.forEach(function(md){
		//console.log(md.ip);
		ips.push(md.ip);
		if (md.metodo==1){
			nprobs+=1;
		} else if (md.metodo==3) {
			nsols+=1;
		} else {
			nvots+=1;
		}
	// fazemos um plot como grafico de barra

})
ips_=_.unique(ips);
nips=ips_.length;

dataset=[nips,nprobs,nsols,nvots]
dataset_=mNormalize(dataset); // para agilizar a escala 
svg.selectAll("rect")
   .data(dataset_)
   .enter()
   .append("rect")
   .attr("x", function(d,i){return i*40;})
   .attr("y", function(d){return h-d;})
   .attr("width", 20)
   .attr("height", function(d){return d;})
   .attr("fill", function(d) {
    return "rgb(0, 0, " + (d * 10) + ")";
});
svg.selectAll(".text1")
   .data(dataset_)
   .enter()
   .append("text")
   .attr("x", function(d,i){return i*40;})
   .attr("y", function(d){return h-d-10;})
   .text(function(d,i){return dataset[i];});

// colocamos numeros originais na parte de cima do svg
// embelezamos a parte gráfica
// fazemos o fundo com as transacoes no tempo
}
$(document).ready(function(){

function doStuff(){
  //do some things
	  setInterval(continueExecution, 3000);
}
w=500;
h=200;
h_=220;
hmax=h*0.8
svg = d3.select(".mcentered")
            .append("svg")
            .attr("width", w)
            .attr("height", h_);
svg.selectAll(".text0")
   .data(["IPs","Probs","Sols","Votos"])
   .enter()
   .append("text")
   .attr("x", function(d,i){return i*40;})
   .attr("y", function(d,i){return h_;})
   .text(function(d){return d;});



function continueExecution() {
//	console.log("esso");
	// refazer a query php,
	// acho que chamando um arquivo externo

  $.ajax({
            url: "getData.php",
		dataType: 'json'
        })
        .done(function(resultt) {
		mdata=resultt;
		tDraw(mdata);
        });
	
}
continueExecution();
doStuff();
// varre mdata para fazer a visualização
});
</script>
<div class="mcentered"></div>
