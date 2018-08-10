class informacionComando:
	def __init__(self, nombre, descripcion, alias, parametros, sintaxis, ejemplo, subs, ident=None):
		self.nombre = nombre
		self.descripcion = descripcion
		self.alias = alias
		self.parametros = parametros
		self.sintaxis = sintaxis
		self.ejemplo = ejemplo
		self.subs = []
		for i in range(len(subs)):
			sub_ident = None
			if len(subs[i]) >= 8:
				sub_ident = subs[i][7]
			self.subs.append(informacionComando(subs[i][0], subs[i][1], subs[i][2], subs[i][3], subs[i][4], subs[i][5], subs[i][6], sub_ident))
		if ident != None:
			self.ident = ident
		else:
			self.ident = nombre
	def __str__(self):
		return nombre+": "+descripcion

info_utilidad = informacionComando(
"Utilidad",
"Este módulo contiene los comandos que son útiles para el usuario del bot.",
None,
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
[],
"informacion")],
"informacion"),
#info_ayuda
("Ayuda",
"Muestra la lista de comandos o el modo de uso y la información sobre cada uno, \
según accedas a la ayuda general o específica.",
("help", "comandos", "commands"),
("Módulo o comando sobre el que se quiere recibir información. **Opcional**: Si no se especifica, se accederá a la ayuda general.",),
"{}ayuda <modulo / comando> (opcional)",
"{}ayuda prefijos.ver",
[]),
#info_prefijos
("Prefijos",
"Comandos que permiten ver o configurar los prefijos disponibles",
("prefijos", "prefix", "prefixes"),
("Acción que se desea realizar. **Opcional**: Si no se especifica, se asume que quiere verse la lista.","Si se quiere añadir, \
quitar o cambiar a un prefijo, debe especificarse cuál. **Nota**: Sólo si la acción deseada es *añadir*, *quitar* o *cambiar*."),
"{}prefijos <acción> (opcional) <nuevo / viejo prefijo> (si se quiere añadir, quitar o cambiar)",
"{}prefijos ver",
[
#info_prefijos.ver
("Ver",
"Muestra la lista de prefijos disponibles actualmente.",
None,
(None,),
"{}prefijos ver",
"{}prefijos ver",
[]),
("Añadir",
"Agrega un nuevo prefijo a la lista para poder utilizarlo.",
("agregar", "añade", "agrega", "nuevo", "pon", "add", "new"),
("Prefijo que se desea incluir en la lista.",),
"{}prefijos añadir <prefijo>",
"{}prefijos añadir $",
[]),
("Quitar",
"Elimina un prefijo de la lista por lo que deja de ser utilizable.",
("borrar", "quita", "borra", "remove", "delete"),
("Prefijo que se desea remover de la lista.",),
"{}prefijos quitar <prefijo>",
"{}prefijos quitar $",
[]),
("Cambiar",
"Elimina todos los prefijos disponibles y los reemplaza por uno nuevo. Éste se convertirá en el único utilizable.",
("cambia", "solo", "unico", "sólo", "único", "change", "only", "set"),
("Prefijo que quieres establecer como único disponible.",),
"{}prefijos cambiar <prefijo>",
"{}prefijos cambiar $",
[])
]),
#info_ping
("Ping",
"Consulta el tiempo de respuesta del bot.",
None,
(None,),
"{}ping",
"{}ping",
[])
]
)