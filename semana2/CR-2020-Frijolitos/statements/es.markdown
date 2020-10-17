# Descripción

El respetable señor, doctor y profesor Gamboa tiene un arreglo $A$ de $n$ platos. En cada plato hay $A_i$ frijolitos especiales que ha estado coleccionando a lo largo de su vida.

Gamboa es un poco supersticioso. En particular, Gamboa quisiera que cualquier subarreglo (contiguo) de platos sumen en total un número de frijolitos **estrictamente menor** que un valor $k$.

Para esto, el primero quisiera contestar a la siguiente pregunta: ¿cuántos subarreglos de platos hay tal que en ellos hayan menos de $k$ frijolitos en total?

# Entrada

En la primera línea, un entero $n$ que representa el número de platos.
En la segunda línea, un entero $k$.
Para las siguientes $n$ líneas vendrán los enteros $A_i$ que representan el número de frijolitos del i-ésimo plato.

# Salida

Un solo entero, el número de subarreglos que cumplen que su suma sea menor a $k$

# Ejemplo

||input
4
15
10
5
2
6
||output
7
||description
Nuestro arreglo se ve así: [10, 5, 2, 6].
Los 7 subarreglos que tienen menos de 15 frijolitos son son: [10], [5], [2], [6], [5, 2], [2, 6], [5, 2, 6].
Nota que el subarreglo [10, 5] no se cuenta ya que 15 no es estrictamente menor a $k$.
||end

# Límites

- $ 1 \leq n \leq 100,000$
- $0 \leq k \leq 10^9$
- $0 \leq A_i \leq 10^9$
- Para el 50% de los casos, $1 \leq n \leq 10000$

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
