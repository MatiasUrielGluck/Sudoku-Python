import random
from sudoku import *
from mapas import MAPAS as mapas

# Constantes de decoración
GUIA_HORIZONTAL = "123456789"
GUIA_VERTICAL = "abcdefghijklmnopqrstuvwxyz"
DECORACIONES = ["╬", "║", "═"] # Índices: [Separador], [Borde vertical], [Borde horizontal]
CARACTER_VACIO = "·"
MENSAJE_ERROR = "No entendí! Por favor ingresá una orden válida, por ejemplo: a 1 1"


def mostrar_juego(juego):
    '''
    Imprime el sudoku "juego".
    '''
    
    fila_separadora = f"{DECORACIONES[0]}{DECORACIONES[2] * 7}" * (ANCHO_TABLERO // ANCHO_CUADRANTE) + f"{DECORACIONES[0]}"

    print("")
    # Guía de horizontal superior
    for n, numero in enumerate(GUIA_HORIZONTAL):
        if n == 0: print("   ", end = "")
        if n % ANCHO_CUADRANTE == 0 and n != 0: print(f"   {numero}", end = "")
        else: print(f" {numero}", end = "")
    print()

    for x, fila in enumerate(juego):
        if x % ALTO_CUADRANTE == 0: print(f"  {fila_separadora}")
        print(GUIA_VERTICAL[x], end = " ") # Guía vertical izquierda

        for y, valor in enumerate(fila):

            if y % ANCHO_CUADRANTE == 0: print(f"{DECORACIONES[1]} ", end = "")

            if valor == 0: print(f"{CARACTER_VACIO} ", end = "")
            
            else:print(f"{valor} ", end = "")
        
        print(f"{DECORACIONES[1]} {GUIA_VERTICAL[x]}") # Guía vertical derecha

    print(f"  {fila_separadora}")

    # Guía de horizontal inferior
    for n, numero in enumerate(GUIA_HORIZONTAL):
        if n == 0: print("   ", end = "")
        if n % ANCHO_CUADRANTE == 0 and n != 0: print(f"   {numero}", end = "")
        else: print(f" {numero}", end = "")
    print("\n")


def letra_a_numero(letra):
    '''
    Convierte una letra en su número correspondiente (índice)
    '''
    for l, valor in enumerate(GUIA_VERTICAL):
        if letra == valor and l < 9:
            return l
        

def main():
    juego = crear_juego(random.choice(mapas))

    celdas_asignadas = [] # Celdas que no se pueden modificar
    for fila in range(len(juego)):
        for columna in range(len(juego[fila])):
            if juego[fila][columna] != VACIO: celdas_asignadas.append([fila, columna])

    print()
    print(" " * (ANCHO_CUADRANTE * ANCHO_TABLERO // 2 - ANCHO_CUADRANTE), "Sudoku")
    print(" " * (ANCHO_CUADRANTE * ANCHO_TABLERO // 2 - ANCHO_CUADRANTE), "¯¯¯¯¯¯")

    while True:
        mostrar_juego(juego)
        entrada = input("Ingrese una orden [f c v | salir]: ")

        # Transformar la entrada en una cadena homogénea
        entrada = "".join(entrada.split()).lower()
        entrada = ",".join(entrada.split())

        if entrada == "salir":
            return

        if len(entrada) == 3 and entrada[1:2].isdigit: # Comprobar que la entrada contenga tres valores, de ser así que sea válida
            if entrada[0] in GUIA_VERTICAL and entrada[1] in GUIA_HORIZONTAL and int(entrada[2]) in range(10):

               celda_candidato = [letra_a_numero(entrada[0]), int(entrada[1]) - 1]
               if celda_candidato in celdas_asignadas: 
                   print("¡No se puede modificar esta celda!")
                   continue

               nuevo_juego = insertar_valor(juego, celda_candidato[0], celda_candidato[1], int(entrada[2]))
               if nuevo_juego == juego: print("¡El movimiento no es válido!")
               else: juego = nuevo_juego
            
            else: print(MENSAJE_ERROR + f"|{entrada}|")

        else: print(MENSAJE_ERROR)

        if esta_terminado(juego): 
            mostrar_juego(juego)
            print("Sudoku terminado!")
            return


main()