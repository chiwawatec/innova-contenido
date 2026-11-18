"""Ampliación de «Estructuras Metálicas» (≈8 min por clase). Misma receta que Naves, Techos y Soldadura."""
from naves_ext import insertar, caja, ejercicio, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · Acero y perfiles ─────────────
EXT['est_c1'] = [
  ejemplo('Pesos que <span class="nar">conviene saber</span>', [
    'Antes de los errores, una tabla de tubos cuadrados que se usan mucho, con su peso aproximado por metro.',
    'Cincuenta por cincuenta por dos milímetros: unos tres kilos por metro. Setenta y cinco por setenta y cinco por tres: casi siete.',
    'Cien por cien por tres: unos nueve. Y el mismo tubo de cien, en cuatro milímetros: doce. Fíjate otra vez: el espesor manda en el peso.',
    'Son valores de referencia. El número exacto lo das con el catálogo de tu proveedor, o con el catálogo de perfiles de InnovApp.',
  ], ['Tubo cuadrado', 'Peso aproximado'],
    [['50 × 50 × 2 mm', '≈ 3.0 kg/m'], ['75 × 75 × 3 mm', '≈ 6.8 kg/m'], ['100 × 100 × 3 mm', '≈ 9.1 kg/m'], ['100 × 100 × 4 mm', '≈ 12.0 kg/m'], ['150 × 150 × 4.5 mm', '≈ 20.2 kg/m']],
    lambda i: [1, 1, 2, 2, 3][i], izq=440, der=440),
  ejemplo('Planchas: <span class="nar">7.85 kg por m² y por mm</span>', [
    'Ahora, la regla de las planchas aplicada a tres piezas de todos los días.',
    'Una placa de veinticinco por veinticinco centímetros, en nueve milímetros: cero punto cero seis dos cinco metros cuadrados, por nueve, por siete punto ochenta y cinco. Unos cuatro kilos y medio.',
    'Una plancha entera de uno veinte por dos cuarenta, en tres milímetros: dos punto ochenta y ocho metros cuadrados. Unos sesenta y ocho kilos. Pide ayuda para cargarla.',
  ], ['Pieza', 'Cálculo', 'Peso'],
    [['Placa 25 × 25 cm, 9 mm', '0.0625 × 9 × 7.85', '≈ 4.4 kg'], ['Plancha 1.20 × 2.40 m, 3 mm', '2.88 × 3 × 7.85', '≈ 68 kg'], ['Plancha estriada 4.5 mm', 'por m², con estrías', '≈ 37 kg/m²']],
    lambda i: [1, 2, 2][i], izq=220, der=220),
  caso('“tubo de cuatro”', [
    'Caso de obra: un maestro pidió por teléfono "tubo de cuatro" para las columnas de una terraza. No dijo el espesor.',
    'Llegó tubo de cuatro pulgadas, pero de uno y medio milímetros: tubo de carpintería, para rejas. Para columnas que cargan, no servía.',
    'Devolverlo costó un día y el flete. Pide siempre con tres datos: medida, espesor y largo de la barra. Por escrito.',
  ], [('📞', 'Pidió <b class="nar">“tubo de 4”</b>, sin espesor'), ('🪶', 'Llegó tubo de <b class="nar">1.5 mm</b>: de carpintería'), ('📝', 'Pide por escrito: <b class="nar">medida · espesor · largo</b>')]),
  *ejercicio(1,
    'Una terraza lleva <b class="nar">8 columnas de 2.50 m</b> en tubo de 100 × 100 × 4 mm (≈ 12 kg/m).<br>¿Cuántos kilos son y cuántas barras de 6 m compras?',
    ['Ahora tú. Una terraza lleva ocho columnas de dos metros cincuenta, en tubo de cien por cien por cuatro milímetros, que pesa unos doce kilos por metro.', '¿Cuántos kilos son, y cuántas barras de seis metros compras?'],
    'Largo: 8 × 2.50 = <b class="nar">20 m</b> → 20 × 12 = <b class="nar">240 kg</b><br>Por barra salen <b class="nar">2 columnas</b> (sobra 1 m) → <b class="nar">4 barras</b>',
    ['Ocho por dos cincuenta: veinte metros. Por doce kilos: doscientos cuarenta kilos.',
     'De cada barra de seis metros salen dos columnas, y sobra un metro. Ocho columnas: cuatro barras. Y esos cuatro metros sobrantes, guárdalos para cartelas.']),
  *ejercicio(2,
    'Las 8 columnas llevan placas base de <b class="nar">25 × 25 cm en 12 mm</b>.<br>¿Cuánto pesan las placas y cuánto agregas de margen (5 %) a todo el pedido?',
    ['Segundo ejercicio. Las ocho columnas llevan placas base de veinticinco por veinticinco centímetros, en doce milímetros.', '¿Cuánto pesan las placas, y cuánto agregas de margen, cinco por ciento, a todo el pedido?'],
    'Una placa: 0.0625 × 12 × 7.85 = <b class="nar">5.9 kg</b> → 8 placas ≈ <b class="nar">47 kg</b><br>Total: 240 + 47 = 287 kg + 5 % ≈ <b class="nar">301 kg</b>',
    ['Una placa: cero punto cero seis dos cinco, por doce, por siete punto ochenta y cinco. Unos cinco punto nueve kilos. Las ocho: unos cuarenta y siete.',
     'Con las columnas, doscientos ochenta y siete kilos. Más cinco por ciento de margen: unos trescientos un kilos.']),
  faq([
    ('¿Cómo sé si es A36 o A500?', 'Por el certificado del proveedor, no a simple vista.', '¿Cómo sé si un perfil es A treinta y seis o A quinientos? A simple vista, no se puede. Lo dice el certificado del proveedor. Pídelo al comprar.'),
    ('¿Compro por kilo o por barra?', 'Se cotiza por kilo, pero se piensa en barras.', '¿Compro por kilo o por barra? El precio suele ir por kilo, pero el corte se piensa en barras, para no botar sobrantes.'),
    ('¿Puedo bajar el espesor para abaratar?', 'Solo si el ingeniero lo verifica.', '¿Puedo usar un espesor menor para abaratar? Solo si el ingeniero lo verifica. Pesar menos es aguantar menos.'),
  ]),
  repaso([
    ('¿Cuánto pesa un metro cuadrado de plancha de un milímetro?', 'Siete punto ochenta y cinco kilos.'),
    ('¿Qué tres datos pides al comprar un tubo?', 'Medida, espesor y largo de la barra.'),
    ('¿Qué acero tienen los tubos estructurales?', 'A quinientos grado B.'),
    ('¿Cuánto margen agregas al pedido?', 'De tres a cinco por ciento.'),
  ]),
]

# ───────────── Clase 2 · Vigas y columnas ─────────────
EXT['est_c2'] = [
  ejemplo('Carga por metro cuadrado, <span class="nar">según el uso</span>', [
    'Antes de los errores, la carga total por metro cuadrado según el uso, sumando unos cien kilos de carga muerta del mezanine.',
    'Vivienda: doscientos de viva, más cien: trescientos. Oficinas: doscientos cincuenta más cien: trescientos cincuenta.',
    'Almacenaje: quinientos más cien: seiscientos. Casi el doble que una oficina.',
    'Y un techo liviano, plano o casi plano: la norma pide como mínimo cien kilos de carga viva, para la gente que sube a darle mantenimiento.',
  ], ['Uso', 'Carga viva (E.020)', 'Total con 100 kg de muerta'],
    [['Vivienda', '200 kg/m²', '300 kg/m²'], ['Oficinas', '250 kg/m²', '350 kg/m²'], ['Almacenaje', '500 kg/m²', '600 kg/m²'], ['Techo plano (mantenimiento)', '100 kg/m²', '—']],
    lambda i: [1, 1, 2, 3][i], izq=220, der=220),
  ejemplo('Si el mezanine se vuelve <span class="nar">almacén</span>', [
    'Ahora mira lo que pasa en las columnas si el mezanine de oficina se usa como almacén.',
    'Columna de esquina, tres metros cuadrados: de mil cincuenta kilos pasa a mil ochocientos.',
    'Columna del medio, seis metros cuadrados: de dos mil cien pasa a tres mil seiscientos. Setenta por ciento más, sin que nadie lo calcule.',
  ], ['Columna', 'Área', 'Oficina (350)', 'Almacén (600)'],
    [['Esquina', '3 m²', '1 050 kg', '1 800 kg'], ['Medio', '6 m²', '2 100 kg', '3 600 kg']],
    lambda i: i + 1, izq=260, der=260, tam=32),
  caso('el piso que vibraba', [
    'Caso de obra: un mezanine se hizo para oficina. A los meses, el dueño lo llenó de cajas de mercadería.',
    'Las viguetas empezaron a bajar, y el piso vibraba cada vez que alguien caminaba. Hubo que reforzar todo, con el depósito lleno.',
    'Por eso, en la cotización y en el acta escribe el uso y la carga para la que se diseñó. Y explícaselo al cliente.',
  ], [('🏢', 'Diseñado para <b class="nar">oficina</b>'), ('📦', 'Usado como <b class="nar">almacén</b>: viguetas bajaron'), ('📝', 'Escribe <b class="nar">uso y carga</b> en la cotización y el acta')]),
  *ejercicio(1,
    'Predimensiona con la regla <b class="nar">peralte ≈ luz ÷ 20</b>:<br>a) Viga principal de <b class="nar">6 m</b> · b) Vigueta de <b class="nar">2.50 m</b>',
    ['Ahora tú. Predimensiona con la regla del peralte, igual a la luz entre veinte.', 'Una viga principal de seis metros, y una vigueta de dos metros cincuenta.'],
    'a) 6 000 ÷ 20 = <b class="nar">300 mm</b> (una viga de unas 12 pulgadas)<br>b) 2 500 ÷ 20 = <b class="nar">125 mm</b> (un canal de 5 o 6 pulgadas)<br>El ingeniero confirma el perfil final',
    ['La viga de seis metros: seis mil entre veinte, trescientos milímetros. Una viga de unas doce pulgadas.',
     'La vigueta: dos mil quinientos entre veinte, ciento veinticinco. Un canal de cinco o seis pulgadas. Y el ingeniero confirma el perfil final.']),
  *ejercicio(2,
    'Con el límite <b class="nar">luz ÷ 360</b>, ¿cuánto puede bajar el piso<br>en una viga de <b class="nar">5 m</b> y en una de <b class="nar">6 m</b>?',
    ['Segundo ejercicio. Con el límite de la luz entre trescientos sesenta, ¿cuánto puede bajar el piso en una viga de cinco metros, y en una de seis?'],
    '5 m: 5 000 ÷ 360 ≈ <b class="nar">14 mm</b><br>6 m: 6 000 ÷ 360 ≈ <b class="nar">17 mm</b>',
    ['Cinco mil entre trescientos sesenta: unos catorce milímetros.',
     'Seis mil entre trescientos sesenta: unos diecisiete milímetros. Si baja más, se nota y vibra.']),
  faq([
    ('¿Puedo poner el tubo rectangular acostado?', 'No en vigas: siempre parado, con el lado alto vertical.', '¿Puedo poner un tubo rectangular acostado como viga? No. Siempre parado, con el lado más alto en vertical.'),
    ('¿La regla L/20 reemplaza el cálculo?', 'No: es para empezar y cotizar.', '¿La regla de la luz entre veinte reemplaza el cálculo? No. Sirve para empezar, cotizar y conversar con el ingeniero.'),
    ('¿Por qué tubos en columnas?', 'Son igual de rígidos en las dos direcciones.', '¿Por qué se prefieren tubos en las columnas? Porque son igual de rígidos en las dos direcciones, y se pandean menos.'),
  ]),
  repaso([
    ('¿Qué es la carga viva?', 'Lo que va y viene: personas, muebles, mercadería.'),
    ('¿Qué importa más en una viga?', 'Su altura, el peralte.'),
    ('¿Cómo falla casi siempre una columna?', 'Por pandeo, doblándose de lado.'),
    ('¿Cuánta carga viva tiene un almacén?', 'Quinientos kilos por metro cuadrado.'),
  ]),
]

# ───────────── Clase 3 · Conexiones empernadas ─────────────
EXT['est_c3'] = [
  ejemplo('Agujeros y distancias, <span class="nar">perno por perno</span>', [
    'Antes de los errores, la tabla completa para los pernos que más vas a usar.',
    'Cinco octavos: agujero de unos diecisiete y medio milímetros, cuarenta y ocho entre agujeros como mínimo, y veinticuatro al borde.',
    'Tres cuartos: veinte punto seis, cincuenta y siete, y unos veintinueve. Siete octavos: veintitrés punto ocho, sesenta y siete, y treinta y tres.',
    'Y una pulgada: veintisiete, setenta y seis, y treinta y ocho. Recuerda: son mínimos prácticos. En el taller deja un poco más, para que entre la llave.',
  ], ['Perno', 'Agujero estándar', 'Entre agujeros (3d)', 'Al borde (≈1.5d)'],
    [['5/8"', '≈ 17.5 mm', '48 mm', '24 mm'], ['3/4"', '≈ 20.6 mm', '57 mm', '29 mm'], ['7/8"', '≈ 23.8 mm', '67 mm', '33 mm'], ['1"', '≈ 27.0 mm', '76 mm', '38 mm']],
    lambda i: [1, 2, 2, 3][i], izq=200, der=200),
  caso('agujeros con soplete', [
    'Caso de obra: en la obra, dos agujeros de una conexión no coincidían. El ayudante los agrandó con el soplete.',
    'El supervisor lo vio: agujeros ovalados y bordes quemados. Mandó cambiar la plancha completa, y además pidió revisar todas las demás.',
    'La solución estaba antes: plantilla para marcar, y taladro. Y si algo no coincide en obra, se consulta, no se quema.',
  ], [('🔥', 'Agujeros agrandados <b class="nar">con soplete</b>'), ('❌', 'Plancha <b class="nar">rechazada</b> y revisión de todo'), ('📐', 'Plantilla + taladro; en obra, <b class="nar">se consulta</b>')]),
  *ejercicio(1,
    'Un perno A325 de <b class="nar">3/4"</b> mide <b class="nar">2½"</b> de largo.<br>Con el método de giro de tuerca, ¿cuánto giras después del ajuste a tope?',
    ['Ahora tú. Un perno A trescientos veinticinco de tres cuartos mide dos pulgadas y media de largo.', 'Con el método de giro de tuerca, ¿cuánto giras después del ajuste a tope?'],
    '4 diámetros = 4 × ¾" = <b class="nar">3"</b> · el perno mide 2½": menos de 4d<br>Giro: <b class="nar">⅓ de vuelta</b> = <b class="nar">120°</b> (marca la tuerca antes)',
    ['Cuatro diámetros de tres cuartos son tres pulgadas. El perno mide dos y media: menos de cuatro diámetros.',
     'Entonces, un tercio de vuelta: ciento veinte grados. Marca la tuerca y la plancha antes de girar, para saber cuánto avanzaste.']),
  *ejercicio(2,
    'Plancha con <b class="nar">4 pernos de 5/8"</b> en dos filas.<br>Entre agujeros dejas <b class="nar">75 mm</b> y al borde <b class="nar">35 mm</b>.<br>¿Qué ancho mínimo tiene la plancha?',
    ['Segundo ejercicio. Una plancha lleva cuatro pernos de cinco octavos, en dos filas.', 'Entre agujeros dejas setenta y cinco milímetros, y al borde treinta y cinco. ¿Qué ancho mínimo tiene la plancha?'],
    '35 + 75 + 35 = <b class="nar">145 mm</b> → usa platina de <b class="nar">150 mm</b> (6")',
    ['Treinta y cinco, más setenta y cinco, más treinta y cinco: ciento cuarenta y cinco milímetros.',
     'Usa una platina de ciento cincuenta, seis pulgadas, que es medida comercial.']),
  faq([
    ('¿Puedo soldar la tuerca para que no se afloje?', 'No: usa la arandela y el apriete correcto.', '¿Puedo soldar la tuerca para que no se afloje? No. Arruina el perno. Usa la arandela y el apriete correcto.'),
    ('¿Hay A325 galvanizados?', 'Sí, con su tuerca y arandela galvanizadas.', '¿Existen pernos A trescientos veinticinco galvanizados? Sí, con su tuerca y su arandela también galvanizadas, compradas juntas.'),
    ('¿Reutilizo un perno pretensado?', 'No: se cambia por uno nuevo.', '¿Puedo reutilizar un perno que ya fue pretensado? No. Se cambia por uno nuevo.'),
  ]),
  repaso([
    ('¿Qué perno va en vigas y columnas?', 'El A trescientos veinticinco.'),
    ('¿Cuánto mide el agujero estándar?', 'El diámetro del perno más un dieciseisavo de pulgada.'),
    ('¿Cuánto entre agujeros?', 'Por lo menos tres veces el diámetro.'),
    ('¿Con qué se hacen los agujeros?', 'Con taladro, nunca con soplete.'),
  ]),
]

# ───────────── Clase 4 · El entrepiso ─────────────
EXT['est_c4'] = [
  respuesta('plancha de 4 pernos de ¾"', [
    'La respuesta del reto de la clase pasada: una plancha con cuatro pernos de tres cuartos.',
    'El agujero: trece dieciseisavos, unos veinte punto seis milímetros. Entre agujeros, tres diámetros: cincuenta y siete como mínimo. Usamos setenta y cinco, para la llave.',
    'Al borde, una vez y media el diámetro: unos veintinueve. Dejamos treinta y cinco. Así la plancha sale de unos ciento cuarenta y cinco por ciento cuarenta y cinco.',
  ], ['Dato', 'Mínimo', 'Usamos'],
    [['Agujero', '20.6 mm', '20.6 mm'], ['Entre agujeros', '57 mm', '75 mm'], ['Al borde', '29 mm', '35 mm']], lambda i: [1, 1, 2][i]),
  ejemplo('Cuánto pesa <span class="nar">cada piso</span>', [
    'Antes de los errores, el peso de cada tipo de piso por metro cuadrado. Va directo a la carga muerta.',
    'Tablero OSB o fenólico de dieciocho milímetros: unos doce kilos. Rejilla metálica: entre veinticinco y cuarenta, según el modelo.',
    'Plancha estriada de cuatro punto cinco: unos treinta y siete. Y placa colaborante con concreto: unos doscientos kilos o más, según el espesor de la losa.',
    'Del tablero a la placa colaborante, el piso pesa quince veces más. Por eso nunca se cambia el piso sin avisar al ingeniero.',
  ], ['Piso', 'Peso aproximado'],
    [['Tablero OSB o fenólico 18 mm', '≈ 12 kg/m²'], ['Rejilla metálica (grating)', '≈ 25 – 40 kg/m²'], ['Plancha estriada 4.5 mm', '≈ 37 kg/m²'], ['Placa colaborante + concreto', '≈ 200 kg/m² o más']],
    lambda i: [1, 1, 2, 3][i], izq=360, der=360),
  caso('la junta en el aire', [
    'Caso de obra: para aprovechar los tableros, el instalador dejó dos juntas entre viguetas, sin apoyo debajo.',
    'Al primer escritorio con una persona sentada, el borde del tablero bajó y se rajó. Hubo que soldar viguetas de relleno debajo y cambiar dos tableros.',
    'Regla: cada junta cae sobre una vigueta. Si el tablero no llega, se agrega un apoyo, no se deja en el aire.',
  ], [('🪵', 'Juntas de tablero <b class="nar">sin apoyo</b>'), ('💥', 'El borde <b class="nar">bajó y se rajó</b>'), ('✅', 'Cada junta <b class="nar">sobre una vigueta</b>')]),
  *ejercicio(1,
    'El mezanine de 4 × 6 m tiene <b class="nar">dos lados contra muros</b>.<br>Los otros dos llevan baranda, menos <b class="nar">1 m</b> de la escalera.<br>¿Cuántos metros de baranda y cuántos parantes, si van cada <b class="nar">1.20 m</b>?',
    ['Ahora tú. El mezanine de cuatro por seis tiene dos lados contra muros. Los otros dos llevan baranda, menos un metro donde llega la escalera.', '¿Cuántos metros de baranda, y cuántos parantes, si van cada metro veinte?'],
    'Baranda: 6 + 4 − 1 = <b class="nar">9 m</b><br>Espacios: 9 ÷ 1.20 = 7.5 → <b class="nar">8 espacios</b> → <b class="nar">9 parantes</b> (+1 en la esquina si cambia de lado)',
    ['Seis más cuatro, menos el metro de la escalera: nueve metros de baranda.',
     'Nueve entre uno veinte da siete y medio. Redondeas a ocho espacios: nueve parantes. Y revisa que haya uno firme en la esquina y a cada lado de la escalera.']),
  *ejercicio(2,
    '¿Cuántos tableros de <b class="nar">1.22 × 2.44 m</b> compras<br>para los <b class="nar">24 m²</b> del mezanine, con 10 % de desperdicio?',
    ['Segundo ejercicio. ¿Cuántos tableros de uno veintidós por dos cuarenta y cuatro compras para los veinticuatro metros cuadrados del mezanine, con diez por ciento de desperdicio?'],
    'Un tablero: 1.22 × 2.44 = <b class="nar">2.98 m²</b><br>24 × 1.10 = 26.4 m² ÷ 2.98 = 8.9 → <b class="nar">9 tableros</b>',
    ['Un tablero cubre uno veintidós por dos cuarenta y cuatro: dos punto noventa y ocho metros cuadrados.',
     'Veinticuatro más diez por ciento: veintiséis punto cuatro. Entre dos noventa y ocho: ocho punto nueve. Compras nueve tableros.']),
  faq([
    ('¿OSB o fenólico?', 'Fenólico resiste mejor la humedad; OSB es más barato.', '¿OSB o fenólico? El fenólico resiste mejor la humedad y el tránsito. El OSB es más barato, para zonas secas.'),
    ('¿La baranda puede ser de tubo delgado?', 'Debe aguantar el empuje de una persona: parantes firmes.', '¿La baranda puede ser de tubo delgado? Lo que importa es que aguante el empuje de una persona. Parantes firmes y bien soldados o empernados.'),
    ('¿Y la escalera del mezanine?', 'Con la regla de oro y su propia baranda.', '¿Y la escalera? Con la regla de oro del curso de Carpintería Metálica, y su propia baranda.'),
  ]),
  repaso([
    ('¿Cada cuánto van las viguetas con tablero de dieciocho milímetros?', 'Entre cuarenta y sesenta centímetros.'),
    ('¿Dónde caen las juntas del tablero?', 'Siempre sobre una vigueta.'),
    ('¿Qué alto mínimo tiene la baranda?', 'Un metro.'),
    ('¿Para qué sirve el rodapié?', 'Para que no caigan objetos sobre la gente de abajo.'),
  ]),
]

# ───────────── Clase 5 · Corte y tolerancias ─────────────
EXT['est_c5'] = [
  respuesta('mezanine de 3 × 5 m', [
    'La respuesta del reto de la clase pasada: un mezanine de tres por cinco, con tablero de dieciocho milímetros.',
    'Las viguetas de tres metros, a lo largo de los cinco. Como máximo cada sesenta centímetros: cinco mil entre seiscientos da ocho punto tres. Redondeamos a nueve espacios: diez viguetas, cada cincuenta y seis centímetros.',
    'El piso: quince metros cuadrados por doce kilos, unos ciento ochenta kilos de tablero.',
  ], ['Dato', 'Resultado'], [['Espacios', '9 (≈ 56 cm)'], ['Viguetas de 3 m', '10'], ['Peso del tablero', '≈ 180 kg']], lambda i: [1, 1, 2][i]),
  ejemplo('Las tolerancias <span class="nar">en una tabla</span>', [
    'Antes de los errores, las tolerancias de la clase en una sola tabla, con ejemplos.',
    'Una pieza que apoya a tope: más o menos un milímetro. Una viga de tres metros ochenta: más o menos dos.',
    'Una viga de doce metros: más o menos tres. Y la rectitud de una columna de tres metros: un milésimo, tres milímetros como máximo.',
  ], ['Caso', 'Tolerancia', 'Ejemplo'],
    [['Extremos a tope (contacto)', '± 1 mm', 'Columna sobre placa'], ['Pieza hasta 9 m', '± 2 mm', 'Viga de 3.83 m'], ['Pieza de más de 9 m', '± 3 mm', 'Viga de 12 m'],
     ['Rectitud de columna', 'L ÷ 1 000', '3 m → 3 mm']],
    lambda i: [1, 1, 2, 2][i], izq=240, der=240),
  caso('las dos winchas', [
    'Caso de obra: el cortador usaba una wincha y el armador otra. Las vigas llegaron a la obra y no entraban entre las columnas.',
    'Compararon las winchas: dos milímetros de diferencia en tres metros. Sumados al ancho del disco, las piezas quedaban justas o largas.',
    'Desde ese día, una sola wincha de referencia para el taller, y las demás comparadas con ella cada semana.',
  ], [('📏', 'Dos winchas: <b class="nar">2 mm de diferencia</b>'), ('🚫', 'Las vigas <b class="nar">no entraban</b>'), ('✅', 'Una <b class="nar">wincha de referencia</b> para todo el taller')]),
  *ejercicio(1,
    'Un marco mide <b class="nar">2 × 3 m</b>.<br>¿Cuánto deben medir sus diagonales si está a escuadra?<br>Mides 3.61 m y 3.59 m: ¿qué haces?',
    ['Ahora tú. Un marco mide dos por tres metros. ¿Cuánto deben medir sus diagonales si está a escuadra?', 'Y si mides tres sesenta y uno y tres cincuenta y nueve, ¿qué haces?'],
    'Diagonal: √(2² + 3²) = √13 ≈ <b class="nar">3.606 m</b><br>3.61 y 3.59: <b class="nar">2 cm de diferencia</b> → no está a escuadra<br>Empuja la esquina de la diagonal larga, <b class="nar">antes de soldar completo</b>',
    ['La diagonal es la raíz de dos al cuadrado más tres al cuadrado: raíz de trece, tres metros sesenta y uno, más o menos.',
     'Si mides tres sesenta y uno y tres cincuenta y nueve, hay dos centímetros de diferencia: no está a escuadra. Empuja por la diagonal larga hasta igualarlas, antes de soldar completo.']),
  *ejercicio(2,
    'Entre caras de las vigas hay <b class="nar">2 840 mm</b>. Dejas <b class="nar">5 mm</b> de holgura por lado.<br>El disco come <b class="nar">3 mm</b>. ¿A cuánto cortas cada vigueta<br>y cuántas salen de una barra de 6 m?',
    ['Segundo ejercicio. Entre caras de las vigas hay dos mil ochocientos cuarenta milímetros. Dejas cinco de holgura por lado, y el disco se come tres.', '¿A cuánto cortas cada vigueta, y cuántas salen de una barra de seis metros?'],
    'Corte: 2 840 − 5 − 5 = <b class="nar">2 830 mm</b><br>2 piezas: 2 × 2 830 + 2 × 3 = 5 666 mm → <b class="nar">2 por barra</b>, sobran <b class="nar">334 mm</b>',
    ['Dos mil ochocientos cuarenta, menos cinco y cinco: dos mil ochocientos treinta.',
     'Dos piezas, más dos cortes de tres: cinco mil seiscientos sesenta y seis. Salen dos por barra, y sobran trescientos treinta y cuatro milímetros, que sirven para cartelas.']),
  faq([
    ('¿Tronzadora o sierra de cinta?', 'Cinta para series y precisión; tronzadora para cortes sueltos.', '¿Tronzadora o sierra de cinta? La cinta para series y cortes precisos. La tronzadora, para cortes sueltos.'),
    ('¿Cada cuánto cambio el disco?', 'Cuando se gasta y empieza a desviarse.', '¿Cada cuánto se cambia el disco? Cuando se gasta y empieza a desviar el corte. Un disco gastado te come la tolerancia.'),
    ('¿Las tolerancias son ley?', 'Son una referencia; manda lo que diga el plano.', '¿Las tolerancias son obligatorias? Son una referencia muy usada. Si el plano o el contrato dicen otra cosa, manda el plano.'),
  ]),
  repaso([
    ('¿Por qué lado de la línea cortas?', 'Por el lado de afuera.'),
    ('¿Qué tolerancia tiene una pieza de hasta nueve metros?', 'Más o menos dos milímetros.'),
    ('¿Cómo controlas la escuadra?', 'Midiendo que las dos diagonales sean iguales.'),
    ('¿Qué haces antes de cortar en serie?', 'Cortar una pieza de prueba y medirla.'),
  ]),
]

# ───────────── Clase 6 · Pintura ─────────────
EXT['est_c6'] = [
  ejemplo('El rendimiento <span class="nar">de tres fichas</span>', [
    'Antes de los errores, la fórmula del rendimiento con tres fichas distintas. Sólidos por diez, entre micras.',
    'Una base con cincuenta por ciento de sólidos a cincuenta micras: diez metros cuadrados por litro. Treinta y ocho por galón, en teoría.',
    'Un esmalte con cuarenta por ciento a cuarenta micras: también diez. Y un epóxico con setenta por ciento a cien micras: solo siete.',
    'En la práctica se pierde pintura en la brocha, en el viento y en los bordes. Como en la clase: calcula con un setenta por ciento del teórico.',
  ], ['Pintura', 'Sólidos · micras', 'Teórico', 'Práctico (70 %)'],
    [['Base anticorrosiva', '50 % · 50 µm', '10 m²/L', '≈ 26 m²/galón'], ['Esmalte', '40 % · 40 µm', '10 m²/L', '≈ 26 m²/galón'], ['Epóxico', '70 % · 100 µm', '7 m²/L', '≈ 18 m²/galón']],
    lambda i: [1, 2, 2][i], izq=200, der=200),
  caso('la pintura que se pelaba', [
    'Caso de obra: para avanzar, pintaron una estructura a las seis de la mañana, cerca del mar, con el acero frío y húmedo.',
    'A la semana, la pintura se levantaba en ampollas y se pelaba con la uña. Debajo, el acero ya tenía óxido.',
    'Se pintó sobre la película de agua del rocío. Pinta cuando el acero esté por lo menos tres grados sobre el punto de rocío, y con humedad de menos de ochenta y cinco por ciento.',
  ], [('🌫️', 'Pintado de madrugada, con <b class="nar">rocío</b>'), ('🫧', '<b class="nar">Ampollas</b> y pintura que se pela'), ('🌡️', 'Acero <b class="nar">≥ 3 °C</b> sobre el rocío · HR &lt; 85 %')]),
  *ejercicio(1,
    'Una estructura tiene <b class="nar">70 m²</b>. La base tiene <b class="nar">60 % de sólidos</b> y se da a <b class="nar">40 µm</b> por mano.<br>Son <b class="nar">2 manos</b>. ¿Cuántos galones compras? (usa 70 % del teórico)',
    ['Ahora tú. Una estructura tiene setenta metros cuadrados. La base tiene sesenta por ciento de sólidos, y se da a cuarenta micras por mano. Son dos manos.', '¿Cuántos galones compras? Usa el setenta por ciento del rendimiento teórico.'],
    'Teórico: 60 × 10 ÷ 40 = <b class="nar">15 m²/L</b> × 3.79 ≈ 57 m²/galón<br>Práctico: 57 × 0.70 ≈ <b class="nar">40 m²/galón</b><br>70 × 2 = 140 m² ÷ 40 = 3.5 → <b class="nar">4 galones</b>',
    ['Teórico: sesenta por diez, entre cuarenta: quince metros cuadrados por litro. Por tres punto setenta y nueve: unos cincuenta y siete por galón.',
     'Práctico, al setenta por ciento: unos cuarenta. Setenta metros por dos manos son ciento cuarenta. Entre cuarenta: tres y medio. Compras cuatro galones.']),
  *ejercicio(2,
    'Son las 7 a. m. El aire está a <b class="nar">20 °C</b>, el punto de rocío es <b class="nar">16 °C</b><br>y el acero está a <b class="nar">17 °C</b>. ¿Puedes pintar?',
    ['Segundo ejercicio. Son las siete de la mañana. El aire está a veinte grados, el punto de rocío es dieciséis, y el acero está a diecisiete.', '¿Puedes pintar?'],
    'El acero debe estar a <b class="nar">16 + 3 = 19 °C</b> o más<br>Está a 17 °C → <b class="nar">no pintes todavía</b>: espera que el sol lo caliente',
    ['El acero debe estar por lo menos a dieciséis más tres: diecinueve grados.',
     'Está a diecisiete: todavía no. Espera a que el sol lo caliente, y vuelve a medir.']),
  faq([
    ('¿Cómo mido el espesor seco?', 'Con un medidor de espesores de película seca.', '¿Cómo mido el espesor seco? Con un medidor de espesores de película, que se apoya sobre la pintura y te da las micras.'),
    ('¿Puedo pintar con brocha?', 'Sí, en piezas chicas; pistola rinde y uniforma más.', '¿Puedo pintar con brocha? Sí, en piezas chicas y retoques. Con pistola rinde más y el espesor sale más parejo.'),
    ('¿Diluyo para que rinda?', 'No: solo lo que diga la ficha.', '¿Diluyo para que rinda más? No. Solo lo que diga la ficha. Diluir de más baja la protección.'),
  ]),
  repaso([
    ('¿Cómo se calcula el rendimiento teórico?', 'Sólidos por diez, entre las micras.'),
    ('¿Cuántas micras tiene el sistema típico de interiores?', 'Unas ciento ochenta.'),
    ('¿Con qué humedad no pintas?', 'Con más de ochenta y cinco por ciento.'),
    ('¿Una mano gruesa o varias delgadas?', 'Varias delgadas.'),
  ]),
]

# ───────────── Clase 7 · Montaje ─────────────
EXT['est_c7'] = [
  ejemplo('Diagonales <span class="nar">para replantear</span>', [
    'Antes de los errores, las diagonales para replantear las plantas más comunes. Raíz del ancho al cuadrado más el largo al cuadrado.',
    'Cuatro por seis, nuestro mezanine: siete metros veintiuno. Cinco por ocho: nueve cuarenta y tres.',
    'Y seis por diez: once sesenta y seis. Las dos diagonales tienen que coincidir, con una diferencia de pocos milímetros.',
  ], ['Planta', 'Diagonal'],
    [['4 × 6 m', '7.21 m'], ['5 × 8 m', '9.43 m'], ['6 × 10 m', '11.66 m']],
    lambda i: [1, 2, 2][i], izq=560, der=560, tam=34),
  ejemplo('Plomo: <span class="nar">1 en 500</span>', [
    'Y el plomo de las columnas, con la referencia de uno en quinientos.',
    'Columna de tres metros: seis milímetros. De cuatro metros: ocho.',
    'Y de seis metros: doce. Mídelo en las dos caras de la columna, no solo en una.',
  ], ['Altura de columna', 'Desvío máximo'],
    [['3 m', '6 mm'], ['4 m', '8 mm'], ['6 m', '12 mm']],
    lambda i: [1, 1, 2][i], izq=560, der=560, tam=34),
  caso('las lainas de madera', [
    'Caso de obra: para nivelar una columna, metieron trozos de madera bajo la placa base. Quedó perfecta el día de la entrega.',
    'A los meses, con la carga y la humedad, la madera se aplastó. La viga se desnivelaba y aparecieron rajaduras en el tablero.',
    'Las lainas son de acero, y debajo de la placa se rellena con mortero sin contracción, el grout, cuando lo pide el plano.',
  ], [('🪵', 'Niveló con <b class="nar">madera</b> bajo la placa'), ('📉', 'Se aplastó: <b class="nar">desnivel y rajaduras</b>'), ('✅', 'Lainas de <b class="nar">acero</b> + grout si lo pide el plano')]),
  *ejercicio(1,
    'Replanteas un mezanine de <b class="nar">4 × 6 m</b> y mides las diagonales:<br><b class="nar">7.23 m</b> y <b class="nar">7.19 m</b>. ¿Está a escuadra? ¿Qué haces?',
    ['Ahora tú. Replanteas un mezanine de cuatro por seis, y mides las diagonales: siete veintitrés y siete diecinueve.', '¿Está a escuadra? ¿Qué haces?'],
    'Deberían medir <b class="nar">7.21 m</b> las dos · hay <b class="nar">4 cm</b> de diferencia: no está<br>Mueve las marcas de la esquina de la diagonal larga<br>hasta que <b class="nar">las dos midan igual</b>',
    ['Las dos deberían medir siete veintiuno. Hay cuatro centímetros de diferencia: no está a escuadra.',
     'Mueve la marca de una esquina de la diagonal larga, sin cambiar los lados, hasta que las dos midan igual.']),
  *ejercicio(2,
    'Una columna de <b class="nar">3.50 m</b> está desviada <b class="nar">9 mm</b> en una cara.<br>¿Pasa con 1 en 500? ¿Cuándo la corriges?',
    ['Segundo ejercicio. Una columna de tres metros cincuenta está desviada nueve milímetros en una cara.', '¿Pasa con uno en quinientos? ¿Y cuándo la corriges?'],
    'Máximo: 3 500 ÷ 500 = <b class="nar">7 mm</b> · tiene 9 mm → <b class="nar">no pasa</b><br>Corrige <b class="nar">antes del ajuste final</b> de pernos, con lainas de acero o tensores',
    ['El máximo es tres mil quinientos entre quinientos: siete milímetros. Tiene nueve: no pasa.',
     'Se corrige antes del ajuste final de los pernos, con lainas de acero bajo la placa o con los tensores del montaje.']),
  faq([
    ('¿Nivel láser o manguera?', 'Los dos sirven; el láser es más rápido.', '¿Nivel láser o manguera? Los dos sirven bien. El láser es más rápido; la manguera es barata y exacta si no tiene burbujas.'),
    ('¿Quién decide el anclaje?', 'El ingeniero y la ficha del fabricante.', '¿Quién decide el anclaje? El ingeniero, con la ficha del fabricante. Tú respetas profundidad, broca y distancia al borde.'),
    ('¿Puedo montar solo con dos personas?', 'Depende del peso: planifica el izaje.', '¿Puedo montar con dos personas? Depende del peso de cada pieza. Planifica el izaje, como vimos en el curso de Seguridad.'),
  ]),
  repaso([
    ('¿Qué va primero en el montaje?', 'Las columnas, sin ajuste final.'),
    ('¿Cuándo se ajustan los pernos?', 'Después de aplomar y nivelar.'),
    ('¿Con qué se nivela bajo la placa?', 'Con lainas de acero, nunca con piedras ni madera.'),
    ('¿Qué entregas al cliente?', 'Una lista de control con medidas y fotos.'),
  ]),
]

# ───────────── Clase 8 · Tijerales planos ─────────────
EXT['est_c8'] = [
  ejemplo('El peralte <span class="nar">según la luz</span>', [
    'Antes de los errores, el rango de peralte para las luces más comunes: entre la luz entre quince y la luz entre diez.',
    'Ocho metros: de cincuenta y tres a ochenta centímetros. Diez metros: de sesenta y siete a un metro.',
    'Doce metros: de ochenta a uno veinte. Y quince metros: de un metro a uno cincuenta.',
  ], ['Luz', 'Peralte (L/15 a L/10)'],
    [['8 m', '0.53 – 0.80 m'], ['10 m', '0.67 – 1.00 m'], ['12 m', '0.80 – 1.20 m'], ['15 m', '1.00 – 1.50 m']],
    lambda i: [1, 1, 2, 2][i], izq=520, der=520, tam=33),
  caso('la correa entre nudos', [
    'Caso de obra: para ahorrar correas, las pusieron cada metro ochenta, aunque los nudos del tijeral estaban cada metro y medio.',
    'Muchas quedaron entre nudos. Con la cobertura y una lluvia fuerte, el cordón superior se dobló entre nudo y nudo.',
    'El paso de las correas y el de los nudos se deciden juntos, antes de fabricar. La correa siempre sobre un nudo.',
  ], [('📏', 'Correas cada 1.80 m, nudos cada <b class="nar">1.50 m</b>'), ('〰️', 'El cordón superior <b class="nar">se dobló</b>'), ('✅', 'Correa siempre <b class="nar">sobre un nudo</b>')]),
  *ejercicio(1,
    'Un tijeral de <b class="nar">12 m</b> con <b class="nar">1 m</b> de peralte.<br>¿Qué ángulo tienen las diagonales con <b class="nar">4 paneles</b> de 3 m?<br>¿Y con <b class="nar">8 paneles</b> de 1.50 m? ¿Cuál eliges?',
    ['Ahora tú. Un tijeral de doce metros, con un metro de peralte.', '¿Qué ángulo tienen las diagonales con cuatro paneles de tres metros? ¿Y con ocho paneles de metro y medio? ¿Cuál eliges?'],
    '4 paneles: 1 ÷ 3 → <b class="nar">≈ 18°</b> (muy acostada ✗)<br>8 paneles: 1 ÷ 1.5 → <b class="nar">≈ 34°</b> (entre 30° y 60° ✓)<br>Eliges <b class="nar">8 paneles</b>',
    ['Con cuatro paneles, la diagonal sube un metro en tres: unos dieciocho grados. Muy acostada.',
     'Con ocho paneles, sube un metro en uno y medio: unos treinta y cuatro grados. Dentro del rango. Eliges ocho paneles.']),
  *ejercicio(2,
    'El tijeral Pratt de la clase lleva <b class="nar">≈ 47 m</b> de perfil.<br>Si el ingeniero aprueba ángulo de <b class="nar">2" × 3/16"</b> (≈ 3.6 kg/m),<br>¿cuánto pesan <b class="nar">6 tijerales</b>?',
    ['Segundo ejercicio. El tijeral Pratt de la clase lleva unos cuarenta y siete metros de perfil.', 'Si el ingeniero aprueba ángulo de dos pulgadas por tres dieciseisavos, de unos tres punto seis kilos por metro, ¿cuánto pesan seis tijerales?'],
    'Un tijeral: 47 × 3.6 ≈ <b class="nar">169 kg</b><br>Seis: 169 × 6 ≈ <b class="nar">1 015 kg</b> · más cartelas y placas',
    ['Un tijeral: cuarenta y siete por tres punto seis, unos ciento sesenta y nueve kilos.',
     'Seis tijerales: unos mil quince kilos. Y súmale las cartelas y las placas de apoyo.']),
  faq([
    ('¿Tijeral de tubo o de ángulo?', 'Tubo se ve mejor y pinta fácil; ángulo es más barato.', '¿Tijeral de tubo o de ángulo? El tubo se ve más limpio y es fácil de pintar. El ángulo suele ser más barato. El ingeniero define el perfil.'),
    ('¿Puedo armarlos en el piso?', 'Sí, sobre un trazo a tamaño real o un gálibo.', '¿Se arman en el piso? Sí, sobre un trazo a tamaño real o un gálibo, para que todos salgan iguales.'),
    ('¿Cómo los subo?', 'Con plan de izaje y arriostre inmediato.', '¿Cómo los subo? Con un plan de izaje, y arriostrando cada tijeral apenas queda en su lugar.'),
  ]),
  repaso([
    ('¿Por qué el triángulo?', 'Porque no se deforma si sus lados no cambian de largo.'),
    ('¿Cuál es la regla de oro del nudo?', 'Que los ejes de todas las barras se crucen en un punto.'),
    ('¿Entre qué ángulos van las diagonales?', 'Entre treinta y sesenta grados.'),
    ('¿Dónde se apoyan las correas?', 'Sobre los nudos del cordón superior.'),
  ]),
]

# ───────────── Clase 9 · Arriostres, viento y sismo ─────────────
EXT['est_c9'] = [
  respuesta('tijeral Pratt de 10 m', [
    'La respuesta del reto de la clase pasada: el tijeral Pratt de diez metros, con ochenta centímetros de peralte y ocho paneles.',
    'Cada panel mide uno punto veinticinco. Los cordones: diez y diez, veinte metros. Nueve montantes de ochenta centímetros: siete punto dos.',
    'Cada diagonal: raíz de uno punto veinticinco al cuadrado más cero punto ocho al cuadrado, uno punto cuarenta y ocho. Por ocho: once punto nueve. En total, unos treinta y nueve metros.',
  ], ['Barra', 'Metros'],
    [['Cordones (10 + 10)', '20.0 m'], ['9 montantes × 0.80', '7.2 m'], ['8 diagonales × 1.48', '11.9 m'], ['Total', '≈ 39.1 m']], lambda i: [1, 1, 2, 2][i]),
  ejemplo('El viento sube <span class="nar">con el cuadrado</span>', [
    'Antes de los errores: la presión del viento crece con el cuadrado de la velocidad. Con coeficiente uno:',
    'A setenta y cinco kilómetros por hora, el mínimo de la norma: unos veintiocho kilos por metro cuadrado.',
    'A ochenta y cinco: treinta y seis. Y a cien kilómetros por hora: cincuenta. Casi el doble que a setenta y cinco.',
    'La velocidad de tu zona la define el ingeniero con el mapa de la norma. Tú entiende por qué cambia tanto.',
  ], ['Velocidad', 'Presión (0.005 × V²)'],
    [['75 km/h', '≈ 28 kg/m²'], ['85 km/h', '≈ 36 kg/m²'], ['100 km/h', '≈ 50 kg/m²']],
    lambda i: [1, 2, 2][i], izq=480, der=480, tam=33),
  caso('la X que estorbaba', [
    'Caso de obra: en una nave, el cliente pidió quitar una cruz de arriostre porque iba a abrir un portón ahí. El maestro la cortó.',
    'Con el primer viento fuerte de la tarde, la nave se movía y los pernos del techo empezaron a sonar. Hubo que llamar al ingeniero de urgencia.',
    'Se resolvió con un pórtico rígido alrededor del portón, que diseñó el ingeniero. Lo que se quita del plano, se consulta antes.',
  ], [('✂️', 'Cortaron una <b class="nar">cruz de arriostre</b>'), ('🌬️', 'Con el viento, la nave <b class="nar">se movía</b>'), ('✅', 'Pórtico rígido <b class="nar">diseñado por el ingeniero</b>')]),
  *ejercicio(1,
    'Una pared de <b class="nar">15 × 6 m</b>, con presión básica de <b class="nar">28 kg/m²</b><br>y coeficiente <b class="nar">0.8</b>. ¿Cuánto empuja el viento?',
    ['Ahora tú. Una pared de quince por seis metros, con presión básica de veintiocho kilos por metro cuadrado, y coeficiente cero ocho.', '¿Cuánto empuja el viento?'],
    'Área: 15 × 6 = <b class="nar">90 m²</b> · Presión: 28 × 0.8 = <b class="nar">22.4 kg/m²</b><br>Empuje: 90 × 22.4 ≈ <b class="nar">2 016 kg</b> (unas dos toneladas)',
    ['El área: quince por seis, noventa metros cuadrados. La presión: veintiocho por cero ocho, veintidós punto cuatro.',
     'Noventa por veintidós punto cuatro: unos dos mil dieciséis kilos. Dos toneladas empujando la pared.']),
  *ejercicio(2,
    'Una nave de <b class="nar">6 paños</b> se arriostra en los <b class="nar">dos paños de los extremos</b>:<br>en el techo y en las <b class="nar">dos paredes</b>, con cruces en X.<br>¿Cuántas diagonales son?',
    ['Segundo ejercicio. Una nave de seis paños se arriostra en los dos paños de los extremos: en el techo y en las dos paredes, con cruces en X.', '¿Cuántas diagonales son?'],
    'Techo: 2 paños × 2 = <b class="nar">4</b><br>Paredes: 2 paredes × 2 paños × 2 = <b class="nar">8</b><br>Total: <b class="nar">12 diagonales</b>, cada una con su templador',
    ['En el techo: dos paños con una X cada uno, cuatro diagonales.',
     'En las paredes: dos paredes, dos paños cada una, dos diagonales por X: ocho. En total, doce diagonales, cada una con su templador.']),
  faq([
    ('¿Varilla lisa o cable para arriostres?', 'Los dos trabajan estirados; el plano define cuál.', '¿Varilla o cable? Los dos trabajan solo estirados. El plano define cuál y de qué diámetro.'),
    ('¿Cuánto se tensa?', 'Firme, sin flojedad, sin torcer la estructura.', '¿Cuánto se tensa un arriostre? Hasta que quede firme y sin flojedad, pero sin torcer la estructura. Tensa por parejas.'),
    ('¿El sismo lo calculo yo?', 'No: es del ingeniero, con la E.030.', '¿El sismo lo calculo yo? No. Lo calcula el ingeniero con la norma E punto cero treinta. Tú respetas el plano.'),
  ]),
  repaso([
    ('¿Cómo trabaja un arriostre de varilla?', 'Solo estirado.'),
    ('¿Por qué los arriostres van en X?', 'Porque cada diagonal trabaja con el viento de un lado.'),
    ('¿Cuál es la velocidad mínima de la norma E punto cero veinte?', 'Setenta y cinco kilómetros por hora.'),
    ('¿Cuándo se ponen los arriostres?', 'Durante el montaje, no al final.'),
  ]),
]

# ───────────── Clase 10 · Refuerzos y ampliaciones ─────────────
EXT['est_c10'] = [
  respuesta('pared de 20 × 4 m', [
    'La respuesta del reto de la clase pasada: el viento sobre una pared de veinte por cuatro metros.',
    'Área: ochenta metros cuadrados. Presión: veintiocho por cero ocho, veintidós punto cuatro kilos por metro cuadrado.',
    'Empuje: ochenta por veintidós punto cuatro, unos mil setecientos noventa y dos kilos. Casi una tonelada y ochocientos kilos.',
  ], ['Dato', 'Resultado'], [['Área', '80 m²'], ['Presión', '22.4 kg/m²'], ['Empuje', '≈ 1 792 kg']], lambda i: i),
  ejemplo('Peso de <span class="nar">platinas de refuerzo</span>', [
    'Antes de los errores, el peso por metro de las platinas que más se usan para reforzar. Ancho por espesor por siete punto ochenta y cinco.',
    'Tres pulgadas por un cuarto: unos tres punto ocho kilos por metro. Cuatro por un cuarto: cinco.',
    'Cuatro por tres octavos, la de nuestro ejemplo: siete punto seis. Y seis por tres octavos: once punto cuatro.',
  ], ['Platina', 'Peso aproximado'],
    [['3" × 1/4"', '≈ 3.8 kg/m'], ['4" × 1/4"', '≈ 5.1 kg/m'], ['4" × 3/8"', '≈ 7.6 kg/m'], ['6" × 3/8"', '≈ 11.4 kg/m']],
    lambda i: [1, 1, 2, 2][i], izq=520, der=520, tam=33),
  caso('el agujero para la tubería', [
    'Caso de obra: el gasfitero necesitaba pasar un tubo de desagüe, y perforó el ala inferior de una viga del mezanine.',
    'Nadie avisó. Meses después, la viga tenía más flecha de lo normal justo en esa zona. El ingeniero pidió un refuerzo con platinas y apuntalar mientras tanto.',
    'En las vigas no se perfora sin autorización. Si hay que pasar instalaciones, se pasa por el alma, donde el ingeniero indique, o por debajo.',
  ], [('🕳️', 'Perforaron el <b class="nar">ala</b> de la viga'), ('📉', 'Más flecha: <b class="nar">refuerzo y puntales</b>'), ('✅', 'Instalaciones por donde <b class="nar">diga el ingeniero</b>')]),
  *ejercicio(1,
    'El ingeniero pide <b class="nar">2 platinas de 4" × 3/8"</b> de <b class="nar">3 m</b>,<br>con filete de 6 mm intermitente: <b class="nar">50 mm cada 150 mm</b>, en los dos bordes.<br>¿Cuántos kilos de platina y cuántos metros de cordón?',
    ['Ahora tú. El ingeniero pide dos platinas de cuatro pulgadas por tres octavos, de tres metros, con filete de seis milímetros intermitente: cincuenta milímetros cada ciento cincuenta, en los dos bordes de cada platina.', '¿Cuántos kilos de platina, y cuántos metros de cordón?'],
    'Platina: 2 × 3 m × 7.6 ≈ <b class="nar">46 kg</b><br>Bordes: 2 platinas × 2 bordes × 3 m = 12 m · solo ⅓ lleva cordón<br>Cordón: 12 ÷ 3 = <b class="nar">4 m</b>',
    ['Las platinas: seis metros por siete punto seis, unos cuarenta y seis kilos.',
     'Bordes: dos platinas, dos bordes, tres metros: doce metros. Pero solo un tercio lleva cordón, cincuenta de cada ciento cincuenta. Cuatro metros de cordón.']),
  *ejercicio(2,
    'El cliente quiere colgar un tecle de <b class="nar">500 kg</b> de una viga vieja del taller.<br>Ordena: apuntalar · consultar al ingeniero · medir el perfil · reforzar · revisar corrosión · probar con carga',
    ['Segundo ejercicio. El cliente quiere colgar un tecle de quinientos kilos de una viga vieja del taller.', 'Ordena estos pasos: apuntalar, consultar al ingeniero, medir el perfil, reforzar, revisar la corrosión y probar con carga.'],
    '1. <b class="nar">Medir</b> el perfil · 2. Revisar <b class="nar">corrosión</b> y soldaduras<br>3. Consultar al <b class="nar">ingeniero</b> · 4. <b class="nar">Apuntalar</b><br>5. <b class="nar">Reforzar</b> según el plano · 6. <b class="nar">Probar</b> con carga controlada',
    ['Primero investigas: mides el perfil y revisas corrosión y soldaduras. Con eso, consultas al ingeniero.',
     'Si decide reforzar: apuntalas, refuerzas según su plano, y al final se prueba con carga controlada, con la zona despejada.']),
  faq([
    ('¿Puedo soldar con la viga cargada?', 'Solo si el ingeniero lo permite; mejor apuntalar.', '¿Puedo soldar el refuerzo con la viga cargada? Solo si el ingeniero lo permite. Lo más seguro es descargar o apuntalar.'),
    ('¿Cómo sé el espesor sin cortar?', 'Con un medidor por ultrasonido.', '¿Cómo sé el espesor sin cortar? Con un medidor de espesores por ultrasonido. Se alquila o lo trae un técnico.'),
    ('¿Cobro aparte la investigación?', 'Sí: la visita y las mediciones tienen costo.', '¿Cobro la investigación? Sí. La visita, las mediciones y el informe tienen costo, aunque al final no se haga el refuerzo.'),
  ]),
  repaso([
    ('¿Qué haces antes de reforzar?', 'Investigar y llevar los datos al ingeniero.'),
    ('¿Qué electrodo para acero viejo?', 'Siete cero dieciocho, de bajo hidrógeno.'),
    ('¿Cómo se sueldan las platinas?', 'Con cordones intermitentes y alternados.'),
    ('¿Qué pasa si perforas el ala de una viga?', 'Pierde mucha resistencia.'),
  ]),
]

# ───────────── Clase 11 · Calidad y documentos ─────────────
EXT['est_c11'] = [
  ejemplo('Un protocolo <span class="nar">bien llenado</span>', [
    'Antes de los errores, un protocolo dimensional con cuatro piezas del mezanine.',
    'La columna C uno: tres mil, más o menos dos, medida tres mil uno. Conforme. La viga V uno: tres mil ochocientos treinta, medida tres mil ochocientos treinta y tres. No conforme: se pasó un milímetro.',
    'La rectitud de C dos: máximo tres milímetros, medida dos. Conforme. Y la diagonal del paño: siete veintiuno, medida siete veintiuno. Conforme.',
    'La viga V uno se corrige, se vuelve a medir, y se registra la no conformidad. Así se ve el control.',
  ], ['Marca', 'Control', 'Tolerancia', 'Medido', 'Resultado'],
    [['C1', 'Largo 3 000 mm', '± 2', '3 001', '✓ Conforme'], ['V1', 'Largo 3 830 mm', '± 2', '3 833', '✗ No conforme'],
     ['C2', 'Rectitud', '≤ 3 mm', '2 mm', '✓ Conforme'], ['Paño', 'Diagonal 7.21 m', 'igual', '7.21 m', '✓ Conforme']],
    lambda i: [1, 1, 2, 2][i], izq=160, der=160, tam=27),
  caso('los certificados que nadie pidió', [
    'Caso de obra: un taller ganó una estructura para una fábrica. Al final, el supervisor pidió el dossier con los certificados del acero y los pernos.',
    'Nadie los había pedido al comprar. El proveedor tardó tres semanas en encontrarlos, y uno ya no existía. El último pago se retuvo todo ese tiempo.',
    'Pide los certificados en el mismo momento de la compra, y guárdalos en la carpeta del proyecto. Es gratis, y vale plata.',
  ], [('📄', 'No pidieron <b class="nar">certificados</b> al comprar'), ('⏳', 'Tres semanas buscando: <b class="nar">pago retenido</b>'), ('✅', 'Pídelos <b class="nar">con la compra</b> y guárdalos')]),
  *ejercicio(1,
    'Revisa estas tres mediciones:<br>a) Viga de 4 200 mm (± 2) medida <b class="nar">4 199</b><br>b) Columna de 3 m: rectitud medida <b class="nar">4 mm</b><br>c) Placa a tope (± 1) medida <b class="nar">+1.5 mm</b>',
    ['Ahora tú. Revisa tres mediciones.', 'Una viga de cuatro mil doscientos, más o menos dos, medida cuatro mil ciento noventa y nueve. Una columna de tres metros con cuatro milímetros de curvatura. Y una placa a tope, más o menos uno, medida un milímetro y medio más larga.'],
    'a) <b class="nar">Conforme</b> (−1 mm, dentro de ± 2)<br>b) <b class="nar">No conforme</b> (máximo 3 mm)<br>c) <b class="nar">No conforme</b> (máximo ± 1 mm)',
    ['La viga: le falta un milímetro, dentro de más o menos dos. Conforme.',
     'La columna: el máximo es tres milímetros, tiene cuatro. No conforme. Y la placa: más uno y medio, cuando el límite es uno. No conforme. Las dos se corrigen y se registran.']),
  *ejercicio(2,
    'La pintura pide <b class="nar">180 µm</b>. Lees: 165 · 190 · 175 · 150 · 185.<br>Regla común: el <b class="nar">promedio</b> llega a 180 y ninguna lectura baja del <b class="nar">80 %</b>.<br>¿Pasa?',
    ['Segundo ejercicio. La pintura pide ciento ochenta micras. Lees: ciento sesenta y cinco, ciento noventa, ciento setenta y cinco, ciento cincuenta y ciento ochenta y cinco.', 'Una regla común: el promedio llega a ciento ochenta, y ninguna lectura baja del ochenta por ciento. ¿Pasa?'],
    'Promedio: 865 ÷ 5 = <b class="nar">173 µm</b> → no llega a 180 ✗<br>Mínimo: 80 % de 180 = 144 → 150 sí pasa ✓<br><b class="nar">No pasa</b>: hay que dar otra mano o retocar y volver a medir',
    ['El promedio: ochocientos sesenta y cinco entre cinco, ciento setenta y tres. No llega a ciento ochenta.',
     'Ninguna baja de ciento cuarenta y cuatro, eso sí cumple. Pero por el promedio, no pasa: otra mano y se vuelve a medir.']),
  faq([
    ('¿Necesito un software para el dossier?', 'No: un formato simple y fotos ordenadas.', '¿Necesito un programa especial para el dossier? No. Un formato simple, firmas y fotos ordenadas. En InnovApp puedes guardar las fotos en la carpeta del cliente.'),
    ('¿Quién firma los protocolos?', 'Quien inspeccionó, y el supervisor si lo pide.', '¿Quién firma los protocolos? Quien hizo la inspección, y el supervisor del cliente si así lo pide el contrato.'),
    ('¿Sirve para obras chicas?', 'Sí: te diferencia y evita reclamos.', '¿Esto sirve para obras chicas? Sí. Un acta con fotos y medidas te diferencia y evita reclamos.'),
  ]),
  repaso([
    ('¿Qué es el número de colada?', 'El lote de fabricación del acero.'),
    ('¿Cuándo se hacen los protocolos?', 'Mientras se fabrica, no al final.'),
    ('¿Qué es una no conformidad?', 'El registro de un error y de cómo se corrigió.'),
    ('¿Qué cierra la entrega?', 'El acta firmada por el cliente.'),
  ]),
]
