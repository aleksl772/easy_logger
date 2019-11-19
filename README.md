Easy logger (elogger) for easy logging

examples:
from logger import logging

logging('critical', True, 'args 4', 'args 2', 'args 3', 'critical')

settings:
global_printing - disable all print

First argument: logging level (str).
Two argument: printing enable (True or False, boolean).
Others arguments (str)