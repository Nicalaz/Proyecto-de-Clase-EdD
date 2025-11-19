class Barrio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

class GrafoBarrios:
    def __init__(self):
        self.barrios = []
        self.conexiones = []

    def agregar_barrio(self, nombre):
        self.barrios.append(Barrio(nombre))

    def conectar_barrios(self, b1, b2, peso):
        self.conexiones.append((b1, b2, peso))
        
    def eliminar_barrio(self, indice_barrio):
        if 0 <= indice_barrio < len(self.barrios):
            self.barrios.pop(indice_barrio)
            self.conexiones = [
                conn for conn in self.conexiones 
                if conn[0] != indice_barrio and conn[1] != indice_barrio
            ]
            print(f"Barrio con índice {indice_barrio} eliminado.")
        else:
            print("Índice de barrio no válido.")

    def eliminar_conexion(self, b1_indice, b2_indice):
        conexiones_antes = len(self.conexiones)
        self.conexiones = [
            conn for conn in self.conexiones 
            if not (conn[0] == b1_indice and conn[1] == b2_indice)
        ]
        
        if len(self.conexiones) < conexiones_antes:
            print(f"Conexión de {self.barrios[b1_indice].nombre} a {self.barrios[b2_indice].nombre} eliminada.")
        else:
            print("Conexión no encontrada.")

    #Calcula la distancia más corta desde un nodo_origen_idx a todos los demás, y almacena el predecesor para reconstruir la ruta. Retorna: (distancia, predecesor)
    def bellman_ford(self, nodo_origen_idx):
        num_barrios = len(self.barrios)
        distancia = [float("inf")] * num_barrios
        predecesor = [-1] * num_barrios 

        distancia[nodo_origen_idx] = 0

        for _ in range(num_barrios - 1):
            for b1, b2, peso in self.conexiones:
                if distancia[b1] != float("inf") and distancia[b1] + peso < distancia[b2]:
                    distancia[b2] = distancia[b1] + peso
                    predecesor[b2] = b1  

        return distancia, predecesor

