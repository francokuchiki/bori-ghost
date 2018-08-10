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
"{}silenciar <usuario> (mención) <tiempo> (opcional) <razón> (opcional)\
<usuario> (mención) (opcional) <razón> (opcional) <tiempo> (opcional)",
"{}silenciar @BORI GHOST#1213 2a Prueba de silenciado.",
[]),
#info_silencio.desilenciar
("Desilenciar",
"Quita el silencio a uno o más usuarios pudiendo especificar una razón (individual para cada uno).\n\
Envía un mensaje al servidor por cada usuario desilenciado y uno al propio usuario, incluyendo el motivo (si fue especificado).",
("desilencia", "unmute"),
("Usuario al que se desea silenciar. **Nota**: Debe ser una mención.", "Razón por la que se le desea silenciar. **Opcional**",
"Usuario al que se desea silenciar. **Nota**: Debe ser una mención. **Opcional**: Puede silenciarse a múltiples usuarios a la vez. Si \
sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.", "Razón por la que se le desea silenciar. **Opcional**: Puede \
silenciarse a múltiples usuarios a la vez. Si sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.",
"**IMPORTANTE**: Si no se desea usar el desilenciado múltiple, sólo deben incluirse los parámetros 1 y 2."),
"{}desilenciar <usuario> (mención) <razón> <usuario> (mención) (opcional) <razón> (opcional)",
"{}desilenciar @BORI GHOST#1213 Prueba de desilenciado.",
[])
]),
#info_exclusion
("Exclusión",
"Módulo con comandos que permiten expulsar, banear y desbanear usuarios del servidor.\n\
Requiere permiso de *expulsar miembros*, en el primer caso, y de *banear miembros* en los otros dos.",
None,
(None,),
None,
None,
[
#info_exclusion.excluir
("Excluir",
"Expulsa a uno o más usuarios especificando una razón (individual para cada uno).\n\
Envía un mensaje al servidor por cada usuario excluido y, también, uno a cada usuario avisándole e incluyendo \
el motivo (si fue especificado).\n\
Requiere permiso de *excluir miembros* en el servidor.",
("kick",),
("Usuario al que se desea excluir. **Nota**: Debe ser una mención.", "Razón por la que se le desea excluir. **Opcional**",
"Usuario al que se desea excluir. **Nota**: Debe ser una mención. **Opcional**: Pueden excluirse múltiples usuarios a la vez. Si \
sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.", "Razón por la que se le desea excluir. **Opcional**: \
Pueden excluirse múltiples usuarios a la vez. Si sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.",
"**IMPORTANTE**: Si no se desea usar la exclusión múltiple, sólo deben incluirse los parámetros 1 y 2."),
"{}excluir <usuario> (mención) <razón> (opcional) <usuario> (mención) (opcional) <razón> (opcional)",
"{}excluir @BORI GHOST#1213 Prueba de exclusión.",
[]),
#info_exclusión.banear
("Banear",
"Banea a uno o más usuarios especificando una razón (individual para cada uno).\n\
Envía un mensaje al servidor por cada usuario baneado y, también, uno a cada usuario avisándole e incluyendo \
el motivo (si fue especificado).\n\
Requiere permiso de *banear miembros* en el servidor.",
("ban",),
("Usuario al que se desea banear. **Nota**: Debe ser una mención.", "Razón por la que se le desea banear. **Opcional**",
"Usuario al que se desea banear. **Nota**: Debe ser una mención. **Opcional**: Pueden banearse múltiples usuarios a la vez. Si \
sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.", "Razón por la que se le desea banear. **Opcional**: \
Pueden banearse múltiples usuarios a la vez. Si sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.",
"**IMPORTANTE**: Si no se desea usar el baneo múltiple, sólo deben incluirse los parámetros 1 y 2."),
"{}banear <usuario> (mención) <razón> (opcional> <usuario> (mención) (opcional) <razón> (opcional)",
"{}banear @BORI GHOST#1213 Prueba de ban.",
[]),
#info_exclusión.desbanear
("Desbanear",
"Desbanea a un usuario del servidor pudiendo especificar una razón para ello.\n\
Envía un mensaje en el servidor y puede, opcionalmente, enviar uno al usuario donde figura quién lo desbaneó y la razón \
(si fue especificada).\n\
Requiere permiso de *banear miembros* en el servidor.",
("unban",),
("Usuario al que se desea desbanear. **Nota**: Debe ser una mención.", "Razón por la que se le desea desbanear. **Opcional**",
"Si se le desea enviar un mensaje al usuario o no. **Opcional**. **Nota**: Puede escribirse lo que sea mientras no esté en blanco.",
"Usuario al que se desea desbanear. **Nota**: Debe ser una mención. **Opcional**: Pueden desbanearse múltiples usuarios a la vez. Si \
sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.", "Razón por la que se le desea desbanear. **Opcional**: \
Pueden desbanearse múltiples usuarios a la vez. Si sólo se desea hacerlo con uno, este parámetro **no** debe incluirse.",
"Si se le desea enviar un mensaje al usuario o no. **Opcional**: Pueden desbanearse múltiples usuarios a la vez. Si sólo se \
desea hacerlo con uno, este parámetro **no** debe incluirse.",
"**IMPORTANTE**: Si no se desea usar el desbaneo múltiple, sólo deben incluirse los parámetros 1 y 2.",
"**NOTA**: Entre cada parámetro debe haber un \";\" o un \"|\"."),
"{}desbanear <usuario>; <razón> (opcional); <aviso> (opcional)",
"{}desbanear @BORI GHOST#1213; Prueba de desbaneo; a",
[])
],
"exclusion"),
#info_confiables
("Confiables",
"Comandos que permiten añadir o quitar miembros de la lista de usuarios confiables así como darles el rol correspondiente. Al \
incluirlos en la lista, se les otorgará el rol automáticamente cada vez que entren al servidor.\n\
Funciona con un rol creado a mano llamado \"Confiable\".\n\
Requiere permiso de *administrar roles* en el servidor.",
("confiable", "conf", "confi", "confia", "confio"),
("Acción a realizar. **Opcional**: Si no se especifica, se asume que es toggle.", "Usuario a quien se desea añadir o quitar\
de la lista. **Nota**: Debe ser una mención.", "Usuario a quien se desea añadir o quitar de la lista. **Nota**: Debe ser una \
mención. **Opcional**: Puedes confiar o desconfiar en múltiples usuarios a la vez. Si sólo quieres hacerlo con uno, **no**\
incluyas este parámetro.",
"**IMPORTANTE**: Si no deseas usar la confianza múltiple, sólo deben incluirse los parámetros 1 y 2."),
"{}confiables <acción> (opcional) <usuario> (mención) <usuario> (mención) (opcional)",
"{}confiables @BORI GHOST#1213",
[
#info_confiables.añadir
("Añadir",
"Este comando añade a un usuario a la lista de confiables y le otorga el rol. Si el usuario ya está allí y tiene el rol, no\
hace nada.\n\
Requiere permiso de *administrar roles* en el servidor.",
("agregar", "añade", "agrega", "pon", "add", "put", "a"),
("Usuario a quien se desea añadir a la lista. **Nota**: Debe ser una mención.", "Usuario a quien se desea añadir a la lista. \
**Nota**: Debe ser una mención. **Opcional**: Puedes añadir múltiples usuarios a la vez. Si sólo quieres \
hacerlo con uno, **no** incluyas este parámetro.",
"**IMPORTANTE**: Si no deseas usar la confianza múltiple, sólo debe incluirse el primer parámetro."),
"{}confiables añadir <usuario> (mención) <usuario> (mención) (opcional)",
"{}confiables añadir @BORI GHOST#1213",
[]),
#info_confiables.quitar
("Quitar",
"Este comando elimina a un usuario de la lista de confiables y le quita el rol. Si el usuario no está allí ni tiene el rol, no\
hace nada.\n\
Requiere permiso de *administrar roles* en el servidor.",
("sacar", "quita", "saca", "remove", "delete", "rm", "del", "q"),
("Usuario a quien se desea quitar de la lista. **Nota**: Debe ser una mención.", "Usuario a quien se desea quitar de la lista. \
**Nota**: Debe ser una mención. **Opcional**: Puedes quitar múltiples usuarios a la vez. Si sólo quieres \
hacerlo con uno, **no** incluyas este parámetro.",
"**IMPORTANTE**: Si no deseas usar la confianza múltiple, sólo debe incluirse el primer parámetro."),
"{}confiables quitar <usuario> (mención) <usuario> (mención) (opcional)",
"{}confiables quitar @BORI GHOST#1213",
[]),
#info_confiables.toggle
("Toggle",
"Este comando agrega o elimina usuarios de la lista de confiables y les otorga o les quita el rol. Si el usuario está \
en la lista, lo quita; y si no está, lo añade.\n\
Requiere permiso de *administrar roles* en el servidor.",
(None,),
("Usuario a quien se desea añadir o quitar de la lista. **Nota: Debe ser una mención.", "Usuario a quien se desea \
añadir o quitar de la lista. **Nota: Debe ser una mención. **Opcional**: Puedes añadir o  quitar múltiples usuarios\
a la vez. Si sólo quieres hacerlo con uno, **no** incluyas este parámetro.",
"**IMPORTANTE**: Si no deseas usar la confianza múltiple, sólo debe incluirse el primer parámetro."),
"{}confiables toggle <usuario> (mención) <usuario> (mención) (opcional)",
"{}confiables toggle @BORI GHOST#1213",
[])
])
],
"moderacion")