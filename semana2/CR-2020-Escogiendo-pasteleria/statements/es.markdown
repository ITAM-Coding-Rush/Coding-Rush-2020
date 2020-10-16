# Descripción

Andrea, mejor conocida como la chica pan, le debe un pastel a Sebastián, pero por culpa de la cuarentena no ha podido pagarselo.
Dado que casi no sale de casa no sabe si la mejor opción es comprarlo en una pastelería cercana a la casa de Sebastián, mandarlo por Rappi o cocinarlo ella misma.
Andrea te dará la lista de locales donde cree que podrían vender pasteles, pero la lista es tan grande que prefiere solo contar con los lugares que tengan 'Pastel' en el nombre.
Si hay más de 15 lugares donde vendan pasteles, le pedirá el Pastel por Rappi porque no cree que le de tiempo de visitar todas las pastelerías.
Si hay máximo 15 lugares Andrea irá personalmente a elegir el pastel que más se le antoje.
Si no hay pastelerías, Andrea tendrá que cocinarle personalmente el pastel.
Ayuda a Andrea a decidir que hacer.

# Entrada

Recibirás una $N$ con el número de lugares a revisar.

A continuación recibirás $N$ Strings con el nombre de los lugares.

# Salida

- 'Pedir por Rappi' si más de 15 lugares tienen 'pastel' en el nombre.
- 'Elegir Personalmente' si hay entre 1 y 15 lugares con 'pastel en el nombre'.
- 'Cocinar' si no hay lugares que tienen 'pastel' en el nombre.

# Ejemplo

||input
5
Pastelería el globo
Pastelería la Zarza
Papapasteles Papapadrisimos
Panes Don Brandon
Papapapanes dulces
||output
Elegir Personalmente
||description
Solo hay 3 pastelerías con "Pastel" en el nombre, por lo que Andrea tendrá que elegir personalmente el pastel

||input
3
Panadería CR
Pastes Quikos
Paletas Trix
||output
Cocinar
||end

# Límites

$25 \leq N \leq 1000$

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
