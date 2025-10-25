#Segunda entrega, se decidió construir un árbol AVL debido a su mayor eficiencia O(log(n))

# Clase Nodo
class Nodo:
    
    # Constructor
    def __init__(self, nombre, distancia):
        self.distancia = distancia # Cada nodo contendrá el valor de la úbicación respecto a la actual raíz
        self.nombre = nombre
        self.derecha = None
        self.izquierda = None
        self.altura = 1
        
# Función para obtener la altura del árbol
def getAltura(nodo):
    if not nodo:
        return 0
    return nodo.altura

# Función para obtener el balance del árbol
def getBalance(nodo):
    if not nodo:
        return 0
    return getAltura(nodo.derecha) - getAltura(nodo.izquierda)

# Función para actualizar la altura del árbol
def actualizarAltura(nodo):
    if nodo:
        nodo.altura = 1 + max(getAltura(nodo.izquierda), getAltura(nodo.derecha))
        
# Función para rotación derecha
def rotacionDerecha(y):
    x = y.izquierda
    T2 = x.derecha
    
    x.derecha = y
    y.izquierda = T2
    
    actualizarAltura(y)
    actualizarAltura(x)
    
    return x

# Función para rotación izquierda
def rotacionIzquierda(x):
    y = x.derecha
    T2 = y.izquierda
    
    y.izquierda = x
    x.derecha = T2   
    
    actualizarAltura(x)
    actualizarAltura(y) 
    
    return y

# Clase Arbol AVL
class ArbolAVL:
    
    # Constructor
    def __init__(self):
        self.raiz = None
    
    # Método para insertar las distancias de las ubicaciones en el árbol
    def insercion(self, nombre, distancia):
        self.raiz = self.insercionRecursiva(self.raiz, nombre, distancia) 
    
    # Método para insertar un nuevo nodo en el árbol en la posición correcta
    def insercionRecursiva(self, nodo, nombre, distancia):
        if not nodo:
            return Nodo(nombre, distancia)
        if distancia < nodo.distancia:
            nodo.izquierda = self.insercionRecursiva(nodo.izquierda, nombre, distancia)
        elif distancia > nodo.distancia:
            nodo.derecha = self.insercionRecursiva(nodo.derecha, nombre, distancia)
        else:
            return nodo
        
        actualizarAltura(nodo)
        balance = getBalance(nodo)     
        
        if balance < -1 and getBalance(nodo.izquierda) <= 0:
            return rotacionDerecha(nodo) 
        elif balance < -1 and getBalance(nodo.izquierda) > 0:
            nodo.izquierda = rotacionIzquierda(nodo.izquierda)
            return rotacionDerecha(nodo) 
        elif balance > 1 and getBalance(nodo.derecha) >= 0:
            return rotacionIzquierda(nodo)
        elif balance > 1 and getBalance(nodo.derecha) < 0:
            nodo.derecha = rotacionDerecha(nodo.derecha)
            return rotacionIzquierda(nodo) 
        
        return nodo   
     
# Método para obtener el nodo con el valor minimo del subárbol.
    def getMinValNodo(self, nodo):
        if nodo is None or nodo.izquierda is None:
            return nodo
        else:
            return self.getMinValNodo(nodo.izquierda)
    
# Método para el recorrido inorden
    def inorden(self, raiz):
        if raiz is None:
            return
        self.inorden(raiz.izquierda)
        print(f"Comuna: {raiz.nombre}, Distancia acumulada: {raiz.distancia} km")
        self.inorden(raiz.derecha)

# Método para buscar comunas
    def buscar(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.nombre.lower() == nombre.lower():
            return nodo
        izquierda = self.buscar(nodo.izquierda, nombre)
        if izquierda:
            return izquierda
        return self.buscar(nodo.derecha, nombre)
    
    def obtenerComunaMasCercana(self, raiz):
        if raiz is None:
            return None
    
    def getMaxNodo(self, nodo):
        if nodo is None or nodo.derecha is None:
            return nodo
        return self.getMaxNodo(nodo.derecha)
        
# Importación de librerias de BigTree y matplotlib para gráficar el árbol
# Importante primero instalar las librerias, usen pip install bigtree matplotlib en una terminal
from bigtree import BinaryNode, plot_tree, reingold_tilford
import matplotlib.pyplot as plt

# Función exclusiva para árboles. Se optó por crear esta función para gráficar el árbol con la ruta más corta
def graficaBigTree(nodo):
    if nodo is None:
        return None
    arbol = BinaryNode(str(nodo.distancia))
    arbol.left = graficaBigTree(nodo.izquierda)
    arbol.right = graficaBigTree(nodo.derecha)
    return arbol

# Prueba para verificar el correcto funcionamiento de BigTree
print("----------RUTA 1----------")
ruta1 = ArbolAVL()
values_to_insert = [0, 3, 6, 9 ,12]
nombres_to_insert = ["La Concordia","Antonia Santos","San Alonso","San Francisco","UIS"]


print("Insertando valores:", values_to_insert)
for nombre, val in zip(nombres_to_insert, values_to_insert):
    ruta1.insercion(nombre, val)

print("RUTA1 inorden:")
ruta1.inorden(ruta1.raiz)

print("----------RUTA 2----------")
#####RUTA2#######
ruta2 = ArbolAVL()
values_to_insert2 = [0, 2, 4, 6, 8]
nombres_to_insert2 = ["La Concordia","Garcia Rovira","Granada","Gaitan","UIS"]

print("Insertando valores:", values_to_insert2)
for nombre, val in zip(nombres_to_insert2, values_to_insert2):
    ruta2.insercion(nombre, val)

print("RUTA2 inorden:")
ruta2.inorden(ruta2.raiz)

print("----------RUTA 3----------")
#####RUTA3#######
ruta3 = ArbolAVL()
values_to_insert3 = [0, 1, 2, 3, 4]
nombres_to_insert3 = ["La Concordia","Kennedy","San Francisco","San Alonso","UIS"]

print("Insertando valores:", values_to_insert3)
for nombre, val in zip(nombres_to_insert3, values_to_insert3):
    ruta3.insercion(nombre, val)

print("RUTA3 inorden:")
ruta3.inorden(ruta3.raiz)

print("\n")
##PRUEBA BUSQUEDA
encontrar = ruta1.buscar(ruta2.raiz, "San Francisco")
if encontrar:
    print(f"Comuna {encontrar.nombre} encontrada a {encontrar.distancia} km.")
else:
    print("No se encontró la comuna.")

dist1 = ruta1.getMaxNodo(ruta1.raiz).distancia
dist2 = ruta2.getMaxNodo(ruta2.raiz).distancia
dist3 = ruta3.getMaxNodo(ruta3.raiz).distancia
mejor = min(dist1, dist2, dist3)
if mejor == dist1:
    print("La mejor ruta es la Ruta 1")
elif mejor == dist2:
    print("La mejor ruta es la Ruta 2")
else:
    print("La mejor ruta es la Ruta 3")

