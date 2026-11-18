"""Carpintería Metálica · Clase 4 ampliada (≈7–8 min): base + escenas nuevas de carp_ext."""
import carp_c4 as base
from carp_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['carp_c4'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'carp_x4')
