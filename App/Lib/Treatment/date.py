from datetime import datetime, timedelta, timezone

def format_date_to_compare(date: timedelta) -> str:
    tz = timezone(timedelta(hours=-5))
    time_24_with_tz = date.replace(tzinfo=tz)
    date_formated = time_24_with_tz.isoformat()
    return date_formated