```python
import os
import sys
from datetime import datetime
```

These lines import necessary modules: `os`, `sys`, and `datetime`. They are used for interacting with the operating system, handling system-specific parameters and functions, and working with dates and times, respectively.

```python
CURRENT_PATH: str = os.path.abspath(os.path.dirname(sys.argv[0])).replace("\\", "/")
```

This line retrieves the absolute path of the directory where the Python script is currently executing (`sys.argv[0]` represents the script's filename), and then converts backslashes to forward slashes (`\` to `/`). It assigns this path to the variable `CURRENT_PATH`.

```python
SOURCE_FOLDER: str = f"{CURRENT_PATH}/src"
```

Here, `SOURCE_FOLDER` is defined as the path to the "src" folder relative to the `CURRENT_PATH`.

```python
LOGGER_FOLDER_PATH: str = f"{CURRENT_PATH}/log"
```

Similar to the previous line, `LOGGER_FOLDER_PATH` is set as the path to the "log" folder relative to `CURRENT_PATH`.

```python
LOGGER_FILE: str = (
    f"{LOGGER_FOLDER_PATH}/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
)
```

This line defines `LOGGER_FILE` as the path to the log file, which includes the timestamp of when the script was executed. The `strftime` function of `datetime.now()` is used to format the current date and time as per the specified format (`'%Y-%m-%d-%H-%M-%S'`, representing Year-Month-Day-Hour-Minute-Second), and this timestamp is appended to the path.

The comments provided above each variable assignment provide additional context and notes for users about the purpose and potential considerations when using these paths.

Overall, this code snippet sets up paths for source files and logging, utilizing system-specific functionality and current date and time to ensure unique file naming.

[Go back](../index.md)
