# Clase Nodo
class Nodo:
    def __init__(self, nombre, distancia_acumulada):
        self.nombre = nombre
        self.distancia_acumulada = distancia_acumulada
        self.siguiente = None

# Clase Lista Simplemente Enlazada
class ListaSE:
    def __init__(self):
        self.cabeza = None

    # Método para verificar si la lista esta vacia
    def vacio(self):
        return self.cabeza is None
    
    # Método para contar la cantidad de elementos existentes en la lista
    def contarElementos(self):
        count = 0
        nodo = self.cabeza
        while nodo:
            count += 1
            nodo = nodo.siguiente
        return count

    # Método para imprimir en pantalla los elementos de la lista
    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(f"Comuna: {nodo_actual.nombre}, Distancia acumulada: {nodo_actual.distancia_acumulada} km")
            nodo_actual = nodo_actual.siguiente

    # Método para agregar un elemento al inicio de la lista
    def agregarInicio(self, nombre, distancia_acumulada):
        nuevo_nodo = Nodo(nombre, distancia_acumulada)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    # Método para buscar un elemento en la lista mediante el ordenamiento de Bubble Sort
    def buscarElemento(self, nombre_buscar):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return False

        cambiamos = True
        while cambiamos:
            cambiamos = False
            nodo_actual = self.cabeza
            while nodo_actual and nodo_actual.siguiente:
                if nodo_actual.nombre.lower() == nombre_buscar.lower():
                    return True
            
                if nodo_actual.nombre.lower() > nodo_actual.siguiente.nombre.lower():
                    nodo_actual.nombre, nodo_actual.siguiente.nombre = nodo_actual.siguiente.nombre, nodo_actual.nombre
                    nodo_actual.distancia_acumulada, nodo_actual.siguiente.distancia_acumulada = nodo_actual.siguiente.distancia_acumulada, nodo_actual.distancia_acumulada
                    cambiamos = True
                
                nodo_actual = nodo_actual.siguiente

        return False
 
    # Buscar la comuna más cercana a La Concordia con la menor distancia acumulada
    def obtenerComunaMasCercana(self):
        if not self.cabeza:
            return None

        nodo_actual = self.cabeza
        comuna_a = None
        comuna_cercana = None

        while nodo_actual:
            if nodo_actual.nombre.lower() == "la concordia":
                comuna_a = nodo_actual
                break
            nodo_actual = nodo_actual.siguiente

        if comuna_a is None:
            return None

        nodo_actual = self.cabeza
        comuna_cercana = None
        while nodo_actual:
            if nodo_actual != comuna_a:
                if comuna_cercana is None or nodo_actual.distancia_acumulada < comuna_cercana.distancia_acumulada:
                    comuna_cercana = nodo_actual
            nodo_actual = nodo_actual.siguiente

        return comuna_cercana

def main():
    # Creación de las rutas, los valores no son los reales, son simplemente simulados a conveniencia
    ruta1 = ListaSE()
    ruta1.agregarInicio("UIS", 12)  # Destino final
    ruta1.agregarInicio("San Francisco", 9)
    ruta1.agregarInicio("San Alonso", 6)
    ruta1.agregarInicio("Antonia Santos", 3)
    ruta1.agregarInicio("La Concordia", 0)  # Ubicación inicial

    ruta2 = ListaSE()
    ruta2.agregarInicio("UIS", 8)  # Destino final
    ruta2.agregarInicio("Gaitan", 6)
    ruta2.agregarInicio("Granada", 4)
    ruta2.agregarInicio("Garcia Rovira", 2)
    ruta2.agregarInicio("La Concordia", 0)  # Ubicación inicial

    ruta3 = ListaSE()
    ruta3.agregarInicio("UIS", 4)  # Destino final
    ruta3.agregarInicio("San Alonso", 3)
    ruta3.agregarInicio("San Francisco", 2)
    ruta3.agregarInicio("Kennedy", 1)
    ruta3.agregarInicio("La Concordia", 0)  # Ubicación inicial

    # Imprimir las rutas
    print("\n------------- SIMULANDO LAS RUTAS MÁS CERCANAS -------------")
    print("\nRuta 1")
    ruta1.imprimir()
    print("\nRuta 2")
    ruta2.imprimir()
    print("\nRuta 3")
    ruta3.imprimir()

    # Obtener la comuna más cercana a La Concordia (la comuna inicial) en cada ruta
    print("\n-------- COMUNA MÁS CERCANA A LA COMUNA INICIAL EN CADA RUTA ---------")
    print("\nComuna más cercana a La Corcordia en la Ruta 1:")
    comuna_cercana1 = ruta1.obtenerComunaMasCercana()
    if comuna_cercana1:
        print(f"Comuna: {comuna_cercana1.nombre}, Distancia a la que se encuentra: {comuna_cercana1.distancia_acumulada} km")
    else:
        print("La Concordia no fue encontrada en esta ruta.")

    print("\nComuna más cercana a La Concrodia en la Ruta 2:")
    comuna_cercana2 = ruta2.obtenerComunaMasCercana()
    if comuna_cercana2:
        print(f"Comuna: {comuna_cercana2.nombre}, Distancia a la que se encuentra: {comuna_cercana2.distancia_acumulada} km")
    else:
        print("La Concordia no fue encontrada en esta ruta.")

    print("\nComuna más cercana a La Concordia en la Ruta 3:")
    comuna_cercana3 = ruta3.obtenerComunaMasCercana()
    if comuna_cercana3:
        print(f"Comuna: {comuna_cercana3.nombre}, Distancia a la que se ecuentra: {comuna_cercana3.distancia_acumulada} km")
    else:
        print("La Concordia no fue encontrada en esta ruta.")
    
    # Buscamos la comuna San Francisco en cada ruta
    print("\n --------- SIMULANDO LA BUSQUEDA DE UNA COMUNA EN LAS RUTAS ---------")
    elemento_buscar = "San Francisco"
    print(f"\nBuscando {elemento_buscar} en la Ruta 1.")
    encontrado1 = ruta1.buscarElemento(elemento_buscar)
    if encontrado1:
        print(f"Comuna {elemento_buscar} se encontró en la Ruta 1.")
    else:
        print(f"Comuna {elemento_buscar} NO se encontró en la Ruta 1.")

    print(f"\nBuscando {elemento_buscar} en la Ruta 2.")
    encontrado2 = ruta2.buscarElemento(elemento_buscar)
    if encontrado2:
        print(f"Comuna {elemento_buscar} se encontró en la Ruta 2.")
    else:
        print(f"Comuna {elemento_buscar} NO se encontró en la Ruta 2.")

    print(f"\nBuscando {elemento_buscar} en la Ruta 3.")
    encontrado3 = ruta3.buscarElemento(elemento_buscar)
    if encontrado3:
        print(f"Comuna {elemento_buscar} se encontró en la Ruta 3.")
    else:
        print(f"Comuna {elemento_buscar} NO se encontró en la Ruta 3.")
    
    # Mostramos la mejor ruta (menor distancia acumulada)
    print("\n------------- MOSTRANDO LA MEJOR RUTA -------------")
    nodo_final_ruta1 = ruta1.cabeza
    while nodo_final_ruta1.siguiente:
        nodo_final_ruta1 = nodo_final_ruta1.siguiente
    distancia_ruta1 = nodo_final_ruta1.distancia_acumulada

    nodo_final_ruta2 = ruta2.cabeza
    while nodo_final_ruta2.siguiente:
        nodo_final_ruta2 = nodo_final_ruta2.siguiente
    distancia_ruta2 = nodo_final_ruta2.distancia_acumulada

    nodo_final_ruta3 = ruta3.cabeza
    while nodo_final_ruta3.siguiente:
        nodo_final_ruta3 = nodo_final_ruta3.siguiente
    distancia_ruta3 = nodo_final_ruta3.distancia_acumulada

    if distancia_ruta1 <= distancia_ruta2 and distancia_ruta1 <= distancia_ruta3:
        print(f"La mejor ruta es la Ruta 1 con la distancia acumulada final de {distancia_ruta1} km.")
    elif distancia_ruta2 <= distancia_ruta1 and distancia_ruta2 <= distancia_ruta3:
        print(f"La mejor ruta es la Ruta 2 con la distancia acumulada final de {distancia_ruta2} km.")
    else:
        print(f"La mejor ruta es la Ruta 3 con la distancia acumulada final de {distancia_ruta3} km.")
        
if __name__ == "__main__":
    main()
