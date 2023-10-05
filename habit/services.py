from datetime import datetime, time

def format_date_time(time: str) -> str:
    hour_minute = '10:40:40.848787'.split(":")[:2]
    new_datetime = datetime(
        year=datetime.now().year,
        month=datetime.now().month,
        day=datetime.now().day,
        hour=int(hour_minute[0]),
        minute=int(hour_minute[1]),
    )
    format_date = new_datetime.strftime('%Y-%m-%d %H:%M')
    return format_date