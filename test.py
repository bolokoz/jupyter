#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importar bibliotecas
import eztrut
import numpy as np
import matplotlib.pyplot as plt

# Criar uma viga de tamanho 4. Momento, inercia e area serao padrao.
viga1 = eztrut.Viga(l=4)

# Criar dois apoios. Um apoio fixo na ponta esquerda (x = 0) e outro livre no fim (x = 4)
apoioA = eztrut.Apoio(x=0, tipo=2)
apoioB = eztrut.Apoio(x=4, tipo=1)

# Criar uma forca CONCENTRADA vertical (de cima para baixo) de 10kN no meio da viga (x = 2)
forca1 = eztrut.ForcaC(f=-10000, x=2, tipo=2)

# Criar a estrutura para resolver os diagramas
apoios = [apoioA, apoioB]
forcas = [forca1]

estrut1 = eztrut.Eztrut(viga1, apoios, forcas)

# Mostrar uma figura  da viga com os apoios e forcas
estrut1.plotagem_apoios()
estrut1.mostrar_figura()

estrut1.estaticidade()
