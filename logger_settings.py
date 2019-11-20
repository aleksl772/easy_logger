class LoggerSettings(object):
    log_file_name: str = 'logfile.log'
    date_time_format: str = r'%Y-%b-%d %H:%M:%S'
    separator: str = ' '
    global_print_level: str = 'INFO'
    global_log_level: str = 'INFO'
    weight_level: dict = {
        'CRITICAL': 50,
        'ERROR': 40,
        'WARNING': 30,
        'INFO': 20,
        'DEBUG': 10,
    }
