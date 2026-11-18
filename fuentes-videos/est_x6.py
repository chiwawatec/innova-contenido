"""Estructuras Metálicas · Clase 6 ampliada (≈8 min): base + escenas nuevas de est_ext."""
import est_c6 as base
from est_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['est_c6'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'est_x6')
