# Descripción

A Javiercito le gusta mucho jugar _Among Us_ (un videojuego que recientemente se popularizó) en sus ratos libres. Como ya lleva tiempo jugando, ya se sabe todos los mapas y los lugares donde los impostores maldosos suelen atacar. Sin embargo, quiere ser el mejor entre sus amigos y para esto te ha pedido tu ayuda.

Javiercito quiere que lo ayudes a determinar cuál de los amigos con los que juega es el impostor. Para esto, aquél que dude cuando le preguntan en las reuniones de emergencia dónde estaba en el momento del asesinato, es el impostor.

# Entrada

Recibirás un entero $N$ entre 2 y 9, con el número de jugadores que quedan vivos (sin incluir a Javiercito).

Después, recibirás $N$ strings, que son lo que cada jugador contestó al ser interrogado. El jugador ha dudado al decir su posición si ha dicho en alguna parte de su respuesta: **hm**.

#Salida

- Si ninguno de los jugadores ha dicho _hm_ deberás imprimir: _Javiercito es el impostor_
- Si el jugador $i$ ha dicho **hm** deberás imprimir: _El jugador $i$ es el impostor_
- Si más de un jugador ha dicho _hm_ deberás imprimir: _Skip_

# Ejemplo

||input
4
Yo estaba en armeria
En la cafeteria
mmm yo estaba en hmmm abajo
Por ahi
||output
El jugador 3 es el impostor
||input
2
Tirando basura
Yo no soy creanme
||output
Javiercito es el impostor
||end

# Límites

$2 \leq N \leq 9$

<details><summary>Revisa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
