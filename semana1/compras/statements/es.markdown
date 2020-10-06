# Descripción

Siempre que va al supermercado, Lorena registra el precio de todas los productos que compra para calcular cuánto gastó.
Debes saber que el supermercado al que asiste ofrece un descuento dependiendo del costo total pagado:

- Si el precio total fue menor a \$250 NO se aplica ningún descuento.
- Si el precio total fue mayor o igual a \$250 y menor a \$500 se aplica un descuento del 5%.
- Si el precio total fue mayor o igual a \$500 y menor a \$1000 se aplica un descuento del 10%.
- Si el precio total fue mayor o igual a \$1000 se aplica un descuento del 15%.

Sin embargo, Lorena a veces se equivoca y suma erróneamente los precios, por lo que tú, como gran amigo que eres, te ofreces a ayudarle y le prometes hacer un programa que le ayude a calcular el precio final incluyendo el descuento.

# Entrada

En cada línea encontrarás precios (enteros), uno por uno, de los productos que Lorena vaya registrando. Cuando ya no haya nada más que sumar, vendrá una línea con el número 0 que marca el fin de los productos.

# Salida

Deberás imprimir el precio total a pagar con el descuento aplicado redondeado a dos decimales. El formato que deberás imprimirlo es el siguiente (sin comillas): "El precio total es: [total]"

Nota: para redondear un número x a dos decimales puedes usar la función `round(x, 2)`.

# Ejemplo

||input
130
27
34
51
223
48
0
||output
El precio total es: 461.7
||end

- Limites

- El precio de cada producto está entre 1 y 1000

<details>
<summary>Revisa la plantilla: `plantilla.py`</summary>

{{plantilla.py}}

</details>
