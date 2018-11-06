from datetime import date


def format_datetime(value: date):
    week_list = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    return value.strftime('%Y/%m/%d, ({})').format(week_list[value.weekday()])
