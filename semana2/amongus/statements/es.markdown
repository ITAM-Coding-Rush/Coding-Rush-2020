# Descripción

A Javiercito le gusta mucho jugar *Among Us* (un videojuego que recientemente se popularizó) en sus ratos libres. Como ya lleva tiempo jugando, ya se sabe todos los mapas y los lugares donde los impostores maldosos suelen atacar. Sin embargo, quiere ser el mejor entre sus amigos y para esto te ha pedido tu ayuda.

Javiercito quiere que lo ayudes a determinar cuál de los amigos con los que juega es el impostor. Para esto, aquél que dude cuando le preguntan en las reuniones de emergencia dónde estaba en el momento del asesinato, es el impostor.

#Entrada
Recibirás un entero $N$ entre 2 y 9, con el número de jugadores que quedan vivos (sin incluir a Javiercito).

Después, recibirás $N$ strings, que son lo que cada jugador contestó al ser interrogados. El jugador ha dudado al decir su posición si ha dicho en alguna parte de su respuesta: **hm**. (Solo habrá un **hm** por respuesta)

#Salida
- Si ninguno de los jugadores ha dicho *hm* deberás imprimir: *Javiercito es el impostor*
- Si el jugador $i$ ha dicho **hm** deberás imprimir: *El jugador $i$ es el impostor*
- Si más de un jugador ha dicho *hm* deberás imprimir: *Skip*

# Ejemplo:
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
$2 < N < 9$

<details>
<summary>Revisa la plantilla: 'plantilla.py'</summary>
{{plantilla.py}}
</details>
