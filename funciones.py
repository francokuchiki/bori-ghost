import discord
import os
import sqlite3
from variables import (embed_titulo, embed_descripcion, usuario_texto, razon_titulo, 
						tiempo_titulo, tiempo_texto, ed_descripcion, fue_usuario_texto,
						tabla_prefijos)

def get_prefijos(message):
	base_de_datos = sqlite3.connect("basesdatos{}{}.db".format(os.sep, message.server.id), isolation_level=None)
	bd = base_de_datos.cursor()
	bd.execute(tabla_prefijos)
	prefijos = bd.execute("SELECT prefijo FROM prefijos;").fetchall()
	base_de_datos.close()
	lista_prefijos = [prefijo[0] for prefijo in prefijos]
	return lista_prefijos

def lista_a_cadena(lista, inicio: int=None, final: int=None, caracter=" "):
	if inicio == None:
		inicio = 0
	if final == None:
		final = len(lista)
	mensaje_sin_comando = ""
	for i in range(inicio,final):
		mensaje_sin_comando += lista[i]+caracter
	return mensaje_sin_comando

def get_mute_role(lista):
	"""Selecciona el rol para los usuarios silenciados en una lista de roles.
		Parámetros:
			-Lista: Una lista que contiene objetos discord.Role en la que se 
			selecciona el rol de silencio.
	"""
	silenciado = discord.utils.get(lista, id="338022067880329216") #CB en SDUMS
	if silenciado == None: #Si no lo encuentra
		silenciado = discord.utils.get(lista, name="CALLATE BOLUDO")
	if silenciado == None: #Si no lo encuentra
		silenciado = discord.utils.get(lista, name="Muted")
	if silenciado == None: #Si no lo encuentra
		silenciado = ""
	return silenciado #Devuelve el rol

def borrar_repetidos(mensaje, caracter):
	"""Borra los caracteres repetidos al principio y al final de un mensaje.
		Lo uso principalmente para borrar espacios extras.
		Parámetros:
			-Mensaje (string): Cadena de texto que quiero modificar.
			-Caracter: Caracter a eliminar (generalmente " ").
	"""
	while mensaje.startswith(caracter):
		mensaje = mensaje[1::]
	while mensaje.endswith(caracter):
		mensaje = mensaje[0:len(mensaje)-1:]
	return mensaje

def get_nick_avatar(miembro):
	"""Devuelve el nick y el avatar de un miembro dado.
		Parámetros:
			-Miembro: Usuario cuyos nick y avatar se quieren obtener.
	"""
	#Si es un objeto discord.Member (no User) y tiene nick
	if hasattr(miembro, "nick") and miembro.nick != None:
		nick = miembro.nick #Lo seleccione
	else: #Si no
		nick = miembro.name #El nick es el nombre de usuario
	if miembro.avatar_url == "": #Si no tiene avatar
		avatar = miembro.default_avatar_url #Selecciona el por defecto
	else: #Si no
		avatar = miembro.avatar_url #Devuelve el del miembro
	return nick, avatar

def crear_embed(titulo:tuple,descripcion,color,miembro,autor,servidor,razon,
				usuario=None,tiempo=None,miniatura=None,pie:str=None,ed:tuple=None):
	"""Función que me permite crear embeds con un sólo código para no andar repitiendo
		lo mismo una y otra vez.
		La llamo para los mensajes que se envían luego de cada comando.
		Parámetros:
			-Titulo (emoji, tipo): El emoji que acompaña al título y la palabra que sigue a "Usuario"
			-Descripción: Discierne entre "en el" o "del" servidor.
			-Color: Color del embed (RGB en hex).
			-Miembro (discord.Member): usuario sobre el que se actúa.
			-Autor (discord.Member o discord.User): Objeto que representa al usuario que usa
				el comando (o al bot).
			-Servidor (discord.Server): Servidor de discord en que se ejecuta el comando.
			-Razon: Motivo por el que se usa el comando.
			-Usuario: Título del campo "usuario" en el embed.
			-Tiempo: Si es el comando mute, es el tiempo de silencio.
			-Miniatura: Si es "avatar", pone el avatar del miembro como miniatura del
				embed. Si es "server_icon", pone el icono del server.
			-Pie: Texto para el footer.
			-ed (tupla): Datos para completar el embed que se manda al usuario.
	"""
	nick, avatar = get_nick_avatar(miembro) #Consigue el nick y el avatar del miembro
	nick_autor, avatar_autor = get_nick_avatar(autor) #Consigue el nick y el avatar del autor
	#Crea el primer embed y lo guarda en la lista "embed"
	embed = [discord.Embed(title=embed_titulo.format(titulo[0],titulo[1].capitalize()),
							description=embed_descripcion.format(titulo[1],descripcion),
							colour=color)]
	if usuario != None: #Si debe llevar el campo "Usuario"
		embed[0].add_field(name=usuario,
						value=usuario_texto.format(nick, miembro.name, miembro.discriminator),
						inline=False) #Lo crea
	embed[0].add_field(name=razon_titulo, value=razon, inline=False) #Crea el campo "Razón"
	if tiempo != None: #Si debe llevar el campo "Tiempo"
		embed[0].add_field(name=tiempo_titulo,
						value=tiempo_texto.format(str(tiempo)),
						inline=False) #Lo crea
	if miniatura == "avatar": #Si debe llevar el avatar
		embed[0].set_thumbnail(url=avatar) #Lo pone de miniatura
	elif miniatura == "server_icon": #Si debe llevar el icono del server (nada por ahora)
		embed[0].set_thumbnail(url=servidor.icon_url) #Lo pone de miniatura
	if pie != None: #Si debe llevar footer
		embed[0].set_footer(text=pie, 
						icon_url=avatar_autor) #Lo crea
	if miembro != autor: #Si el usuario sobre el que se actúa no es quien llamó al comando
		#Crea un segundo embed que se le enviará
		embed.append(discord.Embed(title=u"\U0001F50A "+servidor.name.capitalize(),
									  description=ed_descripcion.format(ed[0],ed[1],servidor.name.capitalize(),ed[2]),
									  colour=color)) #Lo agrega en la lista "embed"
		embed[1].add_field(name=razon_titulo, value=razon, inline=False) #Crea el campo "Razón"
		embed[1].add_field(name=u"\U0001F46E"+" Usuario",
								value=fue_usuario_texto.format(ed[0],nick_autor,autor.name,autor.discriminator),
								inline=False) #Crea el campo que indica quién usó el comando
		if tiempo != None: #Si debe llevar el campo "Tiempo"
			embed[1].add_field(name=tiempo_titulo,
							value=tiempo_texto.format(str(tiempo)),
							inline=False) #Lo crea
		embed[1].set_thumbnail(url=servidor.icon_url) #Pone de miniatura el avatar del server
	return (embed)