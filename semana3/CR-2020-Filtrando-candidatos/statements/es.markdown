# Descripción

Adriana es encargada de Recursos Humanos, es domingo en la noche y está muy estresada porque no ha terminado de ver qué solicitantes sí son candidatos al puesto de panadería del ITAM. Los solicitantes han llenado una encuesta, pero han dejado muchos espacios en blanco. Para el puesto, a Adriana le interesa que hayan contestado algunos campos como mínimo. Ayúdale escribiendo un programa que le permita acabar y dormir temprano.

# Entrada

Un entero $N$, la cantidad de campos totales que tiene la encuesta (distintos entre sí).

Después, $N$ líneas que indican cada uno de estos campos.

Ahora un entero $M$, la cantidad de campos que le interesan (distintos entre sí).

Después $M$ líneas que indican cada uno de estos campos.

Finalmente, un entero $S$ que inidica la cantidad de solicitantes, y por cada solicitante se indica la cantidad de campos que llenó y cuáles (los campos llenados son todos distintos).

# Salida

Un entero $R$ que indica la cantidad de aplicantes que sí son candidatos al puesto.

# Ejemplo

||examplefile
sample
||description
A Adriana sólo le importa que hayan contestado su nombre y su signo zodiacal, cosa que sólo han hecho las últimas dos personas.
||end

# Límites

- $ 1 \leq M \leq N \leq 100,000$
- La suma de los campos llenados entre todos los aplicantes no superará $100,000$
- Los campos serán cadenas de a lo más 10 caracteres.

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
