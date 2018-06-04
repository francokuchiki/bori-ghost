import sqlite3
import os
from variables import tabla_mute, tabla_encuestas, tabla_prefijos, default_prefix

async def servidor_entro(client, servidor):
	"""Al unirse al server, crea una base de datos."""
	if hasattr(servidor, "id"): #Si tiene id, es un servidor
		#Conecta a la BD o la crea si no existe
		base_de_datos = sqlite3.connect("basesdatos{}{}.db".format(os.sep,servidor.id), isolation_level=None)
		bd = base_de_datos.cursor()
		bd.execute(tabla_mute) #Crea la tabla de silenciados si no existe
		bd.execute(tabla_encuestas)
		bd.execute(tabla_prefijos)
		bd.execute("INSERT INTO prefijos('prefijo') VALUES('{}');".format(default_prefix))
		base_de_datos.close() #Cierra la conexión