from enum import Enum


class TimeUnit(Enum):
    """
    Represents a unit of time.

    Attributes:
        DAYS (str): Represents days as a unit of time.
        HOURS (str): Represents hours as a unit of time.
        MINUTES (str): Represents minutes as a unit of time.
    """
    DAYS = 'days'
    HOURS = 'hours'
    MINUTES = 'minutes'
