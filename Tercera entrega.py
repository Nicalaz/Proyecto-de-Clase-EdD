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

# LISTA DE BARRIOS 
ListaBarrios = [
    "UIS", "Barrio Universidad", "Gaitan", "San Francisco", 
    "San Alonso", "Granada", "Kennedy", "Antonia Santos", "García R.", 
    "Cabecera", "Mejoras Públicas", "Campohermoso", "Real de Minas", "La Concordia", 
    "Conucos", "Mutis", "La Victoria", "Girardot"
]

idx = {ListaBarrios[i]: i for i in range(len(ListaBarrios))}
UIS_IDX = idx["UIS"] 

# CONEXIONES CON TIEMPO
Pesos_Nombres = [
    ("Real de Minas", "La Concordia", 8), ("La Concordia", "Real de Minas", 8), ("Campohermoso", "García R.", 4),
    ("García R.", "Campohermoso", 5), ("Campohermoso", "Kennedy", 7), ("La Concordia", "Kennedy", 6),
    ("Kennedy", "La Concordia", 6), ("Kennedy", "Campohermoso", 10), ("La Concordia", "Antonia Santos", 5),
    ("Antonia Santos", "La Concordia", 5), ("La Concordia", "Mejoras Públicas", 6), ("Mejoras Públicas", "La Concordia", 5),
    ("García R.", "Kennedy", 5), ("Kennedy", "García R.", 5), ("García R.", "Girardot", 5),
    ("Girardot", "García R.", 5), ("García R.", "Granada", 6), ("Granada", "García R.", 6),
    ("Kennedy", "García R.", 7), ("Kennedy", "Girardot", 6), ("Kennedy", "San Francisco", 6),
    ("San Francisco", "Kennedy", 6), ("Conucos", "Real de Minas", 9), ("Real de Minas", "Conucos", 9),
    ("Conucos", "La Concordia", 7), ("La Concordia", "Conucos", 7), ("Conucos", "Cabecera", 8),
    ("Cabecera", "Conucos", 10), ("Real de Minas", "Mutis", 6), ("Mutis", "Real de Minas", 8),
    ("Mutis", "Campohermoso", 13), ("Campohermoso", "Mutis", 8), ("Real de Minas", "Kennedy", 8),
    ("Kennedy", "Real de Minas", 12), ("Real de Minas", "Campohermoso", 9), ("Campohermoso", "Real de Minas", 7),
    ("Kennedy", "Antonia Santos", 4), ("Antonia Santos", "Kennedy", 5), ("Girardot", "Kennedy", 4), 
    ("Granada", "Girardot", 3), ("Girardot", "Granada", 3), ("Granada", "Gaitan", 9), 
    ("Gaitan", "Granada", 8), ("Girardot", "Gaitan", 7), ("Gaitan", "Girardot", 7),
    ("Girardot", "San Francisco", 7), ("San Francisco", "Girardot", 6), ("Antonia Santos", "La Concordia", 6),
    ("Antonia Santos", "San Francisco", 4), ("Antonia Santos", "San Alonso", 4), ("Antonia Santos", "Mejoras Públicas", 3),
    ("Mejoras Públicas", "Antonia Santos", 3), ("San Francisco", "Antonia Santos", 5), ("San Alonso", "Antonia Santos", 6),
    ("Cabecera", "Mejoras Públicas", 6), ("Mejoras Públicas", "Cabecera", 9), ("San Francisco", "Gaitan", 5),
    ("Gaitan", "San Francisco", 5), ("UIS", "Gaitan", 9), ("Gaitan", "UIS", 10),
    ("UIS", "Barrio Universidad", 5), ("Barrio Universidad", "UIS", 3), ("UIS", "San Alonso", 4),
    ("San Alonso", "UIS", 4), ("San Francisco", "Barrio Universidad", 3), ("Barrio Universidad", "San Francisco", 3)
]
