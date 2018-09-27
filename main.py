from collections import namedtuple, defaultdict, deque

"""
Aquí están las estructuras de datos para guardar la información respectiva.

NO MODIFICAR.
"""

# Como se vio en la ayudantía, hay varias formas de declarar una namedtuple :)
Entrenador = namedtuple('Entrenador', 'nombre apellido')
Pokemon = namedtuple('Pokemon', ['nombre', 'tipo', 'max_solicitudes'])
Solicitud = namedtuple('Solicitud', ['id_entrenador', 'id_pokemon'])

################################################################################
"""
En esta sección debe completar las funciones para cargar los archivos al sistema.

Puedes crear funcionas auxiliar si tú quieres, ¡pero estas funciones DEBEN
retornar lo pedido en el enunciado!
"""

def cargar_entrenadores(ruta_archivo):
    """
    Esta función debería leer el archivo archivo_entrenadores y cargarlo usando
    las estructuras entregadas.
    """
    entrenadores = []
    with open(ruta_archivo, "r", encoding = "latin-1") as archivo:
        for linea in archivo:
            linea = linea.strip().split(";")
            entrenador_temp = Entrenador(linea[1], linea[2])
            entrenador_temp = (linea[0], entrenador_temp)
            entrenadores.append(entrenador_temp)
        entrenadores = tuple(entrenadores)
    return entrenadores

def cargar_pokemones(ruta_archivo):
    """
    Esta función debería leer el archivo archivo_pokemones y cargarlo usando las
    estructuras entregadas.
    """
    pokemones = []
    with open(ruta_archivo, "r", encoding="latin-1") as archivo:
        for linea in archivo:
            linea = linea.strip().split(";")
            pokemon_temp = Pokemon(linea[1], linea[2], linea[3])
            pokemon_temp = (linea[0], pokemon_temp)
            pokemones.append(pokemon_temp)
        pokemones = tuple(pokemones)
    return pokemones


def cargar_solicitudes(ruta_archivo):
    """
    Esta función debería leer el archivo archivo_solicitudes y cargarlo usando
    las estructuras entregadas.
    """
    solicitudes = defaultdict(int)
    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.strip().split(";")
            solicitudes(linea[0]) = linea[1]
    return solicitudes


################################################################################

"""
Lógica del Sistema.
Debes completar esta función como se dice en el enunciado.
"""

def sistema(modo, entrenadores, pokemones, solicitudes):
    """
    Esta función se encarga de llevar a cabo la 'simulación', de acuerdo al modo
    entregado.
    """
    if modo == "1":
        for elemento in pokemones:
            n = pokemones[elemento][1].max_solicitudes
            for i in solicitudes
    else:

    pass



################################################################################
"""
Funciones de consultas, deben rellenarlos como dice en el enunciado :D.
"""

def pokemones_por_entrenador(id_entrenador, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó el entrenador con el
    id entregado.

    Recuerda que esta función debe retornar una lista.
    """
    pokemones_ganados = []
    for elemento in resultado_simulacion:
        if resultado_simulacion[elemento][0] == id_entrenador:
            pokemones_ganados.append(resultado_simulacion[elemento][1])
    return pokemones_ganados

def mismos_pokemones(id_entrenador1, id_entrenador2, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó tanto el entrenador
    con el id_entrenador1 como el entrenador con el id_entrenador2.

    Recuerda que esta función debe retornar una lista.
    """
    id_entrenador1 = set(id_entrenador1)
    id_entrenador2 = set(id_entrenador2)
    set_union = id_entrenador1 & id_entrenador2
    set_union = list(set_union)
    return set_union

def diferentes_pokemones(id_entrenador1, id_entrenador2, resultado_simulacion):
    """
    Esta función debe retornar todos los pokemones que ganó el entrenador con
    id_entrenador1 y que no ganó el entrenador con id_entrenador2.

    Recuerda que esta función debe retornar una lista.
    """
    id_entrenador1 = set(id_entrenador1)
    id_entrenador2 = set(id_entrenador2)
    set_difference = id_entrenador1 - id_entrenador2
    set_difference = list(set_union)
    return set_difference



if __name__ == '__main__':

    ############################################################################
    """
    Poblando el sistema.
    Ya se hacen los llamados a las funciones, puedes imprimirlos para ver si se
    cargaron bien.
    """

    entrenadores = cargar_entrenadores('entrenadores.txt')
    pokemones = cargar_pokemones('pokemones.txt')
    solicitudes = cargar_solicitudes('solicitudes.txt')

    # print(entrenadores)
    # print(pokemones)
    # print(solicitudes)

    ################################   MENU   ##################################
    """
    Menú.
    ¡No debes cambiar nada! Simplemente nota que es un menú que pide input del
    usuario, y en el caso en que este responda con "1" ó "2", entonces se hace
    el llamado a la función. En otro caso, el programa termina.
    """

    eleccion = input('Ingrese el modo de lectura de solicitudes:\n'
                 '1: Orden de llegada\n'
                 '2: Orden Inverso de llegada\n'
                 '>\t')

    if eleccion in {"1", "2"}:
        resultados_simulacion = sistema(eleccion, entrenadores,
                                        pokemones, solicitudes)
    else:
        exit()

    ##############################   Pruebas   #################################
    """
    Casos de uso.

    Aquí pueden probar si sus consultas funcionan correctamente.
    """
