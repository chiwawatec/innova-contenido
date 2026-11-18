"""Carpintería Metálica · Clase 2 ampliada (≈7–8 min): base + escenas nuevas de carp_ext."""
import carp_c2 as base
from carp_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['carp_c2'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'carp_x2')
