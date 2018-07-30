import re
import psycopg2
import os
from variables import tabla_encuestas, nueva_encuesta
from funciones import borrar_repetidos, lista_a_cadena
from discord import Embed
from operator import itemgetter

async def maneja_encuestas(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	if len(mensaje_separado) < 2:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "Debes elegir la opción que quieres llevar a cabo.")
		return
	if mensaje_separado[1] in {"crear", "start", "empezar", "nueva","create", "new"}:
		await crear_encuesta(client, message, prefijo)
	elif mensaje_separado[1] in {"ver", "revisar", "check", "checkear", "view", "consultar"}:
		await revisa_encuesta(client, message, nick_autor, avatar_autor)
	elif mensaje_separado[1] in {"cerrar", "end", "terminar", "finalizar", "close", "fin"}:
		await cierra_encuesta(client, message, nick_autor, avatar_autor)
	else:
		await vota_encuesta(client, message, nick_autor, mensaje_separado)

async def crear_encuesta(client, message, prefijo):
	if ";" in message.content:
		mensaje_separado = message.content.split(";")
	else:
		mensaje_separado = message.content.split("|")
	if len(mensaje_separado) < 2 or ("t:" in message.content and len(mensaje_separado) < 3):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "Faltan parámetros para iniciar una votación.")
		return
	BD_URL = os.getenv('DATABASE_URL')
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	bd.execute(tabla_encuestas)
	select = "SELECT terminada FROM encuestas WHERE channel_id = '%s' and terminada = %s"
	estado = bd.execute(select, (message.channel.id, 0)).fetchall()
	if len(estado) != 0:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "Ya hay una encuesta iniciada en este canal.")
		return
	opciones = ""
	votos = ""
	titulo = None
	for i in range(0,len(mensaje_separado)):
		if titulo == None:
			titulo = re.search("t:.*[a-zA-Z0-9?]+.*$", mensaje_separado[i])
			if titulo:
				titulo = titulo.group()[2::]
				titulo = borrar_repetidos(titulo, " ")
			else:
				if mensaje_separado[i].startswith(prefijo):
					mensaje_separado2 = mensaje_separado[i].split(" ")[2::]
					mensaje_separado[i] = lista_a_cadena(mensaje_separado2)
				opciones += borrar_repetidos(mensaje_separado[i], " ")+","
				votos += "0,"
		else:
			opciones += borrar_repetidos(mensaje_separado[i], " ")+","
			votos += "0,"
	if titulo == None:
		titulo = "No se ha especificado un título o tema para esta votación."
	bd.execute(nueva_encuesta, (message.channel.id,titulo,opciones,votos,0,""))
	bd.commit()
	bd.close()
	base_de_datos.close()
	await client.send_typing(message.channel)
	await client.send_message(message.channel, "**¡Votación creada!**\n"+
								"Puedes revisarla con el comando '*vota check*'")

async def revisa_encuesta(client, message, nick_autor, avatar_autor):
	BD_URL = os.getenv('DATABASE_URL')
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	encuesta = bd.execute("SELECT titulo,opciones,votos FROM encuestas WHERE channel_id = %s AND terminada = %s", (message.channel.id, 0)).fetchall()
	if len(encuesta) > 0:
		opciones = encuesta[0][1].split(",")
		votos = encuesta[0][2].split(",")
		texto_pie = "Consultados por {} ({}#{})"
		resultados = ""
		for i in range(0, len(opciones)-1):
			resultados += opciones[i]+": "+votos[i]+" votos"+"\n"
		votacion_embed = Embed(title=u"\U0001F5F3"+" Votación",
								description=encuesta[0][0],
								colour=0xCCD6DD)
		votacion_embed.add_field(name="Resultados",
								value=resultados,
								inline=False)
		votacion_embed.set_footer(text=texto_pie.format(nick_autor, message.author.name, message.author.discriminator),
									icon_url=avatar_autor)
		votacion_embed.set_thumbnail(url="https://i.imgur.com/5LEqNv7.png")
		await client.send_typing(message.channel)
		await client.send_message(message.channel, embed=votacion_embed)
	else:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "No hay ninguna votación en transcurso en este canal, "+message.author.mention)
	bd.close()
	base_de_datos.close()

async def vota_encuesta(client, message, nick_autor, mensaje_separado):
	BD_URL = os.getenv('DATABASE_URL')
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	select = "SELECT titulo,opciones,votos,votantes FROM encuestas WHERE channel_id = {} AND terminada = 0"
	encuesta = bd.execute(select, (message.channel.id)).fetchall()
	if len(encuesta) > 0:
		opciones = encuesta[0][1].split(",")
		votos = encuesta[0][2].split(",")
		votantes = encuesta[0][3].split(",")
		if message.author.id in votantes:
			await client.send_typing(message.channel)
			await client.send_message(message.channel, "Ya has participado en esta votación.")
			return
		voto = False
		for i in range(1,len(mensaje_separado)):
			if not voto:
				try:
					mensaje_separado[i] = int(mensaje_separado[i])
					if 1 <= mensaje_separado[i] <= len(opciones) - 1:
						opcion = mensaje_separado[i] - 1
						voto = True
				except ValueError:
					if mensaje_separado[i] in opciones:
						opcion = opciones.index(mensaje_separado[i])
						voto = True
		if voto:
			votos[opcion] = str(int(votos[opcion])+1)
			votos = lista_a_cadena(votos[0:len(votos)-1:],caracter=",")
			votantes.append(message.author.id)
			votantes = ",".join(votantes)
			nuevo_voto = "UPDATE encuestas SET votos = '%s', votantes = '%s' WHERE channel_id = '%s';"
			bd.execute(nuevo_voto, (votos,votantes, message.channel.id))
			bd.commit()
			await client.delete_message(message)
			await client.send_typing(message.channel)
			await client.send_message(message.channel, message.author.mention+": ¡Tu voto ha sido añadido!")
	else:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "No hay una encuesta abierta en este canal.")
	bd.close()
	base_de_datos.close()

async def cierra_encuesta(client, message, nick_autor, avatar_autor):
	BD_URL = os.getenv('DATABASE_URL')
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	select = "SELECT key,titulo,opciones,votos FROM encuestas WHERE channel_id = {} AND terminada = 0"
	encuesta = bd.execute(select, (message.channel.id)).fetchall()
	if len(encuesta) > 0:
		bd.execute("UPDATE encuestas SET terminada = 1 WHERE key = %s", (encuesta[0][0]))
		bd.commit()
		opciones = encuesta[0][2].split(",")
		votos = encuesta[0][3].split(",")
		res_lista = [(opciones[i],votos[i]) for i in range(len(opciones))]
		res_lista.sort(key=itemgetter(1),reverse=True)
		resultados = "**"+res_lista[0][0]+": "+res_lista[0][1]+" votos**\n"
		texto_pie = "{} ({}#{}) terminó la votación."
		for i in range(1,len(opciones)-1):
			resultados += res_lista[i][0]+": "+res_lista[i][1]+" votos\n"
		votacion_embed = Embed(title=u"\U0001F5F3"+" Votación Finalizada",
								description=encuesta[0][1],
								colour=0xCCD6DD)
		votacion_embed.add_field(name="Resultados",
								value=resultados,
								inline=False)
		votacion_embed.set_thumbnail(url="https://i.imgur.com/5LEqNv7.png")
		votacion_embed.set_footer(text=texto_pie.format(nick_autor, message.author.name, message.author.discriminator),
									icon_url=avatar_autor)
		await client.send_typing(message.channel)
		await client.send_message(message.channel, embed=votacion_embed)
	else:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "No hay ninguna votación en proceso en este canal.")
	bd.close()
	base_de_datos.close()