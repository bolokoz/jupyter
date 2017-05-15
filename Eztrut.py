#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pyplot

# Definir class Viga
class Viga:
    """Cria um objeto da classe Viga
    Args:
        l (float): tamanho da viga em metros
        e (float): Módulo de elasticidade em MPa
        i (float): Momento de inércia em metros à quarta
        a (float): Área em m2
    """
    def __init__(self, l = 1, e = 20000, i = 1, a = 1):
        self.e = e
        self.i = i
        self.l = l
        self.a = a

        #Matriz de rigidez
        self.k = e * i / l**3 * np.array([
                [12., 6*l, -12, 6*l],
                [6*l, 4*l**2, -6*l, 2*l**2],
                [-12, -6*l, 12, -6*l],
                [6*l, 2*l**2, -6*l, 4*l**2]
            ])

    def __str__(self):
        return ('Comprimento = ' + str(self.l) + " m, \n"
    + 'Inercia = ' + str(self.i) + ' m^4, \n'
    + 'Elasticidade = ' + str(self.e) + ' MPa \n')

#Definicao da classe Nó
#Tipo 1 = fixo em x (apoiado)
#Tipo 2 = fixo em x e y (fixo)
#Tipo 3 = fixo em x, y e z (engastado)
class Apoio:
    """Cria um objeto da classe Apoio
    Args:
        x (float): localizacao do apoio em relacao a ponta esquerda da viga
        tipo (int): tipo do apoio
            1 = fixo em x (apoiado)
            2 = fixo em x e y (fixo)
            3 = fixo em x, y e z (engastado)
    """
    def __init__(self, x, tipo = 1):
        self.x = x
        self.tipo = tipo

class ForcaC:
    """Cria um objeto da classe Forca concentrada
    Args:
        f (float): magnitude da forca em N
        x (float): localizacao da forca em relacao a ponta esquerda da viga
        tipo (int): tipo da forca
            1 = forca em x (vertical)
            2 = forca em y (horizontal)
            3 = forca em z (momento)
    """

    def __init__(self, f, x, tipo):
        self.f = f
        self.x = x
        self.tipo = tipo

class ForcaD:
    """Cria um objeto da classe Forca distribuida
    Args:
        f_i (float): magnitude da forca mais a ESQUERDA em [N]
        f_f (float): magnitude da forca mais a DIREITA em [N]
        x_i (float): localizacao da forca mais a ESQUERDA em relacao a ponta esquerda da viga
        x_f (float): localizacao da forca mais a DIREITA em relacao a ponta esquerda da viga
        tipo (int): tipo da forca
            1 = forca em x (vertical)
            2 = forca em y (horizontal)
            3 = forca em z (momento)
    """
    def __init__(self, f_i, f_f, x_i, x_f, tipo):
        self.f_i = f_i
        self.f_f = f_f
        self.x_i = x_i
        self.x_f = x_f
        sef.tipo = tipo

class Eztrut:
    """Cria um objeto da classe Eztrut
    Args:
        vigas (Viga): um objeto da classe Viga
        apoios (Apoio[]): vetor de objetos da classe Apoio
        cargas (Forca[]): vetor de objetos da classe Forca
    """
    def __init__(self, vigas, apoios, cargas):
        self.vigas = vigas
        self.apoios = apoios
        self.cargas = cargas

    def mostrar_vigas():
        for viga in self_vigas:
            print(str(viga))


    def estaticidade():
        estaticidade = 0
        for apoio in apoios:
            estacidade+= apoio.tipo
