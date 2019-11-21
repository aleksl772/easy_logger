from logger import logging, logging_info_prt, logging_debug, logging_error_prt

logging('INFO', True, 'args 1', 'args 2', 'args 3', 'args4_info')
logging('debug', True, 'args 1', 'args 2', 'args 3', 'args4_debug')
logging('debug', False, 'args 1', 'args 2', 'args 3', 'args4_debug')
logging('error', True, 'args 1', 'args 2', 'args 3', 'args4_error')
logging('critical', True, 'args 1', 'args 2', 'args 3', 'args4_critical')

logging_info_prt('args 1', 'args 2', 'args 3', 'args4_info')
logging_debug('args 1', 'args 2', 'args 3', 'args4_info')
logging_error_prt('args 1', 'args 2', 'args 3', 'args4_error')
logging_error_prt('args 1', 'args 2', 'args 3', 'args4_error')
