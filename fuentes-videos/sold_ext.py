"""Ampliación de «Soldadura Estructural SMAW y MIG» (≈8 min por clase).
Misma receta que Naves y Techos: antes de los errores, ejemplos con números, un caso de obra, dos ejercicios
para pausar, preguntas frecuentes y un repaso rápido; si el reto anterior tiene respuesta, va al inicio."""
from naves_ext import insertar, caja, ejercicio, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · Seguridad y EPP ─────────────
EXT['sold_c1'] = [
  ejemplo('La sombra según <span class="nar">tu trabajo</span>', [
    'Antes de los errores, una tabla para elegir la sombra según lo que vas a hacer en la obra.',
    'Con electrodo de dos y medio a setenta amperios, o de tres punto dos a ciento veinte: mínimo ocho, recomendada diez. Es lo de todos los días.',
    'Con siete cero dieciocho de cuatro milímetros, a ciento setenta amperios, sube a doce. Y con MIG, que da más luz, entre once y doce.',
    'Y al esmerilar no hace falta filtro oscuro: lentes de seguridad y careta facial transparente, porque el disco lanza partículas a los ojos.',
  ], ['Trabajo', 'Sombra mínima', 'Recomendada'],
    [['Electrodo 2.5 mm · 70 A', '8', '10'], ['Electrodo 3.2 mm · 120 A', '8', '10'], ['7018 de 4 mm · 170 A', '10', '12'],
     ['MIG · 150 a 200 A', '10', '11 – 12'], ['Esmerilar', '—', 'Lentes + careta transparente']],
    lambda i: [1, 1, 2, 2, 3][i], izq=260, der=260),
  caso('el ayudante que no vino', [
    'Caso de obra: el soldador usaba su careta, pero su ayudante sostenía la pieza mirando de costado, sin protección.',
    'Esa noche el ayudante no pudo dormir del ardor en los ojos, y al día siguiente no fue a trabajar. Un día perdido, y un ojo en riesgo.',
    'La solución cuesta poco: lentes con filtro para el ayudante, o una cortina entre los dos. Y que nunca mire el arco de frente.',
  ], [('👀', 'El ayudante miraba <b class="nar">de costado</b>, sin protección'), ('😣', 'Ojo de arco: <b class="nar">un día perdido</b>'), ('🛡️', 'Lentes con filtro o <b class="nar">cortina</b> para el ayudante')]),
  caso('la chispa que bajó por la rendija', [
    'Otro caso: soldaron unas correas en el techo de un depósito, terminaron a las cinco y se fueron.',
    'Una chispa cayó por una rendija sobre cajas de cartón. A las siete, el depósito tenía humo. Por suerte el vigilante lo vio a tiempo.',
    'Por eso: tapa las rendijas o pon una manta ignífuga debajo, revisa abajo antes de irte, y vigila media hora.',
  ], [('🔥', 'Chispa por una rendija → <b class="nar">cartones</b>'), ('⏱', 'El fuego empezó <b class="nar">dos horas después</b>'), ('🧯', 'Manta ignífuga debajo y <b class="nar">vigila 30 min</b>')]),
  *ejercicio(1,
    'Vas a soldar con <b class="nar">7018 de 3.2 mm a 125 A</b> dentro de un depósito.<br>Hay cartones a 4 m, no hay ventana y tu careta es <b class="nar">sombra 9</b>.<br>¿Qué tres cosas corriges antes de prender?',
    ['Ahora tú. Vas a soldar con siete cero dieciocho de tres punto dos, a ciento veinticinco amperios, dentro de un depósito.',
     'Hay cartones a cuatro metros, no hay ventana, y tu careta tiene sombra nueve. ¿Qué tres cosas corriges antes de prender?'],
    '1. Careta con sombra <b class="nar">10</b><br>2. Cartones a <b class="nar">10 m</b> o cubiertos con manta, y extintor a la mano<br>3. <b class="nar">Ventilación</b> que saque el humo, o respirador',
    ['Uno: la careta. A ciento veinticinco amperios, lo recomendado es sombra diez.',
     'Dos: los cartones, a diez metros, o cubiertos con una manta ignífuga, y el extintor a la mano.',
     'Y tres: el humo. Un ventilador que lo saque del depósito, o respirador para humos.']),
  *ejercicio(2,
    'Te piden soldar <b class="nar">20 uniones de tubo galvanizado</b><br>en un cuarto cerrado. Ordena los pasos para hacerlo seguro.',
    ['Segundo ejercicio. Te piden soldar veinte uniones de tubo galvanizado, en un cuarto cerrado.', 'Ordena los pasos para hacerlo sin enfermarte.'],
    '1. Quitar el zinc <b class="nar">2 a 3 cm</b> con la amoladora<br>2. <b class="nar">Ventilación</b> que saque el humo + respirador<br>3. Cabeza <b class="nar">fuera</b> de la columna de humo<br>4. Al final, <b class="nar">galvanizado en frío</b> en la zona',
    ['Primero: quita el zinc, dos o tres centímetros alrededor de cada unión, con la amoladora.',
     'Segundo: un ventilador que saque el humo hacia afuera, y respirador para humos. Tercero: la cabeza fuera de la columna de humo.',
     'Y al terminar, pinta la zona con galvanizado en frío, para que no se oxide. Esto lo vemos a fondo en la clase once.']),
  faq([
    ('¿La careta fotosensible vale la pena?', 'Sí: menos cansancio y no levantas la careta. Revisa sus pilas.', '¿Vale la pena la careta fotosensible? Sí. Te cansas menos y no tienes que levantarla. Solo revisa sus pilas y cambia la luna protectora cuando se ensucie.'),
    ('¿Sirven los lentes de sol?', 'No: no filtran el arco. Nunca.', '¿Sirven unos lentes oscuros de sol? No. No filtran la luz del arco. Nunca los uses para soldar ni para mirar.'),
    ('¿Y si ya me dio ojo de arco?', 'No te frotes, compresas frías y al médico.', '¿Y si ya te dio ojo de arco? No te frotes los ojos, ponte compresas frías y ve al médico. Nada de remedios caseros en los ojos.'),
  ]),
  repaso([
    ('¿Qué sombra recomiendas a ciento veinte amperios?', 'Diez.'),
    ('¿Qué ropa nunca usas para soldar?', 'Ropa sintética: se derrite con una chispa.'),
    ('¿Cuántos metros libres de inflamables?', 'Unos diez metros alrededor.'),
    ('¿Cuánto tiempo vigilas al terminar?', 'Por lo menos media hora.'),
  ]),
]

# ───────────── Clase 2 · Electrodos ─────────────
EXT['sold_c2'] = [
  ejemplo('Lee <span class="nar">cualquier caja</span>', [
    'Antes de los errores, cuatro códigos que vas a encontrar en las ferreterías, leídos con la regla de hoy.',
    'Seis cero once y seis cero trece: sesenta mil, todas las posiciones. Uno celulósico, que penetra; el otro rutílico, fácil y bonito.',
    'Siete cero dieciocho: setenta mil, todas las posiciones, bajo hidrógeno. El de las estructuras.',
    'Y uno que quizá no conocías: el siete cero veinticuatro. Setenta mil, pero solo en plano y horizontal. Deposita muy rápido: sirve para filetes largos en la mesa.',
  ], ['Código', 'Resistencia', 'Posiciones', 'Para qué'],
    [['E6011', '60 000 psi', 'Todas', 'Raíz, obra, piezas sucias'], ['E6013', '60 000 psi', 'Todas', 'Delgado, rejas, liviano'],
     ['E7018', '70 000 psi', 'Todas', 'Estructura'], ['E7024', '70 000 psi', 'Plana y horizontal', 'Filetes largos en la mesa']],
    lambda i: [1, 1, 2, 3][i], izq=200, der=200, tam=29),
  ejemplo('El 7018 y <span class="nar">la humedad</span>', [
    'Ahora, cómo se guarda el siete cero dieciocho, paso a paso.',
    'Caja sellada, de fábrica: se usa directo. Apenas la abres, lo que no vas a usar va al horno de mantenimiento, a unos ciento veinte grados o más.',
    'Fuera del horno, en la obra, tiene un tiempo límite: unas cuatro horas. Usa un termo portátil si sueldas lejos del horno.',
    'Y si pasó ese tiempo o se mojó: o se reseca como dice el fabricante en la caja, o va para trabajos que no cargan. Nunca a la estructura.',
  ], ['Situación', 'Qué haces'],
    [['Caja sellada de fábrica', 'Se usa directo'], ['Caja abierta', 'Horno de mantenimiento ≥ 120 °C'],
     ['En la obra, fuera del horno', 'Máximo ≈ 4 horas · usa termo'], ['Pasado el tiempo o mojado', 'Resecar según el fabricante, o no va a estructura']],
    lambda i: [1, 1, 2, 3][i], izq=280, der=280),
  caso('el cordón lleno de poros', [
    'Caso de obra: un soldador con buena mano empezó a sacar cordones con poros y salpicadura, de un día para otro.',
    'Revisaron la máquina, la tierra, el amperaje. Todo bien. El problema: los electrodos habían pasado la noche en una caja abierta, al lado de la ventana.',
    'Con electrodos secos, el problema desapareció. Cuando un siete cero dieciocho chisporrotea y deja poros, lo primero que miras es la humedad.',
  ], [('🫧', 'De repente: <b class="nar">poros y salpicadura</b>'), ('🌙', 'Causa: caja abierta <b class="nar">toda la noche</b>'), ('🔥', 'Primero revisa la <b class="nar">humedad</b> del 7018')]),
  *ejercicio(1,
    'Un mezanine lleva <b class="nar">80 m de cordón</b> con 7018 (0.28 kg por metro).<br>Botas colillas de 5 cm (<b class="nar">14 %</b> de desperdicio). El kilo cuesta <b class="nar">S/ 19</b>.<br>¿Cuántos kilos compras y cuánto gastas?',
    ['Ahora tú. Un mezanine lleva ochenta metros de cordón con siete cero dieciocho, a cero punto veintiocho kilos por metro.',
     'Botas colillas de cinco centímetros: catorce por ciento de desperdicio. El kilo cuesta diecinueve soles. ¿Cuántos kilos compras, y cuánto gastas?'],
    'Se funden: 80 × 0.28 = <b class="nar">22.4 kg</b><br>Con desperdicio: 22.4 ÷ 0.86 = <b class="nar">26 kg</b> (6 cajas de 5 kg)<br>Gasto: 26 × 19 = <b class="nar">S/ 494</b>',
    ['Se funden ochenta por cero punto veintiocho: veintidós punto cuatro kilos.',
     'Con el catorce por ciento de desperdicio, divides entre cero punto ochenta y seis: unos veintiséis kilos. O sea, seis cajas de cinco kilos.',
     'Y veintiséis kilos por diecinueve soles: cuatrocientos noventa y cuatro soles. Ese número va en tu cotización.']),
  *ejercicio(2,
    '¿Qué electrodo usas en cada trabajo?<br>a) Reja de tubo de 1.5 mm · b) Placa base de columna<br>c) Portón oxidado en obra que no se puede limpiar bien<br>d) Empalme a tope con abertura: raíz y relleno',
    ['Segundo ejercicio. Elige el electrodo para cuatro trabajos.',
     'Una reja de tubo de uno y medio milímetros. La placa base de una columna. Un portón oxidado en obra, que no se puede limpiar bien. Y un empalme a tope con abertura: la raíz y el relleno.'],
    'a) <b class="nar">6013</b> de 2.5 mm · b) <b class="nar">7018</b> de 3.2 mm<br>c) <b class="nar">6011</b> · d) Raíz con <b class="nar">6011</b>, relleno y acabado con <b class="nar">7018</b>',
    ['La reja delgada: seis cero trece de dos y medio. La placa base, que carga: siete cero dieciocho de tres punto dos.',
     'El portón oxidado: seis cero once, que trabaja aunque haya algo de óxido. Y el empalme: raíz con seis cero once, y relleno y acabado con siete cero dieciocho.']),
  faq([
    ('¿El 7018 funciona con máquina de alterna?', 'Hay 7018 para alterna; rinde mejor en continua.', '¿El siete cero dieciocho sirve con una máquina de corriente alterna? Hay versiones hechas para alterna, lo dice la caja. Pero rinde mejor en continua, con el electrodo al positivo.'),
    ('¿Importa la marca?', 'Que cumpla la AWS A5.1 y respeta su caja.', '¿Importa la marca? Lo importante es que cumpla la norma AWS A cinco punto uno, y que respetes el amperaje que dice su caja.'),
    ('¿6010 o 6011?', 'Parecidos; el 6010 solo trabaja en continua.', '¿Seis cero diez o seis cero once? Son parecidos. La diferencia: el seis cero diez solo trabaja en continua, y el seis cero once también en alterna.'),
  ]),
  repaso([
    ('¿Qué dice el setenta del siete cero dieciocho?', 'Setenta mil libras por pulgada cuadrada de resistencia.'),
    ('¿Qué electrodo va en lo que carga?', 'El siete cero dieciocho.'),
    ('¿Cuánto tiempo aguanta el siete cero dieciocho fuera del horno?', 'Unas cuatro horas.'),
    ('¿Con qué amperaje empiezas?', 'Con el del medio del rango que dice la caja.'),
  ]),
]

# ───────────── Clase 3 · La máquina ─────────────
EXT['sold_c3'] = [
  respuesta('ciclo de trabajo', [
    'La respuesta del reto de la clase pasada, con una placa típica: sesenta por ciento a ciento sesenta amperios.',
    'Si sueldas a menos amperaje, el ciclo sube. Una regla práctica: el ciclo de la placa, por el amperaje de la placa entre el tuyo, al cuadrado.',
    'A ciento veinte amperios: sesenta por ciento, por ciento sesenta entre ciento veinte, al cuadrado. Da más de cien: puedes soldar seguido.',
    'Y a doscientos amperios: sesenta por cero punto ocho al cuadrado, unos treinta y ocho por ciento. Menos de cuatro minutos de cada diez.',
  ], ['Amperaje', 'Ciclo aproximado', 'Minutos de cada 10'],
    [['160 A (placa)', '60 %', '6 min'], ['120 A', '≈ 100 %', 'Seguido'], ['200 A', '≈ 38 %', '≈ 4 min']], lambda i: [0, 2, 3][i]),
  ejemplo('El amperaje según <span class="nar">la posición</span>', [
    'Antes de los errores, el mismo electrodo en las cuatro posiciones. Siete cero dieciocho de tres punto dos.',
    'En plano, donde todo es fácil: entre ciento veinte y ciento treinta amperios.',
    'En horizontal, un poquito menos. Y en vertical y sobre cabeza, bajas diez a quince por ciento: unos ciento cinco a ciento diez.',
    'No son números fijos: son el punto de partida. El cordón de prueba manda.',
  ], ['Posición', '7018 de 3.2 mm', 'Por qué'],
    [['Plana', '120 – 130 A', 'El charco no se cae'], ['Horizontal', '115 – 120 A', 'El charco baja un poco'], ['Vertical subiendo', '105 – 110 A', 'Charco chico'], ['Sobre cabeza', '105 – 110 A', 'Charco chico, arco corto']],
    lambda i: [1, 2, 2, 2][i]),
  ejemplo('Soldar con <span class="nar">generador</span>', [
    'En obra muchas veces no hay luz, y se suelda con generador. Tres reglas para no quemar la máquina.',
    'Uno: mira en la placa de la máquina la potencia que pide, y elige un generador con más o menos una vez y media esa potencia.',
    'Dos: prende el generador primero, espera que se estabilice, y recién conecta la máquina. Y tres: no conectes otras herramientas grandes al mismo tiempo.',
  ], ['Regla', 'Por qué'],
    [['Generador ≈ 1.5 × la potencia de la placa', 'Si se queda corto, el arco se cae'], ['Primero el generador, luego la máquina', 'El arranque da picos de voltaje'],
     ['Nada grande en paralelo', 'La amoladora le roba potencia al arco']], lambda i: i + 1, izq=260, der=260),
  caso('el arco débil en el techo', [
    'Caso de obra: en el techo de la nave, el arco se sentía débil. El soldador subía y subía el amperaje, y aun así el electrodo se pegaba.',
    'La máquina estaba abajo, con cuarenta metros de cable delgado y dos empalmes con cinta. En el camino, el cable se comía la corriente.',
    'Subieron la máquina a la plataforma, con cable corto y del calibre correcto. El arco volvió a la normalidad, al mismo amperaje de siempre.',
  ], [('⚡', 'Arco débil aunque <b class="nar">sube el amperaje</b>'), ('🧵', '40 m de cable <b class="nar">delgado y parchado</b>'), ('✅', 'Máquina cerca, <b class="nar">cable corto y grueso</b>')]),
  *ejercicio(1,
    'La placa de tu máquina dice <b class="nar">35 % a 200 A</b>.<br>¿Cuántos minutos de cada diez puedes soldar a <b class="nar">150 A</b>?',
    ['Ahora tú. La placa de tu máquina dice treinta y cinco por ciento a doscientos amperios.', '¿Cuántos minutos de cada diez puedes soldar a ciento cincuenta amperios?'],
    '35 % × (200 ÷ 150)² = 35 % × 1.78 ≈ <b class="nar">62 %</b><br>≈ <b class="nar">6 minutos</b> de cada 10',
    ['Doscientos entre ciento cincuenta da uno punto treinta y tres. Al cuadrado, uno punto setenta y ocho.',
     'Treinta y cinco por ciento, por uno punto setenta y ocho: unos sesenta y dos por ciento. Más o menos seis minutos de cada diez.']),
  *ejercicio(2,
    'Lee el cordón de prueba y decide:<br>a) El electrodo se pega y el cordón sale alto y angosto<br>b) Salpica mucho, muerde los bordes y el electrodo se pone al rojo',
    ['Segundo ejercicio. Lee el cordón de prueba y decide qué haces.',
     'Caso a: el electrodo se pega, y el cordón sale alto y angosto. Caso b: salpica mucho, muerde los bordes, y el electrodo se pone al rojo.'],
    'a) Amperaje <b class="nar">bajo</b>: sube de 5 en 5 A<br>b) Amperaje <b class="nar">alto</b>: baja de 5 en 5 A<br>Siempre con un nuevo cordón de prueba',
    ['Caso a: amperaje bajo. Sube de cinco en cinco amperios.',
     'Caso b: amperaje alto. Baja de cinco en cinco. Y en los dos, otro cordón de prueba antes de ir a la pieza.']),
  faq([
    ('¿Una inversora chica sirve para 7018 de 4 mm?', 'Solo si da 170 A reales con buen ciclo.', '¿Una inversora chica sirve para siete cero dieciocho de cuatro milímetros? Solo si da unos ciento setenta amperios reales, con un ciclo de trabajo que te deje avanzar.'),
    ('¿Por qué el electrodo se pone al rojo?', 'Amperaje alto o electrodo húmedo.', '¿Por qué el electrodo se pone al rojo antes de terminar? Casi siempre, amperaje alto. A veces, electrodo húmedo.'),
    ('¿Puedo alargar el cable?', 'Sí, con un calibre más grueso y sin empalmes con cinta.', '¿Puedo alargar el cable? Sí, pero mientras más largo, más grueso tiene que ser. Y nada de empalmes con cinta.'),
  ]),
  repaso([
    ('¿Qué polaridad usa el siete cero dieciocho?', 'Electrodo al positivo.'),
    ('¿Qué dice un ciclo de sesenta por ciento a ciento sesenta amperios?', 'Que de cada diez minutos sueldas seis a ese amperaje.'),
    ('¿Cuánto bajas en vertical?', 'Entre diez y quince por ciento.'),
    ('¿Qué tan largo es el arco?', 'Más o menos el diámetro del electrodo.'),
  ]),
]

# ───────────── Clase 4 · Juntas y biseles ─────────────
EXT['sold_c4'] = [
  ejemplo('El filete mínimo <span class="nar">en la obra</span>', [
    'Antes de los errores, la regla del filete mínimo aplicada a piezas de nuestra obra, con siete cero dieciocho.',
    'Columna de tubo de tres milímetros sobre placa de doce: manda la pieza más delgada, tres milímetros. Filete mínimo de tres.',
    'Una cartela de ocho milímetros sobre un ala de diez: la más delgada es de ocho. Filete mínimo de cinco.',
    'Y dos planchas de dieciséis: mínimo seis. Recuerda: es el mínimo. Si el plano pide más, manda el plano.',
  ], ['Unión', 'Pieza más delgada', 'Filete mínimo'],
    [['Tubo 3 mm sobre placa 12 mm', '3 mm', '3 mm'], ['Cartela 8 mm sobre ala 10 mm', '8 mm', '5 mm'], ['Plancha 16 mm con plancha 16 mm', '16 mm', '6 mm']],
    lambda i: i + 1),
  ejemplo('Cuánto pesa <span class="nar">un metro de filete</span>', [
    'Ahora, cuánto metal deposita un metro de filete, según su tamaño. Esto es lo que te ahorra plata.',
    'Cinco milímetros: cien gramos por metro. Seis: unos ciento cuarenta. Ocho: doscientos cincuenta.',
    'Y diez: casi cuatrocientos gramos. Fíjate: de cinco a diez milímetros, el metal se multiplica por cuatro.',
  ], ['Filete', 'Metal depositado por metro', 'Comparado con 5 mm'],
    [['5 mm', '≈ 0.10 kg', '1 ×'], ['6 mm', '≈ 0.14 kg', '1.4 ×'], ['8 mm', '≈ 0.25 kg', '2.5 ×'], ['10 mm', '≈ 0.39 kg', '4 ×']],
    lambda i: [1, 1, 1, 2][i]),
  caso('el empalme que se partió', [
    'Caso de obra: un cordón del arco quedó corto, y lo empalmaron con otro tubo. Lo soldaron a tope, por fuera, sin bisel y sin abertura.',
    'Por fuera se veía perfecto. Al izar el arco, el empalme se abrió: la soldadura solo había agarrado un milímetro de la pared.',
    'Un empalme que carga necesita penetración completa: bisel, abertura de raíz, y si se puede, un respaldo por dentro.',
  ], [('🔗', 'Empalme a tope <b class="nar">sin bisel ni abertura</b>'), ('💥', 'Se abrió <b class="nar">al izar</b> el arco'), ('✅', 'Bisel + abertura + respaldo: <b class="nar">penetración completa</b>')]),
  *ejercicio(1,
    'Una ménsula lleva <b class="nar">20 m de filete de 6 mm</b>.<br>¿Cuántos kilos de metal depositas?<br>¿Y si el maestro lo hace de 8 mm "por si acaso"?',
    ['Ahora tú. Una ménsula lleva veinte metros de filete de seis milímetros.', '¿Cuántos kilos de metal depositas? ¿Y si el maestro lo hace de ocho "por si acaso"?'],
    'De 6 mm: 20 × 0.14 = <b class="nar">2.8 kg</b><br>De 8 mm: 20 × 0.25 = <b class="nar">5.0 kg</b> · casi <b class="nar">el doble</b> de electrodo, tiempo y calor',
    ['De seis milímetros: veinte por cero punto catorce, dos punto ocho kilos.',
     'De ocho: veinte por cero punto veinticinco, cinco kilos. Casi el doble de electrodo, de tiempo y de calor, para nada.']),
  *ejercicio(2,
    'Plancha de <b class="nar">10 mm</b> con bisel en V de <b class="nar">60°</b> (30° por lado),<br>talón de <b class="nar">2 mm</b> y abertura de raíz de <b class="nar">2 mm</b>.<br>¿Qué tan ancha queda la junta arriba?',
    ['Segundo ejercicio. Una plancha de diez milímetros, con bisel en V de sesenta grados, treinta por lado.',
     'Talón de dos milímetros, y abertura de raíz de dos. ¿Qué tan ancha queda la junta arriba? Pista: la tangente de treinta grados es cero punto cincuenta y ocho.'],
    'Profundidad del bisel: 10 − 2 = <b class="nar">8 mm</b><br>Cada lado: 8 × 0.58 = <b class="nar">4.6 mm</b><br>Ancho arriba: 4.6 + 4.6 + 2 = <b class="nar">≈ 11 mm</b>',
    ['El bisel baja diez menos dos: ocho milímetros. Cada lado se abre ocho por cero punto cincuenta y ocho: cuatro punto seis.',
     'Arriba: cuatro punto seis, más cuatro punto seis, más la abertura de dos. Unos once milímetros. Con eso sabes cuántas pasadas llevará.']),
  faq([
    ('¿Puedo hacer el bisel con amoladora?', 'Sí: disco de desbaste y una plantilla de ángulo.', '¿Se puede hacer el bisel con la amoladora? Sí, con disco de desbaste y una plantilla de ángulo para que salga parejo.'),
    ('¿Para qué sirve la platina de respaldo?', 'Para que la raíz funda completa sin caerse.', '¿Para qué sirve la platina de respaldo? Para que la raíz funda completa, sin que el charco se caiga por la abertura.'),
    ('¿Cuándo bisel por los dos lados?', 'En planchas gruesas que se pueden voltear: bisel en X.', '¿Cuándo se hace bisel por los dos lados? En planchas gruesas que puedes voltear: bisel en X. Gastas menos electrodo y se deforma menos.'),
  ]),
  repaso([
    ('¿Cómo se mide un filete?', 'Por su cateto, la pierna del triángulo.'),
    ('¿Cuándo necesitas bisel?', 'A tope, en piezas de más de seis milímetros que trabajan con todo su espesor.'),
    ('¿Cada cuánto van los puntos?', 'Cada quince o veinte centímetros, alternando.'),
    ('¿Qué pasa si duplicas el filete?', 'Depositas cuatro veces más metal.'),
  ]),
]

# ───────────── Clase 5 · El cordón perfecto ─────────────
EXT['sold_c5'] = [
  ejemplo('Lee tu cordón <span class="nar">como un libro</span>', [
    'Antes de los errores, aprende a leer el cordón. Cada forma te dice qué hiciste mal.',
    'Escamas en punta, como flechas, y el cordón angosto: vas muy rápido. Escamas redondas y un cordón ancho y gordo: vas muy lento.',
    'Bordes mordidos y salpicadura: amperaje alto o arco largo. Y un cordón alto, como una cuerda, que no moja los bordes: amperaje bajo.',
  ], ['Lo que ves', 'Qué pasó', 'Corrige'],
    [['Escamas en punta, angosto', 'Muy rápido', 'Avanza más lento'], ['Escamas redondas, gordo', 'Muy lento', 'Avanza más rápido'],
     ['Bordes mordidos, salpica', 'Amperaje alto o arco largo', 'Baja o acorta el arco'], ['Alto como cuerda, sin mojar', 'Amperaje bajo', 'Sube 5 A']],
    lambda i: [1, 1, 2, 2][i], izq=200, der=200),
  ejemplo('Medidas que <span class="nar">no fallan</span>', [
    'Unas medidas fáciles de recordar, según el diámetro del electrodo.',
    'Con tres punto dos: arco de unos tres milímetros, cordón recto de siete a nueve de ancho, y vaivén de máximo diez.',
    'Con cuatro milímetros: arco de cuatro, cordón de ocho a doce, y vaivén de máximo doce. Todo crece con el diámetro.',
  ], ['Electrodo', 'Largo del arco', 'Ancho del cordón', 'Vaivén máximo (7018)'],
    [['2.5 mm', '≈ 2.5 mm', '5 – 7 mm', '≈ 7.5 mm'], ['3.2 mm', '≈ 3 mm', '7 – 9 mm', '≈ 10 mm'], ['4 mm', '≈ 4 mm', '8 – 12 mm', '≈ 12 mm']],
    lambda i: [1, 1, 2][i], izq=220, der=220),
  caso('los bultos cada 25 cm', [
    'Caso de obra: un filete largo, bonito en general, pero cada veinticinco centímetros había un bulto o un hueco.',
    'Eran los cambios de electrodo. El soldador prendía justo en el cráter, o lejos de él, y el empalme quedaba mal.',
    'Con la técnica de la clase: picar la escoria, prender un centímetro antes del cráter y regresar a empalmar, los empalmes desaparecieron.',
  ], [('〰️', 'Un bulto o un hueco <b class="nar">cada electrodo</b>'), ('🔁', 'Mal reinicio en el <b class="nar">cráter</b>'), ('✅', 'Pica, prende <b class="nar">1 cm antes</b> y regresa')]),
  *ejercicio(1,
    'Vas a soldar con <b class="nar">7018 de 4 mm</b>.<br>¿Qué largo de arco usas, qué ancho debe tener el cordón<br>y hasta dónde llega tu vaivén?',
    ['Ahora tú. Vas a soldar con siete cero dieciocho de cuatro milímetros.', '¿Qué largo de arco usas, qué ancho debe tener el cordón, y hasta dónde llega tu vaivén?'],
    'Arco: <b class="nar">≈ 4 mm</b> · Cordón: <b class="nar">8 a 12 mm</b><br>Vaivén: máximo 3 × 4 = <b class="nar">12 mm</b>',
    ['El arco: más o menos el diámetro, cuatro milímetros. El cordón, de dos a tres veces el diámetro: de ocho a doce.',
     'Y el vaivén, máximo tres veces el diámetro: doce milímetros. Si te pasas, el siete cero dieciocho pierde su protección.']),
  *ejercicio(2,
    'Tu compañero suelda un filete en una T con el electrodo <b class="nar">a 70°</b> de la pieza de abajo<br>y lo <b class="nar">empuja</b> hacia adelante.<br>¿Qué corriges?',
    ['Segundo ejercicio. Tu compañero suelda un filete en una junta en T. Apunta el electrodo a setenta grados de la pieza de abajo, y lo empuja hacia adelante.', '¿Qué le corriges?'],
    'Ángulo de trabajo: <b class="nar">45°</b>, al medio de las dos piezas<br>Ángulo de avance: <b class="nar">5 a 15°</b> hacia atrás, <b class="nar">arrastrando</b>',
    ['Primero, el ángulo de trabajo: cuarenta y cinco grados, al medio de las dos piezas, para repartir el calor.',
     'Y el avance: con electrodo se arrastra, inclinado de cinco a quince grados hacia atrás. Empujando, la escoria se mete delante del charco.']),
  faq([
    ('¿Cuántas pasadas lleva un filete?', 'En plano, hasta unos 8 mm en una pasada.', '¿Cuántas pasadas lleva un filete? En plano, hasta unos ocho milímetros se pueden hacer en una pasada. Más grande, en varias.'),
    ('¿Picar la escoria caliente?', 'Sí, con lentes puestos.', '¿Se puede picar la escoria en caliente? Sí, pero siempre con lentes de seguridad. Salta en pedazos muy calientes.'),
    ('¿Cómo practico sin gastar mucho?', 'Retazos de 6 mm y cordones encima de cordones.', '¿Cómo practico sin gastar mucho? Con retazos de seis milímetros, cordones uno al lado del otro, y cuando se llena la plancha, sigues encima.'),
  ]),
  repaso([
    ('¿Qué miras mientras sueldas?', 'El charco, no el arco.'),
    ('¿Qué indican escamas en punta?', 'Que vas muy rápido.'),
    ('¿Cómo terminas un cordón?', 'Llenando el cráter, sin levantar de golpe.'),
    ('¿Cuánto es el vaivén máximo con siete cero dieciocho?', 'Dos y media a tres veces el diámetro.'),
  ]),
]

# ───────────── Clase 6 · Nudos del arco sin torcerlo ─────────────
EXT['sold_c6'] = [
  ejemplo('Cuatro técnicas <span class="nar">contra la deformación</span>', [
    'Antes de los errores, cuatro técnicas que usan los talleres grandes. Puedes combinarlas.',
    'Uno: el paso peregrino. En vez de un cordón largo hacia adelante, haces tramos cortos hacia atrás, uno tras otro.',
    'Dos: cordones intermitentes, donde el plano lo permite. Tres: pre-deformar: si sabes que se cierra dos grados, lo armas abierto dos grados.',
    'Y cuatro: arriostres temporales, platinas soldadas con puntos que sujetan la pieza mientras se enfría. Después se retiran.',
  ], ['Técnica', 'Cómo es', 'Cuándo'],
    [['Paso peregrino', 'Tramos cortos hacia atrás', 'Cordones largos'], ['Intermitente', 'Tramos con espacios', 'Si el plano lo permite'],
     ['Pre-deformar', 'Armar al revés de lo que jala', 'Uniones en T, ménsulas'], ['Arriostre temporal', 'Platinas con puntos', 'Arcos y marcos']],
    lambda i: [1, 2, 2, 3][i], izq=200, der=200),
  caso('la viga que se arqueó', [
    'Caso de obra: reforzaron una viga de mezanine con una platina soldada solo por abajo, con un cordón continuo de punta a punta.',
    'Al enfriarse, la viga se arqueó: las puntas subieron casi un centímetro. El cordón de abajo se encogió y la jaló.',
    'Lo correcto: soldar en tramos cortos y alternados, de un lado y del otro de la platina, desde el centro hacia las puntas.',
  ], [('📏', 'Platina soldada <b class="nar">solo por abajo</b>, cordón continuo'), ('🌙', 'La viga se <b class="nar">arqueó ≈ 1 cm</b>'), ('✅', 'Tramos cortos <b class="nar">alternados desde el centro</b>')]),
  *ejercicio(1,
    'Una columna de tubo cuadrado va sobre su placa base.<br>Numera el orden de los <b class="nar">4 lados</b><br>para que no se incline.',
    ['Ahora tú. Una columna de tubo cuadrado va soldada sobre su placa base.', 'Numera en qué orden sueldas los cuatro lados, para que no se incline.'],
    '1 y 2: <b class="nar">dos lados opuestos</b> (norte y sur)<br>3 y 4: <b class="nar">los otros dos opuestos</b> (este y oeste)<br>Y revisa el plomo después de los dos primeros',
    ['Primero, dos lados opuestos, por ejemplo el de adelante y el de atrás. Así los dos jalones se compensan.',
     'Después, los otros dos opuestos. Y entre medio, revisa el plomo: si se inclinó, corriges antes de terminar.']),
  *ejercicio(2,
    'Al soldar una cartela en T, la pieza vertical<br>se te inclina <b class="nar">2°</b> hacia el cordón.<br>¿Cómo armas la siguiente?',
    ['Segundo ejercicio. Al soldar una cartela en T, la pieza de arriba se inclina dos grados hacia el lado del cordón.', '¿Cómo armas la siguiente para que salga recta?'],
    'Pre-deformar: puntéala inclinada <b class="nar">2° hacia el lado contrario</b><br>Al enfriarse, el cordón la jala y queda <b class="nar">recta</b>',
    ['La armas inclinada dos grados hacia el lado contrario, y la punteas así.',
     'Cuando el cordón se encoja, la va a jalar esos dos grados, y queda recta. Eso es pre-deformar.']),
  faq([
    ('¿Puedo enderezar con soplete?', 'Sí, con experiencia: calor en zonas y dejar enfriar al aire.', '¿Se puede enderezar una pieza con soplete? Sí, calentando zonas pequeñas y dejando enfriar al aire. Pide experiencia: hazlo con alguien que sepa.'),
    ('¿Enfriar con agua para avanzar?', 'No: endurece y puede rajar el cordón.', '¿Puedo echarle agua para que enfríe rápido? No. El cambio brusco puede endurecer y rajar el cordón.'),
    ('¿Cada cuánto se puntea el arco?', 'En todos los nudos antes de soldar ninguno.', '¿Cuántos puntos lleva el arco antes de soldar? Todos los nudos punteados, antes de soldar el primero completo.'),
  ]),
  repaso([
    ('¿Por qué se tuerce una pieza al soldar?', 'Porque el cordón se encoge al enfriarse y jala.'),
    ('¿Desde dónde empiezas a soldar el arco?', 'Desde el centro hacia los extremos.'),
    ('¿Qué es pre-deformar?', 'Armar la pieza inclinada al revés de lo que va a jalar.'),
    ('¿Cuándo sueltas el arco de la mesa?', 'Cuando ya se enfrió.'),
  ]),
]

# ───────────── Clase 7 · Defectos e inspección ─────────────
EXT['sold_c7'] = [
  dict(inicio=True, frases=[
    'La respuesta del reto de la clase pasada: el arco con once nudos, numerados en el orden en que se sueldan.',
    'El uno, en el nudo del centro. El dos y el tres, uno a cada lado. El cuatro y el cinco, un nudo más afuera.',
    'Y así, alternando, hasta los apoyos, donde van el diez y el once. Si tu secuencia va del centro hacia afuera, alternando, está perfecta.',
  ], zoom=[(0, 1.0, 50, 50), (2, 1.04, 50, 55)], html=titulo('Respuesta: <span class="nar">secuencia de 11 nudos</span>', top=90) + svg(
    '<path d="M260 760 Q960 120 1660 760" fill="none" stroke="#9aa6b0" stroke-width="10"/>' +
    ''.join(
      (lambda k, x: (lambda y, orden: f'<circle class="pop" data-en="{1 if orden < 5 else 2}" data-mas="{0.35 * (orden if orden < 5 else orden - 5):.2f}" cx="{x}" cy="{y}" r="36" fill="#f97316" stroke="#fff" stroke-width="4"/>'
                                     f'<text class="pop" data-en="{1 if orden < 5 else 2}" data-mas="{0.35 * (orden if orden < 5 else orden - 5):.2f}" x="{x}" y="{y + 12}" fill="#fff" font-size="34" font-weight="900" text-anchor="middle">{orden + 1}</text>')
       (760 - 320 * (1 - ((x - 960) / 700) ** 2), [10, 8, 6, 4, 2, 0, 1, 3, 5, 7, 9][k]))(k, 260 + k * 140)
      for k in range(11)) +
    f'<text x="960" y="660" fill="#fff" font-size="30" {T} text-anchor="middle">del centro hacia los apoyos, alternando</text>')),
  ejemplo('Lo que acepta la norma <span class="nar">(carga estática)</span>', [
    'Antes de los errores, los números del inspector, en una sola tabla. Criterios visuales de la AWS D uno punto uno para carga estática.',
    'Fisuras: ninguna. Cráteres: llenos. Fusión: completa.',
    'Socavación, en planchas de menos de veinticinco milímetros: hasta un milímetro. Filete chico: hasta uno punto seis milímetros menos, en no más del diez por ciento del largo.',
    'Y poros visibles: la suma de sus diámetros no puede pasar de diez milímetros en cada veinticinco milímetros de cordón.',
  ], ['Defecto', 'Se acepta si…'],
    [['Fisura', 'Nunca'], ['Cráter', 'Lleno'], ['Socavación (plancha < 25 mm)', 'Hasta 1 mm de profundidad'],
     ['Filete chico', 'Hasta 1.6 mm menos, en ≤ 10 % del largo'], ['Poros visibles', 'Suma ≤ 10 mm en cada 25 mm']],
    lambda i: [1, 1, 2, 2, 3][i], izq=300, der=300, tam=29),
  caso('lo pintaron antes de revisar', [
    'Caso de obra: para entregar rápido, el taller pintó los arcos con anticorrosivo apenas terminó de soldar.',
    'El inspector rascó la pintura en tres nudos al azar, y en dos encontró escoria sin picar y un cráter abierto. Mandó despintar todos los nudos.',
    'Dos días de trabajo y la pintura perdida. Inspecciona primero, repara, y recién pinta.',
  ], [('🎨', 'Pintaron <b class="nar">antes de inspeccionar</b>'), ('🔍', 'El inspector rascó: <b class="nar">escoria y cráter</b>'), ('⏳', 'Despintar todo: <b class="nar">dos días perdidos</b>')]),
  *ejercicio(1,
    'Una placa base lleva <b class="nar">160 cm</b> de filete de 5 mm.<br>Con la galga, en <b class="nar">12 cm</b> mide 4 mm; en el resto, 5 mm.<br>¿Se acepta?',
    ['Ahora tú. Una placa base lleva ciento sesenta centímetros de filete de cinco milímetros.', 'Con la galga, en doce centímetros mide cuatro milímetros, y en el resto mide cinco. ¿Se acepta?'],
    'Falta: 5 − 4 = <b class="nar">1 mm</b> (menos de 1.6 mm ✓)<br>Largo: 12 ÷ 160 = <b class="nar">7.5 %</b> (menos del 10 % ✓)<br><b class="nar">Se acepta</b>',
    ['Le falta un milímetro: menos de uno punto seis. Bien.',
     'Y el tramo chico es doce entre ciento sesenta: siete y medio por ciento, menos del diez. Se acepta.']),
  *ejercicio(2,
    'En una plancha de <b class="nar">8 mm</b> encuentras una socavación de <b class="nar">1.5 mm</b> de profundidad<br>en 5 cm del borde del cordón. ¿Se acepta? ¿Cómo la reparas?',
    ['Segundo ejercicio. En una plancha de ocho milímetros, encuentras una socavación de uno punto cinco milímetros de profundidad, en cinco centímetros del borde del cordón.', '¿Se acepta? Y si no, ¿cómo la reparas?'],
    'No se acepta: pasa de <b class="nar">1 mm</b><br>Reparación: limpia y rellena con un <b class="nar">cordón fino</b>, con menos amperaje y buen ángulo',
    ['No se acepta: en planchas de menos de veinticinco milímetros, el límite es un milímetro.',
     'La reparas limpiando la zona y rellenando con un cordón fino, con un poco menos de amperaje y apuntando bien al borde.']),
  faq([
    ('¿Qué son los tintes penetrantes?', 'Un ensayo barato que revela fisuras finas.', '¿Qué son los tintes penetrantes? Un ensayo sencillo y barato: un líquido de color entra en las fisuras finas y un revelador las hace visibles.'),
    ('¿Cuándo piden ultrasonido?', 'En uniones de penetración completa importantes.', '¿Cuándo te piden ultrasonido? En uniones de penetración completa importantes, como empalmes que cargan. Lo hace un técnico calificado.'),
    ('¿Quién puede inspeccionar?', 'Un inspector calificado, como un CWI, o la supervisión.', '¿Quién puede inspeccionar? Un inspector de soldadura calificado, por ejemplo un C W I, o la supervisión que el cliente designe.'),
  ]),
  repaso([
    ('¿Cuál es el único defecto que nunca se acepta?', 'La fisura.'),
    ('¿Cuánta socavación se acepta en planchas delgadas?', 'Hasta un milímetro.'),
    ('¿Cómo se repara una fisura?', 'Esmerilando hasta eliminarla completa, y volviendo a soldar.'),
    ('¿Cuándo se pinta?', 'Después de inspeccionar y reparar.'),
  ]),
]

# ───────────── Clase 8 · En obra, MIG y costos ─────────────
EXT['sold_c8'] = [
  ejemplo('¿De dónde salen <span class="nar">los 150 metros</span>?', [
    'Antes de los errores: ¿de dónde salieron los ciento cincuenta metros de cordón del almacén? Así se cuentan.',
    'Los nudos de los siete arcos: unas doscientas ochenta uniones, de unos dieciocho centímetros cada una. Unos cincuenta metros.',
    'Las catorce placas base, con unos sesenta centímetros por columna: ocho metros y medio. Las correas sobre los arcos: unos cuarenta metros.',
    'Y empalmes, cartelas, arriostres y portón: unos cincuenta metros más. En total, ciento cincuenta. Cuéntalo así en cada obra.',
  ], ['Parte', 'Cálculo', 'Metros'],
    [['Nudos de arcos', '280 × 0.18 m', '≈ 50 m'], ['Placas base', '14 × 0.60 m', '≈ 8.5 m'], ['Correas sobre arcos', 'apoyos × largo de cordón', '≈ 40 m'],
     ['Empalmes, cartelas, arriostres, portón', 'por pieza', '≈ 50 m'], ['Total', '', '≈ 150 m']],
    lambda i: [1, 2, 2, 3, 3][i], izq=220, der=220),
  ejemplo('Electrodo o MIG: <span class="nar">dónde rinde cada uno</span>', [
    'Ahora, cuándo conviene cada proceso.',
    'En el taller, sin viento, con mucho cordón en serie: el MIG avanza mucho más rápido, sin cambiar electrodos ni picar tanta escoria.',
    'En la obra, con viento: electrodo. O alambre tubular autoprotegido, que no necesita gas.',
    'Y en piezas delgadas, el MIG también gana: menos calor y menos perforaciones.',
  ], ['Situación', 'Conviene'],
    [['Taller, cordones largos en serie', 'MIG'], ['Obra con viento', 'Electrodo o alambre tubular sin gas'], ['Tubo delgado', 'MIG (o 6013 fino)'], ['Pocas uniones sueltas', 'Electrodo']],
    lambda i: [1, 2, 3, 3][i], izq=300, der=300),
  caso('el MIG en el viento', [
    'Caso de obra: para avanzar rápido, soldaron las correas del techo con MIG y gas, con el viento de la tarde.',
    'Al día siguiente, todas las uniones estaban llenas de poros. El viento se había llevado el gas. Hubo que esmerilar y volver a soldar con electrodo.',
    'En obra, sin protección contra el viento, nada de MIG con gas. Electrodo, o alambre tubular sin gas.',
  ], [('🌬️', 'MIG con gas <b class="nar">en el viento</b>'), ('🫧', 'Todas las uniones <b class="nar">con poros</b>'), ('✅', 'En obra: <b class="nar">electrodo</b> o tubular sin gas')]),
  *ejercicio(1,
    'Un trabajo de taller lleva <b class="nar">60 m de cordón</b>. Con los datos del almacén:<br>0.28 kg/m · 14 % de desperdicio · S/ 19 el kilo<br>20 m por día · soldador + ayudante: <b class="nar">S/ 200</b> por día · consumibles <b class="nar">S/ 60</b><br>¿Cuánto cuesta la soldadura?',
    ['Ahora tú. Un trabajo de taller lleva sesenta metros de cordón. Usa los datos del almacén.',
     'Cero punto veintiocho kilos por metro, catorce por ciento de desperdicio, diecinueve soles el kilo. Veinte metros por día, doscientos soles por día entre soldador y ayudante, y sesenta soles de consumibles. ¿Cuánto cuesta la soldadura?'],
    'Electrodo: 60 × 0.28 ÷ 0.86 ≈ <b class="nar">19.5 kg</b> × 19 ≈ <b class="nar">S/ 371</b><br>Mano de obra: 60 ÷ 20 = 3 días × 200 = <b class="nar">S/ 600</b><br>+ consumibles S/ 60 → Total ≈ <b class="nar">S/ 1 031</b> (≈ S/ 17 por metro)',
    ['Electrodo: sesenta por cero punto veintiocho, entre cero punto ochenta y seis: unos diecinueve kilos y medio. Por diecinueve soles: trescientos setenta y uno.',
     'Mano de obra: sesenta metros entre veinte, tres días, por doscientos: seiscientos soles. Más sesenta de consumibles.',
     'Total: unos mil treinta y un soles. Otra vez, unos diecisiete soles por metro. Ese número es tu referencia.']),
  *ejercicio(2,
    'Esos mismos 60 m, pero <b class="nar">en la obra, en altura</b>:<br>el rendimiento baja a <b class="nar">10 m por día</b> y alquilas andamio a <b class="nar">S/ 30 por día</b>.<br>¿Cuánto cobras?',
    ['Segundo ejercicio. Esos mismos sesenta metros, pero en la obra, en altura.', 'El rendimiento baja a diez metros por día, y alquilas andamio a treinta soles por día. ¿Cuánto cobras?'],
    'Días: 60 ÷ 10 = <b class="nar">6</b> → mano de obra <b class="nar">S/ 1 200</b><br>Andamio: 6 × 30 = <b class="nar">S/ 180</b> · electrodo S/ 371 · consumibles S/ 60<br>Total ≈ <b class="nar">S/ 1 811</b> · casi <b class="nar">S/ 800 más</b> que en el taller',
    ['Seis días: mil doscientos soles de mano de obra. Más ciento ochenta de andamio, trescientos setenta y uno de electrodo y sesenta de consumibles.',
     'Total: unos mil ochocientos once soles. Casi ochocientos más que en el taller. Por eso la soldadura en obra se cotiza aparte.']),
  faq([
    ('¿Cobro por metro de cordón o por día?', 'Calcula por día; cotiza por partida.', '¿Cobro por metro o por día? Calcula con días y rendimiento, como hicimos, y en la cotización preséntalo por partidas.'),
    ('¿Qué alambre MIG para obra?', 'Tubular autoprotegido, sin gas.', '¿Qué alambre uso en obra? Alambre tubular autoprotegido, que no necesita gas. Revisa en la caja que sirva para estructura.'),
    ('¿Incluyo la garantía en el precio?', 'Sí: una pequeña reserva para reparaciones.', '¿Incluyo la garantía en el precio? Sí. Deja una pequeña reserva para las reparaciones que puedan salir.'),
  ]),
  repaso([
    ('¿Qué se suelda en el taller y qué en la obra?', 'Todo lo posible en el taller; en obra, solo lo inevitable.'),
    ('¿Por qué no MIG con gas en obra con viento?', 'Porque el viento se lleva el gas y salen poros.'),
    ('¿Cuánto cuesta más o menos un metro de cordón en taller?', 'Unos diecisiete soles, con los datos del curso.'),
    ('¿Cómo presentas la soldadura en la cotización?', 'En partidas separadas: taller y obra.'),
  ]),
]

# ───────────── Clase 9 · Las 4 posiciones ─────────────
EXT['sold_c9'] = [
  ejemplo('¿Qué te habilita <span class="nar">cada prueba</span>?', [
    'Antes de los errores, por qué importan las posiciones en tu certificado. Según la AWS D uno punto uno, en plancha con ranura:',
    'Si apruebas en uno G, quedas para soldar en plano. Con dos G: plana y horizontal.',
    'Con tres G: plana, horizontal y vertical. Con cuatro G: plana y sobre cabeza.',
    'Y si apruebas tres G y cuatro G, quedas para todas las posiciones. Por eso es la combinación que más piden.',
  ], ['Prueba aprobada', 'Te habilita para'],
    [['1G', 'Plana'], ['2G', 'Plana y horizontal'], ['3G', 'Plana, horizontal y vertical'], ['4G', 'Plana y sobre cabeza'], ['3G + 4G', 'Todas las posiciones']],
    lambda i: [1, 1, 2, 2, 3][i], izq=380, der=380),
  caso('lo soldaron sobre cabeza sin necesidad', [
    'Caso de obra: en una cochera, soldaron las correas desde abajo, sobre cabeza, con el techo ya armado. Tres días, con el cuello torcido.',
    'Si las hubieran soldado desde arriba, antes de colocar la cobertura, eran filetes en plano. Un día y medio, y mejores cordones.',
    'Planifica el orden de la obra para soldar siempre en la posición más fácil. Eso también es saber soldar.',
  ], [('🙃', 'Correas soldadas <b class="nar">sobre cabeza</b>: 3 días'), ('⬇️', 'Desde arriba, antes de la cobertura: <b class="nar">en plano</b>'), ('🗓️', 'Planifica para la <b class="nar">posición más fácil</b>')]),
  *ejercicio(1,
    'En plano sueldas bien a <b class="nar">125 A</b> con 7018 de 3.2 mm.<br>¿Con cuánto empiezas en <b class="nar">vertical subiendo</b>?',
    ['Ahora tú. En plano sueldas bien a ciento veinticinco amperios, con siete cero dieciocho de tres punto dos.', '¿Con cuánto empiezas en vertical, subiendo?'],
    'Bajas 10 a 15 %: 125 × 0.85 a 125 × 0.90<br>= <b class="nar">106 a 112 A</b> → empieza en <b class="nar">≈ 110 A</b> y prueba',
    ['Bajas entre diez y quince por ciento: de ciento seis a ciento doce amperios.',
     'Empieza en unos ciento diez, haz tu cordón de prueba en vertical, y ajusta.']),
  *ejercicio(2,
    '¿Qué posición es cada una?<br>a) Plancha a tope en la mesa · b) Filete subiendo por una columna<br>c) Filete bajo una viga, mirando hacia arriba<br>d) Filete de la columna sobre su placa base, en el piso',
    ['Segundo ejercicio. Di la posición de cada soldadura.',
     'a: plancha a tope en la mesa. b: filete subiendo por una columna. c: filete bajo una viga, mirando hacia arriba. Y d: el filete de la columna sobre su placa base, en el piso.'],
    'a) <b class="nar">1G</b> · b) <b class="nar">3F</b><br>c) <b class="nar">4F</b> · d) <b class="nar">2F</b> (filete horizontal)',
    ['a: uno G, a tope en plano. b: tres F, filete vertical.',
     'c: cuatro F, filete sobre cabeza. Y d: dos F. El cordón corre horizontal alrededor de la columna, en la esquina con la placa.']),
  faq([
    ('¿Vertical bajando con 7018?', 'No: con 7018 siempre subiendo.', '¿Puedo soldar en vertical bajando con siete cero dieciocho? No. Con siete cero dieciocho, siempre subiendo. Bajando no funde bien.'),
    ('¿Qué protejo sobre cabeza?', 'Cuello, orejas y cabeza: gorro y cuello de cuero.', '¿Qué protejo sobre cabeza? Cuello, orejas y cabeza: gorro de soldador y protector de cuello de cuero. Las gotas caen hacia ti.'),
    ('¿Qué electrodo es más fácil en vertical?', 'El 6011 y el 6013 perdonan más; el 7018 da más calidad.', '¿Qué electrodo es más fácil en vertical? El seis cero once y el seis cero trece perdonan más. Pero en lo que carga, siete cero dieciocho.'),
  ]),
  repaso([
    ('¿Qué significan la F y la G?', 'F es filete y G es ranura, a tope.'),
    ('¿Qué pruebas te habilitan todas las posiciones?', 'Tres G y cuatro G juntas.'),
    ('¿Cuál es la regla más rentable?', 'Mover la pieza, no el cuerpo.'),
    ('¿Cómo es el charco en posición?', 'Pequeño, para que no se caiga.'),
  ]),
]

# ───────────── Clase 10 · Tubos y perfiles delgados ─────────────
EXT['sold_c10'] = [
  ejemplo('Delgado: <span class="nar">electrodo y amperaje</span>', [
    'Antes de los errores, una tabla de partida para lo delgado, con seis cero trece.',
    'Tubo de uno a uno y medio milímetros: electrodo de dos milímetros, entre cuarenta y cincuenta y cinco amperios. O de dos y medio, desde sesenta.',
    'Dos milímetros: dos y medio, de sesenta a setenta y cinco. Y tres milímetros: dos y medio, de setenta a noventa.',
    'Con MIG: alambre de cero punto ocho, en las regulaciones más bajas de tu máquina, siempre probando en un retazo del mismo tubo.',
  ], ['Espesor del tubo', 'Electrodo 6013', 'Amperaje de partida'],
    [['1.0 – 1.5 mm', '2.0 mm (o 2.5 mm)', '40 – 55 A (60 A con 2.5)'], ['2.0 mm', '2.5 mm', '60 – 75 A'], ['3.0 mm', '2.5 mm', '70 – 90 A'], ['MIG', 'Alambre 0.8 mm', 'Lo más bajo y probar']],
    lambda i: [1, 2, 2, 3][i], izq=220, der=220),
  caso('la baranda perforada', [
    'Caso de obra: una baranda de tubo de cero punto nueve milímetros. El soldador usó el seis cero trece de tres punto dos, porque era lo que tenía.',
    'Cada unión terminó con un hueco tapado a la fuerza, con bolas de soldadura. Al esmerilarlas para que se vean bien, se abrían de nuevo.',
    'Con electrodo de dos milímetros, o con MIG, y puntos encadenados, la baranda habría quedado limpia a la primera.',
  ], [('🕳️', 'Tubo de 0.9 mm con electrodo de <b class="nar">3.2 mm</b>'), ('⚫', 'Huecos tapados con <b class="nar">bolas de soldadura</b>'), ('✅', 'Electrodo de 2 mm o MIG, <b class="nar">puntos encadenados</b>')]),
  *ejercicio(1,
    'Baranda de tubo cuadrado de <b class="nar">1½" × 1.5 mm</b>.<br>Cada unión en T tiene <b class="nar">4 caras</b> de 3.8 cm.<br>¿En cuántos tramos sueldas cada cara y en qué orden?',
    ['Ahora tú. Una baranda de tubo cuadrado de una y media pulgada por uno punto cinco milímetros.', 'Cada unión en T tiene cuatro caras de tres coma ocho centímetros. ¿En cuántos tramos sueldas cada cara, y en qué orden?'],
    'Tramos de ≈ 2 cm: <b class="nar">2 por cara</b> → 8 tramos por unión<br>Orden: <b class="nar">caras opuestas alternadas</b> (arriba, abajo, izquierda, derecha)<br>y deja enfriar un poco entre tramo y tramo',
    ['Tramos de unos dos centímetros: dos por cara, ocho por unión.',
     'Y el orden: caras opuestas, alternando arriba, abajo, izquierda y derecha, dejando enfriar un momento entre uno y otro.']),
  *ejercicio(2,
    'Vas a unir un tubo de <b class="nar">1.5 mm</b> a una plancha de <b class="nar">6 mm</b>.<br>¿Hacia dónde apuntas el arco y por qué?',
    ['Segundo ejercicio. Vas a unir un tubo de uno punto cinco milímetros a una plancha de seis.', '¿Hacia dónde apuntas el arco, y por qué?'],
    'Hacia la <b class="nar">plancha gruesa</b>: ella aguanta el calor<br>y deja que el charco <b class="nar">"lame" al tubo</b> sin perforarlo',
    ['Hacia la plancha gruesa. Ella aguanta el calor.',
     'Y dejas que el charco llegue al tubo y lo moje, sin apuntarle directo. Así no lo perforas.']),
  faq([
    ('¿Y el estaño o la soldadura autógena?', 'No sirven para uniones que cargan.', '¿Y si mejor uso soldadura de estaño? No. El estaño no sirve para uniones que cargan, como una baranda.'),
    ('¿Puedo tapar un hueco?', 'Sí: deja enfriar y ciérralo con puntos desde el borde.', '¿Cómo tapo un hueco que ya se abrió? Deja enfriar, y ciérralo con puntos cortos desde el borde hacia el centro.'),
    ('¿MIG o electrodo para rejas?', 'MIG si hay mucho; 6013 fino si son pocas.', '¿Para rejas, MIG o electrodo? Si es mucho trabajo, MIG. Si son pocas piezas, seis cero trece fino.'),
  ]),
  repaso([
    ('¿Qué electrodo para tubo de uno y medio milímetros?', 'Seis cero trece de dos o dos y medio milímetros.'),
    ('¿Cómo son los cordones en delgado?', 'Cortos, de dos o tres centímetros, o puntos encadenados.'),
    ('¿Qué corte usan los tubos redondos que se cruzan?', 'Boca de pescado.'),
    ('¿Qué haces con los extremos abiertos?', 'Taparlos para que no entre agua.'),
  ]),
]

# ───────────── Clase 11 · Galvanizado e inoxidable ─────────────
EXT['sold_c11'] = [
  respuesta('tubos de 1.5 mm en T', [
    'La respuesta del reto de la clase pasada: dos tubos de uno y medio milímetros en T.',
    'Seis cero trece de dos o dos y medio, entre cincuenta y sesenta y cinco amperios. Puntos en las cuatro esquinas, sin abertura.',
    'Cordones de dos centímetros, alternando caras opuestas, y dejando enfriar entre uno y otro. Sin huecos: aprobado.',
  ], ['Paso', 'Cómo'],
    [['Electrodo', '6013 de 2 o 2.5 mm · 50 – 65 A'], ['Armado', 'Puntos en 4 esquinas, sin abertura'], ['Soldadura', 'Tramos de 2 cm, caras opuestas, enfriar']], lambda i: i),
  ejemplo('El electrodo para <span class="nar">cada unión</span>', [
    'Antes de los errores, la tabla que resuelve el reto de hoy, con las uniones más comunes.',
    'Inoxidable trescientos cuatro con trescientos cuatro: E trescientos ocho L. Trescientos dieciséis con trescientos dieciséis: E trescientos dieciséis L.',
    'Inoxidable con acero común: E trescientos nueve L, que aguanta la mezcla de los dos metales.',
    'Y galvanizado con galvanizado: quitas el zinc, sueldas con seis cero once, seis cero trece o siete cero dieciocho, y repones la protección con galvanizado en frío.',
  ], ['Unión', 'Electrodo', 'Protección al final'],
    [['Inox 304 + 304', 'E308L', 'Decapado'], ['Inox 316 + 316', 'E316L', 'Decapado'], ['Inox + acero común', 'E309L', 'Decapado + pintura en el fierro'],
     ['Galvanizado + galvanizado', '6011 / 6013 / 7018', 'Galvanizado en frío']],
    lambda i: [1, 1, 2, 3][i], izq=220, der=220),
  caso('el pasamanos con puntos de óxido', [
    'Caso de obra: un pasamanos de inoxidable, bien soldado, con el electrodo correcto. A las semanas apareció óxido en puntitos, por toda la superficie.',
    'La causa: en el mismo taller esmerilaban fierro, y las chispas y el polvo de acero se pegaron al inoxidable. Ese polvo es el que se oxidó.',
    'Lo correcto: trabaja el inox lejos del fierro, o tápalo. Y al final, limpia con pasta decapante y enjuaga.',
  ], [('🟤', 'Óxido en puntitos <b class="nar">en todo el inox</b>'), ('✨', 'Polvo de <b class="nar">fierro</b> esmerilado cerca'), ('✅', 'Inox <b class="nar">lejos del fierro</b> + decapado final')]),
  *ejercicio(1,
    'Una cocina industrial de inox <b class="nar">304</b> lleva patas que se sueldan<br>a un bastidor de <b class="nar">fierro pintado</b>.<br>¿Qué electrodo usas en cada unión y cómo la proteges?',
    ['Ahora tú. Una cocina industrial de inoxidable trescientos cuatro lleva patas que se sueldan a un bastidor de fierro pintado.', '¿Qué electrodo usas en cada unión, y cómo la proteges?'],
    'Inox con inox: <b class="nar">E308L</b> + decapado<br>Inox con fierro: <b class="nar">E309L</b>, quitando antes la pintura<br>Al final: decapado en el inox y <b class="nar">anticorrosivo</b> en el fierro',
    ['Inox con inox: E trescientos ocho L, y decapado al final.',
     'Patas de inox al bastidor de fierro: E trescientos nueve L, quitando antes la pintura. Y al terminar, decapado en el inox y anticorrosivo en el fierro.']),
  *ejercicio(2,
    'Un cerco de tubo galvanizado lleva <b class="nar">48 uniones</b>.<br>Cada una deja <b class="nar">100 cm²</b> de acero desnudo.<br>El galvanizado en frío rinde <b class="nar">2 m² por litro</b> a dos manos. ¿Cuánto compras?',
    ['Segundo ejercicio. Un cerco de tubo galvanizado lleva cuarenta y ocho uniones. Cada una deja cien centímetros cuadrados de acero desnudo.',
     'El galvanizado en frío rinde dos metros cuadrados por litro, a dos manos. ¿Cuánto compras?'],
    'Área: 48 × 100 cm² = 4 800 cm² = <b class="nar">0.48 m²</b><br>Pintura: 0.48 ÷ 2 = <b class="nar">0.24 L</b> → compra un envase de <b class="nar">¼ de galón</b>',
    ['Cuarenta y ocho por cien: cuatro mil ochocientos centímetros cuadrados. O sea, cero punto cuarenta y ocho metros cuadrados.',
     'Entre dos metros por litro: un cuarto de litro, más o menos. Con un envase chico, de un cuarto de galón, te sobra.']),
  faq([
    ('¿Puedo soldar inox con MIG?', 'Sí, con alambre de inox y su gas.', '¿Se puede soldar inoxidable con MIG? Sí, con alambre de inoxidable y el gas que indique el fabricante.'),
    ('¿El imán sirve para saber si es inox?', 'Ayuda: el 304 casi no se pega, pero no es prueba final.', '¿Un imán sirve para saber si es inoxidable? Ayuda: el trescientos cuatro casi no se pega. Pero no es una prueba definitiva.'),
    ('¿Por qué la L en E308L?', 'Bajo carbono: resiste mejor la corrosión al soldar.', '¿Qué significa la L de E trescientos ocho L? Bajo carbono. Resiste mejor la corrosión en la zona que se calentó.'),
  ]),
  repaso([
    ('¿Qué haces antes de soldar galvanizado?', 'Quitar el zinc y ventilar.'),
    ('¿Qué electrodo para inox con fierro?', 'E trescientos nueve L.'),
    ('¿Qué herramientas usas en inox?', 'Solo las de inox, marcadas.'),
    ('¿Cómo se limpia el inox al final?', 'Con pasta decapante y un buen enjuague.'),
  ]),
]

# ───────────── Clase 12 · La prueba de calificación ─────────────
EXT['sold_c12'] = [
  ejemplo('La prueba, <span class="nar">medida por medida</span>', [
    'Antes de los errores, cómo es una plancha de prueba muy común, con la AWS D uno punto uno.',
    'Dos planchas de diez milímetros, de unos quince centímetros de ancho, con bisel de cuarenta y cinco grados en total, y una abertura de raíz de unos seis milímetros.',
    'Abajo, una platina de respaldo de unos seis a diez milímetros de espesor y unos veinticinco de ancho, bien punteada por fuera de la zona de la prueba.',
    'Las medidas exactas te las da el procedimiento del lugar donde te evalúan. Pídelo antes y practica con esas mismas medidas.',
  ], ['Parte', 'Medida típica'],
    [['Planchas', '10 mm (3/8") de espesor'], ['Bisel', '45° en total'], ['Abertura de raíz', '≈ 6 mm'], ['Respaldo', '≈ 6 a 10 × 25 mm, punteado por fuera']],
    lambda i: [1, 1, 1, 2][i], izq=360, der=360),
  ejemplo('Cómo se ve <span class="nar">una probeta que pasa</span>', [
    'Y cuando doblan tu probeta, esto es lo que mira el inspector.',
    'Pasa: la cara estirada sin grietas, o con alguna indicación muy pequeña, de menos de unos tres milímetros.',
    'No pasa: una grieta abierta de más de tres milímetros, o una raíz que se abre porque no fundió contra el respaldo.',
  ], ['Lo que ve', 'Resultado'],
    [['Superficie estirada sin grietas', 'Aprobada'], ['Indicación menor a ≈ 3 mm', 'Aprobada'], ['Grieta mayor a ≈ 3 mm', 'Rechazada'], ['Raíz abierta, sin fusión', 'Rechazada']],
    lambda i: [1, 1, 2, 2][i], izq=380, der=380),
  caso('aprobó la cara, falló la raíz', [
    'Caso real de taller: un soldador con mucha experiencia en obra se presentó a la prueba sin practicar con respaldo.',
    'La cara de su plancha se veía impecable. Pero al doblar la probeta de raíz, se abrió: la raíz no había fundido contra la platina.',
    'Practicó dos semanas solo raíces, cortándolas y doblándolas en su taller. En el segundo intento, aprobó.',
  ], [('👌', 'La cara: <b class="nar">impecable</b>'), ('💥', 'La raíz: <b class="nar">se abrió al doblar</b>'), ('🔁', 'Dos semanas de raíces → <b class="nar">aprobado</b>')]),
  *ejercicio(1,
    'Te evalúan en <b class="nar">3G</b>. Tienes una hora.<br>Ordena: raíz · relleno · acabado · limpieza · revisión del respaldo · cordón de prueba',
    ['Ahora tú. Te evalúan en tres G, vertical. Ordena estos pasos.', 'Raíz, relleno, acabado, limpieza entre pasadas, revisión del respaldo, y cordón de prueba.'],
    '1. Revisión del respaldo · 2. <b class="nar">Cordón de prueba</b> en un retazo<br>3. Raíz · 4. Limpieza · 5. Relleno (limpiando cada pasada)<br>6. <b class="nar">Acabado</b> parejo, cráter lleno',
    ['Primero, revisa que el respaldo esté pegado, sin luz. Luego, un cordón de prueba en un retazo, para regular la máquina en vertical.',
     'Después, la raíz subiendo, limpieza completa, el relleno limpiando cada pasada, y el acabado parejo, con el cráter lleno.']),
  *ejercicio(2,
    'Te califican en 3G y 4G con electrodo, y después trabajas <b class="nar">8 meses</b><br>solo con MIG, sin usar electrodo.<br>¿Tu certificado de electrodo sigue vigente?',
    ['Segundo ejercicio. Te califican en tres G y cuatro G con electrodo. Después trabajas ocho meses solo con MIG, sin usar electrodo.', '¿Tu certificado de electrodo sigue vigente?'],
    'No: pasaste más de <b class="nar">6 meses</b> sin soldar con ese proceso<br>Hay que <b class="nar">recalificarse</b> con electrodo<br>(lleva un registro de tus trabajos para demostrarlo)',
    ['No. Pasaste más de seis meses sin soldar con ese proceso, así que hay que recalificarse con electrodo.',
     'Por eso es tan importante llevar un registro de tus trabajos: demuestra que sigues usando el proceso.']),
  faq([
    ('¿Dónde me califico?', 'En centros de formación o empresas con inspector calificado.', '¿Dónde me puedo calificar? En centros de formación técnica o en empresas que tengan un inspector de soldadura calificado. Pregunta qué norma y qué procedimiento usan.'),
    ('¿Cuánto cuesta?', 'Varía: incluye material, inspección y ensayos.', '¿Cuánto cuesta? Varía según el lugar: normalmente incluye el material, la inspección y los ensayos de doblado.'),
    ('¿Me sirve en otras empresas?', 'Depende: muchas piden su propia prueba.', '¿El certificado me sirve en cualquier empresa? Depende. Muchas lo aceptan, pero algunas piden su propia prueba. Tu registro de trabajos ayuda.'),
  ]),
  repaso([
    ('¿Qué es la W P S?', 'La receta del procedimiento de soldadura.'),
    ('¿Qué pruebas te habilitan todas las posiciones en plancha?', 'Tres G y cuatro G.'),
    ('¿Cuál es la clave para aprobar?', 'La raíz, bien fundida contra el respaldo.'),
    ('¿Cuándo pierdes la calificación?', 'Si pasas más de seis meses sin soldar con ese proceso.'),
  ]),
]
