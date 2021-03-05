"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Selección algorítmo de ordenamiento")
 
def printOptions():
    print('1- ARRAY_LIST')
    print('2- LINKED_LIST')

def printOptions2():
    print('1- Insertion Sort')
    print('2- Selection Sort')
    print('3- Shell Sort')
    print('4- Quick Sort')
    print('5- Merge Sort')



"""
Menu principal
"""

def initCatalog(tipo):

    return controller.initCatalog(tipo)


def loadData(catalog):

    controller.loadData(catalog)
catalog = None



while True:
    tipo= 'ARRAY_LIST'
    algorithm = 'a'
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        printOptions()
        inputs1=input('Seleccione un tipo para la representación de las listas:\n')
        if int(inputs1)==1:
            tipo='ARRAY_LIST'
        elif inputs1==2:
            tipo='LINKED_LIST'
        print("Cargando información de los archivos ....")
        
        catalog = initCatalog(tipo)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        
        


    elif int(inputs) == 2:
        printOptions2()
        inputs2=int(input('Seleccione un tipo para el algorítmo de ordenamiento\n'))

        if inputs2 == 1:
            algorithm = 'Insertion sort'
        elif inputs2 == 2:
            algorithm = 'Selection sort'
        elif inputs2 == 3:
            algorithm = 'Shell sort'
        elif inputs2 == 4:
            algorithm = 'Quick sort'
        elif inputs2 == 5:
            algorithm = 'Merge sort' 
        size = int(input('Seleccione un tamaño de la sublista\n'))
        #print(len(catalog['videos']['elements']))
        '''if size <= len(catalog['videos']['elements']):
            tiempo_carga = controller.sortVideos(catalog, size, algorithm )
            print('El tiempo de carga del algoritmo '+ str(algorithm) + ' con '+ str(size) + ' datos es igual a: '+ str(tiempo_carga))
        elif size > len(catalog['videos']['elements']):
            print('El tamaño de la sublista que escogio es mayor que el total de los datos.')'''
        videos_sublist=controller.sortVideos(catalog, size, algorithm )['elements']
        for video in videos_sublist:
            print(video['title'])
        #print()



    else:
        sys.exit(0)
sys.exit(0)