# Descripción
Siempre que va al supermercado, Lorena registra el precio de todas los productos que compra para calcular cuánto gastó.
Debes saber que el supermercado al que asiste ofrece un descuento dependiendo del costo total pagado:

- Si el precio total fue menor a \$250 o menos NO se aplica ningún descuento.
- Si el precio total fue mayor o igual a \$250 y menor a \$500 se aplica un descuento del 5%.
- Si el precio total fue mayor o igual a \$500 y menor a \$1000 se aplica un descuento del 10%.
- Si el precio total fue mayor o igual a \$1000 se aplica un descuento del 15%.
Sin embargo, Lorena a veces se equivoca y suma erróneamente los precios, por lo que tú, como gran amigo que eres, te ofreces a
ayudarle y le prometes hacer un programa que le ayude a calcular el precio final incluyendo el descuento.

# Entrada

Ingresarás los precios (enteros), uno por uno, de los productos que Lorena vaya registrando. Cuando ya no haya nada más que sumar, debes
ingresar el 0 para finalizar el programa.

# Salida

Imprimirás el precio total a pagar con el descuento aplicado.

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
461.7
||end

# Límites
$0 < precio < 1000$

<details>
<summary>Revisa la plantilla: 'plantilla.py'</summary>
{{plantilla.py}}
</details>
