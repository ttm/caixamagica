# faz ontologia, renderizando a figura, com os labels.
# ver OT, OPS, ORe
import percolation as P, participation as pa
import  importlib, datetime
importlib.reload(P.rdf)
importlib.reload(pa.ontologies.cm)

pa.ontologies.cm.makeCaixaMagicaOntology("/home/r/repos/caixamagica/")
pa.ontologies.cm.makeFirstCaixaMagicaOntology("/home/r/repos/caixamagica/")
