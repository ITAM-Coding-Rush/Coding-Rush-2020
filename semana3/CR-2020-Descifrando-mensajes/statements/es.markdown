# Descripción

Te juntas todos los viernes a tomar café con tus amigos después de la clase de química, y en la última reunión te contaron que el profesor de redacción dejó como tarea desencriptar un mensaje.

Como tus amigos son muy listos se dieron cuenta del truco que usa el profesor. El profesor escribe un **0** antes de un pedazo del mensaje que está en orden y escribe un **1** si lo que sigue en el texto está invertido.

Como tus amigos tienen mucha tarea decides ayudarlos haciendo un código que descifre los mensajes. Para facilitarte el trabajo tus amigos separaron en renglones cada que encontraron un **1** o un **0**.

# Entrada

- En la primera línea, un entero $n$ que es el número de renglones que tiene el mensaje.

- Las siguientes $n$ líneas describen las cadenas de caracteres (las cadenas inician con un **0** si está en orden o con un **1** si está invertido).

# Salida

Una cadena de caracteres que representa el mensaje desencriptado sin los **1** y **0**.

# Ejemplo

||examplefile
sample
||examplefile
sample2
||end

# Límites

- $0 < n < 100$

<details><summary>Revisa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
