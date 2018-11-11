# Entregable Tarea 4 :page_with_curl:

## Alumno :bust_in_silhouette:: Matthias Fröhlich

El primer método que tengo pensado utilizar es el uso de QPainterPath. Lo que se haría es utilizar múltiples threads para realizar un seguimiento de los múltiples recorridos de los distintos jugadores. Por cada tick del programa, se avanzaría cierta distancia, y el espacio recorrido sería agregado a una lista con las coordenadas prohibidas, es decir, las que serán pintadas y en donde uno pierde de pasar por ahí, a excepción de que justo ocurra el evento aleatorio en el cual el movimiento de un jugador no deja rastro. Se utilizaría un módulo como QPen o QPainterPath para poder dibujar el las líneas correspondientes.

