```python
import os
import sys
from datetime import datetime
```

Estas líneas importan los módulos necesarios: `os`, `sys` y `datetime`. Se utilizan para interactuar con el sistema operativo, manejar parámetros y funciones específicas del sistema, y trabajar con fechas y horas, respectivamente.

```python
CURRENT_PATH: str = os.path.abspath(os.path.dirname(sys.argv[0])).replace("\\", "/")
```

Esta línea obtiene la ruta absoluta del directorio donde se está ejecutando el script de Python (`sys.argv[0]` representa el nombre del archivo del script), y luego convierte las barras invertidas en barras inclinadas (`\ a /`). Asigna esta ruta a la variable `CURRENT_PATH`.

```python
SOURCE_FOLDER: str = f"{CURRENT_PATH}/src"
```

Here, `SOURCE_FOLDER` is defined as the path to the "src" folder relative to the `CURRENT_PATH`.

```python
LOGGER_FOLDER_PATH: str = f"{CURRENT_PATH}/log"
```

Similar a la línea anterior, `LOGGER_FOLDER_PATH` se establece como la ruta a la carpeta "log" en relación con `CURRENT_PATH`.

```python
LOGGER_FILE: str = (
    f"{LOGGER_FOLDER_PATH}/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
)
```

Esta línea define `LOGGER_FILE` como la ruta al archivo de registro, el cual incluye la marca de tiempo de cuándo se ejecutó el script. Se utiliza la función `strftime` de `datetime.now()` para dar formato a la fecha y hora actuales según el formato especificado (`'%Y-%m-%d-%H-%M-%S'`, que representa Año-Mes-Día-Hora-Minuto-Segundo), y esta marca de tiempo se agrega a la ruta.

Los comentarios proporcionados encima de cada asignación de variable brindan contexto adicional y notas para los usuarios sobre el propósito y consideraciones potenciales al usar estas rutas.

En general, este fragmento de código configura las rutas para los archivos fuente y de registro, utilizando funcionalidad específica del sistema y la fecha y hora actuales para garantizar nombres de archivo únicos.

[Ir atrás](../index.md)
