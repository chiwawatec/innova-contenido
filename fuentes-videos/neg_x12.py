"""El Negocio del Metalero · Clase 12 ampliada (≈7 min): base + escenas nuevas de neg_ext."""
import neg_c12 as base
from neg_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['neg_c12'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'neg_x12')
