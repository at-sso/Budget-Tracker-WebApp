__all__ = ["logger", "logger_specials"]

import logging as _logging
import os as _os
import traceback as _traceback
from typing import Callable, Dict, Any, Tuple, List

from src import const


class __Logger:
    def __init__(self) -> None:
        """
        The function initializes a logger with a specified log file and logs a message indicating the
        logger has started.
        """
        self.__log_file: str = const.LOGGER_FILE
        self.__log_path: str = const.LOGGER_FOLDER_PATH
        self.__logger: _logging.Logger = _logging.getLogger(__name__)
        self.__logger.setLevel(_logging.DEBUG)
        self.__start_logger()
        self.info("Logger started.")

    def __start_logger(self) -> None:
        """
        The function `__start_logger` sets up a file logger.
        """
        # Ensure the directory exists
        logger_directory: str = _os.path.dirname(self.__log_file)
        if not _os.path.exists(logger_directory):
            _os.makedirs(logger_directory)

        # Delete the oldest files.
        files: List[str] = _os.listdir(self.__log_path)
        if not len(files) < 10:
            logger_amount: int = max((len(files)) // 10, 1)
            files_to_delete: List[str] = files[: len(self.__log_path) - logger_amount]
            for file_name in files_to_delete:
                file_path: str = _os.path.join(self.__log_path, file_name)
                _os.remove(file_path)

        # Create a file handler
        logger_handler = _logging.FileHandler(self.__log_file, mode="w")

        # Create a formatter and set the formatter for the handler
        formatter = _logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        logger_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.__logger.addHandler(logger_handler)

    def debug(self, message: str):
        """
        The function `debug` logs a debug message using a logger message handler.

        @param message The `message` parameter in the `debug` method is a string that represents the
        message to be logged at the 'DEBUG' level.
        """
        self.__logger.debug(message)

    def info(self, message: str) -> None:
        """
        This function logs an informational message using a logger message handler.

        @param message The `message` parameter in the `info` method is a string that represents the
        message to be logged at the 'INFO' level.
        """
        self.__logger.info(message)

    def warning(self, message: str) -> None:
        """
        The `warning` function logs a warning message using a logger message handler.

        @param message The `message` parameter in the `info` warning is a string that represents the
        message to be logged at the 'WARNING' level.
        """
        self.__logger.warning(message)

    def error(self, message: str) -> None:
        """
        The function `error` logs an error message using a logger message handler.

        @param message The `message` parameter in the `error` method is a string that represents the
        message to be logged at the 'ERROR' level.
        """
        self.__logger.error(message)

    def critical(self, message: str) -> None:
        """
        This function logs a critical message using a logger message handler.

        @param message The `message` parameter in the `critical` method is a string that represents the
        message to be logged at the 'CRITICAL' level.
        """
        self.__logger.critical(message)


logger = __Logger()
"""
This instance is used for logging messages at different levels such as debug, 
info, warning, error, and critical.
"""


class __LoggerSpecials:
    def __init__(self) -> None:
        """
        The function initializes a dictionary mapping log levels to corresponding logger functions.
        """
        self.__logger_level: Dict[str, Callable[[str], None]] = {
            "debug": lambda arg: logger.debug(arg),
            "info": lambda arg: logger.info(arg),
            "warn": lambda arg: logger.warning(arg),
            "err": lambda arg: logger.error(arg),
            "crit": lambda arg: logger.critical(arg),
        }

    def __handle_logger_message(self, key: str, message: str) -> None:
        """
        This function handles logging of error messages at different levels based on a specified key.

        @param key The `key` parameter in the `__handle_logger_message` function is a string
        representing the logging level at which the error message should be logged.
        @param message The `message` parameter in the `__handle_logger_message` function represents the
        error message that needs to be logged at a specific logging level.

        @return It will return the result of `self.logger_level.get(key.lower(), logger.debug)(message)`.
        """
        return self.__logger_level.get(key.lower(), logger.debug)(message)

    def from_specific(
        self,
        name: str = "",
        func: str = "",
        func_args: Tuple[Any, ...] | str = "",
        message: Any | str = "",
    ) -> None:
        """
        This function logs a custom message with specific information.

        @param key The `key` parameter in the `from_specific` function is used to specify the logging
        level for the message being logged. It is a string that indicates the severity or type of the
        log message (e.g., INFO, WARNING, ERROR).
        @param function The `function` parameter in the `from_specific` method refers to the function
        that produced the error or the function from which the custom message is being logged.
        @param message The `message` parameter in the `from_specific` function is a string that
        represents the message to be logged. It is the information or content that you want to include
        in the log message when this function is called.
        """
        format_msg: str = (
            f"FROM: {'' if name == '' else f'{name}.'}{func}({func_args})"
            + (f", {message}" if message != "" else "")
        )
        self.__handle_logger_message("debug", format_msg)

    def unexpected_error(self, error_type: str, item: Any) -> None:
        """
        The function `unexpected_error` logs an unexpected error with relevant information.

        @param key The `key` parameter in the `unexpected_error` function is used to specify the logging
        level for the error message. It is a string parameter that indicates the severity or type of the
        log message to be recorded.
        @param error_type The `error_type` parameter in the `unexpected_error` function represents the
        type of the unexpected error that occurred. This could be a description of the nature or
        category of the error, such as "handling", "formatting", "modifying", etc. It helps in
        identifying and categorizing the error.
        @param item The `item` parameter in the `unexpected_error` function represents the item
        associated with the unexpected error. It could be any relevant information or object that is
        related to the error that occurred. When calling this function, you would pass the specific item
        that caused the error as an argument to this parameter.
        Example:
        ------------------------------------------------------------------------------------------------
        When the method is called as for example:
        logger_specials.unexpected_error("crit", "handling", value)

        The message will be formatted as:
        ```log
        2024-04-14 18:58:46 - CRITICAL An unexpected error occurred while handling 'value':
        Traceback (most recent call last):
          {...}
        TypeError: {...}
        ```
        """
        format_msg: str = (
            f"An unexpected error occurred while {error_type} '{item}':\n{_traceback.format_exc()}"
        )
        self.__handle_logger_message("err", format_msg)

    def cannot_handle_absolute(
        self,
        error_type: str,
        absolute_path: str,
        is_exc: bool = False,
        is_file: bool = True,
    ) -> None:
        """
        The function `cannot_handle_absolute` logs an error related to an absolute path or file.

        @param key The `key` parameter in the `cannot_handle_absolute` method is used to specify the
        logging level for the error message. It is a string that indicates the severity or category of
        the error being logged.
        @param error_type The `error_type` parameter in the `cannot_handle_absolute` method represents
        the type of the error that occurred. It is a string that describes the nature or category of the
        error that is being logged.
        @param absolute_path The `absolute_path` parameter in the `cannot_handle_absolute` method
        represents the absolute path or file associated with the error being logged. It is a string that
        should contain the full path to the file or directory that is causing the error.
        @param is_exc The `is_exc` parameter in the `cannot_handle_absolute` method is a boolean flag
        that indicates whether the method is being called within a try-catch block. If `is_exc` is
        `True`, it means that an exception has occurred and the method should include additional
        information in the error message.
        @param is_file The `is_file` parameter in the `cannot_handle_absolute` method is a boolean flag
        that indicates whether the absolute path provided is related to a file. It defaults to `True`,
        meaning that if not specified, the method assumes the absolute path is related to a file.
        """
        format_msg: str = f"{'File ' if is_file else ''}{error_type}: '{absolute_path}'"
        format_msg += (
            f"\n\t^ Unexpected error occurred while {error_type}, {absolute_path}:\n{_traceback.format_exc()}"
            if is_exc is not False
            else ""
        )
        self.__handle_logger_message("err", format_msg)

    def type_set_to(self, datatype: Any, type_name: str) -> None:
        """
        This function logs the type of a variable being modified along with a descriptive name for the
        type.

        @param datatype datatype is the variable whose type is being set.
        @param type_name The `type_name` parameter is a string that serves as a descriptive name for the
        type of the variable being modified. It is used in the log message to provide additional context
        about the type being set.
        """
        self.__handle_logger_message(
            "warn",
            f"Type {type(datatype).__name__}, {type_name}, was set to: {datatype}",
        )

    def adding_value_to(
        self, value: Any, value_name: str, data: Any, data_name: str
    ) -> None:
        """
        The function `adding_value_to` logs a message about adding a value to a data structure.

        @param value The `value` parameter in the `adding_value_to` method represents the actual value
        that is being added to a data structure. It can be of any data type (`Any`) as indicated in the
        type hint.
        @param value_name The `value_name` parameter is a descriptive name for the value being added to
        a data structure. It helps provide context and clarity about the value being added.
        @param data The `data` parameter in the `adding_value_to` method represents the data structure
        to which the `value` is being added. It could be a list, dictionary, set, or any other data
        structure depending on the context in which this method is used.
        @param data_name The `data_name` parameter in the `adding_value_to` method is a descriptive name
        for the data structure to which the value is being added. It helps provide context and clarity
        in the log message that is generated when a value is added to the data structure.
        """
        self.__handle_logger_message(
            "info",
            f"Adding {type(value).__name__}, {value_name} to the {type(data).__name__}, {data_name}.",
        )

    def was_called(
        self, name: str = "", func_name: str = "", key: str = "warn", init: str = ""
    ) -> None:
        """
        The function was_called is responsible for logging a message indicating that a specific function
        was called. It accepts parameters name, func_name, key, and init. If provided, name
        indicates the name of the function, func_name represents the name of the called function,
        key specifies the logging level, and init denotes the initialization point. If name is
        provided, it is used in the message; otherwise, init is used.

        @param name The name parameter represents the name of the function being called. If provided, it
        is used in the log message.
        @param func_name The func_name parameter specifies the name of the called function.
        @param key The key parameter indicates the logging level for the message.
        @param init The init parameter represents the initialization point if name is not provided.
        """
        self.__handle_logger_message(
            key,
            f"The function '{func_name}' was called. "
            f"Init point: {name if name != '' else init}.",
        )

    def value_was_set(
        self,
        value_name: str,
        value: Any = None,
        callabe: Callable[..., Any] = object,
    ) -> None:
        """
        The function value_was_set logs a debug message indicating that a value has been set. It takes
        parameters value_name, value, and callable. value_name specifies the name of the value
        being set, value represents the value itself, and callable denotes the initialization call.
        If value is not None, its type is included in the log message.

        @param value_name The value_name parameter specifies the name of the value being set.
        @param value The value parameter represents the value being set. If provided, its type is
        included in the log message.
        @param callable The callable parameter denotes the initialization call.
        """
        self.__handle_logger_message(
            "debug",
            f"Value {value_name}, was set to {value}."
            + (f" Type: ({type(value).__name__})." if value != None else "")
            + f" Initialization call: '{callabe.__name__}'.",
        )


logger_specials = __LoggerSpecials()
"""
This instance is used for logging special messages at specified levels, which is used to
handle special or specific logging messages.
"""
