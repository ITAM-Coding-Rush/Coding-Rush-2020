# Coding-Rush-2020

## Cómo Colaborar

Prerrequisitos:

- [Saber hacer problemas para omegaUp.](https://github.com/omegaup/omegaup/wiki/C%C3%B3mo-escribir-problemas-para-omegaUp)
- Saber usar git, y conocimiento básico de Python y C++.

Usamos git para coordinar el trabajo, así como pruebas automáticas
que revisan que los problemas tienen entradas válidas y que las
soluciones de prueba sacan los puntos que esperamos. Todo se coordina
con el archivo `problems.json` en la raíz del proyecto, y los
archivos individuales `settings.json` en las carpetas de los problemas.

El flujo de trabajo para hacer un problema es _estrictamente_
el siguiente. En todos los casos, *se debe hacer una branch y posteriormente un pull request* conteniendo una unidad de trabajo. Es importante no
mezclar trabajo de distintos problemas en el mismo branch o pull request.

1. Especificación del problema. Se escribe en el `es.markdown`,
   pero no es la redacción final. Debe contener:

- Descripción corta del problema. (Sin historia)
- Descripción del formato de entrada y salida.
- Descripción de las subtareas, de haber. Cada subtarea tiene que
  tener un identificador único que las distinga. (Más detalles
  en la sección de pruebas.)
- Agrega por lo menos un caso de prueba válido
  (el de ejemplo, probablemente) en `cases/0.in` y `cases/0.out`. Agrega
  un `testplan` que contenga solamente ese caso y obtenga 100 puntos.

2. Pruebas. (`tests`)

- Escribir pruebas que verifiquen los casos de prueba.
- Para C++, el evaluador debe checar que la entrada sea válida y que
  sigue _exactamente_ el formato descrito, cuidando en particular los
  espacios en blanco y saltos de línea.
- Las pruebas tienen que considerar los límites especiales que pueden existir
  para las distintas subtareas. Esto se logra dándole nombres de archivo
  a los casos conteniendo el identificador de su subtarea,
  para poder distinguir a qué subtarea pertenecen.
  [Aquí hay un ejemplo.](https://github.com/ComiteMexicanoDeInformatica/OMI-2018/tree/master/omi/Convertidor)
- En este punto se agrega el `settings.json` y el problema a `problems.json`.
  El alias del problema **no** se determina hasta que se escribe la redacción
  final. Puedes usar el alias temporal `dummy-omi` mientras tanto.
- Crear un archivo `tests/tests.json` indicando qué validador se usará para los casos de prueba. El archivo lleva este contenido:
  ```
  {
    "solutions": [
    ],
    "inputs": {
      "filename": "[validador].[lang]"
    }
  }
  ```
- A partir de aquí, los pull requests deben pasar las pruebas automáticas
  para poder ser integrados.
  Hay bibliotecas que simplifican el trabajo:
  revisa ejemplos de otros problemas de OMIs anteriores para ver cómo usarlas.

3. Solucion modelo.
   - La solución modelo (i.e. la que se usa para generar los `.out`)
     debe guardarse en la ruta `solutions/solution.[lang]`. Cuando
     esté lista la solución modelo, se puede trabajar tanto en soluciones
     como en casos al mismo tiempo.
   - Agrega la solucion a `tests/tests.json`:
     ```
     {
       "solutions": [
         {
           "filename": "../solutions/solution.[lang]",
           "verdict": "AC"
         }
       ],
       "inputs": {
         "filename": "[validador].[lang]"
       }
     }
     ```
   - No olvides borrar `0.out` cuando ya esté lista la solución modelo.
   - Agregar un documento .gitignore con el contenido `**/*.out`.
4. Otras soluciones (`solutions`)
   - Agrega tu solución en `solutions/[sol].[lang]`, así como
     en `tests/tests.json`, con el veredicto o puntaje esperado.
5. Casos. (`cases`)

- Escribe casos ya sea manualmente o autogenerados, siguiendo la
  especificación de la entrada. No olvides agruparlos de ser necesario,
  y si hay subtareas, de incluir en su nombre el identificador de la
  subtarea.
- En caso de que tus casos sean autogenerados, incluye el código que los
  generó en la raíz del problema, con el nombre `case-generator.[lang]`.
- Haz un `testplan` para tus casos. No puede tener puntos decimales y
  necesariamente debe sumar 100.
- Si es un problema con más de una salida válida, agrega aquí el `validator.[lang]`.

6. Redacción. (`statements/es.markdown`)

- Se escribe la redacción final del problema.
- Asegurarse de que los casos de ejemplo (`examples/sample.{in,out}`)
  existen. (Si hay solución modelo, no hace falta el `.out`.)

7. Explicación (`solutions/es.markdown`)

- Hacer un documento que explique la solución oficial.
- Listar las observaciones importantes para poder atacar el problema.
- Enfocarse en dar valor didáctico y si el problema es un tema conocido explicar dónde se puede aprender mas sobre este.

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

- Los tests tienen que tener comentarios explicando qué condiciones
  están evaluando de la entrada.
- Todos los archivos de texto deben de estar en encoding UTF-8.
- Debes correr el linter antes de mandar un PR para asegurarnos que el estilo
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
docker run --volume="${PWD}:/src" omegaup/hook_tools:20200924 fix --all
cd utils
pipenv install
pipenv run python3 runtests.py --all
```