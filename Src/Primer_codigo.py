from email import parser
import numpy as np
import argparse


print("Hola Mundo !!!")

#Esto es una variable de tipo string(str)
Frase= ("hola Jenny")
print(Frase)

frase2 = "jenny y "
palabra = "Esteban"

#Concatenar de Strings
palabra_unida= frase2 + palabra
print(palabra_unida)

# NUmeros son variables enteros (INT)
# operar Strings con numero enteros multiplicar
x = 5
x * palabra

type (x)

type (frase2)

type (palabra_unida)

type (4.85)

# tipod de Variables: str, int, float, bool
dato ="Esteban"
dato_sucio = "Esteban "

print ("limpio", dato *3)

print ("sucio", dato_sucio*3)

# Numeros

x = 3
y = 5
x*y
#----------------------------------------------------------------------------------------------#

def calcular_min_max(lista_numeros, verbose=1):

    '''

    Retorna los valores minimo y maximo de una de lista de numeros

    Args:

        lista_numeros: type list

    '''

    min_value = min(lista_numeros)

    max_value = max(lista_numeros)

    

    if verbose == True:

        print('Valor minimo:', min_value)

        print('Valor maximo:', max_value)

    else:

        pass

    return min_value, max_value

def calcular_valores_centrales(lista_numeros, verbose=1):
    
    """Calcula la media y la deviacion estandar de una lisra de numeros

    Args:

        lista_numeros(list): Lista con valores numericos 
        Verebose (bool, optional): para decidir si imprimir mensajes 
    
    Returns:
        tuple: (media, dev_std)
    """


    media   = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)
    

    if verbose == 1:

        print('Media:', media)

        print('Desviacion Estandar:', dev_std)

    else:

        pass

        return media, dev_std

def calcular_valores(lista_numeros, verbose=1):

    

    suma             = np.sum(lista_numeros)  #calcular_suma(lista_numeros)
   
    min_val, max_val = calcular_min_max(lista_numeros, verbose)
   
    media, dev_std   = calcular_valores_centrales(lista_numeros)

   
    return suma, min_val, max_val, media, dev_std

def main():

        parser = argparse.ArgumentParser()
        parser.add_argument( 
            "--verbose",
            type=bool,
            default=1, 
            help="para imprimir en pantalla informacion"
            )

        args = parser.parse_args()


        lista_valores = [5, 4, 8, 9, 21]
        calcular_valores(lista_numeros = lista_valores, verbose=args.verbose)
        
if __name__ == '__main__':
    main()