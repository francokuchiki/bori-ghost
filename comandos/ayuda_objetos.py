class informacionComando:
	def __init__(self, nombre, descripcion, alias, parametros, sintaxis, ejemplo, subs):
		self.nombre = nombre
		self.descripcion = descripcion
		self.alias = alias
		self.parametros = parametros
		self.sintaxis = sintaxis
		self.ejemplo = ejemplo
		self.subs = []
		for i in range(len(subs)):
			self.subs.append(informacionComando(subs[i][0], subs[i][1], subs[i][2], subs[i][3], subs[i][4], subs[i][5], subs[i][6]))
	def __str__(self):
		return nombre+": "+descripcion

info_utilidad = informacionComando(
"Utilidad",
"Este módulo contiene los comandos que son útiles para el usuario del bot.",
(None,),
(None,),
(None,),
(None,),
[
#info_informacion
("Información",
"Comando que brinda información sobre este bot.",
("information", "info"),
(None,),
"{}informacion",
"{}info",
[("Información",
"Comando que brinda información sobre este bot.",
("information", "info"),
(None,),
"{}informacion",
"{}info",
[])]),
#info_ayuda
("Ayuda",
"Muestra la lista de comandos o el modo de uso y la información sobre cada uno, \
según accedas a la ayuda general o específica.",
("help", "comandos", "commands"),
("Módulo o comando sobre el que se quiere recibir información.*",),
"{}ayuda <modulo/comando> (opcional)",
"{}ayuda prefijos.ver",
[]),
#info_prefijos
("Prefijos",
"Comandos que permiten ver o configurar los prefijos disponibles",
("prefijos", "prefix", "prefixes"),
("Acción que se desea realizar. Si no se especifica, se asume que quiere verse la lista.*","Si se quiere añadir, quitar o \
cambiar a un prefijo, debe especificarse cuál.**"),
"{}prefijos <acción> (opcional) <nuevo/viejo prefijo> (si se quiere añadir, quitar o cambiar)",
"{}prefijos ver",
[]),
#info_ping
("Ping",
"Consulta el tiempo de respuesta del bot.",
(None,),
(None,),
"{}ping",
"{}ping",
[])
]
)