# Redes Bayesianas 

La libreria que realicé permite construir redes bayesianas con sus respectivos nodos, aristas y probabilidades. Asimismo, devuelve factores, un valor booleano para saber si la red está completamente descrita y la forma compacta de la red.

## Arquitectura
Decidí guardar los nodos como objetos en un lista y poder tener acceso a su valor, probabilidades y relaciones entre nodos (Saber si tiene nodos padre o dependencias) para poder realizar los servicios solicitados en la hoja de trabajo.

## Instalación

Usa el manejador de paquetes de python pip para instalar la libreria: pagnetwork

```bash
pip install pagnetwork==0.0.2
```

## Uso

### Para importar libreria y poder usar métodos de la libreria
```python
from pagnetwork import BN
```

### Para crear nodos con dependencias
```python
graph.addEdge("R", "A")
graph.addEdge("T", "A")
graph.addEdge("A", "J")
graph.addEdge("A", "M")
graph.addEdge("J", None)
graph.addEdge("M", None)
```
** En caso de que un nodo no tenga un nodo dependiente colocar None como segundo parámetro.

### Advertencias:
* No permite colocar aristas repetidas.

### Para añadir probabilidades
```python
graph.addProb("R", {'+R': 0.001})
graph.addProb("T", {'+T': 0.002})
graph.addProb("A", {'+A|+R+T': 0.95, '+A|+R-T': 0.94, '+A|-R+T': 0.29, '+A|-R-T': 0.001})
graph.addProb("J", {'+J|-A': 0.05, '+J|+A': 0.9})
graph.addProb("M", {'+M|+A': 0.7, '+M|-A': 0.01})
```
### Advertencias
* Chequea la cantidad neceseria de probabilidades para cada nodo, es decir, 2^n.
* Chequea que la(s) llave(s) sean permitidas para el nodo que desea ingresarlas.
* No permite ingresar probabilidades donde los números no se encuentran en un rango de entre 0 y 1.

### Para obtener la representación compacta de la red bayesiana en forma de string
```python
graph.compactness()
```

### Para obtener los factores de la red bayesiana en forma de hashmap
```python
graph.allFactors()
```

### Para obtener un valor booleano y saber si la red está completamente descrita 
```python
graph.described()
```

### Pull request de colaboración que hice con el repositorio Guillermo Santos 19157. Fue mergeado y aprobado  el 16 de febrero.
![Picture](https://user-images.githubusercontent.com/64711979/219552603-d072d732-c3f9-436d-a6de-3976c5e4d53a.png)

