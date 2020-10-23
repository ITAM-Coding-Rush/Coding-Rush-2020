# Descripción

Gatica esta trabajando en su encuesta de Gateco Go desde que salió el juego. Cada semana actualiza los valores de probabilidad de capturar un Gateco especial, pero como quiere crear una pagina para obtener más datos y filtrarlos automaticamente te ha pedido a ti que le ayudes a revisar los datos mientras él trabaja.

El te pasará las respuestas de los $N$ jugadores de esta semana donde cada una de las respuestas contiene $K_i$ nombres de gatecos especiales y la cantidad de estos gatecos especiales que capturó el jugador $i$

Despues dará el número $M$ de Gatecos especiales que podían aparecer esa semana. Para cada uno de los $M$ gatecos te dirá cuántos Gatecos de este tipo capturaron los jugadores en la semana (normales y especiales) y la probabilidad que él tiene registrada como la probabilidad de aparición de este Gateco especial.

Normalmente si los datos arrojan que se capturaron más Gatecos especiales de los que son probables, Gatica no actualiza esos datos y prefiere revisarlos manualmente, por eso te pide que le digas unicamente qué gatecos cumplen que esta semana la probabilidad de capturarlos fue menor a la esperada y cual fue dicha probabilidad.



# Entrada

Un número $N$ que representa la cantidad de respuestas que te dará Gatica.

Un número $K$ que representa la cantidad de Gatecos diferentes de cada respuesta

$K$ pares de datos:

- Gateco

- Cantidad de Especiales capturados

Un numero $M$ que representa la cantidad de Gatecos especiales disponibles

$M$ triadas de datos:

- Gateco Especial disponible

- Numero de Gatecos totales capturados (especiales y normales)

- Probabilidad de que el Gateco fuera especial

# Salida

Nombre del Gateco : probabilidad real de ser especial

# Ejemplo

||input
3
2
char
3
escuar
8
3
char
3
escuar
8
pkchu
10
1
pkchu
2
5
pkchu
25
0.8
char
15
0.6
escuar
20
0.5
tata
15
0.6
bobosur
20
0.2
||output
char :  0.4
pkchu :  0.48
||description
En el caso de char y pkchu sus probabilidades de ser especial eran 0.6 y 0.8 respectivamente, como la probabilidad real fue menor se imprimen.

escuar no se imprime porque tuvo una probabilidad mayor de 0.5 y Gatica prefiere revisar manualmente él esos datos

tata y bobosur no se imprimen porque no capturaron ninguno esta semana y por lo tanto no se puede actualizar el valor

||end

# Límites

$0 \leq N \leq 100$

$1 \leq M \leq 500$

$1 \leq K \leq 600$