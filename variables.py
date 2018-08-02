whitelist = {
	"295748486253510658": "franco",
	"287554491916746752": "katie",
	"244535132097216512": "yoru",
	"239709477392089109": "zero",
	"451551868070526977": "prueba"
}

#--------- Textos generales de los embeds ---------#
embed_titulo = "{} Usuario {}"
embed_descripcion = "Un usuario ha sido **{}** {} servidor."
en_descripcion = "en el"
del_descripcion = "del"
un_usuario = u"\U0001F64B"+" Usuario"
frown_usuario = u"\U0001F64D"+" Usuario"
razon_titulo = u"\U0001F5DE"+" Razón"
usuario_texto = "**{}** (*{}#{}*)"
tiempo_titulo = u"\U0001F570"+" Tiempo"
tiempo_texto = "La duración del silencio es de {}"
ed_descripcion = "Has sido {} {} **{}**{}."
fue_usuario_texto="Fuiste {} por **{}** (*{}#{}*)"
pie_texto = "Este usuario fue {} por {} ({}#{})"

#--------- Textos mute_embed ---------#
mute_titulo = (u"\U0001F910", "silenciado")
mute_color = 0xFFFF00

#--------- Textos ban_kick_embed ---------#
ban_kick_color = 0xAA0000

#--------- Textos unmute_embed ---------#
unmute_titulo = (u"\U0001F50A", "desilenciado")

#--------- Textos unban_embed ---------#
unban_titulo = (u"\U00002705", "desbaneado")
unban_color = 0x00AA00


tabla_mute="""
CREATE TABLE IF NOT EXISTS silenciados(
key SERIAL NOT NULL PRIMARY KEY,
discord_id VARCHAR(30) NOT NULL,
termina TIMESTAMP WITHOUT TIME ZONE NOT NULL);
"""

nuevo_mute="""
INSERT INTO silenciados (discord_id,termina)
VALUES (%s,%s);
"""

quita_mute="""
DELETE FROM silenciados
WHERE discord_id=%s;
"""

tabla_encuestas="""
CREATE TABLE IF NOT EXISTS encuestas(
key SERIAL NOT NULL PRIMARY KEY,
channel_id VARCHAR(30) NOT NULL,
titulo VARCHAR(2000) NOT NULL,
opciones VARCHAR(2000) NOT NULL,
votos VARCHAR(1000) NOT NULL,
terminada INTEGER NOT NULL,
votantes VARCHAR(30));
"""

nueva_encuesta="""
INSERT INTO encuestas (channel_id,titulo,opciones,votos,terminada, votantes)
VALUES (%s,%s,%s,%s,%s, %s);
"""

tabla_prefijos = """
CREATE TABLE IF NOT EXISTS prefijos(
key SERIAL NOT NULL PRIMARY KEY,
prefijo VARCHAR(20) NOT NULL);
"""

default_prefix = "g$"

tabla_destacados = """
CREATE TABLE IF NOT EXISTS destacados(
id_canal VARCHAR(30) NOT NULL PRIMARY KEY,
emoji VARCHAR NOT NULL DEFAULT '⭐',
minimo INT NOT NULL DEFAULT 1,
ids_destacados VARCHAR NOT NULL DEFAULT '',
ids_destaque VARCHAR NOT NULL DEFAULT '');
"""