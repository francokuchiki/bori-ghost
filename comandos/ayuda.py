import os
import discord
from variables import ayuda, comandos_ayuda

async def ayuda_general(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	embed = discord.Embed(title="**BORI GHOST** Mensaje de Ayuda",
							description=ayuda.format(client.user.mention, prefijo),
							colour=0xEEEEEE)
	mod_i = 1
	for key in comandos_ayuda:
		valor = ""
		for sub_key in comandos_ayuda[key]:
			for i in range(len(comandos_ayuda[key][sub_key])):
				valor += str(mod_i)+"."+str(i+1)+". "+comandos_ayuda[key][sub_key][i]+"\n"
		embed.add_field(name=mod_i+key,
						value=valor)
	embed.set_thumbnail(url=client.user.avatar_url)
	embed.set_footer(icon_url=avatar_autor,
					text="Este mensaje ha sido solicitado por {} ({}#{})".format(nick_autor,
							message.author.name, message.author.discriminator))
	await client.send_message(message.channel, embed=embed)