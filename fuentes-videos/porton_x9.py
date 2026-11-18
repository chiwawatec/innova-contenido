"""Portones Automáticos · Clase 9 ampliada (≈7 min): base + escenas nuevas de porton_ext."""
import porton_c9 as base
from porton_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['porton_c9'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'porton_x9')
