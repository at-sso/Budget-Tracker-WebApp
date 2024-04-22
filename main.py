from src import app
from src.backend.logger import logger
import src.backend.timer as timer

if __name__ == "__main__":
    logger.debug(f"{ app } returned code: { timer.timer(app.run, debug=True) }")
