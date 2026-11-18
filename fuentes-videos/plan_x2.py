"""Lectura de Planos · Clase 2 ampliada (≈7 min): base + escenas nuevas de plan_ext."""
import plan_c2 as base
from plan_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['plan_c2'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'plan_x2')
