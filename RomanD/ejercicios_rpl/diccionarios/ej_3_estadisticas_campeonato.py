"""El siguiente ejercicio nos pide extraer estadísticas para un campeonato de fútbol finalizado a partir de ciertos
datos que se encuentran cargados en un diccionario importado desde un archivo secundario.

El diccionario tiene como clave el nombre del equipo de fútbol y como valor asociado una tupla de largo 5, que contiene
información sobre el desempeño de los equipos en el campeonato. En la primera posición tiene la cantidad de partidos
ganados (vale por 3 puntos); en la segunda posición la cantidad de partidos empatados (vale por 1 punto); en la tercera
posición la cantidad de partidos perdidos (vale por 0 puntos); en la cuarta posición la cantidad de goles realizados;
y en la quinta posición la cantidad de goles recibidos.

A partir de importar este diccionario, se pide construir un programa que calcule las siguientes estadísticas:

    El equipo que salió campeón, con su respectiva cantidad de puntos.
    El equipo que desciende (último), con su respectiva cantidad de puntos.
    El partido que más partidos empatados tuvo, con su respectiva cantidad.
    El equipo que tiene el ratio goles realizados sobre goles recibidos más alto de todos (goles realizados / goles
    recibidos).

La salida debe tener el siguiente formato:

El equipo campeon es Boca con 26 puntos.
El equipo que desciende es San Lorenzo con 4 puntos.
El equipo que mas partidos empato es River con 6 partidos.
El equipo con mejor proporcion goleadora es Huracan con 2.6.

Nota importante: Está claro que conociendo el diccionario pueden hacer las cuentas a mano y printear las respuestas.
El objetivo del ejercicio es que hagan los cálculos. Nuevamente, confiamos en su honestidad y responsabilidad para
aprovechar el ejercicio para practicar."""

campeonato = {
    "Boca": (2, 3, 4, 10, 10),
    "River": (3, 4, 2, 12, 16),
    "Central": (7, 1, 1, 23, 21),
    "Racing": (5, 2, 2, 15, 8),
    "Independiente": (4, 3, 2, 7, 8),
    "San Lorenzo": (1, 8, 0, 5, 9),
    "Godoy Cruz": (3, 3, 1, 3, 3),
    "Estudiantes": (1, 1, 7, 9, 9),
    "Huracan": (3, 2, 4, 4, 6),
    "Gimnasia LP": (0, 2, 7, 1, 26)
}



