from datetime import datetime, timezone


def datetime_utc_format(dt):
    return dt.replace(tzinfo=None).astimezone(tz=timezone.utc)

def format_datetime(date):
    return datetime.strptime(date, '%Y-%m-%d %I:%M %p')

def format_date(date):
    return datetime.strptime(date, '%Y-%m-%d').date()

def round_time(time):
    new_minute = time.minute + 1 if time.second >= 30 else time.minute
    return time.replace(second=0, microsecond=0, minute= new_minute)
