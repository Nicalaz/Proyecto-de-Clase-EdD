#Segunda entrega
class Nodo:
    def __init__(self, nombre, distancia_acumulada):
        self.nombre = nombre
        self.distancia_acumulada = distancia_acumulada
        self.siguiente = None

#Clase Arbol

class Arbol:
    def __init__(self):
        return

#Recorrido inorden

def inorden(self, root):
    if root is None:
        return
    self.inorden(root.left)
    print(root.value)
    self.inorden(root.right)