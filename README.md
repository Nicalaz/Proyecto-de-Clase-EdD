# Proyecto de Clase EdD - Optimización de Rutas
**Carlos Fabián Morales Carrillo 2240062** - **Nicolás Alberto Arciniegas Rincón 2240087** - **Juan Felipe Mora Bejarano 2241754** - **Juan Pablo Vera Suarez 2241807**

Este proyecto se centró en la implementación de un sistema de optimización de rutas, mediante varias estructuras de datos, para determinar la mejor ruta que los estudiantes de la UIS pueden tomar desde cualquier punto de la ciudad de Bucaramanga hasta la Universidad. El objetivo final fue determinar la ruta más eficiente desde sus puntos de origen, simulando una lista de comunas y barrios. Para ello, el desarrollo del proyecto se realizó en tres entregas con implementaciones diferentes, cada una empleando una estructura de datos más compleja, con el fin de mejorar la eficiencia y la efectividad del problema en cada implementación.

# Entrega 1 - listas Simplemente Enlazadas
En la primera etapa, se utilizó una Lista Simplemente Enlazada para establecer una representación secuencial y lineal de las rutas propuestas. Mediante esta implementación, se lograron los siguientes objetivos:

- **Representación de rutas**: cada ruta, ruta 1, ruta 2, ruta 3, se modeló como una lista, donde cada nodo representa una comuna con su distancia acumulada desde un mismo punto de partida que fue la Concordia.
- **Simulación de búsqueda**: se pudo simular la búsqueda de comunas y la identificación de la comuna más cercana al punto inicial.

Esta implementación fue útil para el manejo secuencial de los datos de distancia, permitiendo una representación clara y el cálculo de la distancia total. Sin embargo, se determinó que no fue la mejor opción en cuanto a eficiencia, debido a que la búsqueda secuencial, puede llegar a tener una complejidad final de O(n), si el elemento que se busca no se encuentra dentro de la misma lista o está en la última posición.

# Entrega 2 - Árboles AVL
Para mejorar la eficiencia en la gestión de los datos de distancia, la segunda etapa se enfocó en el uso de una estructura de datos jerárquica como los Árboles AVL. Mediante esta implementación, se lograron los siguientes objetivos:

- **Eficiencia mejorada**: al ser un árbol de búsqueda binario auto-balanceado, las operaciones de inserción, búsqueda y eliminación fueron mucho más rápidas.
- **Organización por distancia**: las ubicaciones se insertaron en el árbol basándose en su valor de distancia, permitiendo un acceso rápido a las distancias mínimas y máximas de una ruta.
- **Recorrido ordenado**: el recorrido Inorden permitió visualizar las comunas ordenadas de menor a mayor distancia desde el origen de la ruta.

Esta segunda implementación, resolvió los problemas de eficiencia de la etapa anterior, proporcionando una forma rápida y organizada de almacenar y acceder a las distancias de las comunas. Además, permitió representar la estructura que manejaba el árbol para cada ruta, permitiendo visualizar de manera gráfica el recorrido que se realizaba. Sin embargo, una de las limitaciones que se encontraron, fue respecto a la capacidad de modelado de una gran cantidad de comunas y rutas, debido a que esta implementación no modelaba completamente una red como tal, sino los puntos de una ruta como una estructura jerárquica.

# Entrega 3 - Grafos 
La entrega final y definitiva abordó el problema de la optimización de rutas como un desafío de la Teoría de Grafos, que es el modelo más adecuado para representar redes complejas. Mediante esta implementación, se lograron los siguientes objetivos:

- **Modelado de la red**: se creó un Grafo Dirigido Ponderado donde cada barrio es un nodo y las conexiones entre ellos son aristas con un peso de tiempo promedio de transporte entre los barrios.
- **Algoritmo Bellman Ford**: se implementó también este algoritmo para encontrar el camino más corto desde cualquier nodo de origen hasta el destino final que es la Universidad.
- **Reconstrucción de la ruta**: se implementó una función para reconstruir la ruta óptima paso a paso a través de los predecesores calculados por Bellman Ford.

Esta implementación final proporcionó una solución mucho más completa al problema de optimización de rutas, calculando de manera dinámica la ruta más eficiente en una red interconectada, superando las limitaciones secuenciales de la implementación 1 y de organización jerárquica de la implementación 2.

# Link Presentación
https://www.canva.com/design/DAG4ze7dwtI/WPUMXhPK9TGD9WzrAvK66A/edit

