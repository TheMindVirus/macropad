# SPDX-FileCopyrightText: 2019 Dave Astels for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# pylint:disable=redefined-outer-name,consider-using-enumerate,no-self-use
# pylint:disable=invalid-name

import time

__version__ = "1.2.8"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Logger.git"


LEVELS = [
    (00, "NOTSET"),
    (10, "DEBUG"),
    (20, "INFO"),
    (30, "WARNING"),
    (40, "ERROR"),
    (50, "CRITICAL"),
]

for value, name in LEVELS:
    globals()[name] = value


def level_for(value):
    for i in range(len(LEVELS)):
        if value == LEVELS[i][0]:
            return LEVELS[i][1]
        if value < LEVELS[i][0]:
            return LEVELS[i - 1][1]
    return LEVELS[0][1]


class LoggingHandler:

    def format(self, level, msg):
        return "{0}: {1} - {2}".format(time.monotonic(), level_for(level), msg)

    def emit(self, level, msg):
        raise NotImplementedError()


class PrintHandler(LoggingHandler):
    def emit(self, level, msg):
        print(self.format(level, msg))


# The level module-global variables get created when loaded
# pylint:disable=undefined-variable

logger_cache = dict()
null_logger = None

# pylint:disable=global-statement
def getLogger(name):
    global null_logger
    if not name or name == "":
        if not null_logger:
            null_logger = NullLogger()
        return null_logger

    if name not in logger_cache:
        logger_cache[name] = Logger()
    return logger_cache[name]


# pylint:enable=global-statement

class Logger:
    def __init__(self):
        self._level = NOTSET
        self._handler = PrintHandler()

    def setLevel(self, value):
        self._level = value

    def getEffectiveLevel(self):
        return self._level

    def addHandler(self, hldr):
        self._handler = hldr

    def log(self, level, format_string, *args):
        if level >= self._level:
            self._handler.emit(level, format_string % args)

    def debug(self, format_string, *args):
        self.log(DEBUG, format_string, *args)

    def info(self, format_string, *args):
        self.log(INFO, format_string, *args)

    def warning(self, format_string, *args):
        self.log(WARNING, format_string, *args)

    def error(self, format_string, *args):
        self.log(ERROR, format_string, *args)

    def critical(self, format_string, *args):
        self.log(CRITICAL, format_string, *args)


class NullLogger:
    def __init__(self):
        pass

    def setLevel(self, value):
        pass

    def getEffectiveLevel(self):
        return NOTSET

    def addHandler(self, hldr):
        pass

    def log(self, level, format_string, *args):
        pass

    def debug(self, format_string, *args):
        pass

    def info(self, format_string, *args):
        pass

    def warning(self, format_string, *args):
        pass

    def error(self, format_string, *args):
        pass

    def critical(self, format_string, *args):
        pass
