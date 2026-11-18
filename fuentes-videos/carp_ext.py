"""Ampliación de «Carpintería Metálica» (≈7–8 min por clase). Misma receta que los demás cursos."""
from naves_ext import insertar, caja, faq, repaso, caso, svg, T
from techo_ext import ejemplo, respuesta
from ext_comun import ejercicio
from sold_comun import *

EXT = {}

# ───────────── Clase 1 · Herramientas y medidas ─────────────
EXT['carp_c1'] = [
  ejemplo('Un vano <span class="nar">medido de verdad</span>', [
    'Antes de los errores, así se ve un vano real cuando lo mides bien. Puerta de un dormitorio.',
    'Ancho abajo: ochocientos ochenta y cinco. Al medio: ochocientos ochenta y dos. Arriba: ochocientos ochenta y ocho. Usas ochocientos ochenta y dos.',
    'Alto a la izquierda, al centro y a la derecha: dos mil ciento cinco, dos mil cien y dos mil ciento tres. Usas dos mil cien.',
    'Y las diagonales: dos mil doscientos ochenta y dos mil doscientos ochenta y ocho. Ocho milímetros de diferencia: el vano está chueco, y el marco lo va a absorber con sus holguras.',
  ], ['Medida', 'Lecturas (mm)', 'Usas'],
    [['Ancho', '885 · 882 · 888', '882'], ['Alto', '2 105 · 2 100 · 2 103', '2 100'], ['Diagonales', '2 280 · 2 288', '8 mm: chueco']],
    lambda i: i + 1, izq=280, der=280),
  ejemplo('Las holguras <span class="nar">en una tabla</span>', [
    'Y las holguras de la clase, juntas, para que las tengas a mano.',
    'Entre el marco y el muro: unos cinco milímetros por lado. Entre la hoja y el marco: unos tres a los costados y arriba.',
    'Y abajo, entre la hoja y el piso terminado: de diez a quince milímetros, según el piso.',
  ], ['Dónde', 'Holgura'],
    [['Marco – muro', '≈ 5 mm por lado'], ['Hoja – marco (costados y arriba)', '≈ 3 mm'], ['Hoja – piso terminado', '10 a 15 mm']],
    lambda i: [1, 1, 2][i], izq=420, der=420, tam=32),
  caso('la puerta que chocaba', [
    'Caso de obra: una puerta de calle bien hecha, bien pintada, bien instalada. Pero abría hacia afuera.',
    'Al abrirla, la hoja golpeaba a la gente en la vereda, y chocaba con el escalón de la entrada. Hubo que cambiar las bisagras de lado y rehacer el marco.',
    'En el croquis, una flecha: hacia dónde abre y de qué lado van las bisagras. Y que el cliente lo firme.',
  ], [('🚪', 'La puerta abría <b class="nar">hacia la vereda</b>'), ('💥', 'Golpeaba a la gente y al <b class="nar">escalón</b>'), ('✍️', 'Croquis con <b class="nar">flecha de apertura</b>, firmado')]),
  *ejercicio(1,
    'Mides el vano de una ventana:<br>anchos <b class="nar">1 205 · 1 198 · 1 201</b> mm · altos <b class="nar">1 002 · 1 006 · 998</b> mm.<br>Con 5 mm por lado contra el muro, ¿de qué medida haces el marco?',
    ['Ahora tú. Mides el vano de una ventana. Anchos: mil doscientos cinco, mil ciento noventa y ocho, y mil doscientos uno. Altos: mil dos, mil seis y novecientos noventa y ocho.',
     'Con cinco milímetros por lado contra el muro, ¿de qué medida haces el marco?'],
    'Usas las más chicas: <b class="nar">1 198 × 998</b> mm<br>La ventana lleva holgura en los 4 lados: −10 mm en cada sentido<br>Marco: <b class="nar">1 188 × 988 mm</b>',
    ['Las medidas más chicas: mil ciento noventa y ocho por novecientos noventa y ocho.',
     'La ventana, a diferencia de la puerta, tiene muro también abajo: le quitas diez milímetros en cada sentido. El marco queda de mil ciento ochenta y ocho por novecientos ochenta y ocho.']),
  *ejercicio(2,
    'La puerta va sobre un piso que todavía <b class="nar">no tiene porcelanato</b>.<br>Irán <b class="nar">10 mm</b> de porcelanato y <b class="nar">5 mm</b> de pegamento.<br>¿A cuánto del piso actual dejas la hoja?',
    ['Segundo ejercicio. La puerta va sobre un piso que todavía no tiene porcelanato. Irán diez milímetros de porcelanato y cinco de pegamento.', '¿A cuánto del piso actual dejas el borde de abajo de la hoja?'],
    'Piso terminado: 10 + 5 = <b class="nar">15 mm</b> más arriba<br>Holgura sobre el piso terminado: 10 a 15 mm<br>Desde el piso actual: <b class="nar">25 a 30 mm</b>',
    ['El piso terminado va a subir quince milímetros. Y sobre ese piso dejas de diez a quince.',
     'Desde el piso de hoy: entre veinticinco y treinta milímetros. Anótalo en el croquis, para que el instalador no se confunda.']),
  faq([
    ('¿Wincha o medidor láser?', 'Los dos; la wincha manda en vanos chicos.', '¿Wincha o medidor láser? Los dos sirven. El láser es rápido para distancias largas; en vanos chicos, la wincha es más que suficiente.'),
    ('¿Y si el vano está muy chueco?', 'Avisa al cliente: el resane o el marco lo absorben.', '¿Y si el vano está muy chueco? Avísale al cliente antes de fabricar. El marco absorbe una parte, y el resto se resuelve con resane.'),
    ('¿Mido antes del tarrajeo?', 'Mejor después; si no, anota el espesor que falta.', '¿Mido antes del tarrajeo? Mejor con el tarrajeo terminado. Si no, anota cuánto espesor falta en cada lado.'),
  ]),
  repaso([
    ('¿En cuántos puntos mides el ancho?', 'En tres: abajo, al medio y arriba.'),
    ('¿Qué medida usas para fabricar?', 'La más chica.'),
    ('¿Cuánto más chico se hace el marco?', 'Unos diez milímetros en el ancho.'),
    ('¿Qué anotas además de las medidas?', 'Hacia dónde abre la puerta.'),
  ]),
]

# ───────────── Clase 2 · Despiece y barras ─────────────
EXT['carp_c2'] = [
  ejemplo('Inglete o tope: <span class="nar">el mismo marco</span>', [
    'Antes de los errores, el mismo marco de uno veinte por uno, en tubo de una pulgada, cortado de las dos formas.',
    'A cuarenta y cinco grados: dos piezas de mil doscientos y dos de mil. Todas miden lo mismo que el lado exterior.',
    'A tope: los dos parantes de mil, y los travesaños entre ellos: mil doscientos menos dos veces veinticinco punto cuatro. Mil ciento cuarenta y nueve.',
  ], ['Corte', 'Parantes', 'Travesaños'],
    [['A 45° (inglete)', '2 × 1 000 mm', '2 × 1 200 mm'], ['A tope (90°)', '2 × 1 000 mm', '2 × 1 149 mm']],
    lambda i: i + 1, izq=320, der=320, tam=32),
  caso('primero lo chico', [
    'Caso de taller: el ayudante empezó cortando las piezas chicas, las que necesitaba primero para armar.',
    'Cuando llegó a los pasamanos de tres metros cincuenta, ninguna barra abierta alcanzaba. Abrió dos barras nuevas, y quedaron cuatro sobrantes de un metro y algo.',
    'La regla: primero lo largo. Las piezas cortas se acomodan después en los sobrantes.',
  ], [('✂️', 'Cortó primero <b class="nar">las piezas chicas</b>'), ('📏', 'Los largos <b class="nar">no alcanzaron</b>: dos barras más'), ('✅', 'Primero <b class="nar">lo largo</b>, después lo corto')]),
  *ejercicio(1,
    'Necesitas <b class="nar">5 piezas de 2.20 m</b> y <b class="nar">5 de 1.50 m</b>, del mismo perfil.<br>Disco de <b class="nar">3 mm</b>. ¿Cuántas barras de 6 m como mínimo?<br>¿Cómo las acomodas?',
    ['Ahora tú. Necesitas cinco piezas de dos veinte y cinco de uno cincuenta, del mismo perfil. Disco de tres milímetros.', '¿Cuántas barras de seis metros como mínimo, y cómo las acomodas?'],
    'Total: 11 + 7.5 = 18.5 m → más de 3 barras → <b class="nar">mínimo 4</b><br>Barras 1 y 2: <b class="nar">2.20 + 2.20 + 1.50</b> (5.91 m con cortes)<br>Barra 3: <b class="nar">2.20 + 1.50 + 1.50</b> · Barra 4: <b class="nar">1.50</b> (sobra 4.5 m)',
    ['Todo suma dieciocho metros y medio: más que tres barras. Mínimo cuatro.',
     'Barras uno y dos: dos veinte, dos veinte y uno cincuenta, con los cortes, cinco noventa y uno. Barra tres: dos veinte y dos de uno cincuenta. Y la barra cuatro, la última de uno cincuenta, y te queda un buen sobrante para otro trabajo.']),
  *ejercicio(2,
    'Un marco de ventana de <b class="nar">1.50 × 1.20 m</b> a inglete.<br>¿Sale de una sola barra de 6 m? ¿Cuánto sobra y qué haces con el sobrante?',
    ['Segundo ejercicio. Un marco de ventana de uno cincuenta por uno veinte, a inglete.', '¿Sale de una sola barra de seis metros? ¿Cuánto sobra, y qué haces con el sobrante?'],
    'Piezas: 1.50 + 1.50 + 1.20 + 1.20 = 5.40 m + 4 cortes (0.012) = <b class="nar">5.412 m</b> ✓<br>Sobra <b class="nar">≈ 0.59 m</b>: más de 50 cm → <b class="nar">se rotula y se guarda</b>',
    ['Cinco cuarenta, más cuatro cortes de tres milímetros: cinco metros cuatrocientos doce. Sí sale de una barra.',
     'Sobran unos cincuenta y nueve centímetros. Más de cincuenta: lo rotulas con el perfil y el largo, y lo guardas.']),
  faq([
    ('¿Cuánto come la sierra de cinta?', 'Menos que el disco: unos 1 a 2 mm.', '¿Cuánto se come la sierra de cinta? Menos que el disco abrasivo, más o menos uno a dos milímetros. Igual, súmalo.'),
    ('¿Hay barras más largas?', 'Algunos proveedores venden de 6.40 m o más.', '¿Hay barras más largas que seis metros? Algunos proveedores tienen de seis cuarenta o más, por pedido. Pregunta si te conviene.'),
    ('¿Tengo que optimizar a mano?', 'No: el módulo de Carpintería Metálica lo hace.', '¿Tengo que optimizar siempre a mano? No. El módulo de Carpintería Metálica de InnovApp optimiza las barras en su despiece.'),
  ]),
  repaso([
    ('¿Cuánto mide una pieza a inglete?', 'Lo mismo que el lado exterior del marco.'),
    ('¿Qué le restas a un travesaño a tope?', 'Dos veces el ancho del perfil.'),
    ('¿Qué se suma siempre al cortar?', 'El ancho del disco.'),
    ('¿Desde qué largo se guarda un sobrante?', 'Desde unos cincuenta centímetros.'),
  ]),
]

# ───────────── Clase 3 · La puerta metálica ─────────────
EXT['carp_c3'] = [
  respuesta('6 de 1.80 y 4 de 1.40', [
    'La respuesta del reto de la clase pasada: seis piezas de uno ochenta y cuatro de uno cuarenta.',
    'Todo suma dieciséis metros cuarenta: tres barras como mínimo. ¿Alcanzan?',
    'Sí. Dos barras con tres piezas de uno ochenta cada una: cinco cuarenta más los cortes. Y la tercera con cuatro de uno cuarenta: cinco sesenta más los cortes. Tres barras.',
  ], ['Barra', 'Piezas', 'Con cortes'],
    [['1', '1.80 + 1.80 + 1.80', '5.409 m'], ['2', '1.80 + 1.80 + 1.80', '5.409 m'], ['3', '1.40 + 1.40 + 1.40 + 1.40', '5.612 m']], lambda i: 2),
  ejemplo('¿Cuánto pesa <span class="nar">nuestra puerta</span>?', [
    'Antes de los errores, el peso de la hoja de nuestra puerta de calle. Sirve para elegir las bisagras.',
    'Bastidor en tubo de una y media por uno punto cinco: contorno y dos travesaños, unos siete metros, a uno punto siete kilos. Unos doce kilos.',
    'Plancha de uno punto cinco milímetros: uno punto seis metros cuadrados, por once punto ocho kilos. Unos diecinueve kilos.',
    'Con chapa y bisagras, la hoja pasa los treinta y cinco kilos. Por eso: tres bisagras.',
  ], ['Parte', 'Cálculo', 'Peso'],
    [['Bastidor', '≈ 7.2 m × 1.7 kg/m', '≈ 12 kg'], ['Plancha 1.5 mm', '1.61 m² × 11.8 kg/m²', '≈ 19 kg'], ['Chapa, bisagras, refuerzos', '', '≈ 5 kg'], ['Total de la hoja', '', '≈ 36 kg']],
    lambda i: [1, 2, 3, 3][i], izq=260, der=260),
  caso('la reja que se descolgó', [
    'Caso de obra: una puerta de reja, sin plancha, de un metro de ancho. Al año, la esquina de la chapa rozaba el piso.',
    'No tenía diagonal. Con su propio peso, el bastidor se fue deformando, como un paralelogramo.',
    'Se arregló con una diagonal desde abajo del lado de las bisagras hasta arriba del lado de la chapa. Desde el inicio, habría costado medio metro de tubo.',
  ], [('↘️', 'La esquina de la chapa <b class="nar">rozaba el piso</b>'), ('▱', 'Sin diagonal: <b class="nar">se deformó</b>'), ('✅', 'Diagonal de <b class="nar">bisagra abajo a chapa arriba</b>')]),
  *ejercicio(1,
    'La hoja mide <b class="nar">2 047 mm</b> de alto. Llevas 3 bisagras:<br>a 20 cm de arriba, a 20 cm de abajo y al medio.<br>¿A qué altura va cada una, desde abajo de la hoja?',
    ['Ahora tú. La hoja mide dos mil cuarenta y siete milímetros de alto. Llevas tres bisagras: a veinte centímetros de arriba, a veinte de abajo, y al medio.', '¿A qué altura va el centro de cada una, desde abajo de la hoja?'],
    'Abajo: <b class="nar">200 mm</b><br>Al medio: 2 047 ÷ 2 ≈ <b class="nar">1 024 mm</b><br>Arriba: 2 047 − 200 = <b class="nar">1 847 mm</b>',
    ['La de abajo, a doscientos. La del medio, a dos mil cuarenta y siete entre dos: mil veinticuatro.',
     'Y la de arriba, a dos mil cuarenta y siete menos doscientos: mil ochocientos cuarenta y siete. Y las tres alineadas con un hilo.']),
  *ejercicio(2,
    'Una hoja de reja mide <b class="nar">0.80 × 2.00 m</b>.<br>¿Cuánto mide su diagonal y entre qué esquinas va?',
    ['Segundo ejercicio. Una hoja de reja mide cero ochenta por dos metros.', '¿Cuánto mide su diagonal, y entre qué esquinas va?'],
    'Diagonal: √(0.80² + 2.00²) = √4.64 ≈ <b class="nar">2.15 m</b><br>Desde <b class="nar">abajo, lado de las bisagras</b><br>hasta <b class="nar">arriba, lado de la chapa</b>',
    ['La diagonal: raíz de cero ochenta al cuadrado más dos al cuadrado. Unos dos metros quince.',
     'Va desde la esquina de abajo, del lado de las bisagras, hasta la esquina de arriba, del lado de la chapa. Así trabaja apretada y sostiene la hoja.']),
  faq([
    ('¿Bisagra común o de barril?', 'En puertas pesadas, barril o reforzada.', '¿Bisagra común o de barril? En puertas pesadas o de calle, de barril o reforzadas, con pin grueso.'),
    ('¿Plancha lisa o estriada?', 'Lisa para pintar bonito; estriada abajo si recibe golpes.', '¿Plancha lisa o estriada? Lisa para un acabado bonito. Si la parte baja recibe golpes, se puede poner un zócalo de estriada.'),
    ('¿Cómo evito que suene al cerrar?', 'Un tope de jebe en el marco.', '¿Cómo evito que la puerta suene al cerrar? Con topes de jebe en el marco. Detalle barato que el cliente agradece.'),
  ]),
  repaso([
    ('¿Cuántas bisagras lleva una puerta de calle?', 'Tres.'),
    ('¿Qué espesor de plancha para una puerta de calle?', 'Uno punto cinco milímetros.'),
    ('¿Cómo se suelda la plancha a la hoja?', 'Con cordones cortos, alternados.'),
    ('¿Qué lleva una hoja de reja o vidrio?', 'Una diagonal.'),
  ]),
]

# ───────────── Clase 4 · Portones ─────────────
EXT['carp_c4'] = [
  respuesta('hoja para marco 900 × 2 100', [
    'La respuesta del reto de la clase pasada: la hoja para un marco de novecientos por dos mil cien, con tubo de treinta y ocho milímetros de cara.',
    'Interior del marco: novecientos menos dos veces treinta y ocho, ochocientos veinticuatro de ancho. Y dos mil cien menos treinta y ocho, dos mil sesenta y dos de alto.',
    'La hoja: ochocientos veinticuatro menos seis, ochocientos dieciocho. Y dos mil sesenta y dos menos tres arriba y doce abajo: dos mil cuarenta y siete.',
  ], ['Medida', 'Cálculo', 'Resultado'],
    [['Interior ancho', '900 − 2 × 38', '824 mm'], ['Interior alto', '2 100 − 38', '2 062 mm'], ['Hoja', '(824 − 6) × (2 062 − 15)', '818 × 2 047 mm']], lambda i: [1, 1, 2][i]),
  ejemplo('El espacio que <span class="nar">pide cada portón</span>', [
    'Antes de los errores, cuánto espacio necesita cada portón para un vano de tres metros.',
    'Batiente de una hoja: un radio de tres metros hacia adentro. Casi imposible en una cochera chica.',
    'Batiente de dos hojas: un metro y medio por cada lado. Y corredizo: nada hacia adentro, pero unos tres metros veinte de muro libre al costado.',
  ], ['Portón', 'Hacia adentro', 'Al costado'],
    [['Batiente, 1 hoja', 'Radio de 3.00 m', '—'], ['Batiente, 2 hojas', 'Radio de 1.50 m', '—'], ['Corredizo', 'Nada', '≈ 3.20 m de muro libre']],
    lambda i: [1, 2, 2][i], izq=300, der=300),
  caso('el corredizo sin guía', [
    'Caso de obra: un portón corredizo se instaló solo con el riel de abajo. La guía de arriba "se ponía después".',
    'Una tarde de viento, al abrirlo, la hoja se inclinó y se salió del riel. Por suerte cayó hacia adentro, sin nadie cerca.',
    'La guía superior va desde el primer día. Y mientras no está, el portón se queda amarrado y nadie lo mueve.',
  ], [('🚫', 'Instalado <b class="nar">sin guía superior</b>'), ('💨', 'Con viento, <b class="nar">se salió del riel</b>'), ('✅', 'La guía va <b class="nar">desde el primer día</b>')]),
  *ejercicio(1,
    'Un portón batiente de <b class="nar">dos hojas</b> para un vano de <b class="nar">3.60 m</b>.<br>¿Cuánto mide cada hoja y cuánto espacio libre necesitas detrás?',
    ['Ahora tú. Un portón batiente de dos hojas para un vano de tres metros sesenta.', '¿Cuánto mide cada hoja, y cuánto espacio libre necesitas detrás para que giren?'],
    'Cada hoja: 3.60 ÷ 2 ≈ <b class="nar">1.80 m</b> (menos las holguras)<br>Espacio libre detrás: un radio de <b class="nar">1.80 m</b> por lado<br>Si ahí se estaciona un carro, <b class="nar">mejor corredizo</b>',
    ['Cada hoja, más o menos la mitad: uno ochenta, menos sus holguras.',
     'Necesitas un metro ochenta libre detrás de cada hoja, para que gire. Si ahí se estaciona un carro, conviene un corredizo.']),
  *ejercicio(2,
    'Un portón corredizo pesa <b class="nar">160 kg</b> y va sobre <b class="nar">2 ruedas</b>.<br>Con la regla del doble, ¿de qué capacidad compras cada rueda?',
    ['Segundo ejercicio. Un portón corredizo pesa ciento sesenta kilos, y va sobre dos ruedas.', 'Con la regla del doble, ¿de qué capacidad compras cada rueda?'],
    'A cada rueda le tocan: 160 ÷ 2 = <b class="nar">80 kg</b><br>Con el doble: <b class="nar">160 kg</b> de capacidad cada una, como mínimo',
    ['A cada rueda le tocan ochenta kilos.',
     'Con la regla del doble: por lo menos ciento sesenta kilos de capacidad cada una. Si el riel tiene polvo o desnivel, mejor un poco más.']),
  faq([
    ('¿Riel en V o ángulo invertido?', 'Los dos; la rueda debe calzar con el riel.', '¿Riel en V o ángulo invertido? Los dos funcionan. Lo importante es que la rueda calce exacto con el riel que elijas.'),
    ('¿Puedo automatizarlo después?', 'Sí, si está bien nivelado y corre suave.', '¿Se puede automatizar después? Sí, si el portón corre suave y está nivelado. Lo vemos en el curso de Portones Automáticos.'),
    ('¿Y el pasador al piso?', 'En la hoja fija de un batiente, con su agujero en el concreto.', '¿Dónde va el pasador al piso? En la hoja que no se usa a diario, con su agujero en el concreto para que no se mueva.'),
  ]),
  repaso([
    ('¿Qué espacio pide un batiente?', 'Un radio igual al ancho de cada hoja.'),
    ('¿Qué pide un corredizo?', 'Muro libre al costado: el ancho más diez a veinte centímetros.'),
    ('¿Es opcional la guía superior?', 'No: sin ella el portón puede caer.'),
    ('¿Qué capacidad deben tener las ruedas?', 'Por lo menos el doble de lo que cargan.'),
  ]),
]

# ───────────── Clase 5 · Rejas y barandas ─────────────
EXT['carp_c5'] = [
  respuesta('portón corredizo de 2.80 m', [
    'La respuesta del reto de la clase pasada: el portón corredizo para un vano de dos metros ochenta, con la misma altura de nuestra cochera.',
    'La hoja: dos ochenta más cinco centímetros por lado, dos noventa. Y el muro libre: el ancho de la hoja más diez a veinte centímetros, unos tres metros.',
    'El peso: bastidor de dos pulgadas, unos dieciséis metros, cuarenta y ocho kilos. Plancha de uno punto cinco: seis y medio metros cuadrados, unos setenta y siete. En total, unos ciento veinticinco kilos.',
  ], ['Dato', 'Resultado'],
    [['Hoja', '2.90 m'], ['Muro libre', '≈ 3.00 – 3.10 m'], ['Bastidor (≈ 16 m)', '≈ 48 kg'], ['Plancha (≈ 6.5 m²)', '≈ 77 kg'], ['Total', '≈ 125 kg']], lambda i: [1, 1, 2, 2, 2][i]),
  ejemplo('Barrotes para <span class="nar">cada ancho</span>', [
    'Antes de los errores, la fórmula de los barrotes aplicada a tres anchos libres, con barrote de media pulgada y separación objetivo de once centímetros.',
    'Ochenta y cinco centímetros libres: seis barrotes, con unos once centímetros de separación real.',
    'Ciento quince: ocho barrotes, como en la clase. Y ciento cuarenta y cinco: once barrotes, con diez punto nueve. Siempre cerca de los once que buscábamos.',
  ], ['Ancho libre', 'Barrotes', 'Separación real'],
    [['85 cm', '6', '≈ 11.0 cm'], ['115 cm', '8', '≈ 11.6 cm'], ['145 cm', '11', '≈ 10.9 cm']],
    lambda i: [1, 2, 2][i], izq=380, der=380, tam=32),
  caso('la reja sin salida', [
    'Caso real: una familia enrejó todas las ventanas del segundo piso, todas fijas, sin ninguna que se pudiera abrir.',
    'Una noche hubo un amago de incendio en la escalera. Los vecinos tuvieron que cortar una reja desde afuera para ayudarlos a salir.',
    'Por eso, en cada piso, por lo menos una reja que se abra desde adentro, con una llave o un pasador fácil, a la vista.',
  ], [('🔒', 'Todas las rejas <b class="nar">fijas</b>'), ('🔥', 'Amago de incendio: <b class="nar">no había salida</b>'), ('✅', 'Una reja <b class="nar">que abra desde adentro</b> por piso')]),
  *ejercicio(1,
    'Una reja tiene <b class="nar">85 cm</b> de ancho libre, barrotes de <b class="nar">1.27 cm</b><br>y separación objetivo de <b class="nar">10 cm</b>.<br>¿Cuántos barrotes y qué separación real?',
    ['Ahora tú. Una reja tiene ochenta y cinco centímetros de ancho libre, barrotes de uno punto veintisiete, y separación objetivo de diez.', '¿Cuántos barrotes, y qué separación real?'],
    'Barrotes: (85 − 10) ÷ (1.27 + 10) = 6.65 → <b class="nar">7</b><br>Separación: (85 − 7 × 1.27) ÷ 8 = <b class="nar">9.5 cm</b>',
    ['Ochenta y cinco menos diez, entre once punto veintisiete: seis punto sesenta y cinco. Redondeas a siete barrotes.',
     'Separación real: ochenta y cinco menos siete por uno punto veintisiete, entre ocho espacios: unos nueve centímetros y medio.']),
  *ejercicio(2,
    'Una baranda de balcón mide <b class="nar">4.50 m</b> de largo.<br>Postes cada <b class="nar">1.50 m</b> como máximo, y uno en cada extremo.<br>¿Cuántos postes y qué alto mínimo?',
    ['Segundo ejercicio. Una baranda de balcón mide cuatro metros cincuenta de largo. Postes cada metro cincuenta como máximo, y uno en cada extremo.', '¿Cuántos postes, y qué alto mínimo?'],
    'Tramos: 4.50 ÷ 1.50 = <b class="nar">3</b> → <b class="nar">4 postes</b><br>Alto en balcón: <b class="nar">1.00 m</b> como mínimo<br>(revisa siempre el reglamento)',
    ['Cuatro cincuenta entre uno cincuenta: tres tramos. Cuatro postes.',
     'Y en un balcón, por lo menos un metro de alto. Siempre revisa lo que pide el reglamento.']),
  faq([
    ('¿Fierro liso o cuadrado para barrotes?', 'Los dos; el cuadrado se ve más firme.', '¿Fierro liso o cuadrado para los barrotes? Los dos sirven. El cuadrado se ve más firme y es más fácil de soldar a escuadra.'),
    ('¿Cómo hago una reja que se abra?', 'Con bisagras de seguridad y una chapa o pasador.', '¿Cómo hago una reja que se abra? Con bisagras de seguridad, que no se puedan sacar desde afuera, y una chapa o pasador por dentro.'),
    ('¿Puedo poner vidrio en la baranda?', 'Sí, con vidrio laminado o templado y sus herrajes.', '¿Se puede poner vidrio en la baranda? Sí, con vidrio laminado o templado, y los herrajes que indique el proveedor.'),
  ]),
  repaso([
    ('¿Cuánto espacio máximo entre barrotes?', 'Unos diez a doce centímetros.'),
    ('¿Barras horizontales en barandas?', 'No: los niños las usan de escalera.'),
    ('¿Cómo se fija una reja?', 'Empotrada o con anclajes, nunca solo pegada con cemento.'),
    ('¿Qué alto tiene la baranda de un balcón?', 'Por lo menos un metro.'),
  ]),
]

# ───────────── Clase 6 · La escalera ─────────────
EXT['carp_c6'] = [
  respuesta('reja de 1.50 m', [
    'La respuesta del reto de la clase pasada: una reja de uno cincuenta, con marco de una pulgada y barrotes de media.',
    'Ancho libre: ciento cincuenta menos dos veces dos punto cincuenta y cuatro, unos ciento cuarenta y cinco centímetros.',
    'Barrotes: ciento cuarenta y cinco menos diez, entre once punto veintisiete: doce. Y la separación real: casi exactamente diez centímetros.',
  ], ['Dato', 'Resultado'], [['Ancho libre', '≈ 145 cm'], ['Barrotes', '12'], ['Separación real', '≈ 9.98 cm']], lambda i: i),
  ejemplo('Combinaciones que <span class="nar">cumplen la regla</span>', [
    'Antes de los errores, varias combinaciones de contrapaso y paso que cumplen la regla de oro.',
    'Diecisiete y veintiocho: sesenta y dos. Dieciocho y veintiséis: sesenta y dos. Dieciséis y treinta: también sesenta y dos.',
    'Y diecinueve con veinticuatro da sesenta y dos, pero el contrapaso de diecinueve ya es alto para una casa. La regla sola no basta: revisa también los rangos.',
  ], ['Contrapaso', 'Paso', '2C + P', '¿Cómoda?'],
    [['17 cm', '28 cm', '62', '✓'], ['18 cm', '26 cm', '62', '✓'], ['16 cm', '30 cm', '62', '✓ (más larga)'], ['19 cm', '24 cm', '62', '✗ muy alta']],
    lambda i: [1, 1, 1, 2][i], izq=300, der=300),
  caso('el último escalón', [
    'Caso de obra: una escalera perfecta en el taller, con todos los contrapasos de diecisiete y medio.',
    'Después, arriba pusieron un piso de madera de dos centímetros. El último escalón quedó de quince y medio. Todos tropezaban justo ahí.',
    'Antes de calcular, pregunta qué piso va arriba y abajo, y mide de piso terminado a piso terminado.',
  ], [('🪜', 'Todos los escalones de <b class="nar">17.5 cm</b>…'), ('🪵', 'Arriba pusieron piso de <b class="nar">2 cm</b>: el último quedó en 15.5'), ('📏', 'Mide de <b class="nar">piso terminado a piso terminado</b>')]),
  *ejercicio(1,
    'Altura de piso terminado a piso terminado: <b class="nar">2.95 m</b>.<br>Paso de <b class="nar">27 cm</b>. Calcula contrapasos, contrapaso real,<br>la regla de oro y el largo en planta.',
    ['Ahora tú. Altura de piso terminado a piso terminado: dos metros noventa y cinco. Paso de veintisiete centímetros.', 'Calcula los contrapasos, el contrapaso real, la regla de oro, y el largo en planta.'],
    '295 ÷ 17.5 = 16.9 → <b class="nar">17 contrapasos</b> · real: 295 ÷ 17 = <b class="nar">17.35 cm</b><br>Regla: 2 × 17.35 + 27 = <b class="nar">61.7</b> ✓<br>Planta: 16 pasos × 27 = <b class="nar">4.32 m</b>',
    ['Doscientos noventa y cinco entre diecisiete y medio da dieciséis punto nueve: diecisiete contrapasos. El real: diecisiete punto treinta y cinco centímetros.',
     'La regla: dos por diecisiete punto treinta y cinco, más veintisiete: sesenta y uno punto siete. Bien. Y el largo en planta: dieciséis pasos de veintisiete, cuatro metros treinta y dos.']),
  *ejercicio(2,
    'Esa escalera lleva <b class="nar">16 peldaños</b> de plancha estriada de 3 mm (≈ 25 kg/m²),<br>de <b class="nar">0.90 m</b> de ancho por <b class="nar">0.33 m</b> de desarrollo con el doblez.<br>¿Cuánto pesan los peldaños?',
    ['Segundo ejercicio. Esa escalera lleva dieciséis peldaños de plancha estriada de tres milímetros, de unos veinticinco kilos por metro cuadrado.', 'Cada peldaño mide noventa centímetros de ancho, por treinta y tres de desarrollo con el doblez. ¿Cuánto pesan los peldaños?'],
    'Un peldaño: 0.90 × 0.33 = <b class="nar">0.30 m²</b> × 25 ≈ <b class="nar">7.4 kg</b><br>Dieciséis: 16 × 7.4 ≈ <b class="nar">119 kg</b> (más las zancas)',
    ['Un peldaño: cero noventa por cero treinta y tres, cero punto treinta metros cuadrados. Por veinticinco kilos: unos siete y medio.',
     'Los dieciséis: unos ciento diecinueve kilos. Y faltan las zancas y la baranda. Planifica cómo la vas a subir y a fijar.']),
  faq([
    ('¿Escalera de caracol?', 'Ahorra espacio, pero es menos cómoda.', '¿Y una escalera de caracol? Ahorra espacio, pero es menos cómoda para subir cosas. Úsala donde no hay otra opción.'),
    ('¿Peldaño de madera sobre metal?', 'Sí: bandeja de ángulo y madera atornillada.', '¿Puedo poner peldaños de madera? Sí, sobre una bandeja de ángulo, atornillados por debajo.'),
    ('¿Cómo la fijo arriba y abajo?', 'Placas con anclajes a la losa.', '¿Cómo se fija? Con placas y anclajes a la losa, arriba y abajo. Nunca solo apoyada.'),
  ]),
  repaso([
    ('¿Cuál es la regla de oro?', 'Dos contrapasos más un paso, entre sesenta y sesenta y cuatro.'),
    ('¿Cuánto mide un contrapaso cómodo?', 'Entre diecisiete y dieciocho centímetros.'),
    ('¿Cuántos pasos hay con quince contrapasos?', 'Catorce.'),
    ('¿Desde dónde se mide la altura?', 'De piso terminado a piso terminado.'),
  ]),
]

# ───────────── Clase 7 · Acabado, instalación y cotización ─────────────
EXT['carp_c7'] = [
  respuesta('escalera de 2.80 m', [
    'La respuesta del reto de la clase pasada: la escalera para dos metros ochenta.',
    'Doscientos ochenta entre diecisiete y medio da dieciséis exacto: dieciséis contrapasos de diecisiete y medio.',
    'Paso de veintiocho: la regla da sesenta y tres, dentro del rango. Y el largo en planta: quince pasos de veintiocho, cuatro metros veinte.',
  ], ['Dato', 'Resultado'], [['Contrapasos', '16 × 17.5 cm'], ['Paso', '28 cm'], ['Regla de oro', '2 × 17.5 + 28 = 63 ✓'], ['Largo en planta', '15 × 28 = 4.20 m']], lambda i: [1, 1, 2, 2][i]),
  ejemplo('Cotizamos <span class="nar">la reja de la ventana</span>', [
    'Antes de los errores, otra cotización con las cinco partes: la reja de la ventana de uno veinte por uno veinte. Precios de ejemplo.',
    'Materiales: marco, ocho barrotes, anclajes, pintura y consumibles: unos ciento sesenta soles. Mano de obra: medio día de maestro y ayudante, cien.',
    'Instalación: sesenta. Gastos del taller, diez por ciento: treinta y dos. Suma: trescientos cincuenta y dos.',
    'Utilidad del veinte por ciento: setenta. Precio: unos cuatrocientos veintidós soles, y si das factura, más IGV.',
  ], ['Parte', 'Monto'],
    [['Materiales', 'S/ 160'], ['Mano de obra (½ día)', 'S/ 100'], ['Instalación', 'S/ 60'], ['Gastos del taller (10 %)', 'S/ 32'], ['Utilidad (20 %)', 'S/ 70'], ['Precio', '≈ S/ 422 + IGV']],
    lambda i: [1, 1, 2, 2, 3, 3][i], izq=440, der=440, tam=29),
  caso('la puerta que se abría sola', [
    'Caso de obra: una puerta instalada rápido, sin aplomar el marco. Se veía bien.',
    'Pero el marco quedó inclinado hacia afuera. Cada vez que la dejaban entreabierta, la hoja se abría sola, y a veces se cerraba de golpe.',
    'Hubo que soltar los anclajes, aplomar y volver a fijar. Aplomar toma cinco minutos; corregirlo después, una mañana.',
  ], [('🚪', 'Marco <b class="nar">sin aplomar</b>'), ('↪️', 'La hoja <b class="nar">se abría sola</b>'), ('⏱', 'Aplomar: 5 min · corregir: <b class="nar">una mañana</b>')]),
  *ejercicio(1,
    'Cotiza: materiales <b class="nar">S/ 650</b> · 2 días de maestro (S/ 120) y ayudante (S/ 80)<br>instalación <b class="nar">S/ 150</b> · gastos 10 % · utilidad 20 % · IGV 18 %.<br>¿Cuál es el precio con IGV?',
    ['Ahora tú. Materiales, seiscientos cincuenta soles. Dos días de maestro a ciento veinte y ayudante a ochenta. Instalación, ciento cincuenta.', 'Gastos del taller diez por ciento, utilidad veinte por ciento, e IGV dieciocho por ciento. ¿Cuál es el precio con IGV?'],
    'Mano de obra: 2 × 200 = <b class="nar">400</b> · Subtotal: 650 + 400 + 150 = 1 200<br>Gastos: <b class="nar">120</b> → 1 320 · Utilidad: <b class="nar">264</b> → <b class="nar">S/ 1 584</b><br>Con IGV: 1 584 × 1.18 ≈ <b class="nar">S/ 1 869</b>',
    ['Mano de obra: dos días por doscientos, cuatrocientos. Con materiales e instalación: mil doscientos. Gastos del diez por ciento: ciento veinte. Mil trescientos veinte.',
     'Utilidad del veinte por ciento: doscientos sesenta y cuatro. Precio: mil quinientos ochenta y cuatro. Y con IGV: unos mil ochocientos sesenta y nueve soles.']),
  *ejercicio(2,
    'Con ese precio (S/ 1 869 con IGV), pides <b class="nar">50 % de adelanto</b>.<br>¿Cuánto cobras al inicio, cuánto al final,<br>y alcanza el adelanto para el material?',
    ['Segundo ejercicio. Con ese precio, mil ochocientos sesenta y nueve con IGV, pides cincuenta por ciento de adelanto.', '¿Cuánto cobras al inicio, cuánto al final, y alcanza el adelanto para el material?'],
    'Adelanto: <b class="nar">≈ S/ 935</b> · Saldo a la entrega: <b class="nar">≈ S/ 934</b><br>El material cuesta S/ 650: <b class="nar">sí alcanza</b>, y no pones plata de tu bolsillo',
    ['El adelanto: unos novecientos treinta y cinco soles. Y el saldo, a la entrega, novecientos treinta y cuatro.',
     'El material cuesta seiscientos cincuenta: el adelanto sí alcanza. No financias al cliente con tu plata.']),
  faq([
    ('¿Cobro el transporte aparte?', 'Inclúyelo en instalación, pero que se vea.', '¿Cobro el transporte aparte? Inclúyelo en la partida de instalación, pero que se vea en la cotización.'),
    ('¿Y si el cliente pide descuento?', 'Quita alcance, no utilidad.', '¿Y si el cliente pide descuento? Mejor quita algo del alcance, como un acabado, que bajar tu utilidad.'),
    ('¿Qué garantía doy?', 'Por escrito: fabricación e instalación, con plazo.', '¿Qué garantía doy? Por escrito: de fabricación e instalación, con un plazo claro y lo que no cubre.'),
  ]),
  repaso([
    ('¿Cuáles son las cinco partes del precio?', 'Materiales, mano de obra, instalación, gastos del taller y utilidad.'),
    ('¿Cuánto adelanto se suele pedir?', 'La mitad.'),
    ('¿Qué haces antes de fijar del todo un marco?', 'Probar que la hoja abre y cierra bien.'),
    ('¿Dónde se pinta?', 'En el taller, antes de instalar.'),
  ]),
]

# ───────────── Clase 8 · Ventanas con vidrio ─────────────
EXT['carp_c8'] = [
  ejemplo('Medidas del vidrio <span class="nar">para tres hojas</span>', [
    'Antes de los errores, la medida del vidrio para tres hojas distintas, con cuatro milímetros de holgura por lado.',
    'Luz libre de seiscientos por mil: el vidrio, quinientos noventa y dos por novecientos noventa y dos.',
    'Mil cien por novecientos, la de la clase: mil noventa y dos por ochocientos noventa y dos. Y quinientos sesenta por mil doscientos: quinientos cincuenta y dos por mil ciento noventa y dos.',
  ], ['Luz libre de la hoja', 'Vidrio (−8 mm por lado total)'],
    [['600 × 1 000 mm', '592 × 992 mm'], ['1 100 × 900 mm', '1 092 × 892 mm'], ['560 × 1 200 mm', '552 × 1 192 mm']],
    lambda i: [1, 2, 2][i], izq=400, der=400, tam=32),
  ejemplo('¿Cuánto pesa <span class="nar">un vidrio</span>?', [
    'Y el peso del vidrio: unos dos kilos y medio por metro cuadrado, por cada milímetro de espesor.',
    'En cuatro milímetros: unos diez kilos por metro cuadrado. En seis: quince. En ocho: veinte.',
    'El vidrio de nuestra ventana, de mil noventa y dos por ochocientos noventa y dos, en cuatro milímetros: casi diez kilos. Las bisagras y los calzos tienen que aguantarlo.',
  ], ['Espesor', 'Peso por m²'],
    [['4 mm', '≈ 10 kg'], ['6 mm', '≈ 15 kg'], ['8 mm', '≈ 20 kg']],
    lambda i: [1, 1, 2][i], izq=560, der=560, tam=34),
  caso('el junquillo soldado', [
    'Caso de obra: un taller soldaba los junquillos de las ventanas, porque era más rápido que atornillarlos.',
    'A los meses, un vidrio se rompió con una pelota. Para cambiarlo, hubo que cortar el junquillo con esmeril, sobre el vidrio roto, y volver a pintar.',
    'El junquillo va atornillado. Cambiar un vidrio debe ser cosa de minutos, no de un día.',
  ], [('🔥', 'Junquillos <b class="nar">soldados</b>'), ('⚽', 'Cambiar un vidrio: <b class="nar">esmeril y pintura</b>'), ('🔩', 'Junquillo <b class="nar">atornillado</b>')]),
  *ejercicio(1,
    'Una ventana corrediza de <b class="nar">2 hojas</b>. Cada hoja tiene una luz libre<br>de <b class="nar">560 × 1 000 mm</b>. Holgura de <b class="nar">4 mm</b> por lado.<br>¿Qué vidrios pides?',
    ['Ahora tú. Una ventana corrediza de dos hojas. Cada hoja tiene una luz libre de quinientos sesenta por mil milímetros. Holgura de cuatro por lado.', '¿Qué vidrios pides?'],
    'Cada vidrio: 560 − 8 = 552 · 1 000 − 8 = 992<br>Pides <b class="nar">2 vidrios de 552 × 992 mm</b>',
    ['A cada medida le restas ocho: cuatro por lado. Quinientos cincuenta y dos por novecientos noventa y dos.',
     'Y son dos hojas: pides dos vidrios de esa medida. Anota también el espesor y si es templado.']),
  *ejercicio(2,
    'Una mampara tiene <b class="nar">2 paños de 1.20 × 2.00 m</b> con vidrio de <b class="nar">6 mm</b>.<br>¿Qué tipo de vidrio va y cuánto pesa cada paño?',
    ['Segundo ejercicio. Una mampara tiene dos paños de uno veinte por dos metros, con vidrio de seis milímetros.', '¿Qué tipo de vidrio va, y cuánto pesa cada paño?'],
    'Es zona de paso: vidrio de <b class="nar">seguridad</b>, templado o laminado<br>Peso: 1.20 × 2.00 = 2.4 m² × 15 = <b class="nar">36 kg</b> por paño',
    ['Es una mampara, donde la gente pasa y puede chocar: vidrio de seguridad, templado o laminado.',
     'Cada paño: dos punto cuatro metros cuadrados por quince kilos: treinta y seis kilos. Se necesitan dos personas para colocarlo.']),
  faq([
    ('¿Silicona o masilla?', 'Silicona neutra para exteriores.', '¿Silicona o masilla? Para exteriores, silicona neutra, que no ataca el metal ni la pintura.'),
    ('¿Puedo cortar el vidrio templado?', 'No: se pide a medida exacta.', '¿Se puede cortar un vidrio templado? No. Se pide a la medida exacta, porque al cortarlo se rompe en pedacitos.'),
    ('¿Calzos de qué material?', 'Jebe o neopreno, nunca madera.', '¿De qué son los calzos? De jebe o neopreno. Nunca madera, que se pudre con la humedad.'),
  ]),
  repaso([
    ('¿Toca el vidrio al fierro?', 'Nunca.'),
    ('¿Cuánta holgura lleva el vidrio?', 'Unos tres a cinco milímetros por lado.'),
    ('¿Cómo va el junquillo?', 'Atornillado, no soldado.'),
    ('¿Qué vidrio va en una puerta?', 'De seguridad: templado o laminado.'),
  ]),
]

# ───────────── Clase 9 · Policarbonato ─────────────
EXT['carp_c9'] = [
  respuesta('vidrio de 800 × 1 200', [
    'La respuesta del reto de la clase pasada: el vidrio para una hoja con luz libre de ochocientos por mil doscientos.',
    'Con cuatro milímetros por lado, le restas ocho a cada medida: setecientos noventa y dos por mil ciento noventa y dos.',
    'Y si es una puerta: vidrio de seguridad, templado o laminado. Nunca vidrio común.',
  ], ['Dato', 'Resultado'], [['Vidrio', '792 × 1 192 mm'], ['Si es puerta', 'Templado o laminado']], lambda i: i + 1),
  ejemplo('Cuánto <span class="nar">se mueve</span> la plancha', [
    'Antes de los errores, cuánto se estira el policarbonato entre el día y la noche: unos tres milímetros por metro.',
    'Una plancha de dos metros: seis milímetros. De tres metros: nueve. Y una plancha entera de cinco ochenta: casi dieciocho milímetros.',
    'Por eso el agujero es más grande que el tornillo, y el tornillo no se aprieta a fondo: solo hasta que la arandela de jebe selle.',
  ], ['Largo de la plancha', 'Movimiento (≈ 3 mm por m)'],
    [['2.00 m', '≈ 6 mm'], ['3.00 m', '≈ 9 mm'], ['5.80 m', '≈ 17 mm']],
    lambda i: [1, 1, 1][i], izq=440, der=440, tam=33),
  ejemplo('La pendiente <span class="nar">en centímetros</span>', [
    'Y la pendiente mínima de unos cinco grados, en centímetros, según el fondo del techito.',
    'Dos metros de fondo: atrás va unos dieciocho centímetros más alto. Tres metros: veintisiete. Cuatro metros: treinta y seis.',
  ], ['Fondo', 'Cuánto más alto atrás (≈ 9 cm por m)'],
    [['2 m', '≈ 18 cm'], ['3 m', '≈ 27 cm'], ['4 m', '≈ 36 cm']],
    lambda i: 1, izq=400, der=400, tam=33),
  caso('el lado UV al revés', [
    'Caso de obra: un toldo de policarbonato alveolar, instalado en un solo día. Se veía perfecto.',
    'Al año estaba amarillo, opaco y con rajaduras. El lado con protección UV había quedado hacia abajo, y el sol lo destruyó.',
    'Antes de quitar el plástico protector, busca la marca del lado UV. Ese lado va hacia el cielo.',
  ], [('☀️', 'Lado UV <b class="nar">hacia abajo</b>'), ('🟡', 'Al año: <b class="nar">amarillo y rajado</b>'), ('✅', 'Lado UV <b class="nar">hacia el cielo</b>, siempre')]),
  *ejercicio(1,
    'Un techito de <b class="nar">5 m de ancho</b> por <b class="nar">3 m de fondo</b>, con alveolar de <b class="nar">2.10 × 5.80 m</b>.<br>¿Cuántas planchas compras y cuánto más alto va atrás?',
    ['Ahora tú. Un techito de cinco metros de ancho por tres de fondo, con planchas alveolares de dos diez por cinco ochenta.', '¿Cuántas planchas compras, y cuánto más alto va atrás?'],
    'Canales a lo largo de la pendiente: tramos de <b class="nar">3 m</b> → 1 por plancha (sobra 2.80)<br>Ancho: 5 ÷ 2.10 = 2.4 → <b class="nar">3 tramos</b> → <b class="nar">3 planchas</b><br>Atrás: 3 × 9 = <b class="nar">27 cm</b> más alto',
    ['Los canales van en el sentido de la pendiente, en tramos de tres metros. De cada plancha sale solo un tramo de tres: sobran dos ochenta.',
     'Para cinco metros de ancho necesitas tres tramos: tres planchas. Y atrás va veintisiete centímetros más alto. Pregunta si venden planchas de tres metros: te ahorras el sobrante.']),
  *ejercicio(2,
    'Con planchas de <b class="nar">3 m</b> de largo, ¿cuánto se mueven?<br>Si el tornillo es de <b class="nar">6 mm</b>, ¿de qué tamaño haces el agujero?',
    ['Segundo ejercicio. Con planchas de tres metros de largo, ¿cuánto se mueven?', 'Si el tornillo es de seis milímetros, ¿de qué tamaño haces el agujero?'],
    'Movimiento: 3 × 3 = <b class="nar">9 mm</b> en todo el largo (≈ 4.5 mm hacia cada extremo si fijas al centro)<br>Agujero: unos <b class="nar">10 a 12 mm</b> para el tornillo de 6 mm<br>(o lo que indique el fabricante)',
    ['Tres metros por tres milímetros: nueve milímetros en todo el largo.',
     'Haz el agujero bastante más grande que el tornillo, unos diez a doce milímetros, o lo que diga la ficha del fabricante. Y la arandela de jebe tapa el agujero.']),
  faq([
    ('¿Alveolar o compacto?', 'Alveolar aísla y es liviano; compacto aguanta golpes.', '¿Alveolar o compacto? El alveolar aísla y es liviano. El compacto aguanta mejor los golpes, como el granizo o una pelota.'),
    ('¿Cómo se unen dos planchas?', 'Con perfil H o de unión.', '¿Cómo se unen dos planchas alveolares? Con un perfil de unión, en forma de H, o el que venda el fabricante.'),
    ('¿Se limpia con cualquier cosa?', 'Agua y jabón suave; nada abrasivo.', '¿Cómo se limpia? Con agua y jabón suave. Nada de solventes ni esponjas abrasivas.'),
  ]),
  repaso([
    ('¿Hacia dónde va el lado UV?', 'Hacia arriba, hacia el sol.'),
    ('¿En qué sentido van los canales?', 'En el sentido de la pendiente.'),
    ('¿Con qué se sella el extremo de abajo?', 'Con cinta microperforada.'),
    ('¿Qué pendiente mínima?', 'Unos cinco grados, nueve centímetros por metro.'),
  ]),
]

# ───────────── Clase 10 · Estanterías y muebles ─────────────
EXT['carp_c10'] = [
  respuesta('toldo de 4 × 2.50 m', [
    'La respuesta del reto de la clase pasada: el toldo de cuatro metros de ancho por dos y medio de fondo.',
    'Los canales a lo largo de la pendiente: tramos de dos y medio. De cada plancha de cinco ochenta salen dos tramos. Y para cuatro metros de ancho, dos tramos de dos diez.',
    'Una sola plancha alcanza. Y atrás va unos veintidós centímetros más alto: dos y medio por nueve.',
  ], ['Dato', 'Resultado'], [['Tramos de 2.50 m', '2 (de una plancha)'], ['Planchas', '1'], ['Más alto atrás', '≈ 22 cm']], lambda i: [1, 2, 2][i]),
  ejemplo('Repisas: <span class="nar">plancha y peso</span>', [
    'Antes de los errores, cuánto pesa la plancha de las repisas. La de uno punto dos milímetros pesa unos nueve punto cuatro kilos por metro cuadrado.',
    'Una repisa de un metro por cuarenta, con pestañas de cuatro centímetros: uno punto cero ocho por cero punto cuarenta y ocho. Medio metro cuadrado, unos cinco kilos.',
    'Una de uno veinte por cincuenta: uno punto veintiocho por cero punto cincuenta y ocho. Unos siete kilos.',
  ], ['Repisa', 'Plancha con pestañas', 'Peso (1.2 mm)'],
    [['1.00 × 0.40 m', '1.08 × 0.48 = 0.52 m²', '≈ 5 kg'], ['1.20 × 0.50 m', '1.28 × 0.58 = 0.74 m²', '≈ 7 kg']],
    lambda i: i + 1, izq=260, der=260, tam=31),
  caso('la estantería que se vino abajo', [
    'Caso de taller: una estantería de dos metros, bien soldada, pero sin anclar al muro. "Total, pesa mucho, no se mueve".',
    'Un trabajador se subió al segundo nivel para alcanzar una caja de arriba. La estantería se inclinó y cayó. Por suerte, él saltó a tiempo.',
    'Toda estantería alta se ancla al muro o al piso. Son dos anclajes y diez minutos.',
  ], [('🗄️', 'Estantería alta <b class="nar">sin anclar</b>'), ('⚠️', 'Alguien se subió: <b class="nar">se cayó</b>'), ('🔩', 'Dos anclajes al muro: <b class="nar">diez minutos</b>')]),
  *ejercicio(1,
    'Estantería de <b class="nar">1.20 × 0.50 × 2.00 m</b> con <b class="nar">4 repisas</b> de 1.2 mm<br>(≈ 7 kg cada una) y 4 parantes de ángulo (≈ 1.9 kg/m).<br>¿Cuánto pesa sin arriostres?',
    ['Ahora tú. Una estantería de uno veinte por cincuenta por dos metros, con cuatro repisas de uno punto dos milímetros, de unos siete kilos cada una, y cuatro parantes de ángulo, de uno punto nueve kilos por metro.', '¿Cuánto pesa, sin contar los arriostres?'],
    'Repisas: 4 × 7 = <b class="nar">28 kg</b><br>Parantes: 4 × 2 m × 1.9 = <b class="nar">15.2 kg</b><br>Total: <b class="nar">≈ 43 kg</b>',
    ['Las repisas: cuatro por siete, veintiocho kilos.',
     'Los parantes: ocho metros por uno punto nueve, unos quince kilos. En total, unos cuarenta y tres kilos.']),
  *ejercicio(2,
    'Esa estantería lleva <b class="nar">arriostres en X</b> atrás y en los dos costados.<br>¿Cuántos metros de platina necesitas?',
    ['Segundo ejercicio. Esa estantería lleva arriostres en X atrás y en los dos costados.', '¿Cuántos metros de platina necesitas?'],
    'Atrás: √(1.20² + 2.00²) ≈ 2.33 m × 2 = <b class="nar">4.66 m</b><br>Costados: √(0.50² + 2.00²) ≈ 2.06 m × 2 × 2 = <b class="nar">8.25 m</b><br>Total: <b class="nar">≈ 12.9 m</b> → compra 3 barras de 6 m (o 2 y un sobrante)',
    ['Atrás: la diagonal de uno veinte por dos, unos dos treinta y tres. Por dos: cuatro sesenta y seis.',
     'Los costados: la diagonal de cincuenta por dos, dos cero seis. Cuatro diagonales: ocho veinticinco. En total, casi trece metros de platina.']),
  faq([
    ('¿Ángulo ranurado o soldado?', 'Ranurado se arma rápido; soldado es más rígido.', '¿Ángulo ranurado o estantería soldada? El ranurado se arma rápido y se ajusta. La soldada es más rígida y sale a medida.'),
    ('¿Cómo pongo el letrero de carga?', 'Una placa o etiqueta en cada nivel.', '¿Cómo pongo la carga máxima? Con una placa o etiqueta visible en cada nivel, o en el costado.'),
    ('¿Qué pintura para muebles?', 'Base y esmalte, o pintura en polvo si tienes horno.', '¿Qué pintura para muebles? Base y esmalte, como siempre. Si tienes acceso a un horno, la pintura en polvo queda muy resistente.'),
  ]),
  repaso([
    ('¿Qué evita que una estantería se vaya de lado?', 'Los arriostres en X.'),
    ('¿Por qué se doblan las repisas con pestañas?', 'Porque la pestaña funciona como el peralte de una viga.'),
    ('¿Qué se ancla en una estantería alta?', 'Al muro o al piso.'),
    ('¿Qué detalles lleva un mueble?', 'Sin rebabas, tubos tapados y regatones.'),
  ]),
]

# ───────────── Clase 11 · Cercos perimétricos ─────────────
EXT['carp_c11'] = [
  respuesta('estantería de 1.20 × 0.50 × 2 m', [
    'La respuesta del reto de la clase pasada: la estantería de uno veinte por cincuenta por dos metros, con cuatro niveles.',
    'Arriostres en X atrás y en los dos costados, y dos anclajes al muro, arriba.',
    'Los parantes: cuatro de dos metros, ocho metros de ángulo de una y media por un octavo. Unos quince kilos.',
  ], ['Dato', 'Resultado'], [['Arriostres', 'X atrás y en 2 costados'], ['Anclajes', '2 al muro, arriba'], ['Parantes', '8 m ≈ 15 kg']], lambda i: i),
  ejemplo('Postes <span class="nar">según el cerco</span>', [
    'Antes de los errores, cada cuánto van los postes según el tipo de cerco. Son referencias para empezar.',
    'Malla, de dos metros de alto: cada dos y medio a tres metros. Paneles de reja: cada dos a dos y medio, porque el panel define la medida.',
    'Y el cerco ciego de planchas, que recibe todo el viento: lo define el ingeniero. Postes más fuertes, más juntos y con dados más grandes.',
  ], ['Cerco', 'Postes cada', 'Ojo con'],
    [['Malla (2 m de alto)', '2.5 – 3.0 m', 'Tensores y puntales'], ['Paneles de reja', '2.0 – 2.5 m', 'La medida del panel'], ['Ciego de planchas', 'Lo define el ingeniero', 'El empuje del viento']],
    lambda i: [1, 1, 2][i], izq=240, der=240),
  caso('el cerco en terreno ajeno', [
    'Caso de obra: un cerco de cincuenta metros, terminado y pintado. El cliente había indicado el límite "más o menos por aquí".',
    'El vecino trajo su plano y un topógrafo: el cerco estaba cuarenta centímetros dentro de su terreno. Hubo que sacarlo completo y volver a hacerlo.',
    'Antes de excavar el primer dado: el límite confirmado por escrito, con el plano o con estacas que el cliente apruebe.',
  ], [('📍', 'Límite "<b class="nar">más o menos por aquí</b>"'), ('📐', '40 cm dentro del <b class="nar">terreno del vecino</b>'), ('✅', 'Límite <b class="nar">confirmado por escrito</b> antes de excavar')]),
  *ejercicio(1,
    'Un cerco de <b class="nar">72 m</b> con postes cada <b class="nar">3 m</b>.<br>Dados de <b class="nar">30 × 30 × 60 cm</b>.<br>¿Cuántos postes y cuánto concreto?',
    ['Ahora tú. Un cerco de setenta y dos metros, con postes cada tres metros. Dados de treinta por treinta por sesenta centímetros.', '¿Cuántos postes, y cuánto concreto?'],
    'Tramos: 72 ÷ 3 = 24 → <b class="nar">25 postes</b><br>Un dado: 0.3 × 0.3 × 0.6 = <b class="nar">0.054 m³</b><br>Concreto: 25 × 0.054 = <b class="nar">1.35 m³</b>',
    ['Setenta y dos entre tres: veinticuatro tramos, veinticinco postes.',
     'Cada dado: cero punto cero cinco cuatro metros cúbicos. Por veinticinco: uno punto treinta y cinco metros cúbicos de concreto.']),
  *ejercicio(2,
    'La malla viene en rollos de <b class="nar">10 m</b>. Para los <b class="nar">72 m</b>, con 10 cm de traslape<br>en cada unión, ¿cuántos rollos compras?<br>¿Y cuántos metros de alambre tensor, si van 3 líneas?',
    ['Segundo ejercicio. La malla viene en rollos de diez metros. Para los setenta y dos metros, con diez centímetros de traslape en cada unión, ¿cuántos rollos compras?', 'Y si van tres líneas de alambre tensor, ¿cuántos metros de alambre?'],
    'Malla: 72 m + 7 traslapes × 0.10 = 72.7 m → <b class="nar">8 rollos</b><br>Tensor: 3 × 72 = 216 m + amarres (≈ 5 %) ≈ <b class="nar">227 m</b>',
    ['Setenta y dos metros, más siete traslapes de diez centímetros: setenta y dos punto siete. Ocho rollos.',
     'El tensor: tres líneas de setenta y dos, doscientos dieciséis metros, más un cinco por ciento para amarres: unos doscientos veintisiete metros.']),
  faq([
    ('¿Poste de tubo redondo o cuadrado?', 'Los dos; el cuadrado facilita soldar paneles.', '¿Poste redondo o cuadrado? Los dos sirven. El cuadrado facilita soldar paneles y abrazaderas.'),
    ('¿Malla galvanizada o plastificada?', 'La plastificada dura más cerca del mar.', '¿Malla galvanizada o plastificada? La plastificada resiste mejor en zonas húmedas o cerca del mar.'),
    ('¿Necesito permiso?', 'A veces: consulta en tu municipalidad.', '¿Necesito permiso para un cerco? Depende del lugar y la altura. Que el cliente consulte en su municipalidad.'),
  ]),
  repaso([
    ('¿Dónde se oxida primero un poste?', 'En la línea del suelo.'),
    ('¿Qué lleva el dado arriba?', 'Una corona en pendiente para que escurra el agua.'),
    ('¿Qué tensa la malla?', 'Los alambres tensores, desde los postes de esquina.'),
    ('¿Qué confirmas antes de empezar?', 'El límite del terreno.'),
  ]),
]
