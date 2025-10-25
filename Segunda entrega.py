#Segunda entrega, se decidió construir un árbol AVL debido a su mayor eficiencia O(log(n))

# Clase Nodo
class Nodo:
    
    # Constructor
    def __init__(self, distancia):
        self.distancia = distancia # Cada nodo contendrá el valor de la úbicación respecto a la actual raíz
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
    def insercion(self, distancia):
        self.raiz = self.insercionRecursiva(self.raiz, distancia) 
    
    # Método para insertar un nuevo nodo en el árbol en la posición correcta
    def insercionRecursiva(self, nodo, distancia):
        if not nodo:
            return Nodo(distancia)
        if distancia < nodo.distancia:
            nodo.izquierda = self.insercionRecursiva(nodo.izquierda, distancia)
        elif distancia > nodo.distancia:
            nodo.derecha = self.insercionRecursiva(nodo.derecha, distancia)
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
        print(raiz.distancia)
        self.inorden(raiz.derecha)
        
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
avl = ArbolAVL()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insercion(val)

print("\n--- Después de inserciones ---")
raiz = graficaBigTree(avl.raiz)
reingold_tilford(raiz)
plot_tree(raiz, "-ok")
plt.title("Árbol AVL después de las inserciones")
plt.show()