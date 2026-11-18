"""El Negocio del Metalero · Clase 11 ampliada (≈7 min): base + escenas nuevas de neg_ext."""
import neg_c11 as base
from neg_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['neg_c11'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'neg_x11')
