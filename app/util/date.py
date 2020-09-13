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


def last_week_day():
    """
    This method will return the last week day
    :return: The last week day
    """
    today = current_time()
    offset = max(1, (today.weekday() + 6) % 7 - 3)
    timedelta = datetime.timedelta(offset)
    most_recent = today - timedelta
    return most_recent
