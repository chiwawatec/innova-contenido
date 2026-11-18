"""Ejercicio con la solución debajo del enunciado sin taparlo (para enunciados de varias líneas)."""
import re
from naves_ext import caja
from sold_comun import titulo, badge


def _lineas(html, por_linea):
    txt = re.sub(r'<(?!br)[^>]+>', '', html)
    return sum(max(1, -(-len(p.strip()) // por_linea)) for p in re.split(r'<br\s*/?>', txt))


def ejercicio(n, enunciado, frases_enunciado, respuesta, frases_respuesta):
    a = dict(despues=4.0, frases=frases_enunciado + ['Pausa el video y resuélvelo. Te espero.'],
             zoom=[(0, 1.0, 50, 50)],
             html=titulo(f'Ejercicio <span class="nar">{n}</span>', top=90) + caja(enunciado, 0, top=250, izq=280, der=280) +
             badge('PAUSA EL VIDEO Y RESUELVE', len(frases_enunciado), 700, 640, '#5b8def', '⏸'))
    alto = _lineas(enunciado, 100) * 26 * 1.55 + 60
    b = dict(frases=frases_respuesta, zoom=[(0, 1.0, 50, 50), (len(frases_respuesta) - 1, 1.03, 50, 55)],
             html=titulo(f'Solución <span class="nar">{n}</span>', top=90) + caja(enunciado, 0, top=200, tam=26, izq=280, der=280, borde='rgba(255,255,255,.25)') +
             caja(respuesta, 0, top=int(200 + alto + 30), izq=280, der=280, tam=31, borde='rgba(63,158,90,.8)', mas=0.4))
    return [a, b]
