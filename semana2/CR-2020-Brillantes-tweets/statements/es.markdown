# Descripción

Estás cursando la materia de ideas en el ITAM y tu profesor te pidió escribir en formato de tweets; esto es, una línea que no tenga más de 140 caracteres. Sin embargo, en su formato también te ha dicho que los **espacios valen por dos caracteres.**

Al no poder usar internet para checar la cantidad de caracteres, la mejor opción para verificar la cantidad de caracteres, es hacer un programa que te regrese si tus líneas son válidas o no, y la cantidad de caracteres que usaste en cada una de ellas.

# Entrada

En la primera línea, un entero $N$ que representa el número de tweets (líneas) que tendrás que revisar.

En las siguientes $N$ líneas vendrá una cadena de caracteres que representan los tweets a revisar.

# Salida

Para cada tweet deberás imprimir dos líneas. En la primera, la cadena "Correcto" o "Incorrecto" si es válido o no el tweet. En la segunda línea deberás imprimir el número de caracteres del tweet.

# Ejemplo

||input
2
Si esperas el momento adecuado, puede que siempre te quedes esperando.
Cuando tenemos una mentalidad demasiado rígida puede ser perjudicial para nuestro bienestar, pues, somo incapaces de ser objetivos.
||output
Correcto
80
Incorrecto
148
||description
Hay dos tweets, el primero cuenta como 80 caracteres y el segundo cuenta como 148 caracteres.
||end

# Límites

- $1 \leq N \leq 100$

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
