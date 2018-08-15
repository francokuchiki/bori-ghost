import discord
from comandos.cartas_objetos import *

async def da_carta(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	await client.send_message(message.channel, espada_1.emoji)
	await client.send_message(message.author, espada_1.emoji)