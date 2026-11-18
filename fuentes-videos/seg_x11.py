"""Seguridad en Obra · Clase 11 ampliada (≈7 min): base + escenas nuevas de seg_ext."""
import seg_c11 as base
from seg_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['seg_c11'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'seg_x11')
