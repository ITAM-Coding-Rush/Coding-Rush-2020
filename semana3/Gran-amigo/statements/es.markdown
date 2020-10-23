# Descripción

Héctor tiene muchos problemas actualmente. No sabe qué está pasando en sus clases ya que rara vez entra y no hace nada en sus horas libres más que perder el tiempo. Tú, un amigo muy cercano, lo notas desanimado y buscas ayudarlo a motivarse para entrar a sus clases y perder el menor tiempo posible. Una idea viene a tu cabeza, hacer un registro de las horas que estudió y las horas en las que no hizo nada. Héctor te dirá un día de la semana, cuantas horas estudió ese día y cuantas no hizo nada. Ya que te haya  dado estos datos, tú compararás si tuvo una mejora para eso Héctor te dirá cuantas horas de productividad tuvo la semana pasada a la escuela.

Para hacer esto más motivante vas a decirle las horas de productividad  $=$ horas en la escuela $-$ horas perdiendo el tiempo. Le mostrarás un mensaje diferente dependiendo del caso: si supero las horas está semana, si se quedo igual o si bajo su rendimiento, en este último caso le mostraras también las horas de diferencia con la semana pasada y el rendimiento en tres días diferentes de esta semana.


# Entrada

Héctor te dará un número $n$ equivalente a los días que hizo algo. Por cada día que hizo algo también te dará el nombre del día de la semana (con mayúscula y sin acento), la(s) hora(s) que dedicó a la escuela y la(s) hora(s) que estuvo perdiendo el tiempo. Una vez recibidos esos $n$ valores te dirá las horas productivas de la semana pasada. Si no superó el tiempo de la semana pasada Héctor te dará tres días de la semana para que le digas cuántas horas trabajó en la escuela dicho día.


# Salida

En caso de haber superado las horas (sin comillas) "Sigue así, intenta mejorar tu marca de esta semana:" (seguido del total de horas que tuvo de productividad)

En caso de igualar las horas (sin comillas) "No has mejorado, pero tampoco empeorado. Esfuérzate un poco más"

En caso de ser inferior a las horas de productividad de la semana pasada (sin comillas) "Te quedaste atrás por: " (seguido de las horas faltantes para igualar la marca de la semana anterior), y según el día indicado,  "El día $x$ invertiste un total de: $y$ horas



# Ejemplo

||input
3           
Lunes       
5           
1           
Martes
6
2
Jueves
4
5
10
Lunes
Martes
Viernes
||output
Te quedaste atrás por: 3
El día Lunes invertiste un total de: 5 horas
El día Martes invertiste un total de: 6 horas
El día Viernes invertiste un total de: 0 horas
||description
La suma de horas invertidas en la escuela esta semana es de 15 y la suma de las horas en las que perdió el tiempo es de 8 por lo tanto sus horas de productividad son 15-8 = 7. Como la semana pasada sus horas de productividad son 20 Héctor no superó sus horas esta semana y por eso te dio tres días para que le mostraras sus horas de trabajo en la escuela dichos días.
||input
5               
Lunes
5
0
Martes
3
4
Miercoles
0
2
Jueves
7
1
Domingo
5
0
12
||output
Sigue así, intenta mejorar tu marca de esta semana: 13
||description
Las horas de productividad esta semana son 20-7 = 13 por lo tanto es mayor a las 12 horas de productividad de la semana pasada
||input
2           
Miercoles
3
0
Sabado
4
1
6
||output
No has mejorado, pero tampoco empeorado. Esfuérzate un poco más
||description
Sus horas de productividad son 7-1 = 6 que es lo mismo que la semana pasada
||end

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>

# Límites

* $ 1 \leq n \leq 7$