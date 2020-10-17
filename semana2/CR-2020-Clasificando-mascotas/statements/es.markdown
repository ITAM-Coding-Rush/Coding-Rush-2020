# Descripción

Andrea tiene muchas mascotas y le encanta complicarle la vida a sus amigos. Decidió que cuando le pregunten algo sobre sus mascotas les dirá lo
siguiente:

1. Si el nombre de la mascota tiene 5 letras o menos, entonces es un perro. Si tiene 6 o más letras, es un gato.
2. Si el nombre de la mascota tiene alguna 'a' o alguna 'y', entonces su mascota es hembra. En caso contrario, es macho.

Ayuda a los amigos de Andrea a que descubran que tipo de animal es cada una de sus mascotas.

# Entrada

En la primera línea un entero $N$ indicando el número de mascotas que tiene Andrea.

Después vendrán $N$ líneas. Cada línea representa cada uno de los nombres de las mascotas de Andrea.

NOTA: Se te asegura que todos los nombres contendrán únicamente letras minúsculas.

# Salida

Deberás imprimir 4 líneas en el siguiente orden y con el siguiente formato (sin comillas):

"Tiene $W$ perros macho"

"Tiene $X$ perros hembra"

"Tiene $Y$ gatos macho"

"Tiene $Z$ gatos hembra"

Donde $W$ es el número de perros macho que tiene Andrea, $X$ el número de perros hembra, $Y$ el número de gatos macho y $Z$ el número de gatos hembra.

# Ejemplo

||input
5
ojitos
calcetas
sopa
belyy
aria
||output
Tiene 0 perros macho
Tiene 3 perros hembra
Tiene 1 gatos macho
Tiene 1 gatos hembra
||end

# Límites

- $0 < N < 100$
- La longitud del nombre de las mascotas será menor a 100,000

<details><summary>Checa la `plantilla.py`</summary>

{{plantilla.py}}

</details>
