from .logger import Logger
import logging

logger = logging.getLogger('casbin')


class DefaultLogger(Logger):
    """the implementation for a Logger using logging."""

    enable = False

    def enable_log(self, enable):
        """controls whether print the message."""
        self.enable = enable
        self.set_logger()

    def is_enabled(self):
        """returns if logger is enabled."""
        return self.enable

    def write(self, *v):
        """formats using the default formats for its operands and logs the message."""
        if self.enable:
            s = ""
            for vv in v:
                s = s + str(vv)
            logger.info(s)

    def writef(self, fmt, *v):
        """formats according to a format specifier and logs the message."""
        if self.enable:
            logger.info(fmt, *v)

    def set_logger(self, log_level=logging.INFO, handler=None):
        logger.setLevel(log_level)
        if handler is None:
            handler = logging.StreamHandler()
            fmt = "%(asctime)s - %(levelname)s - %(message)s"
            formatter = logging.Formatter(fmt)
            handler.setFormatter(formatter)
        logger.addHandler(handler)