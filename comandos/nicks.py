from funciones import borrar_repetidos

async def manejar_apodos(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	if message.author.mention in message.mentions and message.author.server_permissions.change_nickname:
		i = mensaje_separado.index(message.author.mention)+1
		nuevo_apodo = ""
		while i < len(mensaje_separado):
			if mensaje_separado[i] not in message.mentions:
				nuevo_apodo += " "+mensaje_separado[i]
				i += 1
			else:
				i = len(mensaje_separado)
		nuevo_apodo = borrar_repetidos(nuevo_apodo, " ")
		if nuevo_apodo == "":
			nuevo_apodo = None
		elif len(nuevo_apodo) > 32:
			await client.send_typing(message.channel)
			await client.send_message(message.channel, "¡Tu nuevo apodo es demasiado largo! Debe tener **32 carácteres** o menos.")
			return
		await cambiar_apodo(client, message, message.author, nuevo_apodo)
	if len(message.mentions) > 1 and not message.author.server_permissions.manage_nicknames:
		mensaje_permisos = """"Dame un momento... ¡Listo!\n...\n...\n
							JA JA JA Ni lo creas, no tienes los permisos suficientes para cambiar apodos.
							Fue un buen intento, igualmente, {}. ¡Ánimo!"""
		await client.send_typing(message.channel)
		await client.send_message(message.channel, mensaje_permisos.format(message.author.mention))
	if message.author.server_permissions.manage_nicknames:
		for miembro in message.mentions:
			i = mensaje_separado.index(miembro.mention)+1
			nuevo_apodo = ""
			while i < len(mensaje_separado):
				if mensaje_separado[i] not in message.mentions:
					nuevo_apodo += " "+mensaje_separado[i]
					i += 1
				else:
					i = len(mensaje_separado)
			nuevo_apodo = borrar_repetidos(nuevo_apodo, " ")
			if nuevo_apodo == "":
				nuevo_apodo = None
			await cambiar_apodo(client, message, miembro, nuevo_apodo)

async def cambiar_apodo(client, message, miembro, apodo):
	mensaje = "El nuevo apodo para *{}#{}* es **{}**"
	await client.change_nickname(miembro, apodo)
	await client.send_typing(message.channel)
	await client.send_message(message.channel, mensaje.format(miembro.name, miembro.discriminator, miembro.display_name))