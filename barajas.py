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
    for mano in manos:
        valores = []
        for carta in mano: 
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares +=1
    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es de: {probabilidad_par}')


def main():
    tamano_mano = int(input('Ingrese el tamano de la mano: '))
    intentos = int(input('Ingrese el numero de intentos que desea que realice la simulacion: '))
    simulacion(tamano_mano, intentos)


if __name__ == '__main__':
    main()
