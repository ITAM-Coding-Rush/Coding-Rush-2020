# Coding-Rush-2020

## Cómo Colaborar

Prerrequisitos:

- [Lee sobre cómo hacer problemas para OmegaUp](https://github.com/omegaup/omegaup/wiki/C%C3%B3mo-escribir-problemas-para-omegaUp#problemas-de-lenguaje-ccjavapascal).

Usamos git para coordinar el trabajo, así como pruebas automáticas
que revisan que los problemas tienen entradas válidas y que las
soluciones de prueba sacan los puntos que esperamos. Todo se coordina
con el archivo `problems.json` en la raíz del proyecto, y los
archivos individuales `settings.json` en las carpetas de cada problema.

El flujo de trabajo para hacer un problema es _estrictamente_
el siguiente. En todos los casos, **se debe hacer una branch y posteriormente un pull request** para subir un problema. Es decir, NO hacer push desde la branch _master_.

Crea una carpeta con el nombre del problema (puedes copiar la carpeta llamada `problem-template`). Esta nueva carpeta debe contener los siguientes elementos:

- `settings.json`.

  - Modifica el `title` y `source` con el nombre y autor del problema, respectivamente.

- `statements/`

  - `es.markdown`. La redacción del problema. Para visualizar el formato puedes usar [https://omegaup.com/redaccion.php](https://omegaup.com/redaccion.php)

  - (Opcional) `plantilla.py`. Si tu problema tiene plantilla para mostrar en el problema, añade este archivo. Además, al final del archivo `es.markdown` (la redacción del problema) debes insertar lo siguiente:

    ```
    <details><summary>Checa la `plantilla.py`</summary>

    {{plantilla.py}}

    </details>
    ```

- `solutions/`

  - `solution.py`. Es la solución esperada del problema y también la que se utiliza para generar los `.out` en los casos.

  - (Opcional) Otras soluciones. En caso de querer probar otras soluciones (completas o parciales) se agregan como `[sol].[lang]`, así como en `tests.json`, con el veredicto o puntaje esperado.

  - (Opcional) `es.markdown`. Es un documento que explica la solución oficial.

- `tests/`

  - `test-validator.py`. Son pruebas para checar que la entrada de los casos sea válida y que siguen _exactamente_ el formato descrito, cuidando en particular los espacios en blanco y saltos de línea.

  - `tests.json`. Este archivo indica qué validador se usará para los casos de prueba y qué soluciones correrá para los tests. Normalmente, el archivo llevará este contenido:

  ```
  {
    "solutions": [
      {
        "filename": "solutions/solution.[lang]",
        "verdict": "AC"
      }
    ],
    "inputs": {
      "filename": "[validator].[lang]"
    }
  }
  ```

- `cases/`

  - Aquí van los casos ya sea manualmente o autogenerados, siguiendo la especificación de la entrada. Aquí van las entradas (archivos `.in`) y no se debe poner las salidas pues estas serán autogeneradas por la solución modelo.

  - En caso de que tus casos sean autogenerados, incluye el código que los generó en la raíz del problema, con el nombre `case-generator.[lang]`.

- `.gitignore`. Agrega este archivo para que se autogeneren las salidas de los casos. Debe contener lo siguiente:

  ```
  **/*.out
  ```

- `testplan`

  - Haz un `testplan` para los casos. No puede tener puntos decimales y
    necesariamente debe sumar 100. Recuerda que este archivo no tiene extensión.

Finalmente, se agrega el problema a `problems.json`.

Al enviar el pull request, se asegura que pasen las pruebas automáticas para poder ser integrados.

## Convenciones

- A menos de que las salidas sean difíciles de generar por alguna
  razón, solamente se hace commit a las entradas de los casos
  de prueba (`.in`). Los `.out` se generan automáticamente con la
  solución modelo.
- Cuando hay casos agrupados, el primer caso en el `testplan` debe
  tener el valor entero del grupo, y todos los demás 0. Por ejemplo:

  ```
  group.1 40
  group.2 0
  group.3 0
  ```

- Los tests tienen que tener comentarios explicando qué condiciones están evaluando de la entrada.
- Todos los archivos de texto deben de estar en encoding UTF-8.
- Se recomienda correr el linter antes de mandar un PR para asegurarnos que el estilo
  sea consistente y fácil de leer. Para correrlo localmente puedes ejecutar:

  ```shell
  ./utils/lint fix --all
  ```

## Cómo Correr los Tests Localmente

Cambiar el directorio a la raíz del proyecto.

La primera vez necesitas bajar el submódulo de
utilidades para omegaUp:

```bash
git submodule init && git submodule update
```

Instala Python 3, [pipenv](https://github.com/pypa/pipenv),
y la versión más reciente de [Docker](https://docs.docker.com/get-docker/).
Después, corre

```bash
./utils/lint fix --all
cd utils
pipenv install
pipenv run python3 runtests.py --all
```

## Problemas de ejemplo

- https://github.com/ITAM-Coding-Rush/Coding-Rush-2020/tree/master/semana2/frijolitos
