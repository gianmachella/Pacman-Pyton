#Ejercicio 1

def devolver_longitud_de_un_nombre(unNombre):
    return len(unNombre)
    
devolver_longitud_de_un_nombre('Gian')

#Ejercicio 2

def devolver_primer_elemento_de_la_lista(unaLista):
    return unaLista[0]
    
devolver_primer_elemento_de_la_lista(['Gian', 'Franco', 'Machella'])

#Ejercicio 3

def devolver_segundo_elemento_del_nombre(unNombre):
    return unNombre[1]
    
devolver_segundo_elemento_del_nombre('Franco')

#Ejercicio 4 

def devolver_ultimo_elemento_del_nombre(unNombre):
    res=len(unNombre)-1
    return unNombre[res]
    
devolver_ultimo_elemento_del_nombre('Francisco')

#Ejercicio 5

def devolver_la_letra_en_posicion_del_nombre(unNombre, posicion):
    return unNombre[posicion]

devolver_la_letra_en_posicion_del_nombre('Eleana', 2)

#Ejercicio 6 

def reemplazar_ultimo_elemento_de_la_lista(unaLista, unElemento):
    res=len(unaLista)-1
    unaLista[res]=unElemento
    return unaLista

reemplazar_ultimo_elemento_de_la_lista(['Living', 'Dormitorio', 'Baño', 'Cochera'], 'Garage')

#Ejercicio 7

def agregar_25_al_final_de_la_lista(unaLista, unElemento):
    unaLista.append(unElemento)
    return unaLista

agregar_25_al_final_de_la_lista([ "Casa", 5, "A"], 25)

#Ejercicio 8

def agregar_nombre_al_final_de_la_lista(unaLista, unElemento):
    unaLista.append(unElemento)
    return unaLista

agregar_25_al_final_de_la_lista([ "Casa", 5, "A"], 'La Quinta Bella')

#Ejercicio 9

def multiplicar_primer_elemento(unaLista):
    elem=unaLista[0]*2
    return elem

multiplicar_primer_elemento([7, 10, 30, 34])

#Ejercicio 10

def multiplicar_ultimo_elemento(unaLista):
    res=len(unaLista)-1
    ultimoElem=unaLista[res]*3
    return ultimoElem

multiplicar_ultimo_elemento([7, 10, 30, 34])

#Ejercicio 11

def multiplicar_primer_y_ultimo_elemento(unaLista):
    primerElem=unaLista[0]*2
    res=len(unaLista)-1
    ultimoElem=unaLista[res]*3
    return (primerElem, ultimoElem)

multiplicar_primer_y_ultimo_elemento([7, 10, 30, 34])

#Ejercicio 12

def agregar_elemento_a_la_lista(unaLista, elemento):
    unaLista.append(elemento)
    return unaLista

agregar_elemento_a_la_lista([7, 10, 30, 34], 55)