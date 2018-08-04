import os
import discord
import psycopg2
from variables import tabla_destacados

async def editar_destacados(client, antes, despues):
	BD_URL = os.getenv("DATABASE_URL")
	base_de_datos = psycopg2.connect(BD_URL, sslmode='require')
	bd = base_de_datos.cursor()
	bd.execute("SELECT id_canal, ids_destacados, ids_destaque FROM destacados")
	id_canal, ids_destacados, ids_destaque = bd.fetchone()
	ids_destacados = ids_destacados.split(",")
	ids_destaque = ids_destaque.split(",")
	if antes.id in ids_destacados:
		i = ids_destacados.index(antes.id)
		channel = discord.utils.get(antes.server.channels, id= id_canal)
		mensaje_a_editar = await client.get_message(channel, ids_destaque[i])
		if antes.content != despues.content:
			mensaje_a_editar.embeds[0]['description'] = despues.content
			embed = discord.Embed.from_data(mensaje_a_editar.embeds[0])
			if 'thumbnail' in mensaje_a_editar.embeds[0]:
				embed.set_thumbnail(url=mensaje_a_editar_embeds[0]['thumbnail']['url'])
			if 'image' in mensaje_a_editar.embeds[0]:
				embed.set_image(url=mensaje_a_editar.embeds[0]['image']['url'])
			if 'footer' in mensaje_a_editar.embeds[0]:
				embed.set_footer(icon_url=mensaje_a_editar.embeds[0]['footer']['icon_url'],
									text=mensaje_a_editar.embeds[0]['footer']['text'])
			await client.edit_message(mensaje_a_editar, embed=embed)