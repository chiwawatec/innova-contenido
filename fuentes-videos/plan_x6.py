"""Lectura de Planos · Clase 6 ampliada (≈7 min): base + escenas nuevas de plan_ext."""
import plan_c6 as base
from plan_ext import EXT, insertar
from sold_comun import render_clase

E = insertar(base.E, EXT['plan_c6'])
CURSO = base.CURSO

if __name__ == '__main__':
    render_clase(E, CURSO, 'plan_x6')
