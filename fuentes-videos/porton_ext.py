"""Ampliación de «Portones Automáticos» (≈7 min por clase). Misma receta que los demás cursos.
Lo eléctrico es orientación general: la conexión la hace o revisa un electricista, según el CNE."""
from naves_ext import insertar, caja, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · Tipos de portón ─────────────
EXT['porton_c1'] = [
  ejemplo('¿Qué portón <span class="nar">para cada caso</span>?', [
    'Antes de los errores, cuatro situaciones típicas y el portón que suele convenir.',
    'Cochera de casa con muro libre al costado: corredizo. Cochera sin muro libre, pero con espacio adentro y piso plano: batiente.',
    'Cochera con techo alto y poco espacio a los lados: levadizo o seccional.',
    'Y un condominio con muchas aperturas al día: corredizo con motor de uso intensivo.',
  ], ['Situación', 'Conviene'],
    [['Casa, muro libre al costado', 'Corredizo'], ['Sin muro libre, espacio adentro y piso plano', 'Batiente'], ['Techo alto, poco espacio lateral', 'Levadizo o seccional'], ['Condominio, muchas aperturas', 'Corredizo de uso intensivo']],
    lambda i: [1, 1, 2, 3][i], izq=260, der=260),
  ejemplo('Los ciclos <span class="nar">de cada cliente</span>', [
    'Y los ciclos de uso, con números. Un ciclo es abrir y cerrar una vez.',
    'Una casa con dos autos: unos diez ciclos al día. Un edificio de veinte departamentos: unos ochenta.',
    'Un condominio de cuarenta familias: ciento sesenta o más. Para esos usos, el motor de casa no aguanta.',
  ], ['Cliente', 'Ciclos al día (aprox.)', 'Motor'],
    [['Casa', '≈ 10', 'Residencial'], ['Edificio de 20 dptos.', '≈ 80', 'Uso intensivo'], ['Condominio de 40 familias', '≈ 160 o más', 'Uso intensivo / industrial']],
    lambda i: [1, 2, 2][i], izq=260, der=260),
  caso('el corredizo que chocaba', [
    'Caso de obra: se vendió un portón corredizo sin medir bien el muro del costado. Se veía que había espacio.',
    'Al instalarlo, la hoja chocaba con la caja del medidor de luz, a tres metros del vano. El portón solo abría tres cuartos.',
    'Mide el muro libre de punta a punta, y anota todo lo que sobresale: medidores, tubos, ventanas y columnas.',
  ], [('📏', 'Muro "con espacio", <b class="nar">sin medir</b>'), ('⚡', 'La hoja chocaba con el <b class="nar">medidor de luz</b>'), ('✅', 'Mide y anota <b class="nar">todo lo que sobresale</b>')]),
  *ejercicio(1,
    'Un vano de <b class="nar">3.50 m</b>. Quieres un corredizo.<br>¿Cuánto muro libre necesitas al costado, como mínimo?',
    ['Ahora tú. Un vano de tres metros cincuenta. Quieres un portón corredizo.', '¿Cuánto muro libre necesitas al costado, como mínimo?'],
    'El vano más unos 30 cm: 3.50 + 0.30 = <b class="nar">3.80 m</b> libres<br>Sin medidores, tubos ni ventanas en el camino',
    ['El vano más unos treinta centímetros: tres metros ochenta de muro libre.',
     'Y libre de verdad: sin medidores, tubos, ventanas ni columnas que sobresalgan.']),
  *ejercicio(2,
    'Un edificio tiene <b class="nar">24 departamentos</b>. Cada uno abre el portón<br><b class="nar">4 veces al día</b>. ¿Cuántos ciclos son y qué motor eliges?',
    ['Segundo ejercicio. Un edificio tiene veinticuatro departamentos, y cada uno abre el portón unas cuatro veces al día.', '¿Cuántos ciclos son, y qué motor eliges?'],
    '24 × 4 = <b class="nar">96 ciclos al día</b><br>Motor de <b class="nar">uso intensivo</b> (revisa los ciclos en su ficha)<br>Mejor de 24 V, que aguanta más ciclos',
    ['Veinticuatro por cuatro: noventa y seis ciclos al día.',
     'Eso es uso intensivo: un motor hecho para eso, revisando los ciclos en su ficha. Normalmente uno de veinticuatro voltios.']),
  faq([
    ('¿Se puede automatizar un portón viejo?', 'Sí, si corre suave y está firme.', '¿Se puede automatizar un portón viejo? Sí, si corre suave con una mano y su estructura está firme. Si no, primero se arregla.'),
    ('¿Cuál es el más barato?', 'Normalmente el corredizo.', '¿Cuál es el más barato de automatizar? Normalmente el corredizo: un solo motor y sin brazos.'),
    ('¿Y el enrollable?', 'Para locales; necesita espacio arriba para el rollo.', '¿Y el enrollable? Es común en locales comerciales. Necesita espacio arriba para el rollo y su propio motor.'),
  ]),
  repaso([
    ('¿Qué necesita un corredizo?', 'Muro libre al costado: el vano más unos treinta centímetros.'),
    ('¿Qué necesita un batiente?', 'Espacio adentro y piso sin desnivel.'),
    ('¿Qué es un ciclo?', 'Abrir y cerrar una vez.'),
    ('¿Qué se revisa antes de automatizar?', 'Que el portón corra suave a mano.'),
  ]),
]

# ───────────── Clase 2 · Peso y motor ─────────────
EXT['porton_c2'] = [
  ejemplo('Peso de plancha <span class="nar">por espesor</span>', [
    'Antes de los errores, cuánto pesa un metro cuadrado de plancha según el espesor. Espesor por siete punto ochenta y cinco.',
    'Uno punto dos milímetros: unos nueve punto cuatro kilos. Uno punto cinco: once punto ocho. Dos milímetros: quince punto siete.',
    'En nuestra hoja de nueve metros cuadrados y algo, pasar de uno y medio a dos milímetros suma más de treinta y cinco kilos.',
  ], ['Plancha', 'Peso por m²'],
    [['1.2 mm', '≈ 9.4 kg'], ['1.5 mm', '≈ 11.8 kg'], ['2.0 mm', '≈ 15.7 kg']],
    lambda i: [1, 1, 2][i], izq=520, der=520, tam=34),
  caso('el motor justo', [
    'Caso de obra: un portón de doscientos ochenta kilos, con un motor de trescientos. "Total, aguanta".',
    'En verano, con el sol sobre la hoja y el riel con tierra, el motor se calentaba y se apagaba a medio camino. A los ocho meses se quemó.',
    'Con un motor de quinientos o seiscientos, habría trabajado descansado. El margen de una vez y media o dos veces no es un lujo.',
  ], [('⚖️', 'Hoja de 280 kg, motor de <b class="nar">300</b>'), ('🔥', 'Se calentaba y <b class="nar">se quemó</b> en meses'), ('✅', 'Margen de <b class="nar">1.5 a 2 veces</b> el peso')]),
  *ejercicio(1,
    'Hoja de <b class="nar">3.00 × 2.00 m</b>: <b class="nar">18 m</b> de tubo 50 × 50 × 2 (3 kg/m),<br>plancha de <b class="nar">1.5 mm</b>, y unos <b class="nar">15 kg</b> de ruedas, guías y cremallera.<br>¿Cuánto pesa y qué motor eliges?',
    ['Ahora tú. Una hoja de tres por dos metros: dieciocho metros de tubo de cincuenta por cincuenta por dos, de tres kilos por metro, plancha de uno y medio, y unos quince kilos de ruedas, guías y cremallera.', '¿Cuánto pesa, y qué motor eliges?'],
    'Tubo: 18 × 3 = <b class="nar">54 kg</b> · Plancha: 6 m² × 11.8 ≈ <b class="nar">71 kg</b> · Accesorios: <b class="nar">15 kg</b><br>Total ≈ <b class="nar">140 kg</b> → motor de al menos <b class="nar">280 kg</b><br>Elige uno de <b class="nar">400 a 500 kg</b>',
    ['El tubo: cincuenta y cuatro kilos. La plancha: seis metros cuadrados por once punto ocho, unos setenta y uno. Más quince: unos ciento cuarenta kilos.',
     'Con el doble, al menos doscientos ochenta. Elige un motor de cuatrocientos a quinientos kilos, y trabajará tranquilo.']),
  *ejercicio(2,
    'Una hoja recorre <b class="nar">3.50 m</b> y el motor avanza a <b class="nar">12 m por minuto</b>.<br>¿Cuántos segundos tarda en abrir?',
    ['Segundo ejercicio. Una hoja recorre tres metros cincuenta, y el motor avanza a doce metros por minuto.', '¿Cuántos segundos tarda en abrir?'],
    '12 m por minuto = <b class="nar">0.2 m por segundo</b><br>3.50 ÷ 0.2 = <b class="nar">17.5 segundos</b>',
    ['Doce metros por minuto son cero punto dos metros por segundo.',
     'Tres cincuenta entre cero punto dos: diecisiete segundos y medio. Más la frenada suave al final.']),
  faq([
    ('¿Puedo pesar la hoja con balanza?', 'Sí, con dos balanzas bajo las ruedas.', '¿Puedo pesar la hoja? Sí, con dos balanzas de piso bajo las ruedas, y sumas. Si no, calcula en el papel.'),
    ('¿Más potencia es mejor?', 'Hasta cierto punto: la fuerza se regula.', '¿Un motor mucho más grande es mejor? Trabaja más descansado, pero la fuerza igual se regula al mínimo necesario, por seguridad.'),
    ('¿Qué es IP44?', 'Protección contra polvo y salpicaduras.', '¿Qué significa I P cuarenta y cuatro? Que el motor está protegido contra objetos pequeños y salpicaduras de agua.'),
  ]),
  repaso([
    ('¿Cuánto margen lleva el motor?', 'Una vez y media a dos veces el peso real.'),
    ('¿Qué cansa más al motor que el peso?', 'El roce.'),
    ('¿Cuál motor arranca y frena suave?', 'El de veinticuatro voltios.'),
    ('¿Qué pide la ficha de un batiente?', 'Largo máximo y peso máximo por hoja.'),
  ]),
]

# ───────────── Clase 3 · La hoja que corre sola ─────────────
EXT['porton_c3'] = [
  ejemplo('¿Cuánto mide <span class="nar">el riel</span>?', [
    'Antes de los errores, el largo del riel para tres portones. La hoja más lo que recorre.',
    'Hoja de tres metros diez que recorre tres metros: seis metros diez de riel. Hoja de cuatro diez que recorre tres noventa: ocho metros.',
    'Y una hoja de dos noventa que recorre dos ochenta: cinco setenta. Siempre redondea a barras y deja un poco más para los topes.',
  ], ['Hoja', 'Recorrido', 'Riel'],
    [['3.10 m', '3.00 m', '≈ 6.10 m'], ['4.10 m', '3.90 m', '≈ 8.00 m'], ['2.90 m', '2.80 m', '≈ 5.70 m']],
    lambda i: [1, 2, 2][i], izq=400, der=400, tam=32),
  caso('la guía que apretaba', [
    'Caso de obra: un portón nuevo, con motor nuevo, que se apagaba a mitad del recorrido por "sobrecarga".',
    'El técnico cambió la tarjeta, sin resultado. El problema estaba arriba: los rodillos de la guía apretaban la hoja y la frenaban.',
    'Se aflojó la guía, dejando un par de milímetros de juego, y el portón corrió perfecto con el mismo motor.',
  ], [('⚠️', 'El motor se apagaba por <b class="nar">sobrecarga</b>'), ('🔩', 'La guía superior <b class="nar">apretaba</b> la hoja'), ('✅', 'Un par de mm de <b class="nar">juego</b>: corrió perfecto')]),
  *ejercicio(1,
    'Una hoja de <b class="nar">3.90 × 2.40 m</b>. Mides las diagonales:<br><b class="nar">4 583 mm</b> y <b class="nar">4 578 mm</b>.<br>¿Pasa? ¿Cuánto deberían medir?',
    ['Ahora tú. Una hoja de tres noventa por dos cuarenta. Mides las diagonales: cuatro mil quinientos ochenta y tres, y cuatro mil quinientos setenta y ocho.', '¿Pasa? ¿Cuánto deberían medir?'],
    'Deberían medir √(3.90² + 2.40²) ≈ <b class="nar">4 579 mm</b> las dos<br>Diferencia: <b class="nar">5 mm</b> · máximo 2 a 3 mm → <b class="nar">no pasa</b><br>Corrige <b class="nar">antes de soldar completo</b>',
    ['Las dos deberían medir unos cuatro mil quinientos setenta y nueve milímetros.',
     'Hay cinco milímetros de diferencia, y el máximo es dos o tres. No pasa: corrige la escuadra antes de soldar completo.']),
  *ejercicio(2,
    'La hoja hace las tres pruebas sin motor:<br>a) se mueve con una mano ✓ · b) <b class="nar">se va sola hacia la izquierda</b><br>c) roza en un tramo. ¿Qué revisas?',
    ['Segundo ejercicio. La hoja hace las tres pruebas sin motor. Se mueve con una mano: bien. Pero se va sola hacia la izquierda, y roza en un tramo.', '¿Qué revisas?'],
    'Se va sola: el riel <b class="nar">no está a nivel</b> → nivélalo<br>Roza: <b class="nar">guía, ruedas o algo en el riel</b> en ese tramo<br>Recién con las 3 pruebas OK, <b class="nar">va el motor</b>',
    ['Si se va sola, el riel está en pendiente: hay que nivelarlo.',
     'Si roza, revisa la guía superior, la alineación de las ruedas, o algo en el riel justo en ese tramo. Y recién cuando pase las tres pruebas, pones el motor.']),
  faq([
    ('¿Riel en V o ángulo?', 'Los dos; la rueda debe calzar exacto.', '¿Riel en V o ángulo con la punta arriba? Los dos sirven. La rueda debe calzar exacto en el que elijas.'),
    ('¿Cuántas ruedas?', 'Dos, cerca de los extremos.', '¿Cuántas ruedas lleva? Normalmente dos, cerca de los extremos de la hoja, con rodamiento.'),
    ('¿Y el voladizo?', 'Sin riel abajo, pero con cola de casi medio vano.', '¿Cuándo conviene el voladizo? Cuando el piso es de tierra o se ensucia mucho. Pero la cola mide casi la mitad del vano.'),
  ]),
  repaso([
    ('¿Cuánto pueden diferir las diagonales?', 'Dos o tres milímetros como máximo.'),
    ('¿Cómo debe estar el riel?', 'Recto y a nivel.'),
    ('¿Cuánto juego deja la guía?', 'Un par de milímetros.'),
    ('¿Qué son los topes?', 'La última defensa para que la hoja no se salga.'),
  ]),
]

# ───────────── Clase 4 · Motor y cremallera ─────────────
EXT['porton_c4'] = [
  ejemplo('Lo que dice <span class="nar">el ruido</span>', [
    'Antes de los errores, qué te dice cada ruido o síntoma de la cremallera.',
    'Un golpe en el mismo punto, en cada ciclo: un empalme desalineado. Ruido parejo y fuerte: el piñón carga la cremallera, sin holgura.',
    'Salta y patina: demasiada holgura, o la base del motor se movió. Y si se para antes del tope: fin de carrera mal puesto.',
  ], ['Síntoma', 'Causa probable'],
    [['Golpe en el mismo punto', 'Empalme desalineado'], ['Ruido fuerte y parejo', 'Sin holgura: el piñón carga la hoja'], ['Salta o patina', 'Demasiada holgura o base movida'], ['Para antes de llegar', 'Fin de carrera mal ubicado']],
    lambda i: [1, 1, 2, 2][i], izq=300, der=300),
  caso('el piñón que cargaba', [
    'Caso de obra: para que "no salte", el instalador apoyó la cremallera directamente sobre el piñón, sin holgura.',
    'El portón sonaba fuerte desde el primer día. A los meses, el rodamiento del motor estaba gastado: el piñón había cargado el peso de la hoja.',
    'Entre piñón y cremallera, uno a dos milímetros. El peso lo cargan las ruedas, nunca el motor.',
  ], [('⚙️', 'Cremallera <b class="nar">apoyada</b> sobre el piñón'), ('🔊', 'Ruido y <b class="nar">rodamiento gastado</b>'), ('✅', 'Holgura de <b class="nar">1 a 2 mm</b>')]),
  *ejercicio(1,
    'Una hoja de <b class="nar">4.60 m</b> de largo. La cremallera viene en tramos de <b class="nar">1 m</b>.<br>¿Cuántos tramos compras y cómo los empalmas?',
    ['Ahora tú. Una hoja de cuatro metros sesenta de largo. La cremallera viene en tramos de un metro.', '¿Cuántos tramos compras, y cómo los empalmas?'],
    '4.60 m → <b class="nar">5 tramos</b> (el último se corta a 0.60 m)<br>Empalme: un pedazo de cremallera <b class="nar">encima como regla</b><br>para que el paso de los dientes quede igual',
    ['Cuatro sesenta: cinco tramos, y el último se corta a sesenta centímetros.',
     'Cada empalme se hace con un pedazo de cremallera puesto encima, como regla, para que el paso de los dientes no cambie.']),
  *ejercicio(2,
    'El tope mecánico de apertura está a <b class="nar">3.90 m</b> de recorrido.<br>¿Dónde debe parar el motor? ¿Para qué sirve esa diferencia?',
    ['Segundo ejercicio. El tope mecánico de apertura está a tres noventa de recorrido.', '¿Dónde debe parar el motor? ¿Y para qué sirve esa diferencia?'],
    'El fin de carrera para <b class="nar">2 a 3 cm antes</b>: en ≈ <b class="nar">3.87 – 3.88 m</b><br>Así el tope <b class="nar">solo toca si algo falla</b>,<br>y la hoja no golpea en cada ciclo',
    ['El motor debe parar dos o tres centímetros antes: en unos tres ochenta y siete.',
     'Así el tope mecánico solo toca si algo falla. Si el motor para recién en el tope, la hoja golpea en cada ciclo.']),
  faq([
    ('¿Cremallera de nylon o de acero?', 'Nylon para casas; acero para hojas pesadas.', '¿Cremallera de nylon o de acero? La de nylon es silenciosa y va bien en casas. La de acero, para hojas pesadas o uso intensivo.'),
    ('¿Se suelda la cremallera?', 'La de acero se puede soldar o atornillar; la de nylon se atornilla.', '¿La cremallera se suelda? La de acero se puede soldar o atornillar. La de nylon, siempre atornillada.'),
    ('¿Y si el manual se perdió?', 'Búscalo por modelo; no inventes medidas.', '¿Y si se perdió el manual? Búscalo por la marca y el modelo. No inventes las medidas de la base.'),
  ]),
  repaso([
    ('¿Qué holgura lleva el piñón?', 'De uno a dos milímetros.'),
    ('¿Cómo se alinean los empalmes?', 'Con un pedazo de cremallera encima, como regla.'),
    ('¿Qué se deja antes de vaciar la base?', 'El tubo para los cables.'),
    ('¿Dónde para el motor?', 'Dos o tres centímetros antes del tope.'),
  ]),
]

# ───────────── Clase 5 · Portones batientes ─────────────
EXT['porton_c5'] = [
  ejemplo('¿Qué motor <span class="nar">para cada batiente</span>?', [
    'Antes de los errores, los tres motores de batiente, y cuándo conviene cada uno.',
    'Brazo articulado: pilar ancho, con la bisagra lejos de la esquina. Pistón: el más común en casas, para hojas de hasta unos dos metros y medio.',
    'Y el motor enterrado: no se ve, pero necesita una caja en el piso con buen drenaje.',
  ], ['Motor', 'Conviene cuando…'],
    [['Brazo articulado', 'El pilar es ancho y la bisagra queda lejos'], ['Pistón (lineal)', 'Casas, hojas de hasta ≈ 2.5 m'], ['Enterrado', 'Se quiere oculto y hay buen drenaje']],
    lambda i: i + 1, izq=280, der=280),
  caso('las hojas que chocaban', [
    'Caso de obra: un batiente de dos hojas con traslape. Las dos hojas cerraban al mismo tiempo.',
    'La hoja con la pestaña llegaba primero, y la otra chocaba contra ella. A las semanas, la pestaña estaba doblada y la chapa no cerraba.',
    'Se programó el retardo en la tarjeta: la hoja de la pestaña cierra unos segundos después. Y no volvió a pasar.',
  ], [('🚪', 'Dos hojas cerrando <b class="nar">al mismo tiempo</b>'), ('💥', 'La pestaña <b class="nar">se dobló</b>'), ('✅', '<b class="nar">Retardo</b> programado en la tarjeta')]),
  *ejercicio(1,
    'Dos hojas de <b class="nar">1.60 × 2.20 m</b>: cada una con <b class="nar">12 m</b> de tubo (3 kg/m)<br>y plancha de <b class="nar">1.5 mm</b>. ¿Cuánto pesa cada hoja?<br>¿Qué pistón pides?',
    ['Ahora tú. Dos hojas de uno sesenta por dos veinte, cada una con doce metros de tubo de tres kilos por metro, y plancha de uno y medio milímetros.', '¿Cuánto pesa cada hoja? ¿Y qué pistón pides?'],
    'Tubo: 12 × 3 = <b class="nar">36 kg</b> · Plancha: 3.52 m² × 11.8 ≈ <b class="nar">42 kg</b><br>Cada hoja ≈ <b class="nar">80 kg</b> (más bisagras y chapa)<br>Pistón para hojas de <b class="nar">al menos 2 m y 160 kg</b>',
    ['El tubo: treinta y seis kilos. La plancha: tres punto cincuenta y dos metros cuadrados, unos cuarenta y dos. Cada hoja, unos ochenta kilos.',
     'Pide un pistón que admita hojas de al menos dos metros de largo y unos ciento sesenta kilos, con margen. Uno por hoja.']),
  *ejercicio(2,
    'El cliente quiere que el portón abra <b class="nar">110°</b>,<br>pero la tabla del pistón con tus cotas da <b class="nar">95°</b>.<br>¿Qué haces?',
    ['Segundo ejercicio. El cliente quiere que el portón abra ciento diez grados, pero la tabla del pistón, con tus cotas, da noventa y cinco.', '¿Qué haces?'],
    'Buscas en la tabla <b class="nar">otras cotas A y B</b> que den 110°<br>Si el pilar no lo permite: <b class="nar">brazo articulado</b> u otro motor<br>Nunca "forzar" el pistón fuera de la tabla',
    ['Buscas en la tabla otras cotas A y B que den ciento diez grados.',
     'Si el pilar no deja esas cotas, ofreces un brazo articulado u otro motor. Lo que no se hace es forzar el pistón fuera de su tabla.']),
  faq([
    ('¿Un motor para las dos hojas?', 'No: un motor por hoja.', '¿Se puede usar un solo motor para las dos hojas? No. Cada hoja lleva su propio motor.'),
    ('¿Sirve con piso en pendiente?', 'Complica: la hoja raspa o no cierra.', '¿Sirve un batiente con el piso en pendiente? Lo complica mucho: la hoja raspa o queda alta. Mejor corredizo o corregir el piso.'),
    ('¿Y si el pilar es de ladrillo?', 'Refuérzalo o usa una columna metálica anclada.', '¿Y si el pilar es de ladrillo? Hay que reforzarlo, o poner una columna metálica bien anclada, para fijar el pistón.'),
  ]),
  repaso([
    ('¿De qué dependen la apertura y la velocidad del pistón?', 'De las cotas A y B.'),
    ('¿Qué cargan las bisagras?', 'Todo el peso de la hoja.'),
    ('¿Dónde nunca se fija el pistón?', 'En ladrillo hueco ni en tarrajeo.'),
    ('¿Para qué es el retardo?', 'Para que la hoja de la pestaña cierre después.'),
  ]),
]

# ───────────── Clase 6 · Instalación eléctrica ─────────────
EXT['porton_c6'] = [
  ejemplo('Tu lista <span class="nar">para el electricista</span>', [
    'Antes de los errores, la lista de pedido eléctrico para el portón, como se la entregas al electricista.',
    'Circuito exclusivo desde el tablero, con interruptor termomagnético del amperaje del manual, y diferencial de treinta miliamperios.',
    'Cable con su línea de tierra, del calibre que pida el manual, en tubo propio. Y un segundo tubo para los cables de baja tensión.',
    'Cajas de paso donde haga falta, y un pulsador adentro de la casa. El electricista lo conecta y lo revisa según el Código Nacional.',
  ], ['Pedido', 'Detalle'],
    [['Circuito exclusivo', 'Desde el tablero'], ['Protección', 'Termomagnético (según manual) + diferencial 30 mA'], ['Cable', 'Con tierra, calibre según el manual'], ['Tuberías', 'Una de 220 V y otra de baja tensión'], ['Extras', 'Cajas de paso y pulsador interior']],
    lambda i: [1, 1, 2, 2, 3][i], izq=280, der=280),
  caso('el motor en el charco', [
    'Caso de obra: el motor se instaló a ras del piso, junto al vano, porque "así se veía más ordenado".',
    'Con la primera lluvia fuerte, el agua se empozó alrededor y entró por los cables. La tarjeta se quemó.',
    'El motor va sobre su dado de concreto, más alto que el piso, con los cables entrando por abajo y con curva de goteo.',
  ], [('🌧️', 'Motor <b class="nar">a ras del piso</b>'), ('💧', 'El agua entró: <b class="nar">tarjeta quemada</b>'), ('✅', 'Sobre su <b class="nar">dado</b> y con curva de goteo')]),
  *ejercicio(1,
    'El tablero está a <b class="nar">15 m</b> del motor, con un cambio de dirección.<br>¿Qué tuberías y cajas pides?',
    ['Ahora tú. El tablero está a quince metros del motor, con un cambio de dirección en el camino.', '¿Qué tuberías y cajas pides?'],
    '<b class="nar">Dos tubos</b> de unos 15 m: uno para 220 V y otro para baja tensión<br><b class="nar">Caja de paso</b> en el cambio de dirección<br>Sin empalmes dentro del tubo: <b class="nar">solo en cajas</b>',
    ['Dos tubos de unos quince metros: uno para los cables de doscientos veinte, y otro para los de baja tensión, como fotoceldas y pulsador.',
     'Una caja de paso en el cambio de dirección. Y ningún empalme dentro del tubo: solo en las cajas.']),
  *ejercicio(2,
    'Encuentra los errores: el motor está conectado con una <b class="nar">extensión</b>,<br>los cables de fotoceldas van <b class="nar">en el mismo tubo</b> que los de 220 V,<br>y hay un <b class="nar">empalme enterrado</b>.',
    ['Segundo ejercicio. Encuentra los errores. El motor está conectado con una extensión. Los cables de las fotoceldas van en el mismo tubo que los de doscientos veinte. Y hay un empalme enterrado.'],
    '1. Extensión → <b class="nar">circuito exclusivo</b> con protecciones<br>2. Mismo tubo → <b class="nar">tubos separados</b><br>3. Empalme enterrado → <b class="nar">caja de paso</b> accesible<br>Que lo corrija y revise un <b class="nar">electricista</b>',
    ['Tres errores. La extensión: va un circuito exclusivo con sus protecciones. Los cables juntos: van en tubos separados.',
     'Y el empalme enterrado: se hace en una caja de paso accesible. Que lo corrija y lo revise un electricista.']),
  faq([
    ('¿Puedo conectar yo el tablero?', 'Lo hace o revisa un electricista.', '¿Puedo conectar yo al tablero? La conexión a la red la hace o la revisa un electricista, según el Código Nacional de Electricidad.'),
    ('¿Para qué el diferencial?', 'Corta si hay fuga y protege a las personas.', '¿Para qué sirve el diferencial? Corta la corriente si hay una fuga, y protege a las personas de una descarga.'),
    ('¿Dónde va la antena?', 'Alta y lejos de planchas metálicas.', '¿Dónde pongo la antena? En alto y lejos de planchas metálicas, para que el control tenga buen alcance.'),
  ]),
  repaso([
    ('¿De dónde sale el circuito del portón?', 'Del tablero, exclusivo.'),
    ('¿Qué dos protecciones lleva?', 'Termomagnético y diferencial de treinta miliamperios.'),
    ('¿Dónde van los empalmes?', 'Solo en cajas.'),
    ('¿Qué haces antes de tocar un cable?', 'Cortar la energía.'),
  ]),
]

# ───────────── Clase 7 · Seguridad ─────────────
EXT['porton_c7'] = [
  ejemplo('Las protecciones <span class="nar">en una tabla</span>', [
    'Antes de los errores, las protecciones del portón, qué hace cada una y cuándo es obligatoria.',
    'Fotoceldas: detectan si algo corta el rayo. Siempre. Fuerza regulada: detecta el choque. Siempre.',
    'Luz destellante: avisa que se mueve. Obligatoria con cierre automático. Banda de seguridad: retrocede al tocar. Muy recomendable.',
    'Y el desbloqueo con llave: para abrir sin luz. Siempre.',
  ], ['Protección', 'Qué hace', '¿Cuándo?'],
    [['Fotoceldas', 'Detectan si algo corta el rayo', 'Siempre'], ['Fuerza regulada', 'Detecta el choque', 'Siempre'], ['Luz destellante', 'Avisa que se mueve', 'Con cierre automático'],
     ['Banda de seguridad', 'Retrocede al tocar', 'Muy recomendable'], ['Desbloqueo con llave', 'Abrir sin luz', 'Siempre']],
    lambda i: [1, 1, 2, 2, 3][i], izq=220, der=220, tam=29),
  caso('la fuerza al máximo', [
    'Caso de obra: para que el portón "no se trabe", el instalador dejó la fuerza al máximo y sin fotoceldas.',
    'Un día cerró sobre el parachoques de un auto que estaba saliendo, y lo hundió. Pudo haber sido una persona.',
    'Fuerza al mínimo que mueva la hoja, fotoceldas, y la prueba del obstáculo antes de entregar. Siempre.',
  ], [('💪', 'Fuerza <b class="nar">al máximo</b>, sin fotoceldas'), ('🚗', 'Cerró sobre un <b class="nar">auto</b>'), ('✅', 'Fuerza mínima + fotoceldas + <b class="nar">prueba del obstáculo</b>')]),
  *ejercicio(1,
    'Haces la prueba del obstáculo con una caja de cartón:<br>el portón <b class="nar">la toca, se detiene, pero no retrocede</b>.<br>¿Pasa? ¿Qué ajustas?',
    ['Ahora tú. Haces la prueba del obstáculo con una caja de cartón. El portón la toca y se detiene, pero no retrocede.', '¿Pasa? ¿Qué ajustas?'],
    'Debe <b class="nar">detenerse y retroceder</b>: así no pasa del todo<br>Revisa en la tarjeta la <b class="nar">inversión al detectar obstáculo</b><br>y la <b class="nar">fuerza</b>. Repite la prueba hasta que retroceda',
    ['Debe detenerse y retroceder, sin aplastar. Si solo se detiene, la caja queda presa.',
     'Revisa en la tarjeta la función de inversión al detectar obstáculo, y la fuerza. Y repite la prueba hasta que retroceda.']),
  *ejercicio(2,
    'Revisa las <b class="nar">zonas de atrapamiento</b> de un corredizo:<br>¿dónde puede quedar presa una mano o un pie,<br>y cómo lo resuelves?',
    ['Segundo ejercicio. Revisa las zonas de atrapamiento de un portón corredizo.', '¿Dónde puede quedar presa una mano o un pie, y cómo lo resuelves?'],
    '1. Entre la hoja y el <b class="nar">poste de la guía</b> → espacio suficiente o protector<br>2. Entre la hoja y el <b class="nar">muro</b> al abrir → espacio o malla<br>3. Si la hoja tiene huecos → <b class="nar">malla</b> en la parte baja',
    ['Entre la hoja y el poste de la guía, y entre la hoja y el muro cuando abre.',
     'Se resuelven dejando espacio suficiente o con protectores. Y si la hoja tiene huecos, una malla en la parte baja, para que no entre una mano.']),
  faq([
    ('¿A qué altura las fotoceldas?', 'A unos 40 a 50 cm del piso.', '¿A qué altura van las fotoceldas? A unos cuarenta o cincuenta centímetros del piso, donde pasan la gente y los autos.'),
    ('¿Puedo poner dos pares?', 'Sí: más seguridad en vanos anchos.', '¿Puedo poner dos pares de fotoceldas? Sí. En vanos anchos o con mucho tránsito, suma seguridad.'),
    ('¿Cada cuánto pruebo?', 'En cada mantenimiento, cada seis meses.', '¿Cada cuánto se repiten las pruebas? En cada mantenimiento, cada seis meses, y siempre que se cambie algo.'),
  ]),
  repaso([
    ('¿A qué altura van las fotoceldas?', 'Entre cuarenta y cincuenta centímetros.'),
    ('¿Cómo se regula la fuerza?', 'Al mínimo que mueva la hoja de punta a punta.'),
    ('¿Cuándo es obligatoria la luz destellante?', 'Si el portón cierra solo.'),
    ('¿Qué dos pruebas haces delante del cliente?', 'La del obstáculo y la de las fotoceldas.'),
  ]),
]

# ───────────── Clase 8 · Programación, cotización y entrega ─────────────
EXT['porton_c8'] = [
  ejemplo('El margen <span class="nar">en la automatización</span>', [
    'Antes de los errores, el mismo costo de la cochera, dos mil trescientos soles, con distintos márgenes reales.',
    'Con veinte por ciento: dos mil ochocientos setenta y cinco. Con veinticinco: tres mil sesenta y siete, que redondeamos a tres mil cien.',
    'Y con treinta: unos tres mil doscientos ochenta y seis. El margen depende de tu zona y del riesgo; lo importante es calcularlo, no adivinarlo.',
  ], ['Margen real', 'Precio = costo ÷ (1 − margen)'],
    [['20 %', '2 300 ÷ 0.80 = S/ 2 875'], ['25 %', '2 300 ÷ 0.75 ≈ S/ 3 067 → 3 100'], ['30 %', '2 300 ÷ 0.70 ≈ S/ 3 286']],
    lambda i: [1, 2, 2][i], izq=320, der=320, tam=31),
  caso('el control que nadie borró', [
    'Caso de obra: una familia cambió de empleada del hogar, y nadie pensó en el control del portón que ella tenía.',
    'Meses después, notaron que el portón se abría a horas raras. El instalador no había anotado cuántos controles grabó, ni enseñó a borrarlos.',
    'Anota cada control que grabas, entrégale la lista al cliente, y enséñale cómo borrar uno perdido.',
  ], [('🎛️', 'Un control <b class="nar">en manos equivocadas</b>'), ('📋', 'Nadie <b class="nar">anotó</b> los controles'), ('✅', 'Lista de controles y <b class="nar">cómo borrar</b>')]),
  *ejercicio(1,
    'Batiente de <b class="nar">dos hojas</b>: kit de 2 pistones <b class="nar">S/ 1 900</b>,<br>materiales y accesorios <b class="nar">S/ 650</b>, mano de obra <b class="nar">S/ 600</b>.<br>¿Qué precio cobras con <b class="nar">25 %</b> de margen real?',
    ['Ahora tú. Un batiente de dos hojas: el kit de dos pistones cuesta mil novecientos. Materiales y accesorios, seiscientos cincuenta. Mano de obra, seiscientos.', '¿Qué precio cobras con veinticinco por ciento de margen real?'],
    'Costo: 1 900 + 650 + 600 = <b class="nar">S/ 3 150</b><br>Precio: 3 150 ÷ 0.75 = <b class="nar">S/ 4 200</b><br>Ganancia: <b class="nar">S/ 1 050</b>',
    ['El costo: tres mil ciento cincuenta.',
     'Entre cero setenta y cinco: cuatro mil doscientos soles. Ganas mil cincuenta. Y explícale al cliente por qué un batiente cuesta más: dos motores.']),
  *ejercicio(2,
    'Ofreces mantenimiento cada <b class="nar">6 meses</b> a <b class="nar">S/ 120</b> la visita.<br>Si <b class="nar">25 clientes</b> lo toman, ¿cuánto entra al año?',
    ['Segundo ejercicio. Ofreces mantenimiento cada seis meses, a ciento veinte soles la visita.', 'Si veinticinco clientes lo toman, ¿cuánto entra al año?'],
    '25 clientes × 2 visitas = <b class="nar">50 visitas</b><br>50 × 120 = <b class="nar">S/ 6 000 al año</b><br>Más repuestos y <b class="nar">trabajos nuevos</b> de los mismos clientes',
    ['Veinticinco clientes por dos visitas: cincuenta visitas al año.',
     'Por ciento veinte: seis mil soles al año, más los repuestos y los trabajos nuevos que salen de esas visitas.']),
  faq([
    ('¿Cuántos controles entrego?', 'Los acordados; anótalos todos.', '¿Cuántos controles entrego? Los que acordaste en la cotización, normalmente dos. Y los anotas todos.'),
    ('¿Activo el cierre automático?', 'Solo con fotoceldas y luz funcionando.', '¿Activo el cierre automático? Solo si las fotoceldas y la luz destellante están instaladas y probadas.'),
    ('¿Qué garantía doy?', 'La de tu instalación por escrito; la del motor, del fabricante.', '¿Qué garantía doy? La de tu instalación, por escrito, por ejemplo doce meses. La del motor, la del fabricante.'),
  ]),
  repaso([
    ('¿Qué es el aprendizaje del recorrido?', 'Cuando el motor abre y cierra una vez para medir el camino.'),
    ('¿Qué controles conviene usar?', 'De código variable.'),
    ('¿Cómo se cotiza la automatización?', 'Aparte del portón.'),
    ('¿Qué haces en la entrega?', 'Diez ciclos, las dos pruebas y capacitar al cliente.'),
  ]),
]

# ───────────── Clase 9 · Levadizos y seccionales ─────────────
EXT['porton_c9'] = [
  ejemplo('La prueba de <span class="nar">la media altura</span>', [
    'Antes de los errores, cómo leer la prueba de la media altura.',
    'Si al soltarla se queda quieta: está equilibrada, puedes motorizar. Si cae: falta contrapeso o tensión en los resortes.',
    'Si sube sola: sobra contrapeso o tensión. En levadizos con contrapeso, se corrige agregando o quitando planchas. En seccionales, lo ajusta un técnico.',
  ], ['Al soltarla a media altura…', 'Significa', 'Qué haces'],
    [['Se queda quieta', 'Equilibrada', 'Puedes motorizar'], ['Cae', 'Falta contrapeso o tensión', 'Agregar (o técnico en seccional)'], ['Sube sola', 'Sobra contrapeso o tensión', 'Quitar (o técnico en seccional)']],
    lambda i: [1, 2, 2][i], izq=200, der=200),
  caso('el resorte de torsión', [
    'Caso de obra: un maestro quiso "ajustar un poquito" los resortes de torsión de un seccional, con un desarmador.',
    'El resorte se soltó y el desarmador salió disparado. Por suerte, no le dio. Pudo ser una lesión grave.',
    'Los resortes de torsión guardan muchísima energía. Los ajusta un técnico con las barras y el equipo adecuados. Si no tienes ese equipo, no los toques.',
  ], [('🌀', 'Ajustar un resorte de torsión <b class="nar">con desarmador</b>'), ('⚠️', 'Se soltó: <b class="nar">casi una lesión grave</b>'), ('✅', 'Solo un técnico <b class="nar">con su equipo</b>')]),
  *ejercicio(1,
    'Un levadizo pesa <b class="nar">140 kg</b> y lleva contrapesos a los dos lados.<br>¿Cuánto contrapeso, más o menos, va en cada lado?<br>¿Cómo lo afinas?',
    ['Ahora tú. Un levadizo pesa ciento cuarenta kilos, y lleva contrapesos a los dos lados.', '¿Cuánto contrapeso, más o menos, va en cada lado? ¿Y cómo lo afinas?'],
    'Contrapeso ≈ peso de la hoja: <b class="nar">≈ 70 kg por lado</b><br>Se afina con la <b class="nar">prueba de la media altura</b>,<br>agregando o quitando planchas hasta que <b class="nar">se quede quieta</b>',
    ['El contrapeso total pesa más o menos lo mismo que la hoja: unos setenta kilos por lado.',
     'Y se afina con la prueba de la media altura, agregando o quitando planchas, hasta que la hoja se quede quieta.']),
  *ejercicio(2,
    'Un cliente quiere un <b class="nar">seccional</b> para su cochera.<br>¿Qué tres medidas tomas antes de ofrecerlo?',
    ['Segundo ejercicio. Un cliente quiere un seccional para su cochera.', '¿Qué tres medidas tomas antes de ofrecerlo?'],
    '1. <b class="nar">Altura libre</b> sobre el vano (dintel), para el eje y los resortes<br>2. <b class="nar">Espacio lateral</b> a cada lado, para las guías<br>3. <b class="nar">Fondo</b> libre bajo el techo, para que se acueste<br>Y comparas con lo que pide <b class="nar">la ficha del fabricante</b>',
    ['La altura libre sobre el vano, para el eje y los resortes. El espacio a cada lado, para las guías.',
     'Y el fondo libre bajo el techo, para que la hoja se acueste. Después comparas con lo que pide la ficha del fabricante.']),
  faq([
    ('¿Puedo fabricar un levadizo?', 'Sí, con contrapesos bien calculados y guías firmes.', '¿Puedo fabricar un levadizo en mi taller? Sí, con contrapesos bien ajustados, guías firmes y cables revisados.'),
    ('¿Y un seccional?', 'Mejor de fábrica, con su técnico.', '¿Y un seccional? Mejor comprarlo de fábrica e instalarlo con su técnico, por los resortes de torsión.'),
    ('¿Motor de techo o lateral?', 'Techo en casas; lateral sin espacio arriba.', '¿Motor de techo o lateral? El de techo es el más común en casas. El lateral, cuando no hay espacio arriba.'),
  ]),
  repaso([
    ('¿Qué regla va antes de motorizar?', 'Que la hoja esté equilibrada.'),
    ('¿Qué pasa si cae a media altura?', 'Falta contrapeso o tensión.'),
    ('¿Quién ajusta los resortes de torsión?', 'Un técnico con su equipo.'),
    ('¿Qué necesitan los dos tipos?', 'Altura libre sobre el vano.'),
  ]),
]

# ───────────── Clase 10 · Control de acceso ─────────────
EXT['porton_c10'] = [
  ejemplo('Qué ofrecer <span class="nar">a cada cliente</span>', [
    'Antes de los errores, qué control de acceso suele convenir según el cliente.',
    'Una casa: controles remotos y, si quiere, apertura desde el celular. Un edificio pequeño: teclado con clave por departamento.',
    'Un condominio: llaveros de proximidad, teclado y botón para el vigilante. Y una empresa: tarjetas, registro de entradas, y a veces barrera.',
  ], ['Cliente', 'Suele convenir'],
    [['Casa', 'Controles + celular (opcional)'], ['Edificio pequeño', 'Teclado con clave por departamento'], ['Condominio', 'Llaveros + teclado + botón del vigilante'], ['Empresa', 'Tarjetas con registro, y barrera si hace falta']],
    lambda i: [1, 1, 2, 3][i], izq=300, der=300),
  caso('la clave de fábrica', [
    'Caso de obra: un teclado instalado en un edificio, funcionando perfecto. Nadie cambió la clave maestra de fábrica.',
    'Un vecino de otro edificio, que tenía el mismo modelo, probó la clave de fábrica y abrió. Nadie supo cómo entraba.',
    'Cambia todas las claves de fábrica en la instalación, y anótalas en el acta que le entregas al administrador.',
  ], [('🔢', 'Clave <b class="nar">de fábrica</b> sin cambiar'), ('🚪', 'Un extraño <b class="nar">abrió</b>'), ('✅', 'Cambia claves y <b class="nar">anótalas en el acta</b>')]),
  *ejercicio(1,
    'Un condominio de <b class="nar">40 familias</b> pide dos llaveros por familia,<br>y un <b class="nar">10 %</b> de reserva para reposiciones.<br>¿Cuántos llaveros compras?',
    ['Ahora tú. Un condominio de cuarenta familias pide dos llaveros por familia, y un diez por ciento de reserva para reposiciones.', '¿Cuántos llaveros compras?'],
    '40 × 2 = <b class="nar">80</b> llaveros<br>Reserva: 80 × 0.10 = <b class="nar">8</b><br>Total: <b class="nar">88 llaveros</b>, cada uno anotado en la lista',
    ['Cuarenta por dos: ochenta llaveros. Más el diez por ciento de reserva: ocho más.',
     'Ochenta y ocho llaveros. Y cada uno, anotado en la lista de usuarios con su departamento.']),
  *ejercicio(2,
    'Una familia del condominio <b class="nar">se muda</b>, y otra <b class="nar">perdió un llavero</b>.<br>¿Qué haces en cada caso?',
    ['Segundo ejercicio. Una familia del condominio se muda, y otra perdió un llavero.', '¿Qué haces en cada caso?'],
    'Mudanza: <b class="nar">borras sus llaveros y su clave</b>, y anotas la baja<br>Llavero perdido: <b class="nar">borras solo ese</b> y entregas uno de reserva<br>Siempre con la <b class="nar">lista de usuarios</b> al día',
    ['Mudanza: borras sus llaveros y su clave del sistema, y anotas la baja en la lista.',
     'Llavero perdido: borras solo ese, y entregas uno de la reserva. Por eso la lista de usuarios siempre al día.']),
  faq([
    ('¿Funciona con cualquier motor?', 'Casi siempre: un contacto de "abrir".', '¿El teclado funciona con cualquier motor? Casi siempre, porque se conecta como un pulsador de abrir. Revisa el voltaje en el manual.'),
    ('¿Apertura por celular es segura?', 'Sí, con contraseña fuerte y equipo actualizado.', '¿Es seguro abrir desde el celular? Sí, con una contraseña fuerte en el wifi y en la aplicación, y el equipo actualizado.'),
    ('¿Cobro aparte?', 'Sí: son partidas adicionales.', '¿El control de acceso se cobra aparte? Sí. Son partidas adicionales, y además un servicio de altas y bajas.'),
  ]),
  repaso([
    ('¿Cómo le habla un teclado al motor?', 'Con un contacto que dice abre.'),
    ('¿Qué se cambia siempre al instalar?', 'Las claves de fábrica.'),
    ('¿Qué lista se lleva?', 'Quién tiene cada clave o tarjeta.'),
    ('¿Qué se borra si alguien pierde su llavero?', 'Solo ese llavero.'),
  ]),
]

# ───────────── Clase 11 · Cuando se va la luz ─────────────
EXT['porton_c11'] = [
  ejemplo('Tres preguntas, <span class="nar">una solución</span>', [
    'Antes de los errores, cómo las tres preguntas llevan a una solución.',
    'Cortes raros, alguien puede mover la hoja y hay otra entrada: desbloqueo manual y listo.',
    'Cortes frecuentes, o personas que no pueden mover la hoja: motor de veinticuatro voltios con batería.',
    'Y sin red eléctrica, con pocos ciclos al día: veinticuatro voltios con batería y panel solar, calculado.',
  ], ['Situación', 'Solución'],
    [['Cortes raros + otra entrada', 'Desbloqueo manual'], ['Cortes frecuentes o personas que no pueden mover la hoja', '24 V con batería'], ['Sin red eléctrica, pocos ciclos', '24 V + batería + panel solar']],
    lambda i: [1, 2, 3][i], izq=200, der=200),
  caso('la señora que quedó afuera', [
    'Caso de obra: una señora mayor vivía sola, con portón automático y sin puerta peatonal. El desbloqueo estaba adentro.',
    'Un corte de luz de tarde la dejó afuera, con las compras, por casi dos horas, hasta que llegó un familiar.',
    'Para ella, lo correcto era un motor de veinticuatro voltios con batería, o un desbloqueo exterior con llave. Las tres preguntas lo habrían mostrado.',
  ], [('👵', 'Vivía <b class="nar">sola</b>, sin puerta peatonal'), ('🔌', 'Corte de luz: <b class="nar">quedó afuera</b>'), ('✅', '<b class="nar">24 V con batería</b> o desbloqueo exterior')]),
  *ejercicio(1,
    'Una familia: hay <b class="nar">cortes casi cada semana</b>, el portón es pesado<br>y <b class="nar">no tienen puerta peatonal</b>. Abren unas <b class="nar">10 veces al día</b>.<br>¿Qué recomiendas?',
    ['Ahora tú. Una familia: hay cortes de luz casi cada semana, el portón es pesado, y no tienen puerta peatonal. Abren unas diez veces al día.', '¿Qué recomiendas?'],
    'Motor de <b class="nar">24 V con batería</b> de respaldo<br>y además un <b class="nar">desbloqueo exterior</b> con llave, por si la batería se agota<br>Revisa en la ficha <b class="nar">cuántos ciclos</b> da la batería',
    ['Motor de veinticuatro voltios con batería de respaldo.',
     'Y además un desbloqueo exterior con llave, por si un corte largo agota la batería. Revisando en la ficha cuántos ciclos da con ese peso.']),
  *ejercicio(2,
    'La ficha dice que la batería da <b class="nar">20 ciclos</b> con ese portón.<br>La familia abre <b class="nar">8 veces al día</b>.<br>¿Para cuánto tiempo de corte alcanza?',
    ['Segundo ejercicio. La ficha dice que la batería da veinte ciclos con ese portón. La familia abre ocho veces al día.', '¿Para cuánto tiempo de corte alcanza?'],
    '20 ÷ 8 = <b class="nar">2.5 días</b> de uso normal<br>Suficiente para cortes de <b class="nar">horas</b>, y un poco más<br>Dilo así al cliente, <b class="nar">con la ficha</b>',
    ['Veinte entre ocho: unos dos días y medio de uso normal.',
     'Alcanza de sobra para cortes de horas. Díselo así al cliente, con la ficha en la mano, sin prometer más.']),
  faq([
    ('¿La batería dura para siempre?', 'No: se cambia cada cierto tiempo.', '¿La batería dura para siempre? No. Se revisa en cada mantenimiento y se cambia cuando pierde capacidad.'),
    ('¿Puedo poner batería a un motor de 220 V?', 'Normalmente se usa un equipo aparte; consulta la ficha.', '¿Se le puede poner batería a un motor de doscientos veinte? Normalmente necesita un equipo aparte. Revisa lo que dice el fabricante.'),
    ('¿El panel solar sirve en cualquier lugar?', 'Sí, si se calcula con el sol de la zona.', '¿El panel solar sirve en cualquier lugar? Sí, si se calcula con los ciclos del día y el sol de la zona.'),
  ]),
  repaso([
    ('¿Cuál es la primera solución sin luz?', 'El desbloqueo manual.'),
    ('¿Qué motor acepta batería?', 'El de veinticuatro voltios.'),
    ('¿Cuáles son las tres preguntas?', 'Cortes, quién lo usa, y cuántas veces abre.'),
    ('¿Qué no se promete sin ver la ficha?', 'Los ciclos de la batería.'),
  ]),
]

# ───────────── Clase 12 · Fallas y mantenimiento ─────────────
EXT['porton_c12'] = [
  ejemplo('La tabla <span class="nar">del técnico</span>', [
    'Antes de los errores, la tabla de fallas y dónde mirar primero.',
    'No responde al control pero sí al pulsador: pila, receptor o control borrado. Abre un poco y regresa: fotoceldas sucias, fuerza baja o roce.',
    'Zumba pero no se mueve: motor bloqueado, condensador o algo trabado. Y no hace nada: energía, fusible o desbloqueo.',
  ], ['Síntoma', 'Mira primero'],
    [['No responde al control, sí al pulsador', 'Pila, receptor o control borrado'], ['Abre un poco y regresa', 'Fotoceldas, fuerza o roce'], ['Zumba y no se mueve', 'Bloqueo, condensador o algo trabado'], ['No hace nada', 'Energía, fusible o desbloqueo']],
    lambda i: [1, 1, 2, 2][i], izq=240, der=240),
  ejemplo('El contrato, <span class="nar">en números</span>', [
    'Y el contrato de mantenimiento, con números de ejemplo.',
    'Treinta portones, dos visitas al año: sesenta visitas. A ciento veinte soles: siete mil doscientos soles al año.',
    'Son unas cinco visitas al mes, que puedes agendar en tus días flojos. Ingreso fijo, y clientes que te llaman para el próximo trabajo.',
  ], ['Dato', 'Valor'],
    [['Portones en contrato', '30'], ['Visitas al año', '60 (≈ 5 al mes)'], ['Precio por visita', 'S/ 120'], ['Ingreso al año', 'S/ 7 200']],
    lambda i: [1, 1, 2, 2][i], izq=440, der=440, tam=31),
  caso('la tarjeta que no estaba mala', [
    'Caso de servicio: un cliente llamó porque el portón no abría con el control. El técnico cambió la tarjeta, y cobró cuatrocientos soles.',
    'Al mes, otra vez lo mismo. Otro técnico revisó primero lo simple: era la pila del control, y el receptor tenía la antena tapada.',
    'El orden importa: energía, bloqueo, pila, fotoceldas. Recién después se abre la tarjeta.',
  ], [('💳', 'Cambiaron la tarjeta: <b class="nar">S/ 400</b>'), ('🔋', 'Era <b class="nar">la pila</b> y la antena tapada'), ('✅', 'Primero <b class="nar">lo simple</b>, después la tarjeta')]),
  *ejercicio(1,
    'Un portón <b class="nar">abre un poco y regresa</b> en cuanto empieza a cerrar.<br>Con el portón sin motor, <b class="nar">corre suave</b>.<br>¿Qué revisas primero?',
    ['Ahora tú. Un portón abre un poco y regresa, en cuanto empieza a cerrar. Desbloqueado, corre suave a mano.', '¿Qué revisas primero?'],
    'Si corre suave, el roce no es el problema<br>Revisa las <b class="nar">fotoceldas</b>: limpias, alineadas y sin nada en el camino<br>Luego la <b class="nar">fuerza</b> en la tarjeta',
    ['Si corre suave a mano, el roce no es el problema.',
     'Revisa primero las fotoceldas: que estén limpias, alineadas, y que nada corte el rayo. Si siguen bien, revisa la fuerza en la tarjeta.']),
  *ejercicio(2,
    'Tienes <b class="nar">18 portones</b> en contrato, con visitas cada 6 meses.<br>¿Cuántas visitas al mes y cuánto entra al año a <b class="nar">S/ 130</b> por visita?',
    ['Segundo ejercicio. Tienes dieciocho portones en contrato, con visitas cada seis meses.', '¿Cuántas visitas al mes, y cuánto entra al año a ciento treinta soles por visita?'],
    'Visitas al año: 18 × 2 = <b class="nar">36</b> → <b class="nar">3 al mes</b><br>Ingreso: 36 × 130 = <b class="nar">S/ 4 680 al año</b>',
    ['Dieciocho por dos: treinta y seis visitas al año, tres al mes.',
     'Por ciento treinta: cuatro mil seiscientos ochenta soles al año. Y cada visita es una oportunidad de vender una mejora.']),
  faq([
    ('¿Qué lubrico?', 'Lo que diga el manual; nunca grasa en el riel.', '¿Qué se lubrica? Lo que indique el manual del motor. Nunca grasa en el riel: junta tierra.'),
    ('¿Cuánto cobro por visita?', 'Calcula con tu hora y el traslado.', '¿Cuánto cobro por visita? Calcula con el costo de tu hora y el traslado, como en el curso del Negocio del Metalero.'),
    ('¿Llevo repuestos?', 'Pilas, controles y fotoceldas básicas.', '¿Qué repuestos llevo? Pilas, un control de repuesto, y un par de fotoceldas. Resuelven la mayoría de llamadas.'),
  ]),
  repaso([
    ('¿Qué revisas primero en una falla?', 'Lo simple: energía, bloqueo, pila y fotoceldas.'),
    ('¿Cada cuánto el mantenimiento?', 'Cada seis meses.'),
    ('¿Se engrasa el riel?', 'No.'),
    ('¿Qué te da el contrato?', 'Ingreso fijo y trabajos nuevos.'),
  ]),
]
