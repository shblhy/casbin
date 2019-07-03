from .default_logger import DefaultLogger

logger = DefaultLogger()


def set_logger(level, handler=None):
    """set log level and handler"""
    logger.set_logger(level, handler)


def get_logger():
    """returns the current logger."""
    return logger


def log_print(*v):
    """prints the log."""
    logger.write(*v)


def log_printf(fmt, *v):
    """prints the log with the format."""
    logger.writef(fmt, *v)
