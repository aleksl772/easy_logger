import os
import datetime

from logger_settings import LoggerSettings


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
        msg_line = 'Empty'

    if printing and LoggerSettings.global_printing:
        print(msg_line)

    msg_line = '{}\n'.format(msg_line)

    if _check_weight_level(level):
        _save_to_disk(msg_line)


def _get_log_full_path(log_file_name: str) -> str:
    return os.path.join(os.getcwd(), log_file_name)


def _get_date_time():
    now = datetime.datetime.now()
    return now.strftime(LoggerSettings.date_time_format)


def _check_weight_level(level: str) -> bool:
    weight = LoggerSettings.weight_level.get(level.upper())
    global_weight = LoggerSettings.weight_level.get(
        LoggerSettings.global_log_level)
    return weight >= global_weight


def _save_to_disk(log_line: str):
    full_path = _get_log_full_path(LoggerSettings.log_file_name)
    with open(full_path, mode='a') as file:
        try:
            file.write(log_line)
        except:
            print('error write to file:', full_path, log_line)
