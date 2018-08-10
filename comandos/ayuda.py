import os
import discord
from variables import ayuda, comandos_ayuda, descripciones_ayuda

async def ayuda_general(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	if len(mensaje_separado) > 1 and mensaje_separado[1] == "utilidad.informacion":
		objeto = descripciones_ayuda["Este módulo contiene los comandos que son útiles para el usuario del bot."][0]
		embed = discord.Embed(title="Ayuda: "+objeto.nombre,
								description=objeto.descripcion+"\n**__Alias__**\n"+str(objeto.alias),
								colour=0xAAAAAA)
	else:
		embed = discord.Embed(title="BORI GHOST: Mensaje de Ayuda",
								description=ayuda.format(client.user.mention, prefijo, prefijo, prefijo),
								colour=0xAAAAAA)
		mod_i = 1
		for key in comandos_ayuda:
			valor = ""
			sub_i = 1
			for sub_key in comandos_ayuda[key]:
				valor += "**"+str(mod_i)+"."+str(sub_i)+". "+sub_key+"**\n"
				for i in range(len(comandos_ayuda[key][sub_key])):
					valor += "	"+str(mod_i)+"."+str(sub_i)+"."+str(i+1)+". "+comandos_ayuda[key][sub_key][i]+"\n"
				sub_i += 1
			embed.add_field(name=str(mod_i)+". "+key,
							value=valor)
			mod_i += 1
	embed.set_thumbnail(url=client.user.avatar_url)
	embed.set_footer(icon_url=avatar_autor,
					text="Este mensaje ha sido solicitado por {} ({}#{})".format(nick_autor,
							message.author.name, message.author.discriminator))
	await client.send_message(message.channel, embed=embed)