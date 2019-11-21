import os
import datetime

from logger_settings import LoggerSettings


def logging_debug(*args):
    logging('DEBUG', False, *args)


def logging_info(*args):
    logging('INFO', False, *args)


def logging_warning(*args):
    logging('WARNING', False, *args)


def logging_error(*args):
    logging('ERROR', False, *args)


def logging_critical(*args):
    logging('CRITICAL', False, *args)


def logging_debug_prt(*args):
    logging('DEBUG', True, *args)


def logging_info_prt(*args):
    logging('INFO', True, *args)


def logging_warning_prt(*args):
    logging('WARNING', True, *args)


def logging_error_prt(*args):
    logging('ERROR', True, *args)


def logging_critical_prt(*args):
    logging('CRITICAL', True, *args)


def logging(level='INFO', printing=False, *args):
    if args:
        msg_line = _get_date_time() + '{separator}{level}'.format(
            separator=LoggerSettings.separator,
            level=level.upper()
        )
        for one in args:
            msg_line = msg_line + '{separator}{arg}'.format(
                separator=LoggerSettings.separator,
                arg=one
            )
    else:
        msg_line: str = 'Empty'

    if printing and _check_weight_level(level, 'print'):
        print(msg_line)

    msg_line = '{}\n'.format(msg_line)

    if _check_weight_level(level, 'log'):
        _save_to_disk(msg_line)


def _get_log_full_path(log_file_name: str) -> str:
    return os.path.join(os.getcwd(), log_file_name)


def _get_date_time() -> str:
    now = datetime.datetime.now()
    return now.strftime(LoggerSettings.date_time_format)


def _check_weight_level(level: str, action: str) -> bool:
    act_dict: dict = {
        'log': LoggerSettings.global_log_level,
        'print': LoggerSettings.global_print_level,
    }
    weight: int = LoggerSettings.weight_level.get(level.upper())
    global_weight: int = LoggerSettings.weight_level.get(
        act_dict.get(action))
    return weight >= global_weight


def _save_to_disk(log_line: str):
    full_path = _get_log_full_path(LoggerSettings.log_file_name)
    with open(full_path, mode='a') as file:
        try:
            file.write(log_line)
        except Exception as e:
            print('error write to file:', full_path, log_line, e)
