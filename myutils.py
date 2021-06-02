import os
import sys

from datetime import datetime, timedelta
from dateutil.parser import parse
import pytz


def mydatetime():
    try:
        tz = pytz.timezone("US/Eastern")
        dt_utc = datetime.utcnow().isoformat()
        dt_local_tz = parse(dt_utc).astimezone(tz)
    
        return dt_local_tz

    except BaseException as e:
        pass
