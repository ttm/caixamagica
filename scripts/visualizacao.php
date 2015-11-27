<head>
<script src="js/jquery.js"></script>
<script src="js/underscore-min.js"></script>
<script src="js/d3.min.js"></script>
<script src="js/d3.tip.v0.6.3.js"></script>
<style>
.mcentered3 {
    margin: 0 0 3px 0;
    text-align: center;
	font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; 
}
.mcentered, .mcentered2,  {
    margin: 0 0 3px 0;
    text-align: center;
	font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; 
}

svg{
	font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; 
}
.d3-tip {
  line-height: 1;
  font-weight: bold;
  padding: 12px;
  background: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 2px;
font-size: 12px;
	font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; 
text-align:center;
}

/* Creates a small triangle extender for the tooltip */
.d3-tip:after {
  box-sizing: border-box;
  display: inline;
  font-size: 10px;
  width: 100%;
  line-height: 1;
  color: rgba(0, 0, 0, 0.8);
  content: "\25BC";
  position: absolute;
  text-align: center;
}

/* Style northward tooltips differently */
.d3-tip.n:after {
  margin: -1px 0 0 0;
  top: 100%;
  left: 0;
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
	dates=[];
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
	dates.push(new Date(md.timestamp).getTime());
	// fazemos um plot como grafico de barra

})
ips_=_.unique(ips);
nips=ips_.length;
ips__={};
ips_.forEach(function(ip,i){
	ips__[ip]=i;
});
svg.append("rect")
  .attr("x", 0)
  .attr("y", 0)
  .attr("height", h)
  .attr("width", w)
  .style("fill", "#c5d4e7")
  .style("stroke-width", "0px");
svg2.selectAll(".textFoo2")
   .data(["IPs"])
   .enter()
   .append("text")
   .attr("x", margin/4)
   .attr("y", h/2)
   .text(function(d){return d;});


dataset=[nips,nprobs,nsols,nvots]
dataset_=mNormalize(dataset); // para agilizar a escala 
svg.selectAll(".rect0")
   .data(dataset_)
   .enter()
   .append("rect")
   .attr("x", function(d,i){return margin+i*esp_;})
   .attr("y", function(d){return h-d;})
   .attr("width", w_)
   .attr("height", function(d){return d;})
   .attr("fill", function(d) {
    return "rgb(0, 0, " + (d * 10) + ")";
})
	.on('mouseover', tip.show)
      .on('mouseout', tip.hide);

svg.selectAll(".text1")
   .data(dataset_)
   .enter()
   .append("text")
   .attr("x", function(d,i){return margin+i*esp_;})
   .attr("y", function(d){return h-d-10;})
   .text(function(d,i){return dataset[i];});

datesm=Math.min.apply(Math,dates);
datesM=Math.max.apply(Math,dates);
dates_=[]
fator=(w-2*margin)/(datesM-datesm);
dates.forEach(function(d){
	dates_.push(margin*1.5+(d-datesm)*fator);
});
step_y=(h*.9-20)/(nips-1)
svg2.selectAll(".lineTrans")
	.data(dates_)
	.enter()
	.append("line")
	.attr("x1",function(d){return d;})
	.attr("y1",function(d,i){return 20+ips__[ips[i]]*step_y+5;})
	.attr("x2",function(d){return d;})
	.attr("y2",function(d,i){return 20+ips__[ips[i]]*step_y-5;})
	.style("stroke-width","1px")
	.style("stroke","rgb(255,0,0)")
// colocamos numeros originais na parte de cima do svg
// embelezamos a parte gráfica

// fazemos o fundo com as transacoes no tempo

// faz svg grande de fundo, talvez beje
// mapeia os momentos para o eixo x
// mapeia os usuarios para eixo y
// coloca um traço vermelho para cada transação

}
$(document).ready(function(){

function doStuff(){
  //do some things
	  setInterval(continueExecution, 3000);
}
w=250;
w_=20;
h=200;
h_=220;
hmax=h*0.8;
margin=0.1*w;
esp=0.8*w;
esp_=(esp-w_)/3
svg = d3.select(".mcentered")
            .append("svg")
            .attr("width", w)
            .attr("height", h_);
svg.selectAll(".text0")
   .data(["IPs","Probs","Sols","Votos"])
   .enter()
   .append("text")
   .attr("x", function(d,i){return  margin+i*esp_-8;})
   .attr("y", function(d,i){return h_;})
   .text(function(d){return d;});
expl=["Numero de pessoas<br/>conectadas",
      "Numero de problemas<br/>reportados",
      "Numero de solucoes<br/>reportados",
      "Numero de votos<br/>efetuados",
]
tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d,i) {
    return "<span style='color:white'>" + expl[i] + "</span>";
  })
svg.call(tip);


svg2 = d3.select(".mcentered2")
            .append("svg")
            .attr("width", w)
            .attr("height", h_);

svg2.selectAll(".textFoo")
   .data(["Tempo"])
   .enter()
   .append("text")
   .attr("x", margin+w/3)
   .attr("y", h_-3)
   .text(function(d){return d;});
svg2.append("rect")
  .attr("x", 0)
  .attr("y", 0)
  .attr("height", h)
  .attr("width", w)
  .style("fill", "#c5d4e7")
  .style("stroke-width", "0px");
svg2.selectAll(".lineSep")
	.data([margin*1.3])
	.enter()
	.append("line")
	.attr("x1",function(d){return d;})
	.attr("y1",0+10)
	.attr("x2",function(d){return d;})
	.attr("y2",h-10)
	.style("stroke-width","1px")
	.style("stroke","rgb(0,0,0)")

// atividade participativa
// atividade no tempo
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
<div class="mcentered3">
<strong>
Atividade participativa
</strong>
<div class="mcentered"></div>
</div>
<br />
<br />
<br />
<div class="mcentered3">
<strong>
Atividade no tempo
</strong>
<div class="mcentered2"></div>
</div>
