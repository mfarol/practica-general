# Entregable Tarea 3 :page_with_curl:

## Alumno :bust_in_silhouette:: Matthias Fröhlich

Pienso crear una estructura con nodos organizada en varios árboles :deciduous_tree:, con la ligera diferencia de que 
existirán más de un nodo raíz, siendo estos todas las plantas generadoras. También se podría ver como que el nodo raíz es la 
estación elevadora, asumiendo que solo existe una estación elevadora por árbol, y recorriendo primero los nodos que sean de 
plantas generadoras para tener el total de potencia que le llega a la estacíon elevadora. 

Cada árbol se recorrería con el método **Depth Frist Search (DFS)**, es decir, se recorre cada rama hasta su fin antes de 
recorrer otra. Cuando se llegue al fin de cada una, se calcula su demanda de consumo de la manera que se especifica en el 
enunciado, tomando en cuenta las pérdidas por la resistencia, se crea una función que retorne el total de nodos padre que 
posee ese nodo y a cada nodo padre se le agrega el valor de la demanda del nodo dividida por la cantidad de nodos padres más 
la pérdida producto de sus respectivas resistencias. Una vez realizado esto se elimina el nodo límite de la rama. Para que 
este proceso no afecte al árbol permanentemente, se recorre una copia del árbol, una representación. Una vez terminada este 
iteración de DFS se repite hasta llegar al nodo raíz, al cual se le debería haber entregado el valor total de la demanda, y 
definiendo la demanda como una property de cada nodo se pedirá que retorne el valor total.

Este método funcionaría porque, al ir eliminando cada nodo, uno se asegura de que no vuelva a ser recorrido y toda la 
información relevante es traspasada a los nodos padres. Si se quiere saber el total de demanda es cosa de sumar la demanda de 
cada árbol, que son la representación de cada sistema eléctrico independiente.

