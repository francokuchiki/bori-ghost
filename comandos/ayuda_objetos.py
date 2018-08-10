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
None,
None,
[
#info_informacion
("Información",
"Comando que brinda información sobre este bot.",
("information", "info"),
(None,),
"{}informacion",
"{}info",
[],
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
"Comandos que permiten ver o configurar los prefijos disponibles.",
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

info_moderacion = informacionComando(
"Moderación",
"En este módulo se encuentran todos los comandos de moderación que los administradores pueden usar. Se requieren permisos especiales \
que varían según cada comando.",
None,
(None,),
None,
None,
[
#info_nick
("Nick",
"Este comando permite cambiar el apodo de uno o más usuarios. Puede usarse para cambiar el propio.\n\
Requiere, en el primer caso, permiso de *administrar apodos* en el servidor y; en el segundo, premiso de *cambiar apodo*.",
("nicks", "setnick", "apodo", "apodos"),
("Usuario cuyo apodo quiere cambiarse. **Nota**: Ha de ser una mención.", "Apodo que se desea darle.",
"Usuario cuyo apodo quiere cambiarse. **Nota**: Ha de ser una mención. **Opcional**: Puede cambiarse el apodo de \
múltiples usuarios a la vez si se especifica. Si sólo desea cambiársele a uno, este parámetro **no** debe incluirse.",
"Apodo que se desea darle al segundo usuario. **Nota**: Si sólo desea cambiársele a uno, este parámetro **no** debe incluirse",
"**IMPORTANTE**: Si no quieres usar el cambio múltiple, pon solo los dos primeros parámetros."),
"{}nick <usuario> (mención) <apodo>",
"{}nick @BORI GHOST#1213 Ghost",
[]),
#info_roles
("Roles",
"Comandos que permiten dar o quitar roles a los usuarios. No pueden otorgarse roles que estén por encima del máximo poseído por el moderador.\n\
Requiere permiso de *administrar roles* en el servidor.",
("rol", "role"),
("Acción que se desea realizar. **Opcional**: Si no se especifica, se asumirá *toggle*.", "Usuario a quien desea dársele o quitársele \
un rol. **Nota**: Ha de ser una mención.", "Rol que desea dársele o quitársele. **Nota**: Debe ser el nombre (al menos su primera parte) \
o bien una mención.", "Usuario a quien desea dársele o quitársele un rol. **Nota**: Ha de ser una mención. **Opcional**: Puede modificarse \
los roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo para uno, este parámetro **no** debe incluirse.",
"Rol que desea dársele o quitársele. **Nota**: Debe ser el nombre (al menos su primera parte) o bien una mención. **Opcional**: Puede \
modificarse los roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo para uno, este parámetro **no** debe incluirse.",
"**IMPORTANTE** Si no quieres usar la edición múltiple de roles, usa solo los tres primeros parámetros."),
"{}roles <accion> (opcional) <usuario> (mencion) <rol> (comienzo del nombre o mención)",
"{}roles @BORI GHOST#1213 Developer",
[
#info_roles.dar
("Dar",
"Este comando otorga un rol a un usuario. Si el usuario ya tiene ese rol, no hace nada.\n\
Requiere permiso de *administrar roles* en el servidor.",
("da","dale", "give", "add"),
("Usuario a quien desea dársele un rol. **Nota**: Ha de ser una mención.", "Rol que desea dársele. **Nota**: Debe ser \
el nombre (al menos su primera parte o bien una mención.", "Usuario a quien desea dársele un rol. **Nota**: Ha de ser \
una mención. **Opcional**: Puede dársele roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo para \
uno, este parámetro **no** debe incluirse.", "Rol que desea dársele. **Nota**: Debe ser el nombre (al menos su primera \
parte) o bien una mención. **Opcional**: Puede dársele roles a varios usuarios a la vez si se especifica. Si sólo se desea \
hacerlo para uno, este parámetro **no** debe incluirse.", "**IMPORTANTE** Si no quieres usar la edición múltiple de roles, usa solo \
los dos primeros parámetros."),
"{}roles dar <usuario> (mención) <rol> (comienzo del nombre o mención)",
"{}roles dar @BORI GHOST#1213 Developer Profesional",
[]),
#info_roles.quitar
("Quitar",
"Este comando remueve un rol a un usuario. Si el usuario ya tiene ese rol, no hace nada.\n\
Requiere permiso de *administrar roles* en el servidor.",
("quita", "quitale","take", "remove"),
("Usuario a quien desea quitársele un rol. **Nota**: Ha de ser una mención.", "Rol que desea quitársele. **Nota**: Debe ser \
el nombre (al menos su primera parte o bien una mención.", "Usuario a quien desea quitársele un rol. **Nota**: Ha de ser \
una mención. **Opcional**: Puede quitársele roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo para \
uno, este parámetro **no** debe incluirse.", "Rol que desea quitársele. **Nota**: Debe ser el nombre (al menos su primera \
parte) o bien una mención. **Opcional**: Puede quitársele roles a varios usuarios a la vez si se especifica. Si sólo se desea \
hacerlo para uno, este parámetro **no** debe incluirse.", "**IMPORTANTE** Si no quieres usar la edición múltiple de roles, usa solo \
los dos primeros parámetros."),
"{}roles quitar <usuario> (mención) <rol> (comienzo del nombre o mención)",
"{}roles quitar @BORI GHOST#1213 Dev",
[]),
#info_roles.cambiar
("Cambiar",
"Este comando modifica los roles a un usuario, dejándole únicamente con el especificado.\n\
Requiere permiso de *administrar roles* en el servidor.",
("cambia", "cambiale", "change", "set"),
("Usuario cuyos roles desean modificarse. **Nota**: Ha de ser una mención.", "Rol que desea dejársele. **Nota**: Debe ser \
el nombre (al menos su primera parte o bien una mención.", "Usuario cuyos roles desean modificarse. **Nota**: Ha de ser \
una mención. **Opcional**: Puede cambiársele roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo para \
uno, este parámetro **no** debe incluirse.", "Rol que desea dejársele. **Nota**: Debe ser el nombre (al menos su primera \
parte) o bien una mención. **Opcional**: Puede cambiársele roles a varios usuarios a la vez si se especifica. Si sólo se desea \
hacerlo para uno, este parámetro **no** debe incluirse.", "**IMPORTANTE** Si no quieres usar la edición múltiple de roles, usa solo \
los dos primeros parámetros."),
"{}roles cambiar <usuario> (mención) <rol> (comienzo del nombre o mención)",
"{}roles cambiar @BORI GHOST#1213 Developer Prof",
[]),
#info_roles.toggle
("Toggle",
"Este comando otorga o remueve un rol a un usario. Si el usuario ya tiene el rol especificado, se lo quita y, si no lo tiene, se lo da.\n\
Requiere permiso de *administrar roles* en el servidor.",
(None,),
("Usuario a quien desea dársele o quitársele un rol. **Nota**: Ha de ser una mención.", "Rol que desea dársele o quitársele. **Nota**: \
Debe ser el nombre (al menos su primera parte) o bien una mención.", "Usuario a quien desea dársele o quitársele un rol. **Nota**: \
Ha de ser una mención. **Opcional**: Puede modificarse los roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo \
para uno, este parámetro **no** debe incluirse.", "Rol que desea dársele o quitársele. **Nota**: Debe ser el nombre (al menos su primera \
parte) o bien una mención. **Opcional**: Puede modificarse los roles a varios usuarios a la vez si se especifica. Si sólo se desea hacerlo \
para uno, este parámetro **no** debe incluirse.", "**IMPORTANTE** Si no quieres usar la edición múltiple de roles, usa solo los dos \
primeros parámetros."),
"{}roles toggle <usuario> (mención) <rol> (comienzo del nombre o mención)",
"{}roles toggle @BORI GHOST#1213 Develop",
[])
]),
#info_silencio
("Silencio",
"Modúlo con comandos que permiten silenciar a los usuarios, impidiéndoles enviar mensajes, y desilenciarlos, cancelando esa prohibición.\n\
Funciona dándoles un rol que debes crear manualmente llamado \"*CALLATE BOLUDO*\" o \"*Muted*\".\n\
Requiere permiso de *administrar roles* o *expulsar miembros* en el servidor.",
None,
(None,),
None,
None,
[
#info_silencio.silenciar
("Silenciar",
"Silencia a uno o más usuarios, impidiéndoles hablar en el servidor por un tiempo determinado. Puede especificarse el motivo por \
el que se los silencia y el tiempo (10min por defecto).\n\
Envía un mensaje al servidor por cada usuario silenciado y otro al propio usuario que incluye el tiempo y el motivo (si fue \
especificado).\n\
Requiere permiso de *administrar roles* o *expulsar miembros* en el servidor.",
("silencia", "mute"),
("Usuario al que se desea silenciar. **Nota**: Debe ser una mención.", "Razón por la que se le desea silenciar. **Opcional**",
"Tiempo durante el que se le desea silenciar. **Opcional**: Si no se especifica, será de 10 minutos. **Nota**: Pueden usarse sufijos \
para indicar distintas unidades de tiempo: **s** = segundos, **m** = minutos, **h** = horas, **d** = días, **w** = semanas, \
**a** = años.",
"Usuario al que se desea silenciar. **Nota**: Debe ser una mención. **Opcional**: Puede silenciarse a múltiples usuarios a la vez. Si \
sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.", "Razón por la que se le desea silenciar. **Opcional**: Puede \
silenciarse a múltiples usuarios a la vez. Si sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.",
"Tiempo durante el que se le desea silenciar. **Opcional**: Si no se especifica, será de 10 minutos. Puede \
silenciarse a múltiples usuarios a la vez. Si sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.",
"**IMPORTANTE**: Si no se desea usar el silencio múltiple, sólo deben incluirse los parámetros 1, 2 y 3.",
"**NOTA**: El orden de los parámetros 2 y 3 es indistinto."),
"{}silenciar <usuario> (mención) <tiempo> <usuario> (opcional) (mención) <tiempo> (opcional)",
"{}silenciar @BORI GHOST#1213 2a",
[])
])
],
"moderacion")