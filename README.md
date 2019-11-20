#### Easy logger (elogger) for easy logging

###### Requiremets:
python >= 3

###### First argument:
logging level (str).  
Two argument: printing enable (True or False, boolean).  
Others arguments: (str).  

###### Example:
from logger import logging

logging('INFO', True, 'args 1', 'args 2', 'args 3', 'info')  
logging('debug', True, 'args 2', 'args 2', 'args 3', 'debug')  
logging('debug', False, 'args 3', 'args 2', 'args 3', 'debug')  
logging('error', True, 'args 4', 'args 2', 'args 3', 'error')  
logging('critical', True, 'args 4', 'args 2', 'args 3', 'critical')  