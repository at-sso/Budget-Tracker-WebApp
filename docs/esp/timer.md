## Documentación para timer/init.py

Este archivo define una función `timer` que se utiliza para medir y registrar el tiempo de ejecución de otra función, al mismo tiempo que maneja cualquier excepción que pueda ocurrir durante su ejecución.

**Funciones:**

- `timer(func, *args, **kwargs)`
  - Esta función toma una función llamable `func` como su primer argumento, junto con cero o más argumentos posicionales (`*args`) y cero o más argumentos de palabras clave (`**kwargs`) que se pasarán a la función.
  - Ejecuta la función `func` proporcionada y mide su tiempo de ejecución.
  - Registra el inicio y el final de la ejecución, junto con la duración total, en el nivel de depuración.
  - En caso de excepciones no manejadas provocadas dentro de la función `func`, registra el mensaje de excepción y la traza de pila en el nivel crítico y luego vuelve a lanzar la excepción.
  - Devuelve el valor de retorno de la función `func` ejecutada.

**Variables Internas:**

- `__s`: Este es un objeto (callable) similar a una función privada definido usando una expresión lambda. Se utiliza para obtener la hora de inicio cuando se inicia el temporizador.
- `__e`: Este es otro objeto (callable) similar a una función privada definido usando una expresión lambda. Se utiliza para obtener la hora de finalización cuando se detiene el temporizador.

**Ejemplo de Uso:**

```python
from timer import timer

def mi_funcion(a, b):
  # Simular un trabajo en proceso
  time.sleep(1)
  return a + b

resultado = timer(mi_funcion, 5, 3)
print(resultado)  # Salida: 8
```

En este ejemplo, `timer` mide el tiempo de ejecución de `mi_funcion` y registra el inicio, el final y la duración de su ejecución. Luego ejecuta `mi_funcion` con los argumentos 5 y 3, y devuelve el resultado (que en este caso es 8). Si `mi_funcion` genera una excepción, `timer` registraría el error y luego volvería a lanzar la excepción.
