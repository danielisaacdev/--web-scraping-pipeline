import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = "app.log", level=logging.INFO):
    """
    Configura un logger profesional con rotación de archivos y salida a consola.
    """
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
    )

    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    # Handler para archivo con rotación (10MB por archivo, max 5 archivos)
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
