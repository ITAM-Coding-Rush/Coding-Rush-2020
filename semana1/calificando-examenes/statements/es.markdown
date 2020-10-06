# Descripción

El señor Felipe, un distinguido profesor de la universidad, tiene la tarea de calificar varios exámenes en muy poco tiempo. Además de esta ardua tarea, el profesor debe obtener el promedio de las calificaciones obtenidas por las alumnas y los alumnos para así saber cual fue el promedio general del salón. 

Para lograr esto, te ha contratado como programador para que hagas un código que obtenga este promedio.

# Entrada

En la primera línea un entero $n$, el número de alumnos en el salón.

En la segunda línea una cadena de caracteres, el nombre de la materia.

En las siguientes $n$ líneas vendrán la calificación que obtuvo cada alumno.

# Salida

Deberás imprimir el siguiente mensaje (sin comillas): "El promedio del examen de la materia {materia} es {promedio}", donde la materia es el nombre dado y el promedio es el de todos los alumnos que calificó el señor Felipe.

# Ejemplo

||input
5
Bases de datos
10
10
9.8
7.6
5.9
||output
El promedio del examen de la materia Bases de Datos es 8.6
||end

# Límites

- $1 \leq n \leq 100000$
- La calificación de cada alumno estará entre 0 y 10, inclusive.

<details><summary>Revisa la `plantilla.py`</summary>

{{plantilla.py}}

</details>