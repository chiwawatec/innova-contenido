"""Ampliación de «Seguridad en Obra y Trabajos en Altura» (≈7 min por clase). Misma receta que los demás cursos.
Orientación general: para cada caso, consultar con un especialista en seguridad y salud en el trabajo."""
from naves_ext import insertar, caja, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · El orden de los controles ─────────────
EXT['seg_c1'] = [
  ejemplo('El orden, <span class="nar">peligro por peligro</span>', [
    'Antes de los errores, el orden de los controles aplicado a cuatro peligros de nuestra nave.',
    'Caer al soldar arriba: lo eliminamos armando y soldando los arcos en el piso. Caer al colocar correas: línea de vida, que protege a todos.',
    'Que caiga una herramienta: zona marcada abajo y herramientas amarradas. Chispas en los ojos: lentes y careta, la última barrera.',
  ], ['Peligro', 'Control', 'Tipo'],
    [['Caer al soldar arriba', 'Soldar los arcos en el piso', 'Eliminar'], ['Caer al colocar correas', 'Línea de vida', 'Colectivo'], ['Caída de herramientas', 'Zona marcada y herramientas amarradas', 'Colectivo'], ['Chispas en los ojos', 'Lentes y careta', 'Personal']],
    lambda i: [1, 1, 2, 2][i], izq=200, der=200),
  caso('“es solo un ratito”', [
    'Caso de obra: el ayudante subió al techo de tres metros a pasar una herramienta. "Es solo un ratito", no se puso el arnés.',
    'Pisó mal y cayó. Se fracturó el brazo. Dos meses sin trabajar, la obra atrasada y el cliente preocupado.',
    'Ese ratito era justo el momento de mayor riesgo, porque nadie lo había planeado. Por eso el arnés va puesto antes de subir, siempre.',
  ], [('⏱️', '"<b class="nar">Es solo un ratito</b>"'), ('🦴', 'Brazo fracturado: <b class="nar">dos meses</b> sin trabajar'), ('✅', 'El arnés va <b class="nar">antes de subir</b>')]),
  *ejercicio(1,
    'Clasifica cada control: <b class="nar">eliminar</b>, <b class="nar">colectivo</b> o <b class="nar">personal</b>.<br>a) Baranda en el borde de la losa · b) Guantes de cuero<br>c) Pintar las piezas en el taller y no en altura · d) Malla sobre la claraboya',
    ['Ahora tú. Clasifica cada control: eliminar, colectivo o personal.', 'a: baranda en el borde de la losa. b: guantes de cuero. c: pintar las piezas en el taller y no en altura. Y d: malla sobre la claraboya.'],
    'a) <b class="nar">Colectivo</b> · b) <b class="nar">Personal</b><br>c) <b class="nar">Eliminar</b> (ya no se trabaja en altura) · d) <b class="nar">Colectivo</b>',
    ['La baranda: colectivo. Los guantes: personal.',
     'Pintar en el taller: elimina el peligro de altura. Y la malla sobre la claraboya: colectivo, protege a todos sin que nadie tenga que acordarse.']),
  *ejercicio(2,
    'Un accidente para la obra <b class="nar">5 días</b>. Tu equipo cuesta <b class="nar">S/ 900 por día</b>,<br>aunque no trabaje. La línea de vida que faltaba costaba <b class="nar">S/ 1 200</b>.<br>¿Qué salió más caro?',
    ['Segundo ejercicio. Un accidente para la obra cinco días. Tu equipo te cuesta novecientos soles por día, aunque no trabaje. La línea de vida que faltaba costaba mil doscientos.', '¿Qué salió más caro?'],
    'Obra parada: 5 × 900 = <b class="nar">S/ 4 500</b><br>Línea de vida: <b class="nar">S/ 1 200</b><br>Y eso sin contar <b class="nar">la persona</b>, la multa ni el cliente perdido',
    ['Cinco días parados: cuatro mil quinientos soles. La línea de vida: mil doscientos.',
     'Y eso sin contar lo más importante, la persona herida, ni la multa ni el cliente que no te vuelve a llamar.']),
  faq([
    ('¿Y si el cliente no paga la seguridad?', 'Va en tu precio; no se negocia.', '¿Y si el cliente no quiere pagar la seguridad? Va dentro de tu precio, como cualquier material. No se negocia.'),
    ('¿El arnés basta?', 'Es la última barrera; primero lo colectivo.', '¿Con el arnés basta? Es la última barrera. Primero se elimina el peligro o se pone protección colectiva.'),
    ('¿Cuánto tiempo toma?', 'Minutos al día; un accidente, meses.', '¿Cuánto tiempo toma todo esto? Unos minutos al día. Un accidente puede tomar meses.'),
  ]),
  repaso([
    ('¿Cuál es el control más efectivo?', 'Eliminar el peligro.'),
    ('¿Qué es protección colectiva?', 'La que cuida a todos sin que nadie tenga que acordarse.'),
    ('¿Cuál es la última barrera?', 'El equipo de protección personal.'),
    ('¿La seguridad es gasto?', 'No: también es negocio.'),
  ]),
]

# ───────────── Clase 2 · La ley en simple ─────────────
EXT['seg_c2'] = [
  ejemplo('Las cuatro normas <span class="nar">en una tabla</span>', [
    'Antes de los errores, las cuatro normas que más vas a escuchar, en una tabla. Orientación general.',
    'La Ley veintinueve mil setecientos ochenta y tres, con su reglamento, el Decreto Supremo cero cero cinco del dos mil doce: la base para todos.',
    'El reglamento del sector construcción, el Decreto Supremo cero once del dos mil diecinueve. Y la Norma G punto cero cincuenta, con las reglas técnicas.',
    'Y el SCTR, el seguro complementario de trabajo de riesgo, para cada trabajador de construcción.',
  ], ['Norma', 'Qué es'],
    [['Ley 29783 + DS 005-2012-TR', 'Seguridad y salud en el trabajo (todos)'], ['DS 011-2019-TR', 'Reglamento del sector construcción'], ['Norma G.050', 'Reglas técnicas de seguridad en obra'], ['SCTR', 'Seguro para trabajos de riesgo']],
    lambda i: [1, 2, 2, 3][i], izq=240, der=240),
  ejemplo('¿Hace falta <span class="nar">el arnés</span>?', [
    'Y la regla del uno ochenta aplicada a tres casos. La norma lo exige si la caída libre puede superar un metro ochenta, y cerca de bordes sin protección.',
    'Colocar correas en un techo a tres metros: sí, arnés. Soldar al borde de una losa, aunque esté a poca altura: sí, por el borde sin protección.',
    'Trabajar en una plataforma con baranda completa: la baranda ya protege. Pero si te asomas o te subes a algo, vuelve el arnés.',
  ], ['Situación', '¿Arnés?'],
    [['Techo a 3 m, colocando correas', 'Sí'], ['Borde de losa sin baranda', 'Sí'], ['Plataforma con baranda completa', 'La baranda protege (si te asomas, arnés)']],
    lambda i: [1, 2, 3][i], izq=260, der=260),
  caso('sin SCTR', [
    'Caso de obra: un contratista pequeño no tenía el SCTR de su ayudante, "porque era una obra corta".',
    'El ayudante se cortó la mano con la amoladora. Los gastos de la atención los pagó el contratista de su bolsillo, y la empresa cliente lo sacó de la obra.',
    'El SCTR se saca antes de empezar, por los días de obra. Es un costo pequeño frente a lo que cubre.',
  ], [('📄', 'Sin <b class="nar">SCTR</b> "por ser obra corta"'), ('🩹', 'Un corte: gastos de su <b class="nar">bolsillo</b>'), ('✅', 'SCTR <b class="nar">antes de empezar</b>')]),
  *ejercicio(1,
    'Una empresa te contrata con <b class="nar">4 trabajadores</b> para un montaje en altura.<br>¿Qué documentos llevas el primer día?',
    ['Ahora tú. Una empresa te contrata con cuatro trabajadores para un montaje en altura.', '¿Qué documentos llevas el primer día?'],
    '• <b class="nar">SCTR</b> vigente de los 4 · • <b class="nar">IPERC</b> o análisis de riesgos del trabajo<br>• Modelos de <b class="nar">ATS y PETAR</b> · • Certificado de <b class="nar">arneses y líneas</b><br>• Constancias de <b class="nar">entrega de EPP</b> y de capacitación',
    ['El SCTR vigente de los cuatro, el análisis de riesgos del trabajo, y tus modelos de ATS y de permiso de trabajo en altura.',
     'Además, el certificado de los arneses y las líneas, y las constancias de entrega de EPP y de capacitación. Todo eso lo vemos en las próximas clases.']),
  *ejercicio(2,
    '¿Arnés o no? a) Escalera de <b class="nar">1.20 m</b> para cambiar un foco<br>b) Andamio a <b class="nar">2.50 m</b> sin baranda · c) Techo de cochera a <b class="nar">2.40 m</b><br>d) Losa a 3 m con baranda completa, sin asomarse',
    ['Segundo ejercicio. ¿Arnés o no? a: escalera de uno veinte para cambiar un foco. b: andamio a dos cincuenta, sin baranda. c: techo de cochera a dos cuarenta. Y d: losa a tres metros, con baranda completa, sin asomarse.'],
    'a) No por la regla del 1.80, pero <b class="nar">tres puntos de apoyo</b><br>b) <b class="nar">Sí</b> (y mejor completar la baranda) · c) <b class="nar">Sí</b><br>d) La <b class="nar">baranda protege</b>; si te asomas, arnés',
    ['a: no llega a la regla del uno ochenta, pero igual, tres puntos de apoyo en la escalera. b: sí, y lo correcto es completar la baranda.',
     'c: sí, la caída puede superar uno ochenta. Y d: la baranda completa protege, mientras no te asomes ni te subas a algo.']),
  faq([
    ('¿La ley vale si trabajo solo?', 'Sí: alcanza también a independientes.', '¿La ley me alcanza si trabajo solo? Sí, también a los trabajadores por cuenta propia. Y tu cuerpo es tu herramienta.'),
    ('¿Dónde saco el SCTR?', 'Con una aseguradora o corredor.', '¿Dónde saco el SCTR? Con una aseguradora o un corredor de seguros, por el tiempo de la obra.'),
    ('¿Quién fiscaliza?', 'SUNAFIL, en trabajos con trabajadores.', '¿Quién fiscaliza? La SUNAFIL, en los centros de trabajo. Es orientación general: consulta con un especialista para tu caso.'),
  ]),
  repaso([
    ('¿Qué número no se olvida?', 'Uno ochenta: desde ahí, sistema de detención de caídas.'),
    ('¿Qué es el SCTR?', 'El seguro complementario de trabajo de riesgo.'),
    ('¿Qué norma tiene las reglas técnicas?', 'La Norma G punto cero cincuenta.'),
    ('¿Basta con tener los papeles?', 'No: hay que cumplirlos.'),
  ]),
]

# ───────────── Clase 3 · IPERC, ATS y PETAR ─────────────
EXT['seg_c3'] = [
  ejemplo('Una fila <span class="nar">del IPERC</span>', [
    'Antes de los errores, cómo se ve una fila del IPERC de la nave.',
    'Tarea: colocar correas sobre los arcos. Peligro: caída de altura. Probabilidad: media. Gravedad: muy alta. Riesgo: alto.',
    'Controles: línea de vida instalada antes de subir, arnés con línea en Y, y zona marcada abajo. Con eso, el riesgo baja.',
  ], ['Campo', 'Ejemplo'],
    [['Tarea', 'Colocar correas sobre los arcos'], ['Peligro', 'Caída de altura'], ['Probabilidad × gravedad', 'Media × muy alta = riesgo alto'], ['Controles', 'Línea de vida, arnés en Y, zona marcada']],
    lambda i: [1, 1, 1, 2][i], izq=300, der=300),
  ejemplo('Un ATS <span class="nar">de tres pasos</span>', [
    'Y un ATS del izaje de un arco, en tres pasos.',
    'Paso uno: estrobar el arco. Peligro: golpes y atrapamiento. Control: estrobos revisados, guantes, manos fuera de los puntos de pellizco.',
    'Paso dos: izar. Peligro: carga que cae o gira. Control: zona aislada, señalero, cuerdas guía. Paso tres: fijar el arco. Peligro: caída de altura. Control: arnés enganchado.',
  ], ['Paso', 'Peligro', 'Control'],
    [['1. Estrobar', 'Golpes y atrapamiento', 'Estrobos revisados, guantes, manos fuera'], ['2. Izar', 'Carga que cae o gira', 'Zona aislada, señalero, cuerdas guía'], ['3. Fijar en altura', 'Caída de altura', 'Arnés enganchado']],
    lambda i: [1, 2, 2][i], izq=180, der=180, tam=28),
  caso('el viento de la tarde', [
    'Caso de obra: el ATS de la mañana era para colocar planchas sin viento. A las tres de la tarde, el viento subió fuerte.',
    'Nadie paró. Una plancha se levantó y golpeó a un trabajador en el hombro. Por suerte, sin fractura.',
    'Cuando cambian las condiciones, cambia el ATS. Y cualquiera puede parar el trabajo, sin que lo regañen.',
  ], [('🌬️', 'El viento <b class="nar">subió</b> en la tarde'), ('🪧', 'Nadie paró: una plancha <b class="nar">golpeó</b> a un trabajador'), ('✅', 'Cambian las condiciones, <b class="nar">se para y se rehace el ATS</b>')]),
  *ejercicio(1,
    'Haz el ATS de <b class="nar">soldar correas</b> en un techo a 4 m, en tres pasos:<br>subir · soldar · bajar.',
    ['Ahora tú. Haz el ATS de soldar correas en un techo a cuatro metros, en tres pasos: subir, soldar y bajar.'],
    '1. Subir: <b class="nar">caída</b> → escalera amarrada, 3 puntos, arnés antes de subir<br>2. Soldar: <b class="nar">chispas e incendio</b> → mantas, extintor, vigía; <b class="nar">caída</b> → enganchado<br>3. Bajar: <b class="nar">caída y herramientas</b> → manos libres, herramientas en bolso',
    ['Subir: peligro de caída. Escalera amarrada, tres puntos de apoyo, y el arnés puesto antes de subir.',
     'Soldar: chispas e incendio, con mantas, extintor y vigía; y caída, enganchado siempre. Y bajar: con las manos libres y las herramientas en un bolso.']),
  *ejercicio(2,
    '¿Cuáles de estos trabajos necesitan <b class="nar">PETAR</b>?<br>a) Soldar en un techo · b) Pintar una reja en el piso · c) Entrar a un tanque<br>d) Conectar el tablero · e) Cortar con amoladora en el taller',
    ['Segundo ejercicio. ¿Cuáles de estos trabajos necesitan permiso de trabajo de alto riesgo?', 'a: soldar en un techo. b: pintar una reja en el piso. c: entrar a un tanque. d: conectar el tablero. Y e: cortar con amoladora en el taller.'],
    'Sí: <b class="nar">a</b> (altura y caliente), <b class="nar">c</b> (espacio confinado), <b class="nar">d</b> (energía eléctrica)<br>Normalmente no: <b class="nar">b</b> y <b class="nar">e</b> (salvo que el lugar lo pida)<br>Todos llevan su <b class="nar">ATS</b>',
    ['Necesitan PETAR: soldar en el techo, por altura y calor; entrar a un tanque, espacio confinado; y conectar el tablero, energía eléctrica.',
     'Pintar en el piso y cortar en el taller normalmente no, salvo que el lugar lo pida. Pero todos llevan su ATS.']),
  faq([
    ('¿Quién firma el PETAR?', 'El que ejecuta y el que autoriza.', '¿Quién firma el PETAR? El que ejecuta el trabajo y el que lo autoriza, por ejemplo el supervisor.'),
    ('¿El ATS es diario?', 'Sí, antes de empezar y si algo cambia.', '¿El ATS se hace todos los días? Sí, antes de empezar, y otra vez si cambian las condiciones.'),
    ('¿Tengo modelos?', 'Sí: vienen con el curso.', '¿Hay modelos? Sí, con este curso viene un modelo de ATS y de plan de emergencia.'),
  ]),
  repaso([
    ('¿Cuándo se hace el IPERC?', 'Una vez, al planificar la obra.'),
    ('¿Cuándo se hace el ATS?', 'Cada día, antes de empezar.'),
    ('¿Qué es el PETAR?', 'El permiso escrito de trabajo de alto riesgo.'),
    ('¿Quién puede parar el trabajo?', 'Cualquiera que vea una condición peligrosa.'),
  ]),
]

# ───────────── Clase 4 · El EPP correcto ─────────────
EXT['seg_c4'] = [
  ejemplo('EPP <span class="nar">por tarea</span>', [
    'Antes de los errores, el equipo extra que pide cada tarea, en una tabla.',
    'Soldar: careta con filtro, guantes largos de cuero, mandil y respirador para humos. Amoladora: careta facial sobre los lentes, guantes y orejeras.',
    'Pintar con pistola: respirador con filtro para vapores, y lentes. Y en altura: casco con barbiquejo y arnés.',
  ], ['Tarea', 'Además del EPP básico'],
    [['Soldar', 'Careta con filtro, guantes largos, mandil, respirador'], ['Amoladora', 'Careta facial sobre lentes, guantes, orejeras'], ['Pintar con pistola', 'Respirador para vapores, lentes'], ['Altura', 'Casco con barbiquejo, arnés']],
    lambda i: [1, 1, 2, 2][i], izq=240, der=240),
  caso('los lentes en la frente', [
    'Caso de taller: un ayudante esmerilaba con los lentes subidos en la frente, "porque se empañaban".',
    'Una esquirla le entró al ojo. Lo atendieron a tiempo, pero estuvo una semana sin poder trabajar.',
    'Si se empañan, se compran lentes antiempañantes. Los lentes van en los ojos, no en la frente.',
  ], [('🥽', 'Lentes <b class="nar">en la frente</b>'), ('👁️', 'Esquirla en el ojo: <b class="nar">una semana</b> sin trabajar'), ('✅', 'Lentes <b class="nar">antiempañantes</b>, en los ojos')]),
  *ejercicio(1,
    'Arma el pedido de EPP para <b class="nar">4 trabajadores</b>, de los cuales <b class="nar">1 suelda</b>,<br>para un montaje en altura con amoladora.',
    ['Ahora tú. Arma el pedido de EPP para cuatro trabajadores, de los cuales uno suelda, para un montaje en altura con amoladora.'],
    'Para los 4: <b class="nar">casco con barbiquejo</b>, lentes, careta facial, guantes, orejeras,<br>botas, chaleco y <b class="nar">arnés con línea</b><br>Para el soldador: <b class="nar">careta de soldar, guantes largos, mandil y respirador</b>',
    ['Para los cuatro: casco con barbiquejo, lentes, careta facial, guantes, orejeras, botas, chaleco, y arnés con su línea.',
     'Y para el soldador, además: careta de soldar con su filtro, guantes largos, mandil y respirador. Todo anotado en la hoja de entrega con firma.']),
  *ejercicio(2,
    'Revisas el EPP: un casco <b class="nar">rajado</b>, unos guantes <b class="nar">con un hueco</b>,<br>unas botas con la <b class="nar">suela lisa</b> y unos lentes <b class="nar">sin rayas</b>.<br>¿Qué cambias?',
    ['Segundo ejercicio. Revisas el EPP: un casco rajado, unos guantes con un hueco, unas botas con la suela lisa, y unos lentes sin rayas.', '¿Qué cambias?'],
    'Cambias: <b class="nar">casco</b>, <b class="nar">guantes</b> y <b class="nar">botas</b><br>Los lentes, <b class="nar">sirven</b><br>Un EPP malogrado da <b class="nar">falsa seguridad</b>',
    ['Se cambian el casco rajado, los guantes rotos y las botas con la suela lisa.',
     'Los lentes sin rayas, sirven. Recuerda: un equipo malogrado da una falsa seguridad.']),
  faq([
    ('¿Quién paga el EPP?', 'El empleador lo entrega.', '¿Quién paga el EPP? El empleador lo entrega a su gente, y deja constancia con la firma.'),
    ('¿Casco con barbiquejo siempre?', 'En altura, sí.', '¿El casco siempre con barbiquejo? En altura, sí. Si te agachas, el casco no debe caerse.'),
    ('¿Qué respirador para soldar?', 'Uno para humos de soldadura.', '¿Qué respirador uso para soldar? Uno para humos metálicos. Pregunta al proveedor por el filtro adecuado.'),
  ]),
  repaso([
    ('¿Qué lleva el casco en altura?', 'Barbiquejo.'),
    ('¿Qué ropa nunca para soldar?', 'Sintética.'),
    ('¿Qué haces con un EPP malogrado?', 'Cambiarlo.'),
    ('¿Cómo queda constancia de la entrega?', 'Con una hoja firmada.'),
  ]),
]

# ───────────── Clase 5 · Arnés, línea y anclaje ─────────────
EXT['seg_c5'] = [
  ejemplo('¿Este punto <span class="nar">sirve de anclaje</span>?', [
    'Antes de los errores, puntos de anclaje que sí sirven y que no.',
    'Sirven: una viga o columna metálica bien soldada, un anclaje certificado, una línea de vida bien instalada.',
    'No sirven: una baranda, un tubo delgado, una correa liviana, una tubería o un árbol. No aguantan dos mil doscientos sesenta y cinco kilos.',
  ], ['Sí sirve', 'No sirve'],
    [['Viga o columna metálica bien soldada', 'Baranda o tubo delgado'], ['Anclaje certificado', 'Correa liviana'], ['Línea de vida bien instalada', 'Tubería o canaleta']],
    lambda i: i + 1, izq=280, der=280),
  caso('enganchado a la baranda', [
    'Caso de obra: un trabajador se enganchó a la baranda de tubo de una plataforma, "porque estaba cerca".',
    'Al resbalar, la baranda se dobló con el tirón. No cayó porque su compañero lo agarró del arnés.',
    'Una baranda está hecha para apoyarse, no para frenar una caída. El anclaje se elige antes de subir, y aguanta dos mil doscientos sesenta y cinco kilos.',
  ], [('🔗', 'Enganchado a una <b class="nar">baranda</b>'), ('↘️', 'La baranda <b class="nar">se dobló</b> con el tirón'), ('✅', 'Anclaje de <b class="nar">2 265 kg</b>, elegido antes')]),
  *ejercicio(1,
    'Tienes que pasar <b class="nar">por un lado de una columna</b> en altura.<br>¿Por qué usas línea en Y y cómo pasas?',
    ['Ahora tú. Tienes que pasar por un lado de una columna, en altura.', '¿Por qué usas línea en Y, y cómo pasas?'],
    'Con la Y siempre estás enganchado a algo (<b class="nar">100 %</b>)<br>1. Enganchas el ramal libre <b class="nar">del otro lado</b> de la columna<br>2. Recién ahí <b class="nar">sueltas</b> el primero',
    ['La línea en Y te permite estar siempre enganchado.',
     'Primero enganchas el ramal libre del otro lado de la columna, y recién después sueltas el primero. Nunca quedas suelto.']),
  *ejercicio(2,
    '<b class="nar">Tres trabajadores</b> van a usar el mismo punto de anclaje.<br>¿Cuánto debe resistir ese punto?',
    ['Segundo ejercicio. Tres trabajadores van a usar el mismo punto de anclaje.', '¿Cuánto debe resistir ese punto?'],
    '2 265 kg por trabajador × 3 = <b class="nar">6 795 kg</b><br>Si no estás seguro de que aguante: <b class="nar">un anclaje por persona</b><br>o una <b class="nar">línea de vida</b> diseñada para varios',
    ['Dos mil doscientos sesenta y cinco por tres: seis mil setecientos noventa y cinco kilos.',
     'Si no estás seguro de que aguante, mejor un anclaje por persona, o una línea de vida diseñada para varios trabajadores.']),
  faq([
    ('¿Cada cuánto se cambia el arnés?', 'Según el fabricante, o si frenó una caída.', '¿Cada cuánto se cambia el arnés? Según lo que diga el fabricante, y siempre que haya frenado una caída o tenga daños.'),
    ('¿Puedo lavar el arnés?', 'Con agua y jabón suave, secado a la sombra.', '¿Se puede lavar el arnés? Con agua y jabón suave, y secado a la sombra. Nada de solventes.'),
    ('¿Sirve un cinturón de seguridad?', 'No: siempre arnés de cuerpo entero.', '¿Sirve un cinturón? No. Siempre arnés de cuerpo entero.'),
  ]),
  repaso([
    ('¿Cuáles son las tres partes del sistema?', 'Arnés, línea de anclaje y punto de anclaje.'),
    ('¿Cuánto mide la línea como máximo?', 'Un metro ochenta.'),
    ('¿Cuánto resiste un anclaje por trabajador?', 'Dos mil doscientos sesenta y cinco kilos.'),
    ('¿Qué pasa con un arnés que frenó una caída?', 'Se descarta.'),
  ]),
]

# ───────────── Clase 6 · Espacio libre y rescate ─────────────
EXT['seg_c6'] = [
  ejemplo('El espacio libre, <span class="nar">sumado</span>', [
    'Antes de los errores, la suma del espacio libre de caída, parte por parte, medida desde el anclaje.',
    'Línea: un metro ochenta. Amortiguador abierto: hasta un metro seis. Tu cuerpo, de la argolla a los pies: un metro y medio.',
    'Y un margen de seguridad de un metro. En total, unos cinco metros cuarenta: por eso la regla de cinco y medio.',
  ], ['Parte', 'Metros'],
    [['Largo de la línea', '1.80'], ['Amortiguador abierto', 'hasta 1.06'], ['Argolla a los pies', '≈ 1.50'], ['Margen de seguridad', '1.00'], ['Total bajo el anclaje', '≈ 5.40 → 5.5 m']],
    lambda i: [1, 1, 1, 2, 2][i], izq=440, der=440, tam=30),
  caso('el rescate que nadie planeó', [
    'Caso de obra: un trabajador cayó y quedó colgado del arnés, sano, a cinco metros. Su línea funcionó perfecto.',
    'Pero nadie sabía cómo bajarlo. Pasaron varios minutos hasta que trajeron un andamio. Él ya estaba pálido y mareado.',
    'Desde ese día, en esa obra el andamio de rescate quedaba armado cerca, y dos personas sabían usarlo. El rescate se planea antes de subir.',
  ], [('🧗', 'Colgado del arnés, <b class="nar">sano</b>'), ('⏳', 'Nadie sabía <b class="nar">cómo bajarlo</b>'), ('✅', 'Rescate <b class="nar">planeado antes</b> de subir')]),
  *ejercicio(1,
    'Trabajas a <b class="nar">4 m</b> del piso. ¿Alcanza el espacio libre si el anclaje está<br>a) <b class="nar">a la altura de tus pies</b> (4 m del piso)?<br>b) <b class="nar">sobre tu cabeza</b>, a 6 m del piso?',
    ['Ahora tú. Trabajas a cuatro metros del piso.', '¿Alcanza el espacio libre si el anclaje está a la altura de tus pies, a cuatro metros del piso? ¿Y si está sobre tu cabeza, a seis metros del piso?'],
    'Necesitas ≈ <b class="nar">5.5 m</b> bajo el anclaje<br>a) Anclaje a 4 m: <b class="nar">no alcanza</b> → línea retráctil o subir el anclaje<br>b) Anclaje a 6 m: <b class="nar">sí alcanza</b> (6.0 ≥ 5.5)',
    ['Necesitas unos cinco metros y medio bajo el anclaje.',
     'Con el anclaje a cuatro metros, no alcanza: llegarías al piso. Usa línea retráctil o sube el anclaje. Con el anclaje a seis metros, sobre tu cabeza, sí alcanza.']),
  *ejercicio(2,
    'Escribe el <b class="nar">plan de rescate</b> de tu obra en cuatro líneas.',
    ['Segundo ejercicio. Escribe el plan de rescate de tu obra, en cuatro líneas.'],
    '1. <b class="nar">Quién</b> rescata: dos personas entrenadas<br>2. <b class="nar">Con qué</b>: andamio armado o equipo de rescate<br>3. <b class="nar">Cómo</b> se llega a cada punto de la obra<br>4. <b class="nar">A quién</b> se llama: 116 Bomberos · 106 SAMU',
    ['Quién rescata: dos personas entrenadas. Con qué: el andamio armado o un equipo de rescate.',
     'Cómo se llega a cada punto de la obra. Y a quién se llama: ciento dieciséis, bomberos, y ciento seis, el SAMU. Y mientras, el que está colgado mueve las piernas.']),
  faq([
    ('¿Qué es la línea retráctil?', 'Se traba en centímetros, como el cinturón del auto.', '¿Qué es una línea retráctil? Funciona como el cinturón del auto: se traba en centímetros, y necesita mucho menos espacio libre.'),
    ('¿Cuánto tiempo aguanta alguien colgado?', 'Poco: rescatar lo antes posible.', '¿Cuánto tiempo aguanta alguien colgado? Poco. La regla es rescatar lo antes posible, sin esperar.'),
    ('¿Y el efecto péndulo?', 'Ánclate lo más vertical sobre ti.', '¿Cómo evito el péndulo? Engánchate lo más vertical posible sobre ti, y mueve el anclaje mientras avanzas.'),
  ]),
  repaso([
    ('¿Cuánto espacio libre necesitas con línea de uno ochenta?', 'Unos cinco metros y medio.'),
    ('¿Qué haces si no alcanza?', 'Subir el anclaje, usar retráctil o protección colectiva.'),
    ('¿Qué es el trauma por suspensión?', 'Quedar colgado quieto corta la circulación.'),
    ('¿Cuándo se planea el rescate?', 'Antes de subir.'),
  ]),
]

# ───────────── Clase 7 · Andamios y escaleras ─────────────
EXT['seg_c7'] = [
  ejemplo('Las tarjetas <span class="nar">del andamio</span>', [
    'Antes de los errores, las tres tarjetas del andamio en una tabla.',
    'Verde: completo y revisado. Se usa, y en altura, con arnés enganchado.',
    'Amarilla: falta algo. Solo con el arnés enganchado todo el tiempo. Roja: prohibido subir.',
  ], ['Tarjeta', 'Significa', 'Se puede'],
    [['Verde', 'Completo y revisado', 'Usar (con arnés en altura)'], ['Amarilla', 'Falta algo', 'Solo con arnés enganchado siempre'], ['Roja', 'Peligroso', 'No subir']],
    lambda i: [1, 2, 2][i], izq=280, der=280),
  ejemplo('La regla <span class="nar">del cuatro a uno</span>', [
    'Y la regla de la escalera, con números. Por cada cuatro metros de altura, un metro de separación en la base.',
    'Para subir a tres metros: setenta y cinco centímetros. A cuatro metros: un metro. A cinco: un metro veinticinco.',
    'Y que sobresalga un metro sobre el punto donde bajas, amarrada arriba.',
  ], ['Altura de apoyo', 'Separación de la base'],
    [['3 m', '0.75 m'], ['4 m', '1.00 m'], ['5 m', '1.25 m']],
    lambda i: [1, 1, 2][i], izq=480, der=480, tam=33),
  caso('el andamio sobre ladrillos', [
    'Caso de obra: para nivelar un andamio en un piso disparejo, pusieron ladrillos bajo una de las patas.',
    'Con dos personas arriba, un ladrillo se partió. El andamio se ladeó, y se salvaron porque estaban enganchados.',
    'La base va sobre placas y piso firme. Para nivelar, se usan las bases regulables del andamio, nunca ladrillos ni cajas.',
  ], [('🧱', 'Pata sobre <b class="nar">ladrillos</b>'), ('↘️', 'El ladrillo se partió: <b class="nar">se ladeó</b>'), ('✅', 'Bases <b class="nar">regulables</b> y piso firme')]),
  *ejercicio(1,
    'Un andamio tiene una base de <b class="nar">1.20 × 1.80 m</b>.<br>¿Hasta qué altura puede subir sin arriostrarse o amarrarse a la estructura?',
    ['Ahora tú. Un andamio tiene una base de uno veinte por uno ochenta.', '¿Hasta qué altura puede subir sin arriostrarse o amarrarse a la estructura?'],
    'Tres veces el lado <b class="nar">más corto</b>: 3 × 1.20 = <b class="nar">3.60 m</b><br>Más alto que eso: <b class="nar">arriostrado o amarrado</b>',
    ['Tres veces el lado más corto de la base: tres por uno veinte, tres metros sesenta.',
     'Si va más alto, se arriostra o se amarra a la estructura.']),
  *ejercicio(2,
    'Necesitas subir a un techo de <b class="nar">4.80 m</b>. Con la regla 4 a 1<br>y <b class="nar">1 m</b> sobresaliendo arriba, ¿de qué largo es la escalera?',
    ['Segundo ejercicio. Necesitas subir a un techo de cuatro metros ochenta. Con la regla del cuatro a uno, y un metro sobresaliendo arriba, ¿de qué largo es la escalera?'],
    'Base: 4.80 ÷ 4 = <b class="nar">1.20 m</b><br>Hasta el borde: √(4.80² + 1.20²) ≈ <b class="nar">4.95 m</b><br>+ 1 m arriba ≈ <b class="nar">5.95 m</b> → escalera de <b class="nar">6 m</b>',
    ['La base se separa cuatro ochenta entre cuatro: un metro veinte.',
     'Hasta el borde, la escalera mide unos cuatro noventa y cinco. Más el metro que sobresale: casi seis metros. Necesitas una escalera de seis.']),
  faq([
    ('¿Quién revisa el andamio?', 'Una persona competente, cada día.', '¿Quién revisa el andamio? Una persona competente, cada día antes de usarlo, y pone la tarjeta.'),
    ('¿Puedo trabajar horas sobre una escalera?', 'No: es para subir y bajar.', '¿Puedo trabajar horas sobre la escalera? No. La escalera es para subir y bajar. Para trabajar, andamio o plataforma.'),
    ('¿Tablones de cualquier madera?', 'Sanos, sin rajaduras, del espesor indicado.', '¿Cualquier tablón sirve? Sanos, sin rajaduras ni nudos grandes, de unos cinco centímetros de espesor.'),
  ]),
  repaso([
    ('¿Sobre qué va la base del andamio?', 'Sobre piso firme, con sus placas o garruchas frenadas.'),
    ('¿A qué altura va el pasamanos?', 'A un metro cinco.'),
    ('¿Qué significa tarjeta roja?', 'Prohibido subir.'),
    ('¿Cuál es la regla de la escalera?', 'Cuatro a uno.'),
  ]),
]

# ───────────── Clase 8 · Trabajos en caliente e izaje ─────────────
EXT['seg_c8'] = [
  ejemplo('Antes de prender <span class="nar">el arco</span>', [
    'Antes de los errores, la lista de control de un trabajo en caliente, para leerla en voz alta antes de empezar.',
    'Permiso firmado. Lo que arde, retirado o cubierto con mantas ignífugas. Pantallas para proteger a los demás.',
    'Extintor a la mano y vigía de fuego. Cilindros de pie y amarrados. Y al terminar, el vigía se queda revisando.',
  ], ['Antes de soldar', '✓'],
    [['Permiso de trabajo en caliente firmado', '☐'], ['Inflamables retirados o cubiertos', '☐'], ['Pantallas para los demás', '☐'], ['Extintor y vigía de fuego', '☐'], ['Cilindros de pie y amarrados', '☐']],
    lambda i: [1, 1, 1, 2, 2][i], izq=420, der=420, tam=29),
  caso('la mano en la carga', [
    'Caso de obra: al izar un arco, un ayudante lo agarró con la mano para que no girara, en vez de usar la cuerda guía.',
    'El arco giró con el viento y le apretó los dedos contra la columna. Fue un golpe fuerte, pero sin fractura.',
    'La carga se guía con cuerdas, desde lejos. Las manos solo se acercan cuando la carga ya está asentada.',
  ], [('✋', 'Guió el arco <b class="nar">con la mano</b>'), ('💥', 'Dedos apretados contra la <b class="nar">columna</b>'), ('✅', 'Siempre <b class="nar">cuerdas guía</b>, desde lejos')]),
  *ejercicio(1,
    'Terminas de soldar en un techo a las <b class="nar">4:00 p. m.</b>, sobre un depósito con cajas.<br>¿Hasta qué hora se queda el vigía, como mínimo, y qué revisa?',
    ['Ahora tú. Terminas de soldar en un techo a las cuatro de la tarde, sobre un depósito con cajas.', '¿Hasta qué hora se queda el vigía, como mínimo, y qué revisa?'],
    'Hasta las <b class="nar">4:30 p. m.</b> como mínimo (media hora)<br>Revisa <b class="nar">arriba y abajo</b>: rendijas, cajas, humo, olor a quemado<br>Con el <b class="nar">extintor</b> en la mano',
    ['Por lo menos media hora: hasta las cuatro y media.',
     'Revisando arriba y abajo: las rendijas por donde cayeron chispas, las cajas, el olor a quemado. Con el extintor en la mano.']),
  *ejercicio(2,
    'Un arco pesa <b class="nar">650 kg</b>. Se iza con <b class="nar">dos eslingas</b> a <b class="nar">60°</b> de la horizontal.<br>¿Cuánto tira cada eslinga? (sen 60° = 0.87)',
    ['Segundo ejercicio. Un arco pesa seiscientos cincuenta kilos. Se iza con dos eslingas, a sesenta grados de la horizontal.', '¿Cuánto tira cada eslinga? El seno de sesenta grados es cero ochenta y siete.'],
    'Cada eslinga: 650 ÷ (2 × 0.87) ≈ <b class="nar">374 kg</b><br>Usa eslingas con capacidad <b class="nar">bien por encima</b>, por ejemplo de 1 t<br>Mientras más acostadas, <b class="nar">más tiran</b>',
    ['Seiscientos cincuenta, entre dos por cero ochenta y siete: unos trescientos setenta y cuatro kilos por eslinga.',
     'Usa eslingas con capacidad bien por encima, por ejemplo de una tonelada. Y recuerda: mientras más acostadas, más tiran. Lo viste en el curso de Naves.']),
  faq([
    ('¿Puedo soldar con viento?', 'Con pantallas y cuidando las chispas.', '¿Se puede soldar con viento? Con pantallas, y vigilando dónde caen las chispas, que llegan más lejos.'),
    ('¿Quién da las señales a la grúa?', 'Solo el señalero.', '¿Quién da las señales al operador de la grúa? Solo una persona: el señalero.'),
    ('¿Cuándo no se iza?', 'Con viento fuerte o sin saber el peso.', '¿Cuándo no se iza? Con viento fuerte, o si no conoces el peso de la carga.'),
  ]),
  repaso([
    ('¿Qué es un trabajo en caliente?', 'Todo lo que hace chispa o llama.'),
    ('¿Qué hace el vigía de fuego?', 'Mira dónde caen las chispas, con el extintor.'),
    ('¿Cuál es la regla de oro del izaje?', 'Nadie debajo de una carga suspendida.'),
    ('¿Con qué se guía la carga?', 'Con cuerdas, desde lejos.'),
  ]),
]

# ───────────── Clase 9 · Techos y coberturas ─────────────
EXT['seg_c9'] = [
  ejemplo('¿Dónde <span class="nar">se pisa</span>?', [
    'Antes de los errores, dónde se pisa y dónde no sobre un techo metálico.',
    'Sí: sobre las correas y sobre tablas de tránsito apoyadas en dos o más correas.',
    'No: sobre la plancha entre correas, sobre las claraboyas, ni sobre planchas viejas de fibrocemento.',
  ], ['Sí se pisa', 'No se pisa'],
    [['Sobre las correas', 'Plancha entre correas'], ['Tablas de tránsito sobre 2 o más correas', 'Claraboyas'], ['—', 'Fibrocemento viejo']],
    lambda i: i + 1, izq=280, der=280),
  caso('el pie en la claraboya', [
    'Caso de obra: un trabajador retrocedió mirando la plancha que colocaba, y pisó una claraboya sin protección.',
    'El pie la atravesó. No cayó porque estaba enganchado a la línea de vida. Del susto, no pudo seguir trabajando ese día.',
    'Las claraboyas se protegen con malla desde el primer día, hasta el final. Y nadie camina hacia atrás en un techo.',
  ], [('🔙', 'Caminó <b class="nar">hacia atrás</b>'), ('🕳️', 'El pie <b class="nar">atravesó</b> la claraboya'), ('✅', 'Claraboyas con <b class="nar">malla</b> hasta el final')]),
  *ejercicio(1,
    'Las correas van cada <b class="nar">1.20 m</b>. ¿De qué largo mínimo es la tabla de tránsito<br>para que se apoye en <b class="nar">tres correas</b>, con 15 cm de vuelo en cada punta?',
    ['Ahora tú. Las correas van cada uno veinte. ¿De qué largo mínimo es la tabla de tránsito, para que se apoye en tres correas, con quince centímetros de vuelo en cada punta?'],
    'Entre la 1.ª y la 3.ª correa: 2 × 1.20 = <b class="nar">2.40 m</b><br>+ 0.15 + 0.15 = <b class="nar">2.70 m</b><br>Bien sujeta, para que <b class="nar">no se deslice</b>',
    ['Entre la primera y la tercera correa hay dos tramos: dos metros cuarenta.',
     'Más quince centímetros en cada punta: dos metros setenta. Y bien sujeta, para que no se deslice.']),
  *ejercicio(2,
    'Vas a cubrir un techo en <b class="nar">verano</b>. El pronóstico dice <b class="nar">viento fuerte desde las 2 p. m.</b><br>¿Cómo organizas el día?',
    ['Segundo ejercicio. Vas a cubrir un techo en verano. El pronóstico dice viento fuerte desde las dos de la tarde.', '¿Cómo organizas el día?'],
    'Planchas <b class="nar">temprano</b>, cada una fijada apenas se coloca<br>Desde la 1 p. m.: <b class="nar">nada de planchas sueltas</b> arriba<br>Tarde: trabajos <b class="nar">sin planchas</b> o en el piso · agua y sombra todo el día',
    ['Las planchas, temprano, y cada una fijada apenas se coloca.',
     'Antes de que suba el viento, ninguna plancha suelta arriba. En la tarde, trabajos en el piso o sin planchas. Y agua y sombra todo el día.']),
  faq([
    ('¿Puedo caminar sobre el aluzinc nuevo?', 'Sobre las correas; entre correas se abolla.', '¿Puedo caminar sobre el aluzinc nuevo? Solo sobre las correas. Entre correas se abolla y puede ceder.'),
    ('¿Dónde va la línea de vida?', 'A lo largo de la cumbrera o cerca del trabajo.', '¿Dónde va la línea de vida en un techo? Normalmente a lo largo de la cumbrera, o donde se esté trabajando.'),
    ('¿Y el fibrocemento viejo?', 'Nunca pisarlo; tablas y arnés.', '¿Y si el techo es de fibrocemento viejo? Nunca se pisa directo. Tablas de tránsito y arnés siempre.'),
  ]),
  repaso([
    ('¿Por dónde se camina en un techo?', 'Sobre la estructura, no sobre las planchas.'),
    ('¿Qué se hace con las claraboyas?', 'Protegerlas con malla o baranda.'),
    ('¿Qué pasa con el viento fuerte?', 'Se suspende la colocación de planchas.'),
    ('¿Cómo se suben las planchas?', 'Con soga o grúa, nunca por la escalera.'),
  ]),
]

# ───────────── Clase 10 · Herramientas y electricidad ─────────────
EXT['seg_c10'] = [
  ejemplo('¿Este disco <span class="nar">sirve</span>?', [
    'Antes de los errores, cómo comprobar si un disco sirve para tu amoladora.',
    'Tu amoladora gira a once mil revoluciones por minuto. Un disco que dice ocho mil quinientas como máximo: no sirve, puede reventar.',
    'Uno que dice trece mil trescientas: sí sirve. Y además, el diámetro correcto, y de corte para cortar o de desbaste para desbastar.',
  ], ['Amoladora', 'Disco (máximo)', '¿Sirve?'],
    [['11 000 rpm', '8 500 rpm', 'No: puede reventar'], ['11 000 rpm', '13 300 rpm', 'Sí'], ['11 000 rpm', '11 000 rpm', 'Sí (igual o mayor)']],
    lambda i: [1, 2, 2][i], izq=300, der=300),
  caso('sin guarda', [
    'Caso de taller: un maestro le quitó la guarda a la amoladora "para que entre en las esquinas".',
    'El disco se trabó en el corte y se partió. Un pedazo le cortó el antebrazo. Puntos, y dos semanas sin trabajar.',
    'La guarda va siempre puesta. Para las esquinas, hay discos más chicos o una herramienta adecuada.',
  ], [('🪚', 'Amoladora <b class="nar">sin guarda</b>'), ('💥', 'El disco se partió: <b class="nar">corte en el brazo</b>'), ('✅', 'Guarda <b class="nar">siempre</b>; herramienta adecuada')]),
  *ejercicio(1,
    'Tu amoladora de <b class="nar">4½"</b> gira a <b class="nar">11 000 rpm</b>. Tienes tres discos:<br>a) 4½", máx. <b class="nar">13 300 rpm</b>, de corte · b) 7", máx. <b class="nar">8 500 rpm</b><br>c) 4½", máx. 13 300 rpm, <b class="nar">de desbaste</b>. ¿Cuál usas para cortar un tubo?',
    ['Ahora tú. Tu amoladora de cuatro y media pulgadas gira a once mil revoluciones. Tienes tres discos. a: de cuatro y media, máximo trece mil trescientas, de corte. b: de siete pulgadas, máximo ocho mil quinientas. c: de cuatro y media, máximo trece mil trescientas, de desbaste.', '¿Cuál usas para cortar un tubo?'],
    'El <b class="nar">a</b>: diámetro correcto, velocidad mayor y <b class="nar">de corte</b><br>b) Diámetro y velocidad equivocados: <b class="nar">nunca</b><br>c) Es de <b class="nar">desbaste</b>: no se usa para cortar',
    ['El disco a: el diámetro correcto, una velocidad máxima mayor que la de la máquina, y es de corte.',
     'El b es de otro diámetro y de menor velocidad: nunca. Y el c es de desbaste: no se usa para cortar.']),
  *ejercicio(2,
    'En la obra ves: una extensión <b class="nar">con cinta</b> pasando por un <b class="nar">charco</b>,<br>un tablero <b class="nar">sin diferencial</b> y una amoladora que <b class="nar">da corriente</b>.<br>¿Qué haces?',
    ['Segundo ejercicio. En la obra ves una extensión con cinta pasando por un charco, un tablero sin diferencial, y una amoladora que da corriente.', '¿Qué haces?'],
    '<b class="nar">Paras</b> esos trabajos y cortas la energía<br>Extensión: se cambia por una <b class="nar">sin empalmes</b> y fuera del agua<br>Tablero: un electricista instala el <b class="nar">diferencial</b> · Amoladora: <b class="nar">fuera de la obra</b> hasta repararla',
    ['Paras esos trabajos y cortas la energía.',
     'La extensión se cambia por una sin empalmes y fuera del agua. El tablero: que un electricista le instale el diferencial. Y la amoladora sale de la obra hasta que la reparen.']),
  faq([
    ('¿Por qué desenchufar y no solo apagar?', 'Un golpe al interruptor la prende.', '¿Por qué desenchufar y no solo apagar? Porque un golpe al interruptor la puede prender con tu mano en el disco.'),
    ('¿Qué distancia de los cables aéreos?', 'Buena distancia y coordinar con la empresa eléctrica.', '¿Qué distancia dejo con los cables aéreos? Una buena distancia, y coordinas con la empresa eléctrica. La electricidad puede saltar.'),
    ('¿Diferencial o termomagnético?', 'Los dos: uno protege personas, el otro el circuito.', '¿Diferencial o termomagnético? Los dos. El diferencial protege a las personas; el termomagnético, el circuito.'),
  ]),
  repaso([
    ('¿Qué herramienta causa más lesiones en el taller?', 'La amoladora.'),
    ('¿Qué velocidad debe tener el disco?', 'Igual o mayor que la de la máquina.'),
    ('¿Qué te salva de una descarga?', 'El interruptor diferencial.'),
    ('¿Qué miras antes de izar?', 'Hacia arriba, por los cables.'),
  ]),
]

# ───────────── Clase 11 · Emergencias y primeros auxilios ─────────────
EXT['seg_c11'] = [
  ejemplo('Al llamar, <span class="nar">di esto</span>', [
    'Antes de los errores, qué decir cuando llamas a emergencias. Tienes que ser claro y rápido.',
    'Dónde estás, exacto: dirección y una referencia. Qué pasó: por ejemplo, una caída de cuatro metros.',
    'Cuántas personas y cómo están: si responden, si respiran. Y un número para que te devuelvan la llamada. No cuelgues hasta que te lo digan.',
  ], ['Di', 'Ejemplo'],
    [['Dónde estás', 'Av. Los Pinos 450, frente al colegio'], ['Qué pasó', 'Caída de 4 m desde un techo'], ['Cuántos y cómo están', 'Uno, consciente, no mueve la pierna'], ['Tu número', 'Para que te devuelvan la llamada']],
    lambda i: [1, 1, 2, 3][i], izq=280, der=280),
  caso('la esquirla que frotó', [
    'Caso de taller: a un soldador le entró una esquirla en el ojo. Se frotó fuerte para sacársela.',
    'La esquirla rayó el ojo. Lo que pudo ser una molestia de un día terminó en tratamiento y varios días sin trabajar.',
    'Ante algo en el ojo: no frotar. Lavar con abundante agua limpia, y al médico.',
  ], [('👁️', 'Esquirla en el ojo: <b class="nar">se frotó</b>'), ('🩺', 'Terminó en <b class="nar">tratamiento</b>'), ('✅', 'No frotar: <b class="nar">agua limpia y al médico</b>')]),
  *ejercicio(1,
    'Un compañero cayó del andamio, está en el piso, consciente,<br>y la amoladora sigue <b class="nar">encendida</b> a su lado.<br>Ordena: <b class="nar">proteger, avisar, socorrer</b>.',
    ['Ahora tú. Un compañero cayó del andamio. Está en el piso, consciente, y la amoladora sigue encendida a su lado.', 'Ordena los pasos: proteger, avisar y socorrer.'],
    '1. <b class="nar">Proteger</b>: apaga y desenchufa la amoladora, aleja a los demás<br>2. <b class="nar">Avisar</b>: 106 (SAMU) o 116 (Bomberos), con dirección exacta<br>3. <b class="nar">Socorrer</b>: no lo muevas, abrígalo y háblale hasta que llegue la ayuda',
    ['Primero proteger: apagas y desenchufas la amoladora, y alejas a los demás.',
     'Después avisar: ciento seis o ciento dieciséis, con la dirección exacta. Y socorrer: no lo muevas, abrígalo y háblale hasta que llegue la ayuda.']),
  *ejercicio(2,
    'Arma el <b class="nar">botiquín básico</b> de tu obra.<br>¿Qué seis cosas no pueden faltar?',
    ['Segundo ejercicio. Arma el botiquín básico de tu obra. ¿Qué seis cosas no pueden faltar?'],
    'Por ejemplo: <b class="nar">gasas</b> y <b class="nar">vendas</b>, <b class="nar">esparadrapo</b>,<br><b class="nar">guantes</b> descartables, <b class="nar">suero fisiológico</b> para lavar ojos y heridas,<br>y una <b class="nar">tijera</b>. Revísalo cada mes',
    ['Por ejemplo: gasas, vendas, esparadrapo, guantes descartables, suero fisiológico para lavar ojos y heridas, y una tijera.',
     'Y revísalo cada mes, reponiendo lo que se usó o venció. Para lo demás, sigue lo que te enseñen en un curso de primeros auxilios.']),
  faq([
    ('¿Muevo a alguien que cayó?', 'No, salvo peligro inmediato.', '¿Muevo a alguien que cayó? No, salvo que esté en peligro inmediato. Puede tener una lesión de columna.'),
    ('¿Hielo en una quemadura?', 'No: agua corriente fresca.', '¿Pongo hielo en una quemadura? No. Agua corriente fresca por varios minutos, y cubrir con gasa limpia.'),
    ('¿Dónde aprendo primeros auxilios?', 'Cruz Roja, Bomberos u otras instituciones.', '¿Dónde aprendo primeros auxilios? En cursos de la Cruz Roja, de los Bomberos u otras instituciones.'),
  ]),
  repaso([
    ('¿Qué número es el SAMU?', 'Ciento seis.'),
    ('¿Y los Bomberos?', 'Ciento dieciséis.'),
    ('¿Cuáles son los tres pasos?', 'Proteger, avisar y socorrer.'),
    ('¿Qué se hace con un casi accidente?', 'Se anota.'),
  ]),
]

# ───────────── Clase 12 · Seguridad que vende ─────────────
EXT['seg_c12'] = [
  ejemplo('La partida <span class="nar">de la nave</span>', [
    'Antes de los errores, la partida de seguridad de la nave en una tabla, con precios de referencia.',
    'EPP de reposición, ochocientos. Línea de vida y anclajes, mil doscientos. Andamios, seiscientos.',
    'SCTR, novecientos. Charlas y permisos, quinientos. Total: cuatro mil soles, como partida aparte.',
  ], ['Concepto', 'Monto'],
    [['EPP de reposición', 'S/ 800'], ['Línea de vida y anclajes', 'S/ 1 200'], ['Andamios', 'S/ 600'], ['SCTR', 'S/ 900'], ['Charlas y permisos', 'S/ 500'], ['Total', 'S/ 4 000']],
    lambda i: [1, 1, 1, 2, 2, 2][i], izq=460, der=460, tam=29),
  caso('la carpeta que no estaba', [
    'Caso real de taller: una empresa invitó a cotizar a tres talleres, y pidió la carpeta de seguridad en dos días.',
    'Un taller tenía buen precio, pero no tenía nada armado. Cuando la tuvo, la obra ya estaba asignada a otro.',
    'La carpeta se arma una vez, se actualiza, y se envía el mismo día que la piden.',
  ], [('📂', 'Pidieron la <b class="nar">carpeta de seguridad</b>'), ('⌛', 'No estaba lista: <b class="nar">perdió la obra</b>'), ('✅', 'Carpeta <b class="nar">lista y actualizada</b>')]),
  *ejercicio(1,
    'Cotiza la partida de seguridad: <b class="nar">4 personas, 10 días</b>.<br>EPP S/ 400 · línea de vida S/ 800 · andamio S/ 300 · SCTR S/ 300 · charlas S/ 200.<br>¿Cuánto es y cómo la presentas?',
    ['Ahora tú. Cotiza la partida de seguridad para cuatro personas, durante diez días. EPP, cuatrocientos. Línea de vida, ochocientos. Andamio, trescientos. SCTR, trescientos. Y charlas, doscientos.', '¿Cuánto es, y cómo la presentas?'],
    'Total: 400 + 800 + 300 + 300 + 200 = <b class="nar">S/ 2 000</b><br>Como partida aparte: <b class="nar">"Seguridad y salud en el trabajo"</b>,<br>con su detalle, no escondida en otra',
    ['El total: dos mil soles.',
     'Y la presentas como una partida aparte, con su nombre: Seguridad y salud en el trabajo, con su detalle. Así el cliente entiende por qué cuestas lo que cuestas.']),
  *ejercicio(2,
    'Tu presupuesto total es de <b class="nar">S/ 120 000</b> y la seguridad, <b class="nar">S/ 4 000</b>.<br>¿Qué porcentaje es? ¿Qué le dices al cliente que la quiere quitar?',
    ['Segundo ejercicio. Tu presupuesto total es de ciento veinte mil soles, y la seguridad, cuatro mil.', '¿Qué porcentaje es? ¿Y qué le dices al cliente que la quiere quitar?'],
    '4 000 ÷ 120 000 ≈ <b class="nar">3.3 %</b><br>"Es lo que permite que <b class="nar">nadie se lastime</b> y que la obra <b class="nar">no se pare</b>.<br>Sin ella, <b class="nar">no podemos trabajar</b>."',
    ['Cuatro mil entre ciento veinte mil: un tres por ciento, más o menos.',
     'Y al cliente le dices, con calma: es lo que permite que nadie se lastime y que la obra no se pare. Sin ella, no podemos trabajar. La seguridad no se quita.']),
  faq([
    ('¿Y si otro cotiza sin seguridad?', 'Muéstralo: el cliente entiende la diferencia.', '¿Y si otro cotiza sin seguridad? Muestra tu partida y tu carpeta. Los buenos clientes entienden la diferencia.'),
    ('¿Qué fotos publico?', 'Con tu gente usando su EPP.', '¿Qué fotos publico? Con tu gente usando casco, arnés y línea de vida. Eso vende.'),
    ('¿Cada cuánto actualizo la carpeta?', 'Cuando cambie el SCTR, el equipo o la gente.', '¿Cada cuánto actualizo la carpeta? Cada vez que cambie el SCTR, el equipo o tu personal.'),
  ]),
  repaso([
    ('¿Dónde va el costo de la seguridad?', 'En la cotización, como partida aparte.'),
    ('¿Qué lleva la carpeta de seguridad?', 'SCTR, certificados, modelos de IPERC, ATS y PETAR, y constancias.'),
    ('¿Cuándo se envía?', 'El mismo día que la piden.'),
    ('¿Qué fotos alejan a los buenos clientes?', 'Las de gente trabajando sin EPP.'),
  ]),
]
