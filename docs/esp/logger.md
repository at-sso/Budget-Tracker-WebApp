## Documentación para logger/init.py

Este archivo define dos clases, `__Logger` y `__LoggerSpecials`, que se utilizan para registrar mensajes en diferentes niveles.

**Clases:**

- **\_\_Logger**
  - Se encarga de crear y configurar un manejador de archivos para el registrador.
  - También se encarga de inicializar un registrador con un archivo de registro especificado y proporciona métodos para registrar mensajes en diferentes niveles (depuración, información, advertencia, error y crítico), incluyendo:
    - Registra un mensaje de depuración (`debug(self, message: str)`).
    - Registra un mensaje informativo (`info(self, message: str) -> None`).
    - Registra un mensaje de advertencia (`warning(self, message: str) -> None`).
    - Registra un mensaje de error (`error(self, message: str) -> None`).
    - Registra un mensaje crítico (`critical(self, message: str) -> None`).
- **\_\_LoggerSpecials**
  - Esta clase proporciona métodos para registrar mensajes específicos, incluyendo:
    - Errores inesperados con información relevante (`unexpected_error`)
    - Errores relacionados con rutas absolutas o archivos (`cannot_handle_absolute`)
    - Información sobre cómo establecer tipos de variables (`type_set_to`)
    - Agregar valores a estructuras de datos (`adding_value_to`)
    - Llamadas a funciones (`was_called`)
    - Establecer valores de variables (`value_was_set`)

**Variables Globales:**

- `logger`: Una instancia de la clase `__Logger` que se utiliza para el registro general en toda la aplicación.
- `logger_specials`: Una instancia de la clase `__LoggerSpecials` que se utiliza para registrar mensajes específicos.

**Ejemplo de Uso:**

```python
# Registrar un mensaje informativo
logger.info("Este es un mensaje informativo.")

# Registrar un error inesperado
logger_specials.unexpected_error("error", "analizando datos", data_to_parse)

# Registrar que se llamó a una función
logger_specials.was_called(func_name="mi_función")
```

**Nota:**

- Las clases `__Logger`, `__LoggerSpecials` son privados y no estan destinados a usarse directamente fuera de este módulo.
- La clase `logger_specials` proporciona una forma más fácil de usar para registrar mensajes específicos con contexto adicional.
