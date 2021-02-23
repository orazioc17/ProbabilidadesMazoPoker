import random
import collections


#Declarando constantes, en python se hace con mayus
PALOS = ['espada', 'corazon', 'trebol', 'rombo']
VALORES = ['as', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']


#Funcion que crea el mazo
def crear_mazo():
    mazo = []
    for palo in PALOS:
        for valor in VALORES:
            mazo.append((palo, valor))
    
    return mazo


#Funcion que retorna la mano
def obtener_mano(mazo, tamano_mano):
    #Sample es para obtener un valor de un arreglo y que despues aleatoriamente no pueda repetir ese mismo valor
    mano = random.sample(mazo, tamano_mano)

    return mano


#funcion que realiza toda la simulacion
def simulacion(tamano_mano, intentos):
    mazo = crear_mazo()
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(mazo, tamano_mano)
        manos.append(mano)
    
    pares = 0
    trio = 0
    poker = 0
    for mano in manos:
        #Se crea lista para almacenar unicamente los valores de cada mano
        valores = []
        for carta in mano: 
            #Se va llenando la lista por cada mano con sus valores
            valores.append(carta[1])
        #con este counter, se cuentan cuantas veces se repite un valor en una lista y genera un diccionario, en el cual el Key sera la carta y el valor de cada Key sera CUANTO se repite esa carta, por lo cual, el minimo sera 1
        counter = dict(collections.Counter(valores))
        pares_aux = 0
        trio_aux = 0
        poker_aux = 0
        for val in counter.values():
            if val == 2:
                pares_aux += 1
            elif val == 3:
                trio_aux += 1
            elif val == 4:
                poker_aux += 1
        # De esta forma solo verifico con que haya al menos UNO de estos, sin que me afecte si hay 2 o mas, pues lo que se quiere calcular es la probabilidad de obtener al menos UNO de estos por cada mano
        if pares_aux > 0: 
            pares += 1
        if trio_aux > 0: 
            trio += 1
        if poker_aux > 0: 
            poker += 1
    #Se calculan las probabilidades
    probabilidad_par = pares / intentos
    probabilidad_trio = trio / intentos
    probabilidad_poker = poker / intentos

    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es de: {probabilidad_par}')
    print(f'La probabilidad de obtener un trio en una mano de {tamano_mano} cartas es de: {probabilidad_trio}')
    print(f'La probabilidad de obtener un poker en una mano de {tamano_mano} cartas es de: {probabilidad_poker}')


def main():
    aux = 0
    while (aux == 0):
        tamano_mano = int(input('Ingrese el tamano de la mano (menor a 10): '))
        if (tamano_mano > 0) and (tamano_mano <11):
            aux += 1
    
    intentos = int(input('Ingrese el numero de intentos que desea que realice la simulacion: '))
    simulacion(tamano_mano, intentos)


if __name__ == '__main__':
    main()
