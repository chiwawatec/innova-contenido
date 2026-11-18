"""El Negocio del Metalero · Clase 9 ampliada (≈7 min): base + escenas nuevas de neg_ext."""
import neg_c9 as base
from neg_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['neg_c9'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'neg_x9')
