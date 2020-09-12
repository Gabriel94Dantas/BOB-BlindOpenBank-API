"""
    This module is responsible to deal with dates
"""

import datetime


def current_time():
    """
    This method will return the current time
    :return: current time
    """
    return datetime.datetime.now()


def add_minutes(date_parameter, minutes):
    """
    This method will return the date_parameter plus minutes in time format
    :param date_parameter: date parameter
    :param minutes: how many minutes to plus to date parameter
    :return: date_parameter + minutes
    """
    new_date = date_parameter + datetime.timedelta(minutes=minutes)
    return new_date
