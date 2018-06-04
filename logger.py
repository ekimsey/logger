#!/usr/bin/python3

"""
Logger is a simple logging module for Python 3.
Copyright (C) 2018  Eric Kimsey

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# title           :Logger.py
# description     :Error/debug message logger.
# author          :Eric Kimsey
# usage           :
# notes           :
# python_version  :3.5+
# =======================================================================

import os
import datetime


def log_message(level: int, message: str) -> None:
    """
    Write error or debug message to the log file for today in the logs directory.
    :param int level: Level of message '0' for exception, '1' for debug
    :param str message: Message to be written to the log file
    :return None: Nothing
    """
    message = message.replace('"', '""')
    curr_datetime = datetime.datetime.now()
    filepath = 'logs/{0}_{1}_{2}.csv'.format(str(curr_datetime.year), str(curr_datetime.month), str(curr_datetime.day))
    append = os.path.isfile(filepath)
    log_file = open(filepath, 'a')
    if not append:
        log_file.write('Date:,Time:,Level:,Message:\n')

    # Date
    log_file.write('{0}-{1}-{2},'.format(str(curr_datetime.year), str(curr_datetime.month), str(curr_datetime.day)))
    # Time
    log_file.write('{0}:{1}:{2},'.format(str(curr_datetime.hour), str(curr_datetime.minute), str(curr_datetime.second)))
    # Level
    if level == 0:
        log_file.write('EXCEPTION')
    elif level == 1:
        log_file.write('DEBUG')
    log_file.write(',')

    # Message
    log_file.write('\"{0}\"\n'.format(message))
    log_file.close()
