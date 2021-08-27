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


def cent_from_year(year):
    """ takes an integer and returns the matching century """
    if year == 0:
        return 1
    elif year < 0:
        return -(year - 1) // -100
    else:
        return (year - 1) // 100 + 1
