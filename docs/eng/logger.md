## Documentation for logger/init.py

This file defines two classes, `__Logger` and `__LoggerSpecials`, which are used to log messages at different levels.

**Classes:**

- **\_\_Logger**
  - Responsible for creating and configuring a file handler for the logger.
  - Also initializes a logger with a specified log file and provides methods to log messages at different levels (debug, info, warning, error, and critical), including:
    - Logs a debug message (`debug(self, message: str)`)
    - Logs an info message (`info(self, message: str) -> None`)
    - Logs a warning message (`warning(self, message: str) -> None`)
    - Logs an error message (`error(self, message: str) -> None`)
    - Logs a critical message (`critical(self, message: str) -> None`)
- **\_\_LoggerSpecials**
  - This class provides methods to log specific messages, including:
    - Unexpected errors with relevant information (`unexpected_error`)
    - Errors related to absolute paths or files (`cannot_handle_absolute`)
    - Information about setting variable types (`type_set_to`)
    - Adding values to data structures (`adding_value_to`)
    - Function calls (`was_called`)
    - Setting variable values (`value_was_set`)

**Global Variables:**

- `logger`: An instance of the `__Logger` class that is used for general logging throughout the application.
- `logger_specials`: An instance of the `__LoggerSpecials` class that is used to log specific messages.

**Example Usage:**

```python
# Log an info message
logger.info("This is an informational message.")

# Log an unexpected error
logger_specials.unexpected_error("error", "parsing data", data_to_parse)

# Log that a function was called
logger_specials.was_called(func_name="my_function")
```

**Note:**

- The `__Logger`, `__LoggerSpecials` classes are private and not intended to be used directly outside of this module.
- The `logger_specials` class provides a more user-friendly way to log specific messages with additional context.

**Additional Notes:**

- The `logger` class uses the `logging` module to log messages to a file and the console. The default log file is `app.log` and the default logging level is `INFO`, which means that informational messages and higher will be logged to both the file and the console. You can change the log file and logging level by modifying the `logging` configuration in your application.
- The `logger_specials` class provides convenience methods for logging specific types of messages, such as unexpected errors, function calls, and variable assignments. These methods add additional context to the log messages, which can make it easier to debug and understand your application.
