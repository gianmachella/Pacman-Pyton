# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

"""
def graficar(tablero):
    grafico = tablero.copy()
    n_fila = grafico.shape[0]
    n_col = grafico.shape[1]
    for i in range(0, n_fila):
        for j in range(0, n_col):
            if grafico[(i,j)] == "L":
                grafico[(i,j)] = chr(0x0001F981)
            if grafico[(i,j)] == "A":
                grafico[(i,j)] = chr(0x0001F98C)
            if grafico[(i,j)] == "M":
                grafico[(i,j)] = chr(0x000026F0)
            if grafico[(i,j)] == " ":
                grafico[(i,j)] = chr(0x0001F331)
    return grafico
"""
import numpy as np
import random 

#  --Depredador y Presa--

#Montañas as M
#Leones as L
#Antilopes as A

#Faces de los Leones:
# - Comer - Reproducirse - Mover

#Faces de los Antilopes
# - Mover - Reproducir

def generarTablero(ancho, alto):
    t = np . repeat (" ", alto*ancho) . reshape (alto , ancho)
    i=0
    while i < ancho:
        t[(0,i)]="M"
        i=i+1
    
    i=0
    while i < ancho:
        t[(alto-1,i)]="M"
        i=i+1
    
    i=0
    while i < alto:
        t[(i,0)]="M"
        i=i+1
    
    i=0
    while i < alto:
        t[(i,ancho-1)]="M"
        i=i+1
    return t
t=generarTablero(12, 12)


#fil = [2 , 3 , 4 , 4 , 2]
#col = [2 , 3 , 3 , 5 , 5]
#tipo = ["A", "A", "A", "L", "L"]
#
#for i in range (len(tipo)) :
#    t [(fil[i], col[i])] = tipo[i]

    
def mis_vecinos(coord_centro):
    vecinos=[]
    x=coord_centro[0]
    y=coord_centro[1]
    vecinos.append((x-1,y-1))
    vecinos.append((x-1,y))
    vecinos.append((x-1,y+1))
    vecinos.append((x,y+1))
    vecinos.append((x+1,y+1))
    vecinos.append((x+1,y))
    vecinos.append((x+1,y-1))
    vecinos.append((x,y-1))
    
    return vecinos


def buscar_adyacente(tablero, coord_centro, objetivo):
    for vecino in mis_vecinos(coord_centro):
        if tablero[vecino] == objetivo:
            return [vecino]
    return []      
            
def fase_mover(tablero):
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == "L" or tablero [(i,j)] == "A":
                for adyacente in buscar_adyacente(tablero, (i,j), " "):
                    tablero[adyacente] = tablero[(i,j)]
                    tablero[(i,j)] = " "


       
def fase_alimentacion(tablero):
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == "L":
                for adyacente in buscar_adyacente(tablero, (i,j), "A"):
                    tablero[adyacente] = tablero[(i,j)]
                    tablero[(i,j)] = " "



def fase_reproduccion(tablero):
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == "L" or tablero [(i,j)] == "A":
                for adyacente in buscar_adyacente(tablero, (i,j), tablero [(i,j)]):
                    if tablero[adyacente] == tablero[(i,j)]:
                        for vacio in buscar_adyacente(tablero, (i,j), " "):
                            tablero[vacio] = tablero[(i,j)]

         
def evolucionar(tablero):

    fase_alimentacion(tablero)
    fase_reproduccion(tablero)
    fase_mover(tablero)
    return tablero

def contar_antilopes(tablero):
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    contador=0
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == "A":
               contador=contador +1
    return contador

def cuantos_antilopes(tablero):
    vivos=[]
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero [(i,j)] == "A":
                vivos.append("A")
    print ("Quedaron vivos", len(vivos), "Antilopes")


def evolucionar_en_el_tiempo(tablero, tiempo_limite):
    i=0
    while i < tiempo_limite:
        evolucionar(tablero)
        res=contar_antilopes(tablero)
        viven= "Aun vive al menos un antilope"
        extincion="Se extingieron todos los antilopes en el ciclo", i
        if res == 0:
            print (extincion)
            return extincion
        i=i+1
    viven=cuantos_antilopes(tablero)
    return viven
#evolucionar_en_el_tiempo(t,10)

def mezclar_celdas ( tablero ) :
    celdas = []
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            celdas . append (( i , j ) )
            
    random . shuffle ( celdas )
    return celdas
#print(mezclar_celdas(t))

def generar_tablero_azar(filas, columnas, n_antilopes, n_leones):
    tablero=generarTablero(columnas, filas)
    celdas=mezclar_celdas(tablero)
    i=0
    while i < n_antilopes:
        tablero[celdas.pop(0)]="A"
        i=i+1
    j=0
    while j < n_leones:
        tablero[celdas.pop(0)]="L"
        j=j+1
    return tablero
tablero=generar_tablero_azar(12, 12, 10, 5)

def cuantos_de_cada(tablero):
    leones=0
    antilopes=0
    animalesVivos=[]
    n_fila = tablero . shape [0]
    n_col = tablero . shape [1]
    for i in range (1 , n_fila - 1) :
        for j in range (1 , n_col - 1) :
            if tablero[i,j] == "A":
                antilopes=antilopes+1
            if tablero[i,j] == "L":
                leones=leones+1
    animalesVivos.append(antilopes)
    animalesVivos.append(leones)
    return animalesVivos
cuantos=cuantos_de_cada(tablero)

def registrar_evolucion(tablero, tiempo_limite):
    i=0
    animalesVivos=[]
    while i < tiempo_limite:
        evolucionar(tablero)
        print (tablero)
        animalesVivos.append(cuantos_de_cada(tablero))
        i=i+1
    return animalesVivos

animalesVivos=registrar_evolucion(tablero, 5)
