"""Ampliación de «El Negocio del Metalero» (≈7 min por clase). Misma receta que los demás cursos.
Temas de impuestos, contratos y trabajo: orientación general, siempre con la recomendación de consultar."""
from naves_ext import insertar, caja, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · De maestro a empresario ─────────────
EXT['neg_c1'] = [
  ejemplo('Las horas <span class="nar">que no cobras</span>', [
    'Antes de los errores, mira cuánto valen las horas que nadie te paga en una sola obra como la cochera.',
    'La visita: tres horas. Ir a comprar el material: cuatro. Traslados: cinco. Y armar la cotización: dos.',
    'Catorce horas. A treinta y cuatro soles la hora, que calculamos en la próxima clase, son cuatrocientos setenta y seis soles. Si no están en tu precio, los regalas.',
  ], ['Tarea', 'Horas', 'A S/ 34 la hora'],
    [['Visita técnica', '3', 'S/ 102'], ['Compras', '4', 'S/ 136'], ['Traslados', '5', 'S/ 170'], ['Cotización', '2', 'S/ 68'], ['Total', '14 h', 'S/ 476']],
    lambda i: [1, 1, 1, 1, 2][i], izq=360, der=360, tam=30),
  caso('mucho trabajo, nada de plata', [
    'Caso de taller: un maestro tenía tres obras a la vez. Todos le decían que le iba muy bien.',
    'Pero compraba todo el material con su plata y cobraba al final. A mitad de mes no tenía para pagarle al ayudante, y tuvo que prestarse.',
    'Tener trabajo no es lo mismo que tener plata. Con adelantos y una caja separada, esas mismas tres obras le habrían dejado tranquilo.',
  ], [('🔨', '<b class="nar">Tres obras</b> a la vez'), ('💸', 'Pagaba todo y <b class="nar">cobraba al final</b>'), ('✅', 'Adelantos y <b class="nar">caja separada</b>')]),
  *ejercicio(1,
    'Cobraste una reja en <b class="nar">S/ 2 800</b>. Materiales <b class="nar">S/ 1 300</b>, ayudante <b class="nar">S/ 400</b>,<br>transporte <b class="nar">S/ 150</b>, discos y pintura <b class="nar">S/ 180</b>. Trabajaste <b class="nar">4 días</b>.<br>¿Cuánto te quedó y cuánto ganaste por día?',
    ['Ahora tú. Cobraste una reja en dos mil ochocientos soles. Materiales, mil trescientos. Ayudante, cuatrocientos. Transporte, ciento cincuenta. Discos y pintura, ciento ochenta. Trabajaste cuatro días.', '¿Cuánto te quedó, y cuánto ganaste por día?'],
    'Gastos: 1 300 + 400 + 150 + 180 = <b class="nar">S/ 2 030</b><br>Te quedó: 2 800 − 2 030 = <b class="nar">S/ 770</b><br>Por día: 770 ÷ 4 ≈ <b class="nar">S/ 192</b> · y aún falta el alquiler y la luz del taller',
    ['Los gastos suman dos mil treinta. Te quedaron setecientos setenta.',
     'Entre cuatro días: unos ciento noventa y dos soles por día. Y todavía no restaste el alquiler, la luz ni el desgaste de las máquinas. Por eso la próxima clase es tan importante.']),
  *ejercicio(2,
    'Este mes entraron <b class="nar">S/ 10 000</b> de obras. Salieron <b class="nar">S/ 4 800</b> en materiales y ayudantes,<br>y <b class="nar">S/ 1 900</b> de gastos fijos. Tu sueldo es <b class="nar">S/ 3 000</b>.<br>¿Cuánto queda para la reserva del taller?',
    ['Segundo ejercicio. Este mes entraron diez mil soles de obras. Salieron cuatro mil ochocientos en materiales y ayudantes, y mil novecientos de gastos fijos. Tu sueldo es de tres mil.', '¿Cuánto queda para la reserva del taller?'],
    '10 000 − 4 800 − 1 900 − 3 000 = <b class="nar">S/ 300</b><br>Poco: un mes flojo y no alcanza → revisa <b class="nar">precios y margen</b>',
    ['Diez mil, menos cuatro mil ochocientos, menos mil novecientos, menos tus tres mil: trescientos soles.',
     'Es poco. Con un mes flojo, no alcanza. Esa es la señal de que tu precio o tu margen necesitan ajuste. Lo vemos en la clase cinco.']),
  faq([
    ('¿Necesito ser empresa para pensar como empresa?', 'No: empieza por medir y anotar.', '¿Tengo que tener una empresa para pensar como empresario? No. Empieza por medir y anotar. La formalización la vemos en la clase diez.'),
    ('¿Dónde anoto los gastos?', 'En un cuaderno, una hoja de cálculo o InnovApp.', '¿Dónde anoto los gastos? En un cuaderno, una hoja de cálculo, o en InnovApp, en los gastos de cada proyecto.'),
    ('¿Y si no tengo tiempo?', 'Cinco minutos al día, al cerrar el taller.', '¿Y si no tengo tiempo? Son cinco minutos al día, al cerrar el taller. Es el tiempo mejor pagado de tu semana.'),
  ]),
  repaso([
    ('¿Cuáles son los tres números del taller?', 'Costo de tu hora, margen real y flujo de caja.'),
    ('¿Qué horas casi nadie cobra?', 'Visitas, compras, traslados y cotizaciones.'),
    ('¿Qué se separa desde hoy?', 'La plata del taller y la de la casa.'),
    ('¿Qué pides al terminar una obra?', 'Una recomendación.'),
  ]),
]

# ───────────── Clase 2 · El costo de tu hora ─────────────
EXT['neg_c2'] = [
  ejemplo('Cómo cambia <span class="nar">tu hora</span>', [
    'Antes de los errores, cómo cambia el costo de tu hora cuando cambian tus horas productivas. Con cuatro mil novecientos al mes.',
    'Con sesenta por ciento de horas productivas: ciento veinticinco horas, treinta y nueve soles la hora.',
    'Con setenta: ciento cuarenta y seis horas, treinta y cuatro soles. Con ochenta: ciento sesenta y seis horas, unos treinta.',
    'Mientras menos horas se pierdan en vueltas y esperas, más barata te sale la hora, y más competitivo eres sin bajar tu ganancia.',
  ], ['Horas productivas', 'Horas al mes', 'Costo de tu hora'],
    [['60 %', '≈ 125 h', '≈ S/ 39'], ['70 %', '≈ 146 h', '≈ S/ 34'], ['80 %', '≈ 166 h', '≈ S/ 30']],
    lambda i: [1, 2, 2][i], izq=340, der=340, tam=32),
  caso('la máquina que nadie ahorró', [
    'Caso de taller: un maestro cobraba veinticinco soles la hora, "porque así cobran todos". Nunca separó plata para sus equipos.',
    'A los tres años se le quemó la soldadora en plena obra. Tuvo que comprar otra con un préstamo, y alquilar una mientras llegaba.',
    'El desgaste de las máquinas es un gasto real, aunque no lo pagues cada mes. Si está en tu hora, el día que se malogra, la plata ya está.',
  ], [('💰', 'Cobraba <b class="nar">S/ 25</b> "como todos"'), ('🔥', 'Se quemó la soldadora: <b class="nar">préstamo</b>'), ('✅', 'El desgaste va <b class="nar">dentro de tu hora</b>')]),
  *ejercicio(1,
    'Alquiler <b class="nar">600</b> · luz <b class="nar">180</b> · internet y celular <b class="nar">100</b> · transporte <b class="nar">250</b><br>Equipos: <b class="nar">S/ 8 000</b> que duran 4 años · Tu sueldo: <b class="nar">S/ 2 800</b><br>24 días de 8 h, con 70 % productivo. ¿Cuánto cuesta tu hora?',
    ['Ahora tú. Alquiler, seiscientos. Luz, ciento ochenta. Internet y celular, cien. Transporte, doscientos cincuenta. Equipos por ocho mil soles que duran cuatro años. Tu sueldo, dos mil ochocientos.', 'Trabajas veinticuatro días de ocho horas, con setenta por ciento productivo. ¿Cuánto cuesta tu hora?'],
    'Desgaste: 8 000 ÷ 48 meses ≈ <b class="nar">167</b> · Fijos: 600 + 180 + 100 + 250 + 167 = <b class="nar">1 297</b><br>Con tu sueldo: <b class="nar">4 097</b> al mes<br>Horas: 24 × 8 × 0.70 ≈ <b class="nar">134</b> → hora ≈ <b class="nar">S/ 30.5</b>',
    ['El desgaste: ocho mil entre cuarenta y ocho meses, unos ciento sesenta y siete. Los fijos suman mil doscientos noventa y siete. Con tu sueldo: cuatro mil noventa y siete al mes.',
     'Horas productivas: veinticuatro por ocho por cero setenta, unas ciento treinta y cuatro. Tu hora cuesta unos treinta soles y medio.']),
  *ejercicio(2,
    'Con esa hora (S/ 30.5), una reja te toma <b class="nar">12 h</b> y al ayudante <b class="nar">6 h</b> a S/ 15.<br>Materiales <b class="nar">S/ 420</b> y consumibles <b class="nar">S/ 40</b>.<br>¿Cuál es el costo total de la reja?',
    ['Segundo ejercicio. Con esa hora, de treinta soles y medio, una reja te toma doce horas, y al ayudante seis horas, a quince soles.', 'Materiales, cuatrocientos veinte, y consumibles, cuarenta. ¿Cuál es el costo total de la reja?'],
    'Tus horas: 12 × 30.5 = <b class="nar">366</b> · Ayudante: 6 × 15 = <b class="nar">90</b><br>+ materiales 420 + consumibles 40<br>Costo total: <b class="nar">S/ 916</b> (todavía sin utilidad)',
    ['Tus horas: doce por treinta y medio, trescientos sesenta y seis. El ayudante: noventa.',
     'Más materiales y consumibles: novecientos dieciséis soles. Ese es el costo. La utilidad se suma después, como veremos en la clase cinco.']),
  faq([
    ('¿Mi sueldo va en el costo?', 'Sí: eres un trabajador del taller.', '¿Mi sueldo va dentro del costo? Sí. Eres un trabajador del taller, y tu trabajo se paga. La utilidad es otra cosa.'),
    ('¿Y si mi hora sale más cara que la competencia?', 'Revisa horas perdidas; no regales trabajo.', '¿Y si mi hora sale más cara que la de otros? Revisa tus horas perdidas y tus gastos. Pero no trabajes por debajo de tu costo.'),
    ('¿InnovApp calcula esto?', 'Registra gastos y personal por proyecto.', '¿InnovApp me ayuda con esto? Puedes registrar gastos y personal por proyecto, y ver cuánto te queda en cada obra.'),
  ]),
  repaso([
    ('¿Qué son los costos fijos?', 'Los que pagas al mes aunque no tengas obra.'),
    ('¿Cuántas horas son productivas?', 'Una parte: por ejemplo, el setenta por ciento.'),
    ('¿Cómo se calcula tu hora?', 'Fijos más tu sueldo, entre las horas productivas.'),
    ('¿Cada cuánto lo revisas?', 'Cada seis meses, o cuando cambie algo grande.'),
  ]),
]

# ───────────── Clase 3 · La visita técnica ─────────────
EXT['neg_c3'] = [
  ejemplo('La ficha de visita, <span class="nar">llena</span>', [
    'Antes de los errores, las seis preguntas con las respuestas que dio el cliente de la cochera.',
    '¿Para qué? Para un auto. ¿Ideas? Mandó fotos de portones de su barrio. ¿Para cuándo? Fin de mes.',
    '¿Quién decide? Él y su esposa: ella estuvo en la visita. ¿Monto? Tenía un rango pensado. ¿Luz y acceso? Sí, con buen acceso para el camión.',
  ], ['Pregunta', 'Respuesta del cliente'],
    [['¿Para qué lo usará?', 'Para un auto'], ['¿Fotos o ideas?', 'Portones de su barrio'], ['¿Para cuándo?', 'Fin de mes'], ['¿Quién decide?', 'Él y su esposa'], ['¿Monto pensado?', 'Un rango'], ['¿Luz y acceso?', 'Sí, buen acceso']],
    lambda i: [1, 1, 1, 2, 2, 2][i], izq=400, der=400, tam=29),
  caso('el precio por WhatsApp', [
    'Caso de taller: un cliente mandó una foto de su vano y pidió precio. El maestro respondió con un número, sin ir.',
    'Cuando llegó a medir, había una columna de concreto y un desnivel de diez centímetros. El trabajo costaba bastante más, y el cliente se molestó por el cambio.',
    'Sin ver la obra, solo se da un rango amplio, y se explica que el precio final va en la cotización.',
  ], [('📱', 'Precio por WhatsApp <b class="nar">sin ver la obra</b>'), ('🧱', 'Había <b class="nar">columna y desnivel</b>'), ('✅', 'Sin visita: solo <b class="nar">un rango</b>')]),
  *ejercicio(1,
    'Una visita lejana te toma <b class="nar">2 h</b> en la obra y <b class="nar">1.5 h</b> de ida y vuelta,<br>más <b class="nar">S/ 20</b> de pasajes. Tu hora cuesta <b class="nar">S/ 34</b>.<br>¿Cuánto te cuesta esa visita?',
    ['Ahora tú. Una visita lejana te toma dos horas en la obra y una hora y media de ida y vuelta, más veinte soles de pasajes. Tu hora cuesta treinta y cuatro.', '¿Cuánto te cuesta esa visita?'],
    'Horas: 3.5 × 34 = <b class="nar">S/ 119</b> + pasajes 20 = <b class="nar">S/ 139</b><br>Por eso las visitas lejanas <b class="nar">se cobran</b>, y se descuentan si contrata',
    ['Tres horas y media por treinta y cuatro: ciento diecinueve. Más veinte de pasajes: ciento treinta y nueve soles.',
     'Por eso una visita lejana se puede cobrar, avisando antes, y se descuenta si el cliente contrata.']),
  *ejercicio(2,
    'En la visita, el cliente dice: <b class="nar">"Lo decido con mi hermano, que hoy no vino"</b>.<br>¿Qué haces para no perder la venta?',
    ['Segundo ejercicio. En la visita, el cliente te dice: lo decido con mi hermano, que hoy no vino.', '¿Qué haces para no perder la venta?'],
    'Mide y registra igual, con fotos<br>Ofrece una <b class="nar">llamada o videollamada</b> con los dos al enviar la cotización<br>Y manda las <b class="nar">tres opciones</b> por escrito, para que comparen juntos',
    ['Mide y registra todo igual, con fotos.',
     'Y cuando envíes la cotización, ofrece una llamada o videollamada con los dos, para explicar las opciones. Así no dependes de que el cliente lo explique bien.']),
  faq([
    ('¿Cuánto cobro por la visita?', 'Lo que cuesta tu tiempo; se descuenta si contrata.', '¿Cuánto cobro por una visita? Más o menos lo que te cuesta en horas y pasajes. Y se descuenta si el cliente contrata.'),
    ('¿Llevo catálogo?', 'Sí: fotos de tus trabajos en el celular.', '¿Llevo un catálogo? Sí: fotos de tus trabajos, ordenadas en el celular o en tu WhatsApp Business.'),
    ('¿Puedo medir con láser?', 'Sí, y anota en la ficha.', '¿Puedo usar medidor láser? Claro. Lo importante es anotar todo en la ficha, con fotos.'),
  ]),
  repaso([
    ('¿Qué haces antes de la visita?', 'Pedir fotos y ubicación, y agendar una hora exacta.'),
    ('¿Qué haces primero en la visita?', 'Escuchar.'),
    ('¿Cuántas veces mides?', 'Dos veces, y el vano en tres alturas.'),
    ('¿Das precio en la visita?', 'No: envías la cotización a la hora prometida.'),
  ]),
]

# ───────────── Clase 4 · La cotización profesional ─────────────
EXT['neg_c4'] = [
  ejemplo('Alcance: <span class="nar">vago o claro</span>', [
    'Antes de los errores, tres trabajos con su alcance vago y su alcance claro.',
    'Vago: "reja de ventana". Claro: reja de uno veinte por uno veinte, marco de una pulgada, ocho barrotes de media, empotrada, negro mate.',
    'Vago: "escalera". Claro: escalera recta de dieciséis contrapasos, zancas de tubo, peldaños de plancha estriada, con baranda.',
    'Vago: "techo". Claro: techo de tres veinte por seis, estructura de tubo, plancha TR4, con canaleta y bajada.',
  ], ['Vago', 'Claro'],
    [['"Reja de ventana"', '1.20 × 1.20 m · marco 1" · 8 barrotes ½" · empotrada · negro mate'],
     ['"Escalera"', 'Recta, 16 contrapasos · zancas de tubo · peldaños estriados · con baranda'],
     ['"Techo"', '3.20 × 6.00 m · tubo · plancha TR4 · canaleta y bajada']],
    lambda i: i + 1, izq=180, der=180, tam=27),
  caso('"yo pensé que incluía"', [
    'Caso de obra: un portón entregado a tiempo. Al final, el cliente esperaba que también le resanaras y pintaras la pared alrededor.',
    'La cotización no decía nada de eso. Para no pelear, el maestro lo hizo gratis: un día de trabajo y materiales.',
    'Escribe siempre lo que no incluye. Es una línea en la cotización, y te ahorra un día de trabajo regalado.',
  ], [('🧱', 'Esperaba <b class="nar">resane y pintura</b> de la pared'), ('🎁', 'Se hizo gratis: <b class="nar">un día regalado</b>'), ('✍️', 'Escribe <b class="nar">lo que no incluye</b>')]),
  *ejercicio(1,
    'Vas a cotizar una <b class="nar">reja de ventana con instalación</b>.<br>Escribe cuatro cosas que <b class="nar">no incluye</b>.',
    ['Ahora tú. Vas a cotizar una reja de ventana, con instalación.', 'Escribe cuatro cosas que no incluye.'],
    'No incluye, por ejemplo:<br>• <b class="nar">Resane y pintura</b> de la pared alrededor<br>• <b class="nar">Cambio o arreglo</b> de la ventana existente<br>• <b class="nar">Permisos</b> de condominio o municipalidad · • Retiro de <b class="nar">rejas antiguas</b>',
    ['Por ejemplo: el resane y la pintura de la pared, el arreglo de la ventana existente, los permisos de condominio, y el retiro de rejas antiguas.',
     'Si el cliente quiere alguno, se cotiza aparte. Así nadie se siente engañado.']),
  *ejercicio(2,
    'Cotizaste materiales por <b class="nar">S/ 3 000</b>. El acero sube <b class="nar">8 %</b> en un mes.<br>Si el cliente acepta a los 40 días y tu validez era de 15,<br>¿cuánto perderías si respetas el precio?',
    ['Segundo ejercicio. Cotizaste materiales por tres mil soles. El acero sube ocho por ciento en un mes.', 'Si el cliente acepta a los cuarenta días, y tu validez era de quince, ¿cuánto perderías si respetas el precio?'],
    '8 % de 3 000 = <b class="nar">S/ 240</b> menos de ganancia<br>Por eso la <b class="nar">validez</b>: pasados 15 días, <b class="nar">se actualiza</b> la cotización',
    ['Ocho por ciento de tres mil: doscientos cuarenta soles que salen de tu ganancia.',
     'Para eso está la validez. Pasados los quince días, actualizas la cotización con los precios de hoy, con amabilidad y explicando por qué.']),
  faq([
    ('¿Dónde hago la cotización?', 'En la plantilla del curso o en InnovApp, en PDF.', '¿Dónde armo la cotización? En la plantilla del curso, o en los módulos de InnovApp, y la envías en PDF.'),
    ('¿Pongo el precio por partida?', 'Sí: el cliente entiende qué paga.', '¿Separo el precio por partidas? Sí. El cliente entiende qué paga, y es más fácil negociar el alcance.'),
    ('¿Y si me piden rebaja antes de ver?', 'Primero que lea las tres opciones.', '¿Y si piden rebaja sin leerla? Pide que primero revise las tres opciones. Muchas veces la básica resuelve el problema.'),
  ]),
  repaso([
    ('¿Cuál es la parte más importante?', 'El alcance.'),
    ('¿Desde cuándo se cuenta el plazo?', 'Desde el pago del adelanto.'),
    ('¿Por qué la cotización tiene validez?', 'Porque el precio del acero cambia.'),
    ('¿Cuántas opciones conviene dar?', 'Tres.'),
  ]),
]

# ───────────── Clase 5 · Precio y negociación ─────────────
EXT['neg_c5'] = [
  ejemplo('Sumar % <span class="nar">no es ganar %</span>', [
    'Antes de los errores, la tabla de la trampa más común. Lo que sumas al costo, y lo que de verdad ganas sobre el precio.',
    'Sumas quince por ciento: ganas trece. Sumas veinte: ganas dieciséis coma siete. Sumas veinticinco: ganas veinte.',
    'La fórmula para no equivocarte: precio igual al costo dividido entre uno menos el margen que quieres. Para ganar veinte por ciento: costo entre cero ochenta.',
  ], ['Sumas al costo', 'Ganas sobre el precio', 'Para ganar eso: costo ÷'],
    [['+ 15 %', '13.0 %', '0.87'], ['+ 20 %', '16.7 %', '0.833'], ['+ 25 %', '20.0 %', '0.80'], ['+ 30 %', '23.1 %', '0.769']],
    lambda i: [1, 1, 1, 2][i], izq=280, der=280),
  ejemplo('Lo que se lleva <span class="nar">cada descuento</span>', [
    'Y lo que hace cada descuento en la cochera de seis mil quinientos, con mil ciento cuarenta de ganancia.',
    'Cinco por ciento: trescientos veinticinco menos. Pierdes casi el veintinueve por ciento de tu ganancia.',
    'Diez por ciento: pierdes el cincuenta y siete. Y quince por ciento: te quedan ciento sesenta y cinco soles. Casi trabajaste gratis.',
  ], ['Descuento', 'Bajas', 'Te queda', 'Perdiste'],
    [['5 %', 'S/ 325', 'S/ 815', '29 %'], ['10 %', 'S/ 650', 'S/ 490', '57 %'], ['15 %', 'S/ 975', 'S/ 165', '86 %']],
    lambda i: [1, 2, 2][i], izq=300, der=300, tam=31),
  caso('“está caro”', [
    'Caso de taller: un cliente dijo que otro le cotizaba el mismo portón quinientos soles menos.',
    'El maestro pidió ver la otra cotización. No incluía pintura, ni instalación, ni la guía superior. Con todo eso, era más cara.',
    'Antes de bajar, compara lo que incluye cada una. Muchas veces el "barato" no está cotizando lo mismo.',
  ], [('💬', '"Otro me lo deja <b class="nar">S/ 500 menos</b>"'), ('🔎', 'No incluía <b class="nar">pintura, instalación ni guía</b>'), ('✅', 'Compara <b class="nar">qué incluye</b> antes de bajar')]),
  *ejercicio(1,
    'Una obra cuesta <b class="nar">S/ 3 000</b> en total.<br>Quieres ganar un <b class="nar">20 % real</b> del precio.<br>¿Qué precio pones y cuánto ganas?',
    ['Ahora tú. Una obra cuesta tres mil soles en total. Quieres ganar un veinte por ciento real del precio.', '¿Qué precio pones, y cuánto ganas?'],
    'Precio: 3 000 ÷ 0.80 = <b class="nar">S/ 3 750</b><br>Ganancia: 3 750 − 3 000 = <b class="nar">S/ 750</b> = 20 % de 3 750 ✓',
    ['Tres mil entre cero ochenta: tres mil setecientos cincuenta.',
     'Ganas setecientos cincuenta, que es justo el veinte por ciento del precio. Si hubieras sumado veinte por ciento al costo, ganarías menos.']),
  *ejercicio(2,
    'El cliente pide <b class="nar">10 % de descuento</b> sobre los S/ 3 750.<br>¿Cuánto ganarías? ¿Qué le ofreces en lugar del descuento?',
    ['Segundo ejercicio. El cliente pide diez por ciento de descuento sobre los tres mil setecientos cincuenta.', '¿Cuánto ganarías? ¿Y qué le ofreces en lugar del descuento?'],
    'Descuento: <b class="nar">S/ 375</b> → ganancia: 750 − 375 = <b class="nar">S/ 375</b> (la mitad)<br>En su lugar: la <b class="nar">opción básica</b>, o un descuento menor<br>a cambio de <b class="nar">pago completo adelantado</b> o una recomendación',
    ['Bajarías trescientos setenta y cinco, y tu ganancia quedaría en la mitad.',
     'Mejor ofrece la opción básica, que cuesta menos porque tiene menos alcance. O un descuento pequeño a cambio de algo: pago completo adelantado, o fotos y una recomendación.']),
  faq([
    ('¿Cuál es un buen margen?', 'Depende del riesgo; por ejemplo 15 a 25 %.', '¿Cuál es un buen margen? Depende del riesgo, del cliente y de tu zona. Por ejemplo, entre quince y veinticinco por ciento del precio.'),
    ('¿Y si el cliente se va?', 'Algunos se van; los que se quedan pagan bien.', '¿Y si el cliente se va por el precio? Algunos se van. Los que se quedan valoran tu trabajo y pagan a tiempo.'),
    ('¿Puedo cobrar más por urgencia?', 'Sí: horas extra y prioridad tienen precio.', '¿Puedo cobrar más si es urgente? Sí. Las horas extra y dejar otras obras tienen precio. Dilo por escrito.'),
  ]),
  repaso([
    ('¿Cómo calculas el precio para un margen real?', 'Costo entre uno menos el margen.'),
    ('¿Qué pasa con un diez por ciento de descuento?', 'Puedes perder más de la mitad de tu ganancia.'),
    ('¿Qué negocias en lugar del precio?', 'El alcance.'),
    ('¿Cuál es tu límite?', 'Tu costo más un margen mínimo.'),
  ]),
]

# ───────────── Clase 6 · El acuerdo y el adelanto ─────────────
EXT['neg_c6'] = [
  respuesta('costo de S/ 4 200', [
    'La respuesta del reto de la clase pasada: una obra con costo de cuatro mil doscientos, y margen real de veinte por ciento.',
    'Precio: cuatro mil doscientos entre cero ochenta, cinco mil doscientos cincuenta. Ganancia: mil cincuenta.',
    'Con cinco por ciento de descuento bajas doscientos sesenta y dos cincuenta. Tu ganancia queda en setecientos ochenta y siete cincuenta. Perdiste la cuarta parte.',
  ], ['Dato', 'Resultado'],
    [['Precio', 'S/ 5 250'], ['Ganancia', 'S/ 1 050'], ['Con 5 % de descuento', 'S/ 4 987.50'], ['Ganancia con descuento', 'S/ 787.50 (−25 %)']], lambda i: [1, 1, 2, 2][i]),
  ejemplo('El acuerdo <span class="nar">de la cochera</span>', [
    'Antes de los errores, el acuerdo simple de la cochera, con sus ocho puntos llenos.',
    'Las partes, con nombre y documento. Cotización número veinticinco, opción estándar. Seis mil quinientos soles, cincuenta y cincuenta.',
    'Plazo: quince días hábiles desde el adelanto. Cambios: solo por escrito, con precio y días.',
    'Garantía: un año en fabricación e instalación. Y la aceptación de los dos, por escrito.',
  ], ['Punto', 'Cochera'],
    [['Partes', 'Nombres y documentos'], ['Cotización', 'N.° 25, opción estándar'], ['Precio y pagos', 'S/ 6 500 · 50 % y 50 %'], ['Plazo', '15 días hábiles desde el adelanto'],
     ['Cambios', 'Por escrito, con precio y días'], ['Garantía', '1 año (fabricación e instalación)'], ['Aceptación', 'De los dos, por escrito']],
    lambda i: [1, 1, 1, 2, 2, 3, 3][i], izq=360, der=360, tam=27),
  caso('el adicional de palabra', [
    'Caso de obra: a mitad de obra, el cliente pidió agregar una puerta peatonal en el portón. "Después vemos el precio", le dijeron.',
    'Al final, el maestro cobró cuatrocientos. El cliente pensaba que eran cien. Terminaron peleados, y la recomendación se perdió.',
    'El adicional se manda por escrito antes de hacerlo: qué, cuánto y cuántos días. Y se hace cuando el cliente lo acepta.',
  ], [('🚪', 'Adicional "<b class="nar">después vemos el precio</b>"'), ('😠', 'S/ 400 vs. S/ 100: <b class="nar">pelea</b>'), ('✅', 'Adicional <b class="nar">por escrito antes</b> de hacerlo')]),
  *ejercicio(1,
    'La cochera, con el adicional, quedó en <b class="nar">S/ 7 150</b>.<br>Forma de pago: <b class="nar">50 % / 40 % / 10 %</b>.<br>¿Cuánto es cada pago y cuándo se cobra?',
    ['Ahora tú. La cochera, con el adicional, quedó en siete mil ciento cincuenta.', 'La forma de pago es cincuenta, cuarenta y diez por ciento. ¿Cuánto es cada pago, y cuándo se cobra?'],
    '50 % al firmar: <b class="nar">S/ 3 575</b><br>40 % con todo fabricado: <b class="nar">S/ 2 860</b><br>10 % a la conformidad: <b class="nar">S/ 715</b>',
    ['El cincuenta por ciento al firmar: tres mil quinientos setenta y cinco. El cuarenta, cuando todo está fabricado: dos mil ochocientos sesenta.',
     'Y el diez por ciento final, a la conformidad: setecientos quince. Ese último pago le da tranquilidad al cliente.']),
  *ejercicio(2,
    'Precio <b class="nar">S/ 6 500</b> + adicional aceptado <b class="nar">S/ 650</b>.<br>Pagos recibidos: <b class="nar">S/ 3 250</b> y <b class="nar">S/ 1 000</b>.<br>¿Cuánto es el saldo?',
    ['Segundo ejercicio. Precio, seis mil quinientos, más un adicional aceptado de seiscientos cincuenta. Pagos recibidos: tres mil doscientos cincuenta, y mil.', '¿Cuánto es el saldo?'],
    'Total: 6 500 + 650 = <b class="nar">S/ 7 150</b><br>Pagado: 3 250 + 1 000 = <b class="nar">S/ 4 250</b><br>Saldo: <b class="nar">S/ 2 900</b>',
    ['El total: siete mil ciento cincuenta. Lo pagado: cuatro mil doscientos cincuenta.',
     'El saldo: dos mil novecientos. Con las capturas de cada pago guardadas, no hay discusión.']),
  faq([
    ('¿Un WhatsApp vale como acuerdo?', 'Deja registro; en obras grandes, mejor un documento firmado.', '¿Un mensaje de WhatsApp vale como acuerdo? Deja un registro escrito. En obras grandes, mejor un documento firmado. Es orientación general: si tienes dudas, consulta con un abogado.'),
    ('¿Y si el cliente no quiere dar adelanto?', 'Sin adelanto no se compra material.', '¿Y si el cliente no quiere dar adelanto? Explica que con él se compra el material. Sin adelanto, no se empieza.'),
    ('¿Doy recibo aunque no tenga RUC?', 'Sí: un recibo simple con fecha y monto.', '¿Doy constancia si todavía no tengo RUC? Sí: un recibo simple con fecha, monto y concepto. La formalización la vemos en la clase diez.'),
  ]),
  repaso([
    ('¿Cuántas cosas dice un acuerdo simple?', 'Ocho.'),
    ('¿Cuánto adelanto es lo común?', 'El cincuenta por ciento.'),
    ('¿Cuándo se hace un adicional?', 'Cuando el cliente acepta su precio por escrito.'),
    ('¿Qué guardas de cada pago?', 'El recibo o la captura.'),
  ]),
]

# ───────────── Clase 7 · Cobranza y flujo de caja ─────────────
EXT['neg_c7'] = [
  ejemplo('Flujo de caja <span class="nar">de una obra más grande</span>', [
    'Antes de los errores, el flujo de caja de una obra de diez mil soles, con pagos de cincuenta, cuarenta y diez por ciento.',
    'Semana uno: sale cuatro mil quinientos, entran cinco mil. Caja: más quinientos. Semana dos: salen mil quinientos. Caja: menos mil.',
    'Semana tres: entran cuatro mil, salen ochocientos. Caja: más dos mil doscientos. Semana cuatro: entran mil, salen quinientos. Termina en más dos mil setecientos.',
    'Fíjate en la semana dos: aun con adelanto, la caja baja de cero. Por eso necesitas una reserva.',
  ], ['Semana', 'Entra', 'Sale', 'Caja acumulada'],
    [['1', 'S/ 5 000', 'S/ 4 500', '+ S/ 500'], ['2', '—', 'S/ 1 500', '− S/ 1 000'], ['3', 'S/ 4 000', 'S/ 800', '+ S/ 2 200'], ['4', 'S/ 1 000', 'S/ 500', '+ S/ 2 700']],
    lambda i: [1, 1, 2, 2][i], izq=300, der=300, tam=31),
  caso('tres obras sin adelanto', [
    'Caso de taller: para no perder clientes, un maestro aceptó tres obras seguidas sin adelanto.',
    'Compró material para las tres. A la tercera semana no tenía para el sueldo del ayudante ni para la luz. Pidió prestado con interés.',
    'Ganó en las tres obras, en papel. Pero el interés y el estrés se comieron buena parte. El adelanto no es desconfianza: es caja.',
  ], [('🔨', '<b class="nar">Tres obras</b> sin adelanto'), ('🏦', 'Préstamo <b class="nar">con interés</b> para pagar'), ('✅', 'El adelanto <b class="nar">es caja</b>')]),
  *ejercicio(1,
    'Obra de <b class="nar">S/ 5 000</b>, pagos <b class="nar">50 / 50</b> (semanas 1 y 3).<br>Salidas: semana 1, <b class="nar">S/ 2 500</b> · semana 2, <b class="nar">S/ 600</b> · semana 3, <b class="nar">S/ 400</b>.<br>¿Cómo queda la caja cada semana?',
    ['Ahora tú. Una obra de cinco mil soles, con pagos de cincuenta y cincuenta, en las semanas uno y tres.', 'Salidas: semana uno, dos mil quinientos. Semana dos, seiscientos. Semana tres, cuatrocientos. ¿Cómo queda la caja cada semana?'],
    'Semana 1: 2 500 − 2 500 = <b class="nar">S/ 0</b><br>Semana 2: 0 − 600 = <b class="nar">− S/ 600</b><br>Semana 3: −600 + 2 500 − 400 = <b class="nar">+ S/ 1 500</b>',
    ['Semana uno: entra dos mil quinientos y sale lo mismo. Caja en cero.',
     'Semana dos: menos seiscientos. Y semana tres: entra el saldo, sale cuatrocientos, y terminas con mil quinientos a favor. La semana dos la cubre tu reserva.']),
  *ejercicio(2,
    'El cliente debe <b class="nar">S/ 2 900</b> y la entrega es mañana a las 10 a. m.<br>Escribe el mensaje de recordatorio.',
    ['Segundo ejercicio. El cliente debe dos mil novecientos soles, y la entrega es mañana a las diez de la mañana.', 'Escribe el mensaje de recordatorio.'],
    '"Buenas tardes, señora Ruiz. <b class="nar">Mañana a las 10 a. m.</b> le entregamos su obra terminada.<br>Le recuerdo el saldo de <b class="nar">S/ 2 900</b>, por transferencia o Yape.<br>¡Gracias por su confianza!"',
    ['Algo así: buenas tardes, señora Ruiz. Mañana a las diez le entregamos su obra terminada. Le recuerdo el saldo de dos mil novecientos soles, por transferencia o Yape. Gracias por su confianza.',
     'Claro, amable y con el monto exacto. Sin pena: cobrar lo trabajado es lo justo.']),
  faq([
    ('¿Cuánto guardo de reserva?', 'Por ejemplo, una parte de cada ganancia.', '¿Cuánto guardo de reserva? Por ejemplo, una parte de la ganancia de cada obra, hasta juntar lo de uno o dos meses de gastos fijos.'),
    ('¿Una cuenta aparte cuesta?', 'Hay cuentas sin costo; pregunta en tu banco.', '¿Abrir una cuenta aparte cuesta? Muchas cuentas no cobran mantenimiento. Pregunta en tu banco.'),
    ('¿Y si el cliente no paga?', 'Sube de a pocos; con escrito, más fuerza.', '¿Y si de verdad no paga? Sube de a pocos, como vimos. Con el acuerdo y los pagos por escrito, tienes más fuerza. Para montos grandes, consulta con un abogado.'),
  ]),
  repaso([
    ('¿Qué diferencia hay entre ganancia y caja?', 'La ganancia es al final; la caja es cada semana.'),
    ('¿Qué pasa si cobras todo al final?', 'Financias al cliente con tu plata.'),
    ('¿Cuándo recuerdas el saldo?', 'Un día antes de la entrega.'),
    ('¿Qué tres hábitos cuidan la caja?', 'Cuentas separadas, reserva y anotar cada semana.'),
  ]),
]

# ───────────── Clase 8 · Entrega, garantía y postventa ─────────────
EXT['neg_c8'] = [
  ejemplo('La garantía: <span class="nar">qué cubre</span>', [
    'Antes de los errores, la garantía en una tabla, para escribirla igual en tus documentos.',
    'Cubre: una soldadura que se suelta, un portón que se descuadra, una gotera por mala instalación.',
    'No cubre: golpes de un auto, mal uso, falta de mantenimiento, o cambios que hizo otra persona.',
  ], ['Cubre', 'No cubre'],
    [['Soldadura que se suelta', 'Golpes (por ejemplo, un auto)'], ['Portón que se descuadra solo', 'Mal uso'], ['Gotera por mala instalación', 'Falta de mantenimiento'], ['Pintura que se pela antes de tiempo', 'Cambios hechos por otra persona']],
    lambda i: [1, 1, 2, 2][i], izq=260, der=260),
  caso('la entrega sin el cliente', [
    'Caso de obra: para no esperar, el maestro dejó la reja instalada y le mandó una foto al cliente, que estaba trabajando.',
    'Esa noche, el cliente encontró un rayón y dijo que había sido en la instalación. Pudo haber sido cualquiera. El maestro volvió a pintar gratis.',
    'La entrega se hace con el cliente presente, recorriendo la obra, y con su conformidad escrita.',
  ], [('📸', 'Entregó <b class="nar">solo con una foto</b>'), ('🪛', 'Reclamo por un <b class="nar">rayón</b>'), ('✅', 'Entrega <b class="nar">con el cliente</b> y conformidad escrita')]),
  *ejercicio(1,
    'Un portón se cobró en <b class="nar">S/ 4 800</b>, más un adicional de <b class="nar">S/ 300</b>.<br>El costo total, con el adicional, fue <b class="nar">S/ 4 250</b>.<br>¿Cuánto ganaste y qué porcentaje del precio es?',
    ['Ahora tú. Un portón se cobró en cuatro mil ochocientos, más un adicional de trescientos. El costo total, con el adicional, fue de cuatro mil doscientos cincuenta.', '¿Cuánto ganaste, y qué porcentaje del precio es?'],
    'Precio: 4 800 + 300 = <b class="nar">S/ 5 100</b><br>Ganancia: 5 100 − 4 250 = <b class="nar">S/ 850</b><br>Margen: 850 ÷ 5 100 ≈ <b class="nar">16.7 %</b>',
    ['El precio final: cinco mil cien. La ganancia: ochocientos cincuenta.',
     'Entre cinco mil cien: dieciséis coma siete por ciento. Con tu hora ya pagada dentro del costo.']),
  *ejercicio(2,
    'Entregaste una obra el <b class="nar">10 de marzo</b>.<br>¿Cuándo envías el mensaje de los 30 días<br>y el recordatorio de mantenimiento de los 6 meses?',
    ['Segundo ejercicio. Entregaste una obra el diez de marzo.', '¿Cuándo envías el mensaje de los treinta días, y el recordatorio de mantenimiento de los seis meses?'],
    '30 días: <b class="nar">9 de abril</b> → "¿Todo bien con su portón?"<br>6 meses: <b class="nar">10 de setiembre</b> → recordatorio de mantenimiento<br>Anótalos en tu calendario <b class="nar">el día de la entrega</b>',
    ['A los treinta días: el nueve de abril. Un mensaje corto: todo bien con su portón.',
     'Y a los seis meses: el diez de setiembre, el recordatorio de mantenimiento. Agéndalos en tu calendario el mismo día que entregas.']),
  faq([
    ('¿Cuánto tiempo de garantía doy?', 'Por ejemplo, seis meses o un año, según el trabajo.', '¿Cuánta garantía doy? Por ejemplo, de seis meses a un año, según el trabajo. Lo importante es que esté por escrito.'),
    ('¿Y si me piden una reseña falsa?', 'No: solo reseñas de clientes reales.', '¿Puedo pedir reseñas a amigos? No. Solo a clientes reales. Las reseñas falsas se notan y dañan tu imagen.'),
    ('¿Cómo guardo mis clientes?', 'Una lista con nombre, teléfono, obra y fecha.', '¿Cómo guardo mis clientes? En una lista con nombre, teléfono, obra y fecha. En InnovApp, en la carpeta de clientes.'),
  ]),
  repaso([
    ('¿Qué haces antes de llamar al cliente?', 'Revisar tú mismo la obra.'),
    ('¿Cómo se da la garantía?', 'Por escrito, con lo que cubre y no cubre.'),
    ('¿Qué tres cosas pides al final?', 'Fotos, reseña y recomendación.'),
    ('¿Cuándo es la postventa?', 'A los treinta días y a los seis meses.'),
  ]),
]

# ───────────── Clase 9 · Consigue clientes ─────────────
EXT['neg_c9'] = [
  ejemplo('¿Qué canal <span class="nar">te da obras</span>?', [
    'Antes de los errores, cómo medir no solo de dónde vienen las consultas, sino cuántas se vuelven obras.',
    'Recomendaciones: ocho consultas, cinco obras. Sesenta y dos por ciento.',
    'Facebook: veinte consultas, cuatro obras: veinte por ciento. Google: seis consultas, dos obras: treinta y tres.',
    'Las recomendaciones cierran mucho más. Por eso pedir una recomendación en cada entrega vale tanto como publicar.',
  ], ['Canal', 'Consultas', 'Obras', 'Cierre'],
    [['Recomendación', '8', '5', '62 %'], ['Facebook', '20', '4', '20 %'], ['Google', '6', '2', '33 %']],
    lambda i: [1, 2, 2][i], izq=320, der=320, tam=32),
  ejemplo('Una semana <span class="nar">de publicaciones</span>', [
    'Y un plan simple para una semana, sin que te quite tiempo del taller.',
    'Lunes: el antes y después de una obra, en estados y Facebook. Miércoles: un video corto del portón funcionando.',
    'Viernes: un consejo útil, por ejemplo cómo mantener el riel. Y todos los días: responder rápido los mensajes.',
  ], ['Día', 'Qué publicar'],
    [['Lunes', 'Antes y después de una obra'], ['Miércoles', 'Video corto de 15 a 30 s'], ['Viernes', 'Un consejo útil para el cliente'], ['Todos los días', 'Responder rápido']],
    lambda i: [1, 1, 2, 2][i], izq=400, der=400, tam=31),
  caso('las fotos de noche', [
    'Caso de taller: un maestro publicaba sus portones con fotos de noche, desde el celular, con herramientas en el piso. Casi nadie preguntaba.',
    'Empezó a tomarlas de día, de frente, con la obra limpia, y a mostrar el antes y el después. En un mes, las consultas se triplicaron.',
    'Tu trabajo puede ser excelente. Si la foto es mala, nadie lo ve.',
  ], [('🌙', 'Fotos <b class="nar">de noche y desordenadas</b>'), ('☀️', 'De día, de frente, <b class="nar">antes y después</b>'), ('📈', 'Las consultas <b class="nar">se triplicaron</b>')]),
  *ejercicio(1,
    'Este trimestre: <b class="nar">30 consultas</b> por Facebook → <b class="nar">3 obras</b>.<br><b class="nar">10 consultas</b> por recomendación → <b class="nar">6 obras</b>.<br>¿Cuál cierra más y qué harías?',
    ['Ahora tú. Este trimestre tuviste treinta consultas por Facebook, que se volvieron tres obras. Y diez consultas por recomendación, que se volvieron seis obras.', '¿Cuál cierra más, y qué harías?'],
    'Facebook: 3 ÷ 30 = <b class="nar">10 %</b> · Recomendación: 6 ÷ 10 = <b class="nar">60 %</b><br>Pide recomendación <b class="nar">en cada entrega</b><br>y mejora fotos y respuestas en Facebook',
    ['Facebook cierra el diez por ciento. Las recomendaciones, el sesenta.',
     'Pide una recomendación en cada entrega. Y en Facebook, mejora las fotos y responde más rápido: muchas consultas se pierden por responder tarde.']),
  *ejercicio(2,
    'Escribe una publicación corta para un <b class="nar">portón corredizo</b> que terminaste.<br>Debe tener: historia, foto, y cómo contactarte.',
    ['Segundo ejercicio. Escribe una publicación corta para un portón corredizo que terminaste.', 'Debe tener una pequeña historia, la foto, y cómo contactarte.'],
    '"La familia Torres no tenía espacio para que gire un portón.<br>Les hicimos uno <b class="nar">corredizo de 3 × 2.40 m</b>, que corre suave y queda seguro.<br>📸 Antes y después · 💬 Cotiza gratis: <b class="nar">tu WhatsApp</b>"',
    ['Por ejemplo: la familia Torres no tenía espacio para que gire un portón. Les hicimos uno corredizo de tres por dos cuarenta, que corre suave y queda seguro.',
     'Con la foto del antes y el después, y tu WhatsApp para cotizar. Con permiso del cliente para usar su nombre y las fotos.']),
  faq([
    ('¿Pago publicidad?', 'Primero publica bien gratis; luego prueba con poco.', '¿Pago publicidad en redes? Primero publica bien, gratis, unas semanas. Después prueba con un monto pequeño y mide si llegan obras.'),
    ('¿Qué hago con un mal comentario?', 'Responde con calma y ofrece solución.', '¿Qué hago con un comentario negativo? Responde con calma, sin pelear, y ofrece una solución. Los demás clientes miran cómo respondes.'),
    ('¿Necesito página web?', 'Al inicio basta Google y WhatsApp Business.', '¿Necesito una página web? Al inicio, con tu perfil de Google y WhatsApp Business es suficiente.'),
  ]),
  repaso([
    ('¿Cuál es la regla de las fotos?', 'Antes, durante y después.'),
    ('¿Qué te pone en el mapa de Google?', 'El Perfil de Empresa en Google.'),
    ('¿Qué preguntas a cada cliente nuevo?', 'Cómo nos conoció.'),
    ('¿Qué canal suele cerrar más?', 'La recomendación.'),
  ]),
]

# ───────────── Clase 10 · Formaliza tu taller ─────────────
EXT['neg_c10'] = [
  ejemplo('¿Qué régimen <span class="nar">emite factura</span>?', [
    'Antes de los errores, un dato que decide mucho para el metalero: qué régimen te deja emitir factura.',
    'En el Nuevo RUS emites boletas, pero no facturas. En el Régimen Especial, en el MYPE Tributario y en el General, sí puedes emitir facturas.',
    'Si quieres trabajar con empresas y constructoras, que casi siempre piden factura, necesitas un régimen que la permita. Elige con tu contador.',
  ], ['Régimen', '¿Emite factura?'],
    [['Nuevo RUS', 'No (solo boletas)'], ['Régimen Especial (RER)', 'Sí'], ['Régimen MYPE Tributario', 'Sí'], ['Régimen General', 'Sí']],
    lambda i: [1, 2, 2, 2][i], izq=420, der=420, tam=31),
  caso('la obra que no existía', [
    'Caso de taller: una constructora quería contratar a un buen metalero para veinte portones de un condominio.',
    'Le pidieron factura, y él no tenía RUC. La obra se la llevó otro taller, menos bueno, pero formal.',
    'Esa sola obra pagaba los costos de formalizarse de varios años. Sin comprobante, para una empresa, no existes.',
  ], [('🏗️', 'Constructora: <b class="nar">20 portones</b>'), ('🧾', 'Pidió factura: <b class="nar">no tenía RUC</b>'), ('✅', 'Se la llevó un taller <b class="nar">formal</b>')]),
  *ejercicio(1,
    'Una obra cuesta <b class="nar">S/ 4 200 sin IGV</b>. ¿Cuánto es con IGV (18 %)?<br>Y si te dicen que el precio <b class="nar">S/ 5 000 ya incluye IGV</b>,<br>¿cuánto es para ti y cuánto es impuesto?',
    ['Ahora tú. Una obra cuesta cuatro mil doscientos soles sin IGV. ¿Cuánto es con IGV, de dieciocho por ciento?', 'Y si te dicen que el precio de cinco mil ya incluye IGV, ¿cuánto es para ti, y cuánto es impuesto?'],
    'Con IGV: 4 200 × 1.18 = <b class="nar">S/ 4 956</b><br>5 000 con IGV: 5 000 ÷ 1.18 ≈ <b class="nar">S/ 4 237</b> para ti · IGV ≈ <b class="nar">S/ 763</b><br>Siempre escribe si tu precio es <b class="nar">con o sin IGV</b>',
    ['Cuatro mil doscientos por uno punto dieciocho: cuatro mil novecientos cincuenta y seis.',
     'Y si cinco mil ya incluyen IGV: divides entre uno punto dieciocho. Unos cuatro mil doscientos treinta y siete son tuyos, y unos setecientos sesenta y tres son impuesto. Por eso, escribe siempre si tu precio es con o sin IGV.']),
  *ejercicio(2,
    'Un contador te cobra <b class="nar">S/ 150 al mes</b>. Una obra con una constructora<br>de <b class="nar">S/ 20 000</b> te deja un <b class="nar">15 %</b> de ganancia.<br>¿Cuántos meses de contador paga esa obra?',
    ['Segundo ejercicio. Un contador te cobra ciento cincuenta soles al mes. Una obra con una constructora, de veinte mil soles, te deja quince por ciento de ganancia.', '¿Cuántos meses de contador paga esa obra?'],
    'Ganancia: 20 000 × 0.15 = <b class="nar">S/ 3 000</b><br>Contador: 3 000 ÷ 150 = <b class="nar">20 meses</b><br>Una sola obra formal paga <b class="nar">más de un año</b> de contador',
    ['Quince por ciento de veinte mil: tres mil soles de ganancia.',
     'Entre ciento cincuenta: veinte meses de contador. Una sola obra formal paga más de un año y medio.']),
  faq([
    ('¿Persona natural o empresa?', 'Depende de tu caso: consulta con un contador.', '¿Me conviene ser persona natural con negocio o empresa? Depende de tu caso. Es orientación general: consulta con un contador.'),
    ('¿Qué es el SCTR?', 'Seguro de trabajo de riesgo que piden en obra.', '¿Qué es el SCTR? Un seguro complementario de trabajo de riesgo, que suelen pedir en obras de construcción. Inclúyelo en tus cotizaciones para empresas.'),
    ('¿Y la licencia del taller?', 'Se tramita en tu municipalidad.', '¿Dónde saco la licencia de funcionamiento? En tu municipalidad. Pregunta qué piden para un taller.'),
  ]),
  repaso([
    ('¿Qué se saca primero?', 'El RUC.'),
    ('¿Qué régimen no permite factura?', 'El Nuevo RUS.'),
    ('¿Qué guardas de tus compras?', 'Los comprobantes.'),
    ('¿Quién te ayuda a elegir el régimen?', 'Un contador.'),
  ]),
]

# ───────────── Clase 11 · Tu equipo ─────────────
EXT['neg_c11'] = [
  ejemplo('Jornal, destajo <span class="nar">o sueldo</span>', [
    'Antes de los errores, las tres formas de pago, con lo bueno y lo que debes cuidar.',
    'Jornal: simple, pero sin incentivo para avanzar. Destajo: avanzan rápido, pero cuida la calidad.',
    'Y sueldo fijo: para tu gente de confianza, con los derechos que da la ley a un trabajador permanente. Consulta con tu contador.',
  ], ['Forma', 'Ventaja', 'Cuida'],
    [['Jornal (por día)', 'Simple', 'Sin incentivo para avanzar'], ['Destajo (por obra)', 'Avanzan rápido', 'La calidad y los retrabajos'], ['Sueldo fijo', 'Gente de confianza', 'Derechos laborales: consulta']],
    lambda i: i + 1, izq=240, der=240),
  caso('el ayudante sin arnés', [
    'Caso de obra: el ayudante subió al techo "un ratito" a pasar una plancha, sin arnés. El maestro no le dijo nada.',
    'Una plancha se movió con el viento y casi lo tumba. Se salvó agarrándose de una correa.',
    'Desde ese día, la regla del taller: en altura, sin arnés no se sube. Ni un ratito. Y el maestro es el primero en cumplirla.',
  ], [('🧗', 'Subió <b class="nar">sin arnés</b> "un ratito"'), ('💨', 'La plancha y el viento: <b class="nar">casi cae</b>'), ('✅', 'Sin arnés <b class="nar">no se sube</b>')]),
  *ejercicio(1,
    'Un portón le toma a tu maestro de apoyo <b class="nar">3 días</b> a jornal de <b class="nar">S/ 120</b>.<br>Te propone hacerlo a destajo por <b class="nar">S/ 330</b>.<br>¿Qué conviene y qué pones como condición?',
    ['Ahora tú. Un portón le toma a tu maestro de apoyo tres días, a un jornal de ciento veinte. Te propone hacerlo a destajo por trescientos treinta.', '¿Qué conviene, y qué pones como condición?'],
    'Jornal: 3 × 120 = <b class="nar">S/ 360</b> · Destajo: <b class="nar">S/ 330</b><br>Conviene el destajo, con condición:<br><b class="nar">pasa tu lista de revisión</b>; si no, corrige sin costo extra',
    ['A jornal serían trescientos sesenta. A destajo, trescientos treinta: conviene.',
     'Pero con una condición clara: el portón debe pasar tu lista de revisión. Si no, lo corrige sin costo extra.']),
  *ejercicio(2,
    'Arma una <b class="nar">charla de seguridad de 5 minutos</b> para mañana:<br>van a montar un techo a <b class="nar">4 m</b> de altura y a soldar correas.<br>¿Qué cuatro puntos dices?',
    ['Segundo ejercicio. Arma una charla de seguridad de cinco minutos para mañana. Van a montar un techo a cuatro metros de altura, y a soldar correas.', '¿Qué cuatro puntos dices?'],
    '1. <b class="nar">Arnés y línea de vida</b> siempre arriba<br>2. Andamio o escalera <b class="nar">firmes y revisados</b><br>3. <b class="nar">Extintor</b> y nada inflamable cerca al soldar · 4. Zona de abajo <b class="nar">señalizada</b>',
    ['Uno: arnés y línea de vida, siempre arriba. Dos: andamio o escalera firmes y revisados.',
     'Tres: extintor a la mano y nada inflamable cerca al soldar. Y cuatro: la zona de abajo señalizada, para que nadie pase. Lo ves a fondo en el curso de Seguridad en Obra.']),
  faq([
    ('¿Cómo pruebo a alguien nuevo?', 'Con un trabajo pequeño y pagado.', '¿Cómo pruebo a un trabajador nuevo? Con un trabajo pequeño, pagado, y mirando su actitud y su cuidado.'),
    ('¿Le enseño todo?', 'Sí: tus estándares por escrito.', '¿Le enseño todo lo que sé? Sí. Con tus estándares por escrito, tu taller funciona aunque no estés.'),
    ('¿Qué es un buen ayudante?', 'Puntual, ordenado y con ganas de aprender.', '¿Qué busco en un ayudante? Puntualidad, orden, ganas de aprender y cuidado con la seguridad.'),
  ]),
  repaso([
    ('¿Cuándo contratar?', 'Cuando rechazas obras o la calidad baja por cansancio.'),
    ('¿Qué se enseña y qué no?', 'La habilidad se enseña; la actitud casi nunca.'),
    ('¿De quién es la seguridad del equipo?', 'Tuya.'),
    ('¿Qué haces tú al delegar?', 'Vendes, cotizas y supervisas.'),
  ]),
]

# ───────────── Clase 12 · Crecer ─────────────
EXT['neg_c12'] = [
  ejemplo('Tus cinco números, <span class="nar">un mes real</span>', [
    'Antes de los errores, los cinco números de un mes de ejemplo.',
    'Ventas: dieciocho mil soles. Margen promedio: diecisiete por ciento. Ganancia: unos tres mil sesenta.',
    'Cotizaciones: doce, obras ganadas: cuatro. Tasa de cierre: treinta y tres por ciento. Ticket promedio: cuatro mil quinientos.',
    'Y caja a fin de mes: dos mil cuatrocientos. Con esto ya sabes qué mejorar el mes que viene.',
  ], ['Número', 'Este mes'],
    [['Ventas', 'S/ 18 000'], ['Margen promedio', '17 %'], ['Tasa de cierre', '4 de 12 = 33 %'], ['Ticket promedio', 'S/ 4 500'], ['Caja a fin de mes', 'S/ 2 400']],
    lambda i: [1, 1, 2, 2, 3][i], izq=440, der=440, tam=30),
  caso('la constructora que pagaba a 60 días', [
    'Caso de taller: un metalero ganó su primera obra con una constructora, de treinta mil soles. Pago a sesenta días de entregada la factura.',
    'Compró todo el material y pagó tres semanas de planilla. Se quedó sin caja para las demás obras, y tuvo que prestarse.',
    'Antes de aceptar, haz el flujo de caja: ¿puedes financiar la obra hasta el pago? Si no, negocia un adelanto o un pago por avance.',
  ], [('🏗️', 'Obra de <b class="nar">S/ 30 000</b>, pago a 60 días'), ('🏦', 'Sin caja: <b class="nar">préstamo</b>'), ('✅', 'Flujo de caja <b class="nar">antes de aceptar</b>')]),
  *ejercicio(1,
    'Una cortadora cuesta <b class="nar">S/ 4 500</b> y te ahorra <b class="nar">15 horas al mes</b>.<br>Tu hora cuesta <b class="nar">S/ 34</b>. ¿En cuántos meses se paga?',
    ['Ahora tú. Una cortadora cuesta cuatro mil quinientos soles, y te ahorra quince horas al mes. Tu hora cuesta treinta y cuatro.', '¿En cuántos meses se paga?'],
    'Ahorro: 15 × 34 = <b class="nar">S/ 510</b> al mes<br>Se paga en: 4 500 ÷ 510 ≈ <b class="nar">9 meses</b><br>Si esas horas <b class="nar">se usan para cobrar</b> otras obras, conviene',
    ['Quince horas por treinta y cuatro: quinientos diez soles al mes.',
     'Cuatro mil quinientos entre quinientos diez: unos nueve meses. Conviene, si esas horas ahorradas de verdad se usan para hacer más obras.']),
  *ejercicio(2,
    'Mandaste <b class="nar">24 cotizaciones</b> y ganaste <b class="nar">6 obras</b>.<br>Si subes tu cierre a <b class="nar">35 %</b>, con las mismas cotizaciones<br>y un ticket de <b class="nar">S/ 4 500</b>, ¿cuánto más vendes?',
    ['Segundo ejercicio. Mandaste veinticuatro cotizaciones, y ganaste seis obras.', 'Si subes tu cierre a treinta y cinco por ciento, con las mismas cotizaciones y un ticket de cuatro mil quinientos, ¿cuánto más vendes?'],
    'Hoy: 6 ÷ 24 = <b class="nar">25 %</b><br>Con 35 %: 24 × 0.35 ≈ <b class="nar">8.4 obras</b> → unas 2 obras más<br>2.4 × 4 500 ≈ <b class="nar">S/ 10 800</b> más en ventas',
    ['Hoy cierras el veinticinco por ciento. Con treinta y cinco, serían unas ocho obras y media: unas dos más.',
     'Dos coma cuatro obras por cuatro mil quinientos: unos diez mil ochocientos soles más en ventas, sin buscar ni un cliente nuevo.']),
  faq([
    ('¿Cuál palanca muevo primero?', 'La tasa de cierre: mejores visitas y cotizaciones.', '¿Qué palanca muevo primero? Normalmente la tasa de cierre: visitas y cotizaciones mejores. No necesitas más clientes, sino cerrar mejor.'),
    ('¿Cómo elijo mi especialidad?', 'Lo que haces mejor y más te piden.', '¿Cómo elijo mi especialidad? Lo que haces mejor, lo que más te piden en tu zona, y lo que mejor margen te deja.'),
    ('¿Dónde llevo los números?', 'Una hoja simple o InnovApp.', '¿Dónde llevo los cinco números? En una hoja simple, o en InnovApp, con tus proyectos y gastos.'),
  ]),
  repaso([
    ('¿Cuáles son los cinco números?', 'Ventas, margen, tasa de cierre, ticket promedio y caja.'),
    ('¿Cuáles son las tres palancas?', 'Más cotizaciones, mejor cierre y mejor margen.'),
    ('¿Cuándo conviene una máquina?', 'Cuando ahorra horas que puedes cobrar.'),
    ('¿Qué revisas antes de una obra grande?', 'Tu caja.'),
  ]),
]
