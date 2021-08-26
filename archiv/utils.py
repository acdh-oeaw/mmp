import re


def parse_date(input, default=1):
    dates = (re.findall(r'\d+', input), input)[0]
    try:
        date_str = dates[0]
    except IndexError:
        date_str = default
    try:
        out = int(date_str)
    except (ValueError, TypeError):
        out = default
    return out
