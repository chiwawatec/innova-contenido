"""Soldadura Estructural · Clase 1 ampliada (≈8 min): base + escenas nuevas de sold_ext."""
import sold_c1 as base
from sold_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['sold_c1'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'sold_x1')
