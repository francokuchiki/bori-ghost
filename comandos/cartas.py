import discord
from comandos.cartas_objetos import *

async def da_carta(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	servidor = discord.utils.get(client.servers, id = "310951366736609281")
	e1_emoji = discord.utils.get(servidor.emojis, name="espada_1")
	await client.send_message(message.channel, e1_emoji)
	await client.send_message(message.author, e1_emoji)