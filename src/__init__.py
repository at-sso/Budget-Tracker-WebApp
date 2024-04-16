from .logger import *
from .api_handler import *


def main() -> int:
    "Main function."
    WEBAPP.run(debug=True)
    return 0
