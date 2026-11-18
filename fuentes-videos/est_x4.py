"""Estructuras Metálicas · Clase 4 ampliada (≈8 min): base + escenas nuevas de est_ext."""
import est_c4 as base
from est_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['est_c4'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'est_x4')
