# Descripción

Pablo está próximo a graduarse, sin embargo se encuentra cursando sus últimas 4 materias. Él desea terminar la carrera con la posibilidad de obtener la mención honorífica. Para ello, es imperativo que tenga un promedio de 9.5 en su último semestre y presentar un excelente examen profesional.

Los maestros de Pablo le van a entregar 3 de sus 4 calificaciones: la de Antenas, la de Radiación y la de Redes Convergentes. La calificación que le falta es la de Seminario de Titluación.

Ayuda a Pablo a crear un programa en el que pueda meter sus calificaciones y le diga cuál es la calificación mínima que necesita en Seminario de Comunicación para poder ser acreedor a la mención honorífica.

# Entrada

Tres enteros $a$, $b$, $c$ que indiquen la calificación que sacó en Antenas, en Radiación y en Redes respectivamente.

# Salida

Si existe tal calificación mínima (número entero), una concatenación de caracteres que diga lo siguiente (sin comillas):
"Pablo será candidato a la mención honorífica si su calificación en Seminario de Titulación es de $n$.", donde $n$ representa la calificación mínima que necesita sacar.

Si es imposible que Pablo saque su mención honorífica escribe lo siguiente (sin comillas):
"No hay poder humano que haga que Pablo obtenga su mención honorífica."

# Ejemplo

||input
10
10
10
|| output
Pablo será candidato a la mención honorífica si su calificación en Seminario de Titulación es de 8.
||input
6
6
9
|| output
No hay poder humano que haga que Pablo obtenga su mención honorífica.
|| end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
