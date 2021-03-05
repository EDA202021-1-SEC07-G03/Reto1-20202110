"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import time
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import mergesort as mrg

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(tipo):
   
    catalog = {'videos': lt.newList(tipo)
               }

    
    

    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    
    lt.addLast(catalog['videos'], video)
    

    

# Funciones para creacion de datos

# Funciones de consulta
def sortVideos_time(catalog, size, algorithm):
    sub_list = lt.subList(catalog['videos'], 0, size)

    
    if algorithm == 'Insertion sort':
        start_time = time.process_time()
        ins.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()

    elif algorithm == 'Selection sort':
        start_time = time.process_time()
        ses.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()

    elif algorithm == 'Shell sort':
        start_time = time.process_time()
        shs.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()
    
    elif algorithm == 'Merge sort':
        start_time = time.process_time()
        mrg.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()

    elif algorithm == 'Quick sort':
        start_time = time.process_time()
        qck.sort(sub_list, cmpVideosbyViews)
        stop_time = time.process_time()
    
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg

def sortVideos(catalog, size, algorithm):
    sub_list = lt.subList(catalog['videos'], 0, size)
    if algorithm == 'Insertion sort':
        sorted=ins.sort(sub_list, cmpVideosbyViews)

    elif algorithm == 'Selection sort':
        sorted=ses.sort(sub_list, cmpVideosbyViews)

    elif algorithm == 'Shell sort':
        sorted=shs.sort(sub_list, cmpVideosbyViews)
    
    elif algorithm == 'Merge sort':
        sorted=mrg.sort(sub_list, cmpVideosbyViews)

    elif algorithm == 'Quick sort':
        sorted=qck.sort(sub_list, cmpVideosbyViews)
    return sorted
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def cmpVideosbyViews(video1,video2):
    return(video1["views"]<video2["views"])