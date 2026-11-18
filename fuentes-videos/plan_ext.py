"""Ampliación de «Lectura de Planos Metálicos» (≈7 min por clase). Misma receta que los demás cursos."""
from naves_ext import insertar, caja, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · Rótulo, escalas y láminas ─────────────
EXT['plan_c1'] = [
  ejemplo('La escala <span class="nar">en números</span>', [
    'Antes de los errores, la escala con cuatro ejemplos. Siempre con el plano impreso en su tamaño original.',
    'A uno a cincuenta, ocho centímetros del papel son cuatro metros. A uno a veinte, cinco centímetros son un metro.',
    'A uno a cien, doce centímetros son doce metros. Y a uno a diez, tres centímetros son treinta centímetros reales.',
    'Pero recuerda: esto es para entender el dibujo. Para fabricar, manda la cota escrita.',
  ], ['Escala', 'En el papel', 'En la realidad'],
    [['1 : 50', '8 cm', '4.00 m'], ['1 : 20', '5 cm', '1.00 m'], ['1 : 100', '12 cm', '12.00 m'], ['1 : 10', '3 cm', '0.30 m']],
    lambda i: [1, 1, 2, 2][i], izq=380, der=380, tam=32),
  ejemplo('Los tamaños <span class="nar">de hoja</span>', [
    'Y por qué un plano impreso más chico ya no está a escala.',
    'El A uno mide cincuenta y nueve por ochenta y cuatro centímetros. El A tres, veintinueve punto siete por cuarenta y dos: la mitad de largo.',
    'Un plano a uno a cincuenta pensado para A uno, impreso en A tres, queda a uno a cien. Si mides con regla, todo te sale la mitad.',
  ], ['Hoja', 'Medidas', 'Si el original era A1 a 1:50'],
    [['A1', '594 × 841 mm', '1 : 50 (correcto)'], ['A2', '420 × 594 mm', '≈ 1 : 71'], ['A3', '297 × 420 mm', '≈ 1 : 100'], ['WhatsApp', 'Cualquiera', 'Sin escala']],
    lambda i: [1, 2, 2, 2][i], izq=260, der=260),
  caso('la viga de la mitad', [
    'Caso de obra: un maestro recibió el plano por WhatsApp, lo imprimió en A cuatro y midió una viga que no tenía cota escrita.',
    'Cortó la viga con lo que le dio la regla y la escala del rótulo. Le salió casi un metro más corta de lo debido.',
    'Si una medida no está escrita, se pregunta por escrito. Nunca se mide un plano reducido.',
  ], [('📱', 'Plano por WhatsApp, impreso en <b class="nar">A4</b>'), ('📏', 'Midió con regla: viga <b class="nar">casi 1 m más corta</b>'), ('✍️', 'Sin cota escrita: <b class="nar">consulta por escrito</b>')]),
  *ejercicio(1,
    'En un plano a <b class="nar">1 : 25</b>, impreso en su tamaño original,<br>un detalle mide <b class="nar">6.4 cm</b> en el papel.<br>¿Cuánto mide en la realidad? ¿Lo usarías para cortar?',
    ['Ahora tú. En un plano a uno a veinticinco, impreso en su tamaño original, un detalle mide seis punto cuatro centímetros en el papel.', '¿Cuánto mide en la realidad? ¿Y lo usarías para cortar?'],
    '6.4 × 25 = <b class="nar">160 cm = 1.60 m</b><br>Sirve para <b class="nar">entender</b>, no para cortar:<br>para fabricar, <b class="nar">la cota escrita</b> o una consulta',
    ['Seis punto cuatro por veinticinco: ciento sesenta centímetros. Un metro sesenta.',
     'Sirve para entender el tamaño. Pero para cortar, solo la cota escrita. Si no está, consulta.']),
  *ejercicio(2,
    'En la obra hay dos copias de la lámina E-03:<br>una con <b class="nar">revisión A</b> del 3 de marzo y otra con <b class="nar">revisión C</b> del 20 de abril.<br>¿Con cuál trabajas y qué haces con la otra?',
    ['Segundo ejercicio. En la obra hay dos copias de la lámina E cero tres: una con revisión A, del tres de marzo, y otra con revisión C, del veinte de abril.', '¿Con cuál trabajas, y qué haces con la otra?'],
    'Trabajas con la <b class="nar">revisión C</b>, la última<br>La A se marca <b class="nar">"ANULADA"</b> o se retira de la obra<br>Y confirmas que no exista una revisión D',
    ['Con la revisión C, la última.',
     'La A se marca como anulada o se saca de la obra, para que nadie fabrique con ella. Y preguntas si no hay una más nueva.']),
  faq([
    ('¿Qué es una RFI?', 'Una consulta por escrito al proyectista.', '¿Qué es una R F I? Una consulta por escrito al proyectista. Guarda la pregunta y la respuesta: son parte de la obra.'),
    ('¿Y si el plano no tiene escala?', 'Dice S/E: solo valen las cotas.', '¿Y si el plano no tiene escala? Dirá S barra E, sin escala. Solo valen las cotas escritas.'),
    ('¿Puedo trabajar con el PDF en el celular?', 'Sí, para leer cotas; nunca para medir.', '¿Puedo trabajar con el PDF en el celular? Sí, para leer las cotas escritas y hacer zoom. Nunca para medir.'),
  ]),
  repaso([
    ('¿Qué dice el rótulo?', 'Proyecto, lámina, escala, fecha, revisión y responsable.'),
    ('¿Con qué revisión trabajas?', 'Siempre con la última.'),
    ('¿Qué lámina se lee primero?', 'La de notas generales.'),
    ('¿Qué manda: la regla o la cota?', 'La cota escrita.'),
  ]),
]

# ───────────── Clase 2 · Vistas, cortes y detalles ─────────────
EXT['plan_c2'] = [
  ejemplo('Las líneas <span class="nar">y lo que dicen</span>', [
    'Antes de los errores, las líneas del plano en una tabla, con un ejemplo de cada una.',
    'Continua gruesa: el borde de la placa base que ves. A trazos: el agujero que queda detrás de la columna.',
    'Raya y punto: el eje de la columna. Y la línea fina con flechas: la cota de trescientos milímetros de la placa.',
  ], ['Línea', 'Significa', 'Ejemplo'],
    [['Continua gruesa', 'Se ve', 'Borde de la placa'], ['A trazos', 'Oculto, detrás', 'Agujero detrás de la columna'], ['Raya y punto', 'Eje o centro', 'Eje de la columna'], ['Fina con flechas', 'Cota', '300 mm de la placa']],
    lambda i: [1, 1, 2, 2][i], izq=240, der=240),
  caso('las cartelas iguales', [
    'Caso de taller: el plano pedía ocho cartelas "cuatro de cada mano". El cortador las cortó y perforó las ocho iguales.',
    'En el armado, cuatro quedaban con los agujeros hacia afuera. No servían. Se cortaron cuatro nuevas.',
    'Cuando el plano dice "de mano" u "opuesta", marca con tiza cuáles van en espejo antes de cortar.',
  ], [('📄', 'Plano: "<b class="nar">4 de cada mano</b>"'), ('✂️', 'Cortaron las 8 <b class="nar">iguales</b>'), ('✅', 'Marca con tiza cuáles van <b class="nar">en espejo</b>')]),
  *ejercicio(1,
    'En la planta ves un círculo con <b class="nar">5</b> arriba y <b class="nar">E-03</b> abajo.<br>Y una línea de corte con <b class="nar">B</b> en las dos puntas, con flechas hacia el norte.<br>¿Qué significa cada cosa?',
    ['Ahora tú. En la planta ves un círculo con un cinco arriba y E cero tres abajo. Y una línea de corte con B en las dos puntas, con flechas hacia el norte.', '¿Qué significa cada cosa?'],
    'Círculo: <b class="nar">detalle 5</b>, dibujado en la <b class="nar">lámina E-03</b><br>Línea B–B: busca el dibujo <b class="nar">"Corte B-B"</b><br>y lo verás <b class="nar">mirando hacia el norte</b>',
    ['El círculo: es el detalle cinco, que está dibujado en la lámina E cero tres. Ve a buscarlo.',
     'La línea B: en alguna lámina hay un dibujo llamado corte B B, y ese corte se ve mirando hacia donde apuntan las flechas, hacia el norte.']),
  *ejercicio(2,
    'La planta muestra una placa con <b class="nar">4 agujeros</b>. La elevación muestra<br>la placa de <b class="nar">12 mm</b> con dos cartelas, y líneas a trazos detrás de la columna.<br>¿Qué sabes de cada vista?',
    ['Segundo ejercicio. La planta muestra una placa con cuatro agujeros. La elevación muestra la placa de doce milímetros con dos cartelas, y unas líneas a trazos detrás de la columna.', '¿Qué te dice cada vista?'],
    'Planta: <b class="nar">dónde van los agujeros</b> y las medidas de la placa<br>Elevación: el <b class="nar">espesor</b> (12 mm) y las <b class="nar">cartelas</b><br>Trazos: <b class="nar">agujeros o piezas ocultas</b> detrás de la columna',
    ['La planta te da la posición de los agujeros y el largo y ancho de la placa.',
     'La elevación, el espesor de doce y las cartelas. Y las líneas a trazos son lo que queda escondido detrás de la columna, normalmente los otros agujeros.']),
  faq([
    ('¿Qué es una isometría?', 'Una vista en 3D que ayuda a entender, sin medidas exactas.', '¿Qué es una isometría? Un dibujo en tres dimensiones que ayuda a entender la pieza. Las medidas, igual, en las vistas acotadas.'),
    ('¿Por qué el corte se ve rayado?', 'Lo rayado es lo que la sierra imaginaria cortó.', '¿Por qué una parte del corte está rayada? Porque es justo lo que la sierra imaginaria cortó.'),
    ('¿Y si no encuentro el detalle?', 'Consulta: puede faltar una lámina.', '¿Y si no encuentro el detalle que indica la llamada? Consulta. Puede faltar una lámina en tu juego de planos.'),
  ]),
  repaso([
    ('¿Qué vista da el largo y el ancho?', 'La planta.'),
    ('¿Qué indica una línea a trazos?', 'Algo oculto, detrás.'),
    ('¿Qué dice tres sobre E cero cuatro?', 'Detalle tres, en la lámina E cero cuatro.'),
    ('¿Qué son piezas de mano?', 'Piezas en espejo, una izquierda y una derecha.'),
  ]),
]

# ───────────── Clase 3 · Ejes, cotas y niveles ─────────────
EXT['plan_c3'] = [
  ejemplo('De ejes a caras, <span class="nar">según el perfil</span>', [
    'Antes de los errores, cuánto queda de cara a cara cuando entre ejes hay cuatro metros, según la columna.',
    'Tubo de ciento cincuenta: tres mil ochocientos cincuenta. Tubo de cien: tres mil novecientos.',
    'Y una columna W de doscientos tres milímetros de peralte, en ese sentido: tres mil setecientos noventa y siete. Siempre restas el perfil, mitad y mitad.',
  ], ['Columna', 'Entre ejes', 'Cara a cara'],
    [['Tubo 150 mm', '4 000 mm', '3 850 mm'], ['Tubo 100 mm', '4 000 mm', '3 900 mm'], ['W de 203 mm', '4 000 mm', '3 797 mm']],
    lambda i: [1, 1, 2][i], izq=360, der=360, tam=32),
  caso('la viga que no entraba', [
    'Caso de taller: el plano decía cuatro mil entre ejes. El cortador cortó la viga de cuatro mil.',
    'En la obra, entre las caras de las columnas había tres mil ochocientos cincuenta. La viga no entraba por ciento cincuenta milímetros.',
    'Antes de cortar, pregúntate: ¿esta cota es entre ejes o hasta una cara? Y resta lo que corresponda.',
  ], [('📐', 'Cota de <b class="nar">4 000 entre ejes</b>'), ('✂️', 'Cortaron la viga de <b class="nar">4 000</b>'), ('✅', 'Entre caras eran 3 850: <b class="nar">resta el perfil</b>')]),
  *ejercicio(1,
    'Una cadena de cotas dice: <b class="nar">2 850 + 3 150 + 2 950</b>.<br>La cota total dice <b class="nar">9 000</b>.<br>¿Cuadra? ¿Qué haces?',
    ['Ahora tú. Una cadena de cotas dice: dos mil ochocientos cincuenta, más tres mil ciento cincuenta, más dos mil novecientos cincuenta. La cota total dice nueve mil.', '¿Cuadra? ¿Qué haces?'],
    'Suma: 2 850 + 3 150 + 2 950 = <b class="nar">8 950</b> ≠ 9 000<br>Faltan <b class="nar">50 mm</b>: hay un error en el plano<br>No adivines: <b class="nar">consulta por escrito</b> antes de cortar',
    ['La suma da ocho mil novecientos cincuenta. No cuadra: faltan cincuenta milímetros.',
     'Puede estar mal un tramo, o la total. No adivines: consulta por escrito antes de cortar nada.']),
  *ejercicio(2,
    'El plano dice: vigas a <b class="nar">+3.00</b> sobre el NPT.<br>El taller todavía no tiene el piso: le faltan <b class="nar">3 cm</b> de contrapiso.<br>¿A qué altura del piso actual van las vigas?',
    ['Segundo ejercicio. El plano dice: vigas a más tres cero cero sobre el nivel de piso terminado.', 'El taller todavía no tiene el piso: le faltan tres centímetros de contrapiso. ¿A qué altura del piso actual van las vigas?'],
    'El piso terminado estará <b class="nar">3 cm más arriba</b><br>Desde el piso actual: 3.00 + 0.03 = <b class="nar">3.03 m</b><br>Marca el nivel cero con el láser antes de montar',
    ['El piso terminado va a quedar tres centímetros más arriba que el actual.',
     'Desde el piso de hoy, las vigas van a tres metros tres. Marca el nivel cero con el láser, y mide todo desde ahí.']),
  faq([
    ('¿Qué es NPT?', 'Nivel de piso terminado; otras siglas, en la leyenda.', '¿Qué es N P T? Nivel de piso terminado. Si ves otras siglas, búscalas en la leyenda del plano.'),
    ('¿Ejes con letras o con números?', 'Una dirección con números y otra con letras.', '¿Qué ejes llevan letras y cuáles números? Una dirección con números y la otra con letras. El plano lo define.'),
    ('¿Cómo marco ejes en la obra?', 'Con tiralíneas y comprobando diagonales.', '¿Cómo marco los ejes en la obra? Con tiralíneas, wincha y comprobando las diagonales, como en el curso de Estructuras.'),
  ]),
  repaso([
    ('¿Cómo se nombra una columna?', 'Por el cruce de sus ejes, como B dos.'),
    ('¿Las cotas van entre ejes o entre caras?', 'Casi siempre entre ejes.'),
    ('¿Qué compruebas en una cadena?', 'Que los tramos sumen la total.'),
    ('¿Desde dónde se miden los niveles?', 'Desde el cero, normalmente el piso terminado.'),
  ]),
]

# ───────────── Clase 4 · Simbología de soldadura ─────────────
EXT['plan_c4'] = [
  ejemplo('Cinco símbolos <span class="nar">leídos en voz alta</span>', [
    'Antes de los errores, cinco símbolos leídos en voz alta, como lo harías en el taller.',
    'Triángulo de cinco debajo de la línea: filete de cinco, del lado de la flecha. El mismo triángulo arriba y abajo: filete de cinco de los dos lados.',
    'Cinco, triángulo, cincuenta guion ciento cincuenta: filete de cinco, intermitente, cincuenta cada ciento cincuenta.',
    'Con un círculo en el quiebre: todo alrededor. Y con una bandera: se suelda en la obra.',
  ], ['Símbolo', 'Se lee'],
    [['5 ◺ debajo de la línea', 'Filete de 5, lado de la flecha'], ['5 ◺ arriba y abajo', 'Filete de 5, los dos lados'], ['5 ◺ 50-150', 'Intermitente: 50 mm cada 150 mm'],
     ['○ en el quiebre', 'Todo alrededor'], ['🚩 bandera', 'Soldadura de campo (en obra)']],
    lambda i: [1, 1, 2, 3, 3][i], izq=300, der=300),
  caso('la bandera que nadie vio', [
    'Caso de taller: unas columnas tenían, en el plano, la unión con su ménsula marcada con bandera. En el taller la soldaron completa.',
    'La columna con la ménsula soldada ya no entraba en el camión, ni pasaba por la puerta de la obra. Hubo que cortar la ménsula y volver a soldarla allá.',
    'La bandera no es decoración: dice que esa unión se hace en la obra, por algo. Respétala.',
  ], [('🚩', 'La unión tenía <b class="nar">bandera</b>'), ('🚚', 'Soldada en taller: <b class="nar">no entraba</b> en el camión'), ('✂️', 'Cortar y soldar en obra: <b class="nar">doble trabajo</b>')]),
  *ejercicio(1,
    'Lee este símbolo: un triángulo con un <b class="nar">6</b> a la izquierda,<br><b class="nar">encima</b> de la línea, y <b class="nar">75-200</b> a la derecha. Sin círculo ni bandera.',
    ['Ahora tú. Lee este símbolo: un triángulo con un seis a la izquierda, encima de la línea, y setenta y cinco guion doscientos a la derecha. Sin círculo ni bandera.'],
    'Filete de <b class="nar">6 mm</b>, del <b class="nar">otro lado</b> de la flecha<br>Intermitente: cordones de <b class="nar">75 mm cada 200 mm</b> (centro a centro)<br>Soldado <b class="nar">en el taller</b>, sin rodear',
    ['Filete de seis milímetros. Como está encima de la línea, va del otro lado de la junta, no del lado de la flecha.',
     'Intermitente: cordones de setenta y cinco milímetros, cada doscientos de centro a centro. Y sin bandera: se hace en el taller.']),
  *ejercicio(2,
    'Una platina de <b class="nar">3 m</b> lleva filete <b class="nar">5 ◺ 50-150</b> de los dos lados.<br>¿Cuántos metros de cordón son?<br>¿Y si alguien lo suelda corrido?',
    ['Segundo ejercicio. Una platina de tres metros lleva filete de cinco, cincuenta cada ciento cincuenta, de los dos lados.', '¿Cuántos metros de cordón son? ¿Y si alguien lo suelda corrido?'],
    'Intermitente: ⅓ del largo → 3 × ⅓ × 2 lados = <b class="nar">2 m</b> de cordón<br>Corrido: 3 × 2 = <b class="nar">6 m</b> → <b class="nar">el triple</b> de electrodo, tiempo y calor',
    ['Intermitente, cincuenta de cada ciento cincuenta: un tercio del largo. Tres metros por un tercio, por dos lados: dos metros de cordón.',
     'Corrido serían seis metros: el triple de electrodo, de tiempo y de calor. Y más deformación.']),
  faq([
    ('¿La flecha siempre apunta a la pieza con bisel?', 'En biseles de un solo lado, sí: la flecha indica cuál.', '¿La flecha indica qué pieza llevaba el bisel? En juntas con bisel en una sola pieza, sí: la flecha apunta a la pieza que se bisela.'),
    ('¿Qué va en la cola?', 'El proceso, el electrodo o la especificación.', '¿Qué se escribe en la cola? El proceso, el electrodo, o la referencia a la especificación.'),
    ('¿Dónde aprendo todos los símbolos?', 'En la guía AWS A2.4 del curso.', '¿Dónde veo todos los símbolos? En la guía de simbología AWS A dos punto cuatro que viene con este curso.'),
  ]),
  repaso([
    ('¿Qué significa el símbolo debajo de la línea?', 'Que se suelda del lado de la flecha.'),
    ('¿Qué va a la izquierda del triángulo?', 'El tamaño del filete.'),
    ('¿Qué indica la bandera?', 'Soldadura de campo, en la obra.'),
    ('¿Y el círculo en el quiebre?', 'Soldar todo alrededor.'),
  ]),
]

# ───────────── Clase 5 · Notas generales ─────────────
EXT['plan_c5'] = [
  respuesta('el símbolo del reto', [
    'La respuesta del reto de la clase pasada: el símbolo para un filete de seis, de los dos lados, todo alrededor, en obra, con siete cero dieciocho.',
    'Un triángulo con un seis encima de la línea y otro igual debajo: los dos lados.',
    'Un círculo en el quiebre de la flecha: todo alrededor. Una bandera: en obra. Y en la cola, E siete cero uno ocho.',
  ], ['Lo que pide', 'Cómo se dibuja'],
    [['Filete de 6, dos lados', '6 ◺ arriba y abajo de la línea'], ['Todo alrededor', '○ en el quiebre'], ['En obra', '🚩 bandera'], ['Con 7018', 'Cola: E7018']], lambda i: [1, 2, 2, 2][i]),
  ejemplo('Abreviaturas <span class="nar">en la vida real</span>', [
    'Antes de los errores, cuatro notas reales, traducidas.',
    'P L doce por trescientos por trescientos: plancha de doce milímetros, de trescientos por trescientos.',
    'H S S cien por cien por cuatro: tubo estructural de cien por cien, de cuatro milímetros. L dos por dos por tres dieciseisavos: ángulo de dos pulgadas por tres dieciseisavos.',
    'Y barrotes diámetro media arroba diez c barra c: barrotes redondos de media pulgada, cada diez centímetros de centro a centro.',
  ], ['Nota', 'Se lee'],
    [['PL 12 × 300 × 300', 'Plancha de 12 mm, 300 × 300'], ['HSS 100 × 100 × 4', 'Tubo estructural de 100 × 100 × 4 mm'], ['L 2" × 2" × 3/16"', 'Ángulo de 2" por 3/16"'], ['Ø ½" @ 10 c/c', 'Barrotes de ½" cada 10 cm, centro a centro']],
    lambda i: [1, 2, 2, 3][i], izq=260, der=260),
  caso('el equivalente que nadie aprobó', [
    'Caso de obra: no había stock del tubo que pedía el plano. El taller usó uno "parecido": misma medida, pero de menor espesor.',
    'En la inspección, el supervisor midió el espesor y rechazó las columnas. Nadie había aprobado el cambio.',
    'Si falta un material, pide la aprobación por escrito antes. Con la aprobación, el cambio es del proyectista; sin ella, es tuyo.',
  ], [('📦', 'Sin stock: tubo <b class="nar">"parecido"</b>'), ('🔎', 'El supervisor <b class="nar">midió y rechazó</b>'), ('✍️', 'Cambio <b class="nar">aprobado por escrito</b>, antes')]),
  *ejercicio(1,
    'Una nota dice: <b class="nar">"Filetes no indicados: 5 mm típico. Pernos A325 Ø 5/8" salvo indicación"</b>.<br>Un detalle muestra pernos de 3/4" y un filete sin tamaño.<br>¿Qué usas en ese detalle?',
    ['Ahora tú. Una nota dice: filetes no indicados, cinco milímetros típico; pernos A trescientos veinticinco de cinco octavos, salvo indicación.', 'Un detalle muestra pernos de tres cuartos y un filete sin tamaño. ¿Qué usas en ese detalle?'],
    'Pernos: <b class="nar">3/4"</b> (el detalle lo indica: manda el detalle)<br>Filete sin tamaño: <b class="nar">5 mm</b> (lo típico de la nota)',
    ['Los pernos: tres cuartos, porque el detalle lo indica. "Salvo indicación" significa eso: si un detalle dice otra cosa, manda el detalle.',
     'Y el filete sin tamaño: cinco milímetros, lo típico de la nota general.']),
  *ejercicio(2,
    'Las notas piden: <b class="nar">arenado comercial + 2 manos epóxico de 100 µm</b>.<br>Tú habías cotizado limpieza manual + 2 manos de anticorrosivo.<br>¿Qué cambia en tu precio?',
    ['Segundo ejercicio. Las notas piden arenado comercial, y dos manos de epóxico de cien micras.', 'Tú habías cotizado limpieza manual y dos manos de anticorrosivo. ¿Qué cambia en tu precio?'],
    'Se suma el <b class="nar">arenado</b> (servicio aparte, por m²)<br>El epóxico es <b class="nar">más caro</b> y a 100 µm rinde menos: <b class="nar">más galones</b><br>Recalcula la partida de pintura <b class="nar">antes de firmar</b>',
    ['Se suma el arenado, que normalmente es un servicio aparte, por metro cuadrado.',
     'Y el epóxico cuesta más y, a cien micras, rinde menos: necesitas más galones. Recalcula la partida antes de firmar, o pierdes plata.']),
  faq([
    ('¿Qué significa "típico"?', 'Que se repite igual en todos los casos parecidos.', '¿Qué significa típico? Que ese detalle o medida se repite igual en todos los casos parecidos, aunque no se dibujen todos.'),
    ('¿Qué hago si dos notas se contradicen?', 'Consulta por escrito.', '¿Y si dos notas se contradicen? Consulta por escrito. No elijas tú.'),
    ('¿Las notas valen más que el dibujo?', 'Se leen juntas; si chocan, consulta.', '¿Valen más las notas o el dibujo? Se leen juntos. Si chocan, consulta.'),
  ]),
  repaso([
    ('¿Qué significa "salvo indicación"?', 'Que vale siempre, a menos que un detalle diga otra cosa.'),
    ('¿Qué es HSS?', 'Tubo estructural.'),
    ('¿Qué significa la arroba?', 'Cada.'),
    ('¿Qué nota cambia más el precio?', 'La de pintura.'),
  ]),
]

# ───────────── Clase 6 · Marcas y plano de montaje ─────────────
EXT['plan_c6'] = [
  ejemplo('Una lista de piezas <span class="nar">de verdad</span>', [
    'Antes de los errores, la lista de piezas del mezanine, como la verías junto al plano de montaje.',
    'C uno: seis columnas de tubo de seis por seis por cuatro y medio, de tres metros. Unos trescientos sesenta y cuatro kilos.',
    'V uno: tres vigas W ocho por dieciocho, de tres metros ochocientos treinta. V T uno: dieciséis viguetas de canal C de seis.',
    'Con esta lista se compra, se controla el taller y se despacha. Cada pieza marcada se tacha al cargar el camión.',
  ], ['Marca', 'Cant.', 'Perfil', 'Largo', 'Peso'],
    [['C1', '6', 'HSS 6" × 6" × 4.5 mm', '3 000 mm', '≈ 364 kg'], ['V1', '3', 'W8 × 18', '3 830 mm', '≈ 310 kg'], ['VT1', '16', 'C 6" × 2" × 2.5 mm', '≈ 2 830 mm', '≈ 240 kg'], ['PL1', '6', 'PL 12 × 300 × 300', '—', '≈ 51 kg']],
    lambda i: [1, 2, 2, 3][i], izq=160, der=160, tam=27),
  caso('la misma marca', [
    'Caso de obra: dos vigas parecidas llevaban la misma marca, V uno. Pero una tenía dos agujeros más, para una ménsula.',
    'En la obra montaron la que no era. Cuando llegó la ménsula, no había dónde empernarla. Hubo que perforar arriba, en altura.',
    'Si dos piezas se diferencian en algo, aunque sea un agujero, llevan marcas distintas: V uno y V dos.',
  ], [('🏷️', 'Dos vigas con la <b class="nar">misma marca</b>'), ('🕳️', 'Una tenía <b class="nar">dos agujeros más</b>'), ('✅', 'Diferentes en algo → <b class="nar">marcas distintas</b>')]),
  *ejercicio(1,
    'Tienes 4 vigas W8: dos de <b class="nar">3 830 mm</b> iguales, una de 3 830 mm<br>con <b class="nar">dos agujeros extra</b>, y una de <b class="nar">4 230 mm</b>.<br>¿Cómo las marcas?',
    ['Ahora tú. Tienes cuatro vigas W ocho: dos de tres mil ochocientos treinta, idénticas. Una de tres mil ochocientos treinta, con dos agujeros extra. Y una de cuatro mil doscientos treinta.', '¿Cómo las marcas?'],
    'Las dos idénticas: <b class="nar">V1</b> (cantidad 2)<br>La de agujeros extra: <b class="nar">V2</b><br>La de 4 230 mm: <b class="nar">V3</b>',
    ['Las dos idénticas llevan la misma marca: V uno, cantidad dos.',
     'La que tiene agujeros extra es distinta: V dos. Y la más larga: V tres.']),
  *ejercicio(2,
    'La lista de despacho tiene <b class="nar">31 piezas</b>. Al cargar, tachas <b class="nar">30</b>.<br>Falta una <b class="nar">PL1</b>. ¿Sale el camión?',
    ['Segundo ejercicio. La lista de despacho tiene treinta y una piezas. Al cargar, tachas treinta. Falta una plancha PL uno.', '¿Sale el camión?'],
    '<b class="nar">No todavía</b>: busca la PL1 en el taller<br>Si no está lista, anótalo en la guía y avisa a la obra<br>para que no esperen a montar esa columna',
    ['Todavía no. Busca la plancha en el taller: muchas veces quedó debajo de otra pieza.',
     'Si no está lista, anótalo en la guía y avisa a la obra, para que planifiquen el montaje sin esperar esa pieza.']),
  faq([
    ('¿Dónde va la marca en la pieza?', 'Siempre en el mismo extremo, el que mira a un eje conocido.', '¿Dónde se pone la marca? Siempre en el mismo extremo, por ejemplo el que va hacia el eje uno.'),
    ('¿Plumón o punzón?', 'Plumón de pintura, y punzón si se va a galvanizar.', '¿Plumón o punzón? Plumón de pintura para lo normal. Si la pieza se va a galvanizar, mejor punzón, que no se borra.'),
    ('¿InnovApp hace la lista?', 'El despiece de Carpintería Metálica sí.', '¿InnovApp hace la lista de piezas? El módulo de Carpintería Metálica arma el despiece con sus piezas y cantidades.'),
  ]),
  repaso([
    ('¿Qué significa V T?', 'Vigueta.'),
    ('¿Cuándo dos piezas llevan la misma marca?', 'Solo si son idénticas.'),
    ('¿Para qué es el plano de montaje?', 'Para saber qué marca va en cada sitio.'),
    ('¿Qué haces al cargar el camión?', 'Tachar cada pieza en la lista.'),
  ]),
]

# ───────────── Clase 7 · Cimentación y anclajes ─────────────
EXT['plan_c7'] = [
  ejemplo('Un cuadro <span class="nar">de zapatas</span>', [
    'Antes de los errores, un cuadro de zapatas como el que verás en el plano, leído fila por fila.',
    'Z uno: un metro por un metro, cincuenta de alto, con acero de media pulgada cada veinte centímetros en las dos direcciones.',
    'Z dos: uno veinte por uno veinte, sesenta de alto, con media cada quince. La Z dos va donde la columna recibe más carga.',
  ], ['Zapata', 'Largo × ancho', 'Alto', 'Acero'],
    [['Z1', '1.00 × 1.00 m', '0.50 m', 'Ø ½" @ 0.20 (ambos sentidos)'], ['Z2', '1.20 × 1.20 m', '0.60 m', 'Ø ½" @ 0.15 (ambos sentidos)']],
    lambda i: i + 1, izq=200, der=200, tam=29),
  caso('el pedestal al ras', [
    'Caso de obra: el maestro de obra vació los pedestales al ras del piso terminado, "para que se vea limpio".',
    'No quedó espacio para el grout ni para nivelar con lainas. Las placas quedaron apoyadas en un concreto disparejo.',
    'Hubo que picar cinco centímetros de cada pedestal, con cuidado de no dañar los pernos. Una conversación antes del vaciado lo habría evitado.',
  ], [('🧱', 'Pedestal vaciado <b class="nar">al ras</b>'), ('📏', '<b class="nar">Sin espacio</b> para grout ni lainas'), ('⛏️', 'Picar 5 cm en cada uno: <b class="nar">coordinar antes</b>')]),
  *ejercicio(1,
    'Pernos de <b class="nar">1"</b>. Grout de <b class="nar">50 mm</b>, placa de <b class="nar">25 mm</b>,<br>arandela de <b class="nar">5 mm</b> y tuerca de <b class="nar">25 mm</b>. Quieres <b class="nar">15 mm</b> de hilos libres.<br>¿Qué proyección mínima pides?',
    ['Ahora tú. Pernos de una pulgada. Grout de cincuenta milímetros, placa de veinticinco, arandela de cinco, y tuerca de veinticinco. Quieres quince milímetros de hilos libres.', '¿Qué proyección mínima pides?'],
    '50 + 25 + 5 + 25 + 15 = <b class="nar">120 mm</b> sobre el pedestal',
    ['Cincuenta, más veinticinco, más cinco, más veinticinco, más quince: ciento veinte milímetros.',
     'Esa es la proyección mínima sobre el pedestal. Compárala con la del plano antes del vaciado.']),
  *ejercicio(2,
    'El piso terminado es <b class="nar">±0.00</b> y el grout será de <b class="nar">5 cm</b>.<br>¿A qué nivel termina el pedestal?<br>¿Y qué entregas antes del vaciado?',
    ['Segundo ejercicio. El piso terminado es el nivel cero, y el grout será de cinco centímetros.', '¿A qué nivel termina el pedestal? ¿Y qué entregas antes del vaciado?'],
    'Pedestal a <b class="nar">−0.05</b> (5 cm bajo el piso terminado)<br>Entregas: <b class="nar">plantilla de pernos</b>, ejes, niveles y proyección revisados<br>y <b class="nar">fotos</b> antes de vaciar',
    ['El pedestal termina a menos cero cinco: cinco centímetros por debajo del piso terminado, para el grout.',
     'Y antes del vaciado entregas la plantilla de pernos, revisas ejes, niveles y proyección con el maestro de obra, y tomas fotos.']),
  faq([
    ('¿Perno en J o recto con tuerca abajo?', 'El que diga el plano; no se cambia.', '¿Perno en J o recto con placa abajo? El que diga el plano. Cada uno se calcula distinto: no se cambia por cuenta propia.'),
    ('¿Qué es el grout?', 'Mortero sin contracción bajo la placa.', '¿Qué es el grout? Un mortero especial, que no se encoge, y que llena el espacio bajo la placa base.'),
    ('¿Y si el perno quedó corrido?', 'Consulta: hay soluciones, pero las da el ingeniero.', '¿Y si un perno quedó corrido en el vaciado? Consulta al ingeniero. Hay soluciones, pero no se dobla ni se calienta por cuenta propia.'),
  ]),
  repaso([
    ('¿Dónde están las medidas de las zapatas?', 'En el cuadro de zapatas.'),
    ('¿Qué es la proyección del perno?', 'Lo que sale por encima del concreto.'),
    ('¿Por qué el pedestal queda más abajo?', 'Para el grout y la nivelación.'),
    ('¿Qué entregas antes del vaciado?', 'La plantilla de pernos.'),
  ]),
]

# ───────────── Clase 8 · Arquitectura para el metalero ─────────────
EXT['plan_c8'] = [
  respuesta('proyección con pernos de ⅝"', [
    'La respuesta del reto de la clase pasada: pernos de cinco octavos, grout de cuarenta y placa de diez.',
    'Arandela de unos cuatro milímetros, y tuerca de cinco octavos, de unos dieciséis.',
    'Cuarenta, más diez, más cuatro, más dieciséis: setenta. Con quince de hilos libres: unos ochenta y cinco milímetros de proyección mínima.',
  ], ['Parte', 'mm'],
    [['Grout', '40'], ['Placa', '10'], ['Arandela', '≈ 4'], ['Tuerca ⅝"', '≈ 16'], ['Hilos libres', '15'], ['Proyección mínima', '≈ 85']], lambda i: [1, 1, 2, 2, 2, 2][i]),
  ejemplo('Un cuadro <span class="nar">de vanos</span>', [
    'Antes de los errores, un cuadro de vanos, y cómo encuentras tu trabajo en él.',
    'P uno: puerta de cero noventa por dos diez, de madera. No es tuya. P tres: puerta metálica de uno por dos veinte. Esa sí.',
    'V dos: ventana de uno veinte por uno, alféizar de uno, de fierro con vidrio. También tuya. Y la V tres, de aluminio, para otro especialista.',
  ], ['Código', 'Ancho × alto', 'Alféizar', 'Material'],
    [['P1', '0.90 × 2.10', '—', 'Madera'], ['P3', '1.00 × 2.20', '—', '<b class="nar">Metálica</b>'], ['V2', '1.20 × 1.00', '1.00', '<b class="nar">Fierro y vidrio</b>'], ['V3', '1.50 × 1.20', '0.90', 'Aluminio']],
    lambda i: [1, 1, 2, 2][i], izq=300, der=300, tam=30),
  caso('el tarrajeo que faltaba', [
    'Caso de obra: el maestro fabricó las ventanas con las medidas del cuadro de vanos, sin ir a la obra.',
    'Los muros estaban en bruto. Cuando llegó, cada vano era tres centímetros más ancho. Las ventanas bailaban. Hubo que rellenar con mortero, y se notaba.',
    'El plano te dice qué y cómo. La medida para fabricar se toma en obra, y si el tarrajeo falta, se espera o se acuerda.',
  ], [('📄', 'Fabricó con el <b class="nar">cuadro de vanos</b>'), ('🧱', 'Muros en bruto: vanos <b class="nar">3 cm más anchos</b>'), ('📏', 'La medida para fabricar: <b class="nar">en obra</b>')]),
  *ejercicio(1,
    'Dos ventanas del cuadro de vanos:<br><b class="nar">V1: 1.20 × 1.00, alféizar 1.00</b> · <b class="nar">V4: 1.50 × 1.20, alféizar 0.90</b><br>¿A qué altura del piso termina cada una?',
    ['Ahora tú. Dos ventanas del cuadro de vanos. La V uno: uno veinte por uno, con alféizar de uno. Y la V cuatro: uno cincuenta por uno veinte, con alféizar de noventa.', '¿A qué altura del piso termina cada una?'],
    'V1: 1.00 + 1.00 = <b class="nar">2.00 m</b><br>V4: 0.90 + 1.20 = <b class="nar">2.10 m</b>',
    ['La V uno: alféizar de uno, más uno de alto: termina a dos metros.',
     'La V cuatro: noventa más uno veinte: termina a dos metros diez. Las dos alturas, para revisar el dintel.']),
  *ejercicio(2,
    'El plano dice puerta de <b class="nar">0.90 × 2.10</b> (vano terminado).<br>El muro está en bruto y el tarrajeo será de <b class="nar">1.5 cm</b> por lado (y arriba).<br>¿Cuánto mide hoy el vano y cómo procedes?',
    ['Segundo ejercicio. El plano dice puerta de cero noventa por dos diez, vano terminado. El muro está en bruto, y el tarrajeo será de uno y medio centímetros por lado, y arriba.', '¿Cuánto mide hoy el vano, y cómo procedes?'],
    'Hoy: ancho 90 + 3 = <b class="nar">0.93 m</b> · alto 210 + 1.5 = <b class="nar">2.115 m</b><br>Lo mejor: <b class="nar">medir con el tarrajeo hecho</b><br>Si no, acordar por escrito la medida final',
    ['Hoy el vano mide noventa y tres de ancho, y dos ciento quince de alto, aproximadamente.',
     'Lo mejor es medir cuando el tarrajeo esté hecho. Si no se puede esperar, acuerda por escrito con el maestro de obra la medida final.']),
  faq([
    ('¿Qué significa NTN o NPT en arquitectura?', 'Niveles de terreno y de piso terminado.', '¿Qué son N T N y N P T en arquitectura? Nivel de terreno natural, y nivel de piso terminado.'),
    ('¿Quién define el color?', 'La leyenda de acabados o el cliente, por escrito.', '¿Quién define el color de lo metálico? La leyenda de acabados del plano, o el cliente, por escrito.'),
    ('¿Y si la puerta abre contra un mueble?', 'Consulta antes: cambiar la mano es barato en el papel.', '¿Y si la puerta abre contra un mueble o una columna? Consulta antes de fabricar. En el papel, cambiarla es gratis.'),
  ]),
  repaso([
    ('¿Qué indica el arco de una puerta en planta?', 'Hacia dónde abre y dónde van las bisagras.'),
    ('¿Qué es el alféizar?', 'La altura del piso hasta donde empieza la ventana.'),
    ('¿Las medidas del plano son del vano en bruto?', 'Normalmente del vano terminado.'),
    ('¿Dónde se toma la medida para fabricar?', 'En la obra.'),
  ]),
]

# ───────────── Clase 9 · Tu croquis acotado ─────────────
EXT['plan_c9'] = [
  ejemplo('El croquis <span class="nar">en una lista</span>', [
    'Antes de los errores, todo lo que lleva un croquis acotado, en una lista para revisar antes de enviarlo.',
    'Medidas totales y parciales que sumen. Perfiles y espesores. Sentido de apertura.',
    'Acabado y color. Unidad de las medidas, fecha, y espacio para la firma o el "aprobado" del cliente.',
  ], ['Debe tener', '¿Lo tiene?'],
    [['Medidas totales (ancho × alto)', '☐'], ['Parciales que suman la total', '☐'], ['Perfiles y espesores', '☐'], ['Sentido de apertura', '☐'],
     ['Acabado y color', '☐'], ['Unidad, fecha y aprobación', '☐']],
    lambda i: [1, 1, 1, 1, 2, 2][i], izq=440, der=440, tam=29),
  caso('"yo pedí otro diseño"', [
    'Caso de taller: un portón entregado, bien hecho. El cliente dijo que él había pedido barrotes verticales, no planchas.',
    'No había croquis firmado. Solo una conversación de voz, y cada uno recordaba algo distinto. El taller terminó haciendo una hoja nueva.',
    'Un croquis con el "aprobado" del cliente, por escrito, cierra esa discusión antes de que empiece.',
  ], [('🗣️', 'Solo se habló <b class="nar">de palabra</b>'), ('😠', '"Yo pedí <b class="nar">otro diseño</b>"'), ('✅', 'Croquis con <b class="nar">aprobado por escrito</b>')]),
  *ejercicio(1,
    'Reja de <b class="nar">1 200 mm</b> de ancho, marco de <b class="nar">25 mm</b> por lado,<br><b class="nar">8 barrotes</b> de 12.7 mm, espacios iguales.<br>¿Qué separación libre escribes en el croquis?',
    ['Ahora tú. Una reja de mil doscientos milímetros de ancho, con marco de veinticinco por lado, y ocho barrotes de doce punto siete, con espacios iguales.', '¿Qué separación libre escribes en el croquis?'],
    'Libre: 1 200 − 2 × 25 = 1 150 · barrotes: 8 × 12.7 = 101.6<br>Espacios: 9 → (1 150 − 101.6) ÷ 9 ≈ <b class="nar">116.5 mm</b><br>Comprueba: 9 × 116.5 + 101.6 + 50 ≈ <b class="nar">1 200</b> ✓',
    ['Ancho libre: mil doscientos menos cincuenta, mil ciento cincuenta. Los barrotes ocupan ciento uno punto seis.',
     'Quedan nueve espacios: unos ciento dieciséis y medio milímetros cada uno. Y compruebas que todo sume mil doscientos.']),
  *ejercicio(2,
    'Un croquis dice: ancho total <b class="nar">1 200</b>, parciales <b class="nar">400 + 400 + 390</b>.<br>No dice unidad, ni color, ni hacia dónde abre.<br>¿Qué corriges antes de enviarlo?',
    ['Segundo ejercicio. Un croquis dice ancho total mil doscientos, y parciales de cuatrocientos, cuatrocientos y trescientos noventa. No dice unidad, ni color, ni hacia dónde abre.', '¿Qué corriges antes de enviarlo?'],
    'Parciales: 400 + 400 + 390 = <b class="nar">1 190</b> ≠ 1 200 → corrige un tramo<br>Agrega: <b class="nar">unidad</b> (mm), <b class="nar">color y acabado</b>, <b class="nar">sentido de apertura</b><br>Y la fecha y el espacio para el aprobado',
    ['Los parciales suman mil ciento noventa: no dan la total. Corrige el tramo que falla.',
     'Y agrega la unidad, el color y acabado, el sentido de apertura, la fecha y el espacio para el aprobado.']),
  faq([
    ('¿Puedo hacer el croquis en el celular?', 'Sí: foto de papel cuadriculado o el módulo de InnovApp.', '¿Puedo hacer el croquis en el celular? Sí: una foto clara de tu dibujo en papel cuadriculado, o el diseño del módulo de Carpintería Metálica.'),
    ('¿Y si el cliente cambia algo después?', 'Es un cambio: nuevo croquis y nuevo precio.', '¿Y si el cliente cambia algo después de aprobar? Es un cambio: nuevo croquis, nuevo precio si corresponde, y nuevo aprobado.'),
    ('¿Milímetros o centímetros?', 'Cualquiera, pero una sola, escrita.', '¿Milímetros o centímetros? Cualquiera, pero una sola en todo el croquis, y escrita.'),
  ]),
  repaso([
    ('¿Para qué sirve un croquis?', 'Es el acuerdo con el cliente y la guía del taller.'),
    ('¿Qué deben hacer las parciales?', 'Sumar la total.'),
    ('¿Qué puede ser aproximado?', 'El dibujo; las medidas escritas no.'),
    ('¿Qué pides al enviarlo?', 'Que el cliente responda aprobado.'),
  ]),
]
