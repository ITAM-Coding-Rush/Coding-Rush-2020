# Descripción

Gatica está trabajando en su encuesta de Gateco Go desde que salió el juego. Cada semana actualiza los valores de probabilidad de capturar un Gateco especial. Como quiere crear una página para obtener más datos y filtrarlos automaticamente, te ha pedido a ti que le ayudes a revisar los datos mientras él trabaja.

Él te pasará las respuestas de los $N$ jugadores de esta semana donde cada una de las respuestas contiene la información de $K_i$ gatecos: su nombre junto con la cantidad de estos gatecos que capturó el jugador $i$.

Después dará el número $M$ de Gatecos especiales que podían aparecer esa semana. Para cada uno de los $M$ gatecos te dirá cuántos Gatecos de este tipo aparecieron en la semana y la probabilidad que él tiene registrada como la probabilidad de captura de este Gateco especial.

Normalmente si los datos arrojan que se capturaron más Gatecos especiales de los que son probables, Gatica no actualiza esos datos y prefiere revisarlos manualmente, por eso te pide que le digas unicamente qué gatecos cumplen que esta semana la probabilidad de capturarlos fue menor a la esperada y cual fue dicha probabilidad.

# Entrada

Un número $N$ que representa la cantidad de respuestas que te dará Gatica.

Posteriormente vendrá la información de los $N$ jugadores. Un número $K_i$ que representa la cantidad de Gatecos diferentes de esa respuesta. Después vendrán $K_i$ pares de datos: Gateco y Cantidad de Especiales capturados, una cadena y un entero, respectivamente.

En la siguiente línea, un numero $M$ que representa la cantidad de Gatecos especiales disponibles.

Finalmente vendrán $M$ triadas de datos:

- Una cadena, el nombre del Gateco Especial disponible.

- Un entero, el numero de Gatecos totales que aparecieron.

- Un número real, la probabilidad esperada de capturar al Gateco.

# Salida

Deberás imprimir el nombre y probabilidad real de captura de todos los gatecos que cumplen que la probabilidad real de capturarlos fue menor a la esperada y cual fue dicha probabilidad, en el formato (sin comillas) "[Nombre del Gateco]: [probabilidad real de ser capturado]".

No importa el orden en que imprimas los gatecos.

# Ejemplo

||examplefile
sample
||description
En el caso de char y pkchu sus probabilidades de ser capturado eran 0.6 y 0.8 respectivamente, como la probabilidad real fue menor se imprimen.

escuar no se imprime porque tuvo una probabilidad mayor de 0.5 y Gatica prefiere revisar manualmente él esos datos

tata y bobosur no se imprimen porque no capturaron ninguno esta semana y por lo tanto no se puede actualizar el valor

||end

# Límites

- $0 \leq N \leq 100$
- $1 \leq K_i \leq 600$
- $1 \leq M \leq 500$
