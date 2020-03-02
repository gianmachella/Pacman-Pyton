#Ejercicio1

def decir_si_es_mayor_a_5(elemento):
    if elemento > 5:
        return 'Este numero es Mayor a 5'
    else:
        return 'Este numero es Menor a 5'
    
decir_si_es_mayor_a_5(4)

#Ejercicio2

def decir_si_la_longitud_es_mayor_a_5(elemento):
    longitud=len(elemento)
    if longitud > 5:
        return 'La longitud de este string es Mayor a 5'
    else:
        return 'La longitud de este string es Menor a 5'
    
decir_si_la_longitud_es_mayor_a_5('Casa Blanca')