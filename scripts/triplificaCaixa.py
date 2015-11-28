import pymysql, participation as pa
import  importlib, datetime, os
importlib.reload(pa.triplification.caixaMagicaTriplification)
dbname,username,passwd="cm2","root","foobar"
conn = pymysql.connect(user=username, passwd=passwd, db=dbname) # cm2
cur = conn.cursor()
cur.execute("SELECT * FROM transacoes_caixamagica")
trans=[i for i in cur]

cur.execute("DESCRIBE transacoes_caixamagica")
cols=[i[0] for i in cur]

scriptpath=os.path.realpath(__file__)
pa.triplification.caixaMagicaTriplification.triplificaCaixaMagica(dbname,username,passwd,"tempoT",scriptpath)

