__all__ = ["timer"]

import time
import traceback
from typing import Any, Callable

from .logger import *

# The code snippet `__s: Callable[[], float] = lambda: time.time()` and
# `__e: Callable[[], float] = lambda: time.time()` is defining placeholder
# lambdas for the start and end timer functions.
__s: Callable[[], float] = lambda: time.time()
__e: Callable[[], float] = lambda: time.time()


def __handle_end_timer(start: float, func: Callable[..., Any]) -> None:
    """
    The function `__handle_end_timer` logs the execution time of a given function based on the start and
    end timestamps.

    @param start The `start` parameter is the start timestamp of the timer, indicating when the timer
    was initially started.
    @param func The `func` parameter in the `__handle_end_timer` function is a callable that represents
    the function being executed. It can be any function that can be called with any number of arguments
    and returns a value of any type.
    """
    end: float = __e()
    logger.debug(f"Operation: {func}, took: { abs(start - end) } ms.")


def timer(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    The `timer` function executes a given callable function, measures its execution time, logs the
    duration, and handles any unhandled exceptions.

    @param func The `func` parameter in the `timer` function is a callable function that you want
    to execute. It can be any function that you define in your code or a built-in function. When calling
    `timer`, you pass this function as the first argument.
    @param *args Positional arguments for the function.
    @param **kwargs Keyword arguments for the function.

    @return The `timer` function returns the return value of the callable function `func` that is
    being executed.
    """
    start: float = __s()
    func_val: Any = None
    logger.info(f"Operation: {func}, started.")

    try:
        func_val = func(*args, **kwargs)
    except Exception:
        __handle_end_timer(start, func)
        logger.critical(
            f"Unhandled exception raised in {func}:\n{ traceback.format_exc() }"
        )
        raise

    __handle_end_timer(start, func)
    return func_val
