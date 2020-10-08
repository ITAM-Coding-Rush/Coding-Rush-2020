# Descripción

Guillermo, un estudiante promedio, ha bajado su rendimiento escolar drásticamente por culpa de la pandemia. A su vez, ha estado jugando muchas más horas videojuegos y le ha dedicado menos horas a estudiar. Tú, al ser su gran amigo, le ofreces ayuda para que pueda volver a tener buenas calificaciones. Para esto, le vas a hacer primero un programa que, con base en las horas que estudió Guillermo, estime cuánto va a sacar en sus exámenes.

Se sabe que Guillermo estudió $n$ días y para cada día estudió $H_i$ horas. Ahora bien, si en total estudió 20 o más horas, sacará 10; si estudió 15 o más, pero menos de 20 horas, sacará 9; si estudió 12 o más horas y menos de 15 horas, sacará 8; si estudió 10 o más horas y menos de 12 horas, sacará 7; si estudió 8 o más horas pero menos de 10 horas, sacará 6; y si estudió menos de 8 horas, reprobará.

# Entrada

En la primera línea un entero $n$, la cantidad de días que estudió Guillermo.

En las siguientes $n$ líneas vendrá un entero por línea $H_i$ que representa la cantidad de horas que estudió en el $i-ésimo$ día.

# Salida

En caso de haber reprobado, deberás imprimir la cadena "Reprobaras" (sin comillas). En otro casó deberás imprimir "Sacaras [calificación]" con la calificación estimada.

# Ejemplo

||input
5
4
5
3
5
2
||output
Sacaras 9
||description
Guillermo estudió 5 días. En total estudió 4 + 5 + 3 + 5 + 2 = 19 horas, por lo que su calificación estimada es de 9.
||input
3
3
2
2
||output
Reprobaras
||description
Guillermo estudió solamente 7 horas en total, por lo que reprobará.
||end

# Límites

- $0 \leq n \leq 30$
- $1 \leq H_i \leq 24$

<details><summary>Revisa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
