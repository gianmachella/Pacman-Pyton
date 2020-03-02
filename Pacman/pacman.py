#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:48:18 2019

@author: gianmachella
"""
"""
=======   VALORES   =======

0 = Espacio vacio
6 = Pacman
1 = Pared
2 = Puntitos
7 = Fantasma1
8 = Fantasma2
9 = Fantasma3

"""
import numpy as np
import random


def crearTablero(fila, columna):
    tablero = np . repeat (0, columna*fila) . reshape (columna , fila)
    i=0
    while i < columna:
        tablero[(0,i)]=1
        i=i+1   
    i=0
    while i < columna:
        tablero[(fila-1,i)]=1
        i=i+1   
    i=0
    while i < fila:
        tablero[(i,0)]=1
        i=i+1   
    i=0
    while i <fila:
        tablero[(i,columna-1)]=1
        i=i+1
    return tablero

tablero=crearTablero(22, 22)

def crearTableroGO(fila, columna):
    tablero = np . repeat (0, columna*fila) . reshape (columna , fila)
    i=0
    while i < columna:
        tablero[(0,i)]=1
        i=i+1   
    i=0
    while i < columna:
        tablero[(fila-1,i)]=1
        i=i+1   
    i=0
    while i < fila:
        tablero[(i,0)]=1
        i=i+1   
    i=0
    while i <fila:
        tablero[(i,columna-1)]=1
        i=i+1
    return tablero

def posicionesIniciales(tablero):
    casa=[(9,8), (9,9), (9,10), (9,11),
          (10,8), (10,9), (10,10), (10,11)]
    random.shuffle(casa)
    tablero[casa.pop(0)]=7
    tablero[casa.pop(0)]=8
    tablero[casa.pop(0)]=9
    tablero[(18,9)]=6

def rellenarTablero(tablero):
    coordParedes=[(2,1), (2,2), (2,3), (2,5), (2,6), (2,7), (2,8), (2,9), (2,10), (2,11), (2,12), (2,13), (2,14), (2,16), (2,17), (2,18), (2,19), 
                  (3,3), (3,6), (3,8), (3,9), (3,10), (3,11), (3,13), (3,16), 
                  (4,1), (4,19), 
                  (5,1), (5,2), (5,3), (5,5), (5,6), (5,7), (5,8), (5,9), (5,10), (5,11), (5,12), (5,13), (5,14), (5,16), (5,17), (5,18), (5,19), 
                  (6,1), (6,19),
                  (7,1), (7,3), (7,4), (7,5), (7,7),(7,8), (7,9), (7,10), (7,11), (7,12), (7,14), (7,15), (7,16), (7,18), (7,19),
                  (8,4), (8,15),
                  (9,1), (9,2), (9,4), (9,15), (9,17), (9,18),
                  (10,2), (10,4), (10,7), (10,12), (10,15), (10,17), 
                  (11,4), (11,7), (11,12), (11,15), (11,19), (11,20),
                  (12,2), (12,3), (12,4), (12,5), (12,7), (12,8), (12,9), (12,10), (12,11), (12,12), (12,14), (12,15), (12,16), (12,17), 
                  (14,1), (14,2), (14,3), (14,5), (14,6), (14,7), (14,8), (14,9), (14,10), (14,11), (14,12), (14,13), (14,14), (14,16), (14,17), (14,18), (14,19),
                  (15,1), (15,19),
                  (16,3), (16,6), (16,8), (16,9), (16,10), (16,11), (16,13), (16,16), 
                  (17,1), (17,2), (17,3), (17,5), (17,6), (17,7), (17,8), (17,9), (17,10), (17,11), (17,12), (17,13), (17,14), (17,16), (17,17), (17,18), (17,19),
                  (19,2), (19,3), (19,4), (19,5), (19,6), (19,7), (19,8), (19,9), (19,10), (19,11), (19,12), (19,13), (19,14), (19,15), (19,16), (19,17), (19,18), (19,19)]
    i=0
    while i < len(coordParedes):
        tablero[coordParedes[i]]=1
        i=i+1
    
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == 0:
                    tablero[(i,j)] = 2
    posicionesIniciales(tablero)
rellenarTablero(tablero)


def rellenarTableroGO(tableroGO):
    coordParedes=[(2,2), (2,3), (2,4), (2,5), (2,8), (2,11), (2,11), (2,15), (2,17), (2,18), (2,19),
                  (3,2), (3,7), (3,9), (3,11), (3,12), (3,14), (3,15), (3,17), 
                  (4,2), (4,4), (4,5), (4,7), (4,9), (4,11), (4,13), (4,15), (4,17), (4,18),
                  (5,2), (5,5), (5,7), (5,8), (5,9), (5,7), (5,11), (5,15), (5,17),
                  (6,2), (6,3), (6,4), (6,5), (6,7), (6,9), (6,11), (6,15), (6,17), (6,18), (6,19),
                  (8,3), (8,4), (8,7), (8,11), (8,13), (8,14), (8,15), (8,17), (8,18), (8,19),
                  (9,2), (9,5), (9,5), (9,7), (9,11), (9,13), (9,17), (9,19),
                  (10,2), (10,5), (10,7), (10,11), (10,13), (10,14), (10,17), (10,18), (10,19),
                  (11,2), (11,5), (11,8), (11,10), (11,13), (11,17),  (11,18),
                  (12,3), (12,4), (12,9), (12,13), (12,14), (12,15), (12,17), (12,19)]
    i=0
    while i < len(coordParedes):
        tableroGO[coordParedes[i]]=1
        i=i+1
    
    n_fila = tableroGO . shape [0]
    n_col = tableroGO . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tableroGO [(i,j)] == 0:
                    tableroGO[(i,j)] = 0

def casaDeFantasmas(tablero):
    casa=[(9,8), (9,9), (9,10), (9,11),
          (10,8), (10,9), (10,10), (10,11),
          (11,8), (11,9), (11,10), (11,11)]
    i=0
    while i < len(casa):
        tablero[casa[i]]=5
        i=i+1

def mis_vecinos(coord_centro):
    vecinos=[]
    x=coord_centro[0]
    y=coord_centro[1]
    vecinos.append((x-1,y))
    vecinos.append((x,y+1))
    vecinos.append((x+1,y))
    vecinos.append((x,y-1))
    random.shuffle(vecinos)
    
    return vecinos

def buscar_adyacente(tablero, coord_centro, objetivo):
    for vecino in mis_vecinos(coord_centro):
        if tablero[vecino] == objetivo:
            return [vecino]
    return []    

def graficar(tablero):         
    k=0
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            if i!=k:
                print()
                k+=1
            if tablero[(i,j)]==0:
                print(chr(0x000025FE),end="")
            if tablero[(i,j)]==1:
                print(chr(0x00002B1B),end="")
            if tablero[(i,j)]==2:
                print(chr(0x00001F538),end="")
            if tablero[(i,j)]==6:
                print(chr(0x0001F617),end="")
            if tablero[(i,j)]==7 or tablero[(i,j)]==8 or tablero[(i,j)]==9:
                print(chr(0x0001F47B),end="")
    print()
    print()

#def graficar(tablero):         
    # k=0
    # for i in range(tablero.shape[0]):
    #     for j in range(tablero.shape[1]):
    #         if i!=k:
    #             print()
    #             k+=1
    #         if tablero[(i,j)]==0:
    #             print(chr(0x00002B1C),end="")
    #         if tablero[(i,j)]==1:
    #             print(chr(0x00002B1B),end="")
    #         if tablero[(i,j)]==2:
    #             print(chr(0x000026AB),end="")
    #         if tablero[(i,j)]==6:
    #             print(chr(0x0001F617),end="")
    #         if tablero[(i,j)]==7 or tablero[(i,j)]==8 or tablero[(i,j)]==9:
    #             print(chr(0x0001F47B),end="")
    # print()
    # print()


def buscarFantasma(tablero, fantasma):
    coordenadas=[]
    graficar(tablero)
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == fantasma:
                coordenadas=(i,j)
    return coordenadas

def gameOver():
    tableroGO=crearTablero(22, 22)
    rellenarTableroGO(tableroGO)
    graficar(tableroGO)
    exit()

def reproducir():
    os.system("start nombre de tu archivo")

def buscarPacman(tablero):
    coordenadas=[]
    
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == 6:
                coordenadas=(i,j)
    return coordenadas

def mover_fantasma(tablero):
    
    fantasma7=buscarFantasma(tablero,7)
    fantasma8=buscarFantasma(tablero,8)
    fantasma9=buscarFantasma(tablero,9)
    
    buscar=buscar_adyacente(tablero,fantasma7, 6)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma7]
        tablero[fantasma7]=0
        gameOver()
    
    buscar=buscar_adyacente(tablero,fantasma8, 6)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma8]
        tablero[fantasma8]=0
        gameOver()
    
    buscar=buscar_adyacente(tablero,fantasma9, 6)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma9]
        tablero[fantasma9]=0
        gameOver()
    
    buscar=buscar_adyacente(tablero,fantasma7, 0)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma7]
        tablero[fantasma7]=0
    if tablero[fantasma7] != tableroMonedas[fantasma7]:
        tablero[fantasma7]=tableroMonedas[fantasma7]

    buscar=buscar_adyacente(tablero,fantasma8, 0)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma8]
        tablero[fantasma8]=0

    buscar=buscar_adyacente(tablero,fantasma9, 0)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma9]
        tablero[fantasma9]=0
    
    buscar=buscar_adyacente(tablero,fantasma7, 2)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma7]
        tablero[fantasma7]=0

    buscar=buscar_adyacente(tablero,fantasma8, 2)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma8]
        tablero[fantasma8]=0

    buscar=buscar_adyacente(tablero,fantasma9, 2)
    if len(buscar)>0:
        tablero[buscar[0]]=tablero[fantasma9]
        tablero[fantasma9]=0


    return tablero

# def mover_pacman(tablero):
#     pacman=buscarPacman(tablero)
#     buscar=buscar_adyacente(tablero,pacman)
#     if len(buscar)>0:
#         tablero[buscar[0]]=tablero[pacman]
#         tablero[pacman]=0

#     return tablero

# mover_pacman(tablero)

def moverPacmanManualmente(tablero, tecla):
    posicionActual=buscarPacman(tablero)
    x=posicionActual[0]
    y=posicionActual[1]
    
    if tecla == "w" and tablero[(x-1,y)] in [0,2]:
        tablero[(x-1,y)]=6
        tablero[(x,y)]=0
    if tecla == "d" and tablero[(x,y+1)] in [0,2]:
        tablero[(x,y+1)]=6
        tablero[(x,y)]=0
    if tecla == "s" and tablero[(x+1,y)] in [0,2]:
        tablero[(x+1,y)]=6
        tablero[(x,y)]=0
    if tecla == "a" and tablero[(x,y-1)] in [0,2]:
        tablero[(x,y-1)]=6
        tablero[(x,y)]=0
    

# def evolucionar_en_el_tiempo(tablero, tiempo_limite):
#     i=0
#     while i < tiempo_limite:
#         mover_fantasma(tablero)
#         moverPacmanManualmente(tablero, "d")
#         time.sleep(0.3)
#         graficar(tablero)
#         i=i+1
#     i=0
#     while i < tiempo_limite:
#         mover_fantasma(tablero)
#         moverPacmanManualmente(tablero, "w")
#         time.sleep(0.3)
#         graficar(tablero)
#         i=i+1
#     return tablero

# evolucionar_en_el_tiempo(tablero, 6)

import sys
import select
import termios
import contextlib
from IPython.display import clear_output
import os

@contextlib.contextmanager
def decanonize(fd):
    old_settings = termios.tcgetattr(fd)
    new_settings = old_settings[:]
    new_settings[3] &= ~termios.ICANON
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_settings)
    yield
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_settings)

with decanonize(sys.stdin.fileno()):
    try:
        while True:
            i,o,e = select.select([sys.stdin],[],[],1)
            if i and i[0] == sys.stdin:
                tecla = sys.stdin.read(1)
                
                
                ###########
                # la variable tecla dice que tecla presionaron
                # completar con la logica de mover el pacman y los fantasmas
                moverPacmanManualmente(tablero, tecla)
                mover_fantasma(tablero)
                ###########
                
                clear_output()
                os.system("clear")
                
                ###########
                # Aca se imprime el tablero
                graficar(tablero)
                ###########
                
    except KeyboardInterrupt:
        pass
  