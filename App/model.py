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
def newCatalog():
   
    catalog = {'videos': lt.newList('ARRAY_LIST'), 'category': lt.newList('ARRAY_LIST')
               }
    

    
    

    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    
    lt.addLast(catalog['category'], category)
    

    

# Funciones para creacion de datos
def nombre_id_categoria(catalog,nombre_categoria):
    i=0
    while i <= (lt.size(catalog['category'])-1):
        if nombre_categoria in ((catalog['category']['elements'][i]['name']).lower()):
            id_categoria= catalog['category']['elements'][i]['id']
        i+=1
    return id_categoria
    



# Funciones de consulta



# Funciones utilizadas para comparar elementos dentro de una lista

def videos_pais_categoria(catalog,pais,nombre_categoria,n):
 
    
    id_categoria = nombre_id_categoria(catalog,nombre_categoria)
    

  
    sub_list=lt.newList('ARRAY_LIST')
    j=1
    while j <  (lt.size(catalog['videos'])):
        if (pais in ((catalog['videos']['elements'][j]['country']).lower())) and (id_categoria in (catalog['videos']['elements'][j]['category_id'])):
            lt.addLast(sub_list, catalog['videos']['elements'][j])
        j+=1

    sub_list = sub_list.copy()
    mrg.sort(sub_list,cmpVideosbyViews)
    subsub_list = lt.subList(sub_list, 1, n)
    subsub_list = subsub_list.copy()
    return subsub_list


# Funciones de ordenamiento
def cmpVideosbyViews(video1,video2):
    return(int(video1["views"])>int(video2["views"]))