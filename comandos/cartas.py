import discord
import random
from comandos.cartas_objetos import *

async def da_carta(client, message, nick_autor, avatar_autor, mensaje_separado, prefijo):
	servidor = discord.utils.get(client.servers, id = "310951366736609281")
	mano_1 = []
	while len(mano_1) < 3:
		i = random.randint(40)
		if baraja[i] not in mano_1:
			mano_1.append(baraja[i])
	mensaje = ""
	for carta in mano_1:
		emoji = discord.utils.get(servidor.emojis, name=carta.emoji)
		mensaje += emoji
	await client.send_message(message.channel, mensaje)
	await client.send_message(message.author, mensaje)