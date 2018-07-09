import discord
import re

async def toggle_roles(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	if message.author.server_permissions.manage_roles:
		for miembro in message.mentions:
			mencion = re.search("<@!?{}>".format(miembro.id), message.content)
			i = mensaje_separado.index(mencion.group())+1
			rol = ""
			while i < len(mensaje_separado):
				if mensaje_separado[i] in message.role_mentions:
					rol = discord.utils.get(message.server.roles, mention= mensaje_separado[i])
					i = len(mensaje_separado)
				else:
					if not re.search("<@!?[0-9]+>", mensaje_separado[i]):
						if mensaje_separado[i] != "\n":
							rol += mensaje_separado[i]
						i += 1
					else:
						i = len(mensaje_separado)
			for rol_server in message.server.roles:
				if rol_server.name.startswith(rol):
					Rol = rol_server
				else:
					Rol = None
			if Rol == None:
				await client.send_typing(message.channel)
				await client.send_message(message.channel, "No juegues conmigo que soy profesional, tienes que especificar un rol válido en tu mac.")
			else:
				puede = False
				for rol_autor in message.author.roles:
					if rol_autor.position > Rol.position:
						puede = True
				if puede:
					if Rol in miembro.roles:
						quita_mensaje = "A *{}* se le ha quitado el rol '**{}**'."
						await client.remove_roles(miembro, Rol)
						await client.send_typing(message.channel)
						await client.send_message(message.channel, quita_mensaje.format(miembro.display_name,Rol.name))
					else:
						da_mensaje = "A *{}* se le ha concedido el rol '**{}**'."
						await client.add_roles(miembro, Rol)
						await client.send_typing(message.channel)
						await client.send_message(message.channel, da_mensaje.format(miembro.display_name,Rol.name))
				else:
					error_permisos = "No tienes los permisos suficientes para eso. Tal vez no eres tan profesional como creí..."
					await client.send_typing(message.channel)
					await client.send_message(message.channel, error_permisos)
	else:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "No eres profesional, cómprate una MAC y tal vez puedas editar roles.")