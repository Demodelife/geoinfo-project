from datetime import datetime
import pytz


def get_difference_tzs(tmz_1: str, tmz_2: str) -> str:
    """
    Function to get difference between time zones.
    Returns difference in hours.
    """

    offset_1 = pytz.timezone(tmz_1).utcoffset(datetime.utcnow())
    offset_2 = pytz.timezone(tmz_2).utcoffset(datetime.utcnow())

    if offset_2 > offset_1:
        return f'-{abs(offset_1 - offset_2)}'
    else:
        return f'+{abs(offset_1 - offset_2)}'
