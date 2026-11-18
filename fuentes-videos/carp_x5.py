"""Carpintería Metálica · Clase 5 ampliada (≈7–8 min): base + escenas nuevas de carp_ext."""
import carp_c5 as base
from carp_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['carp_c5'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'carp_x5')
