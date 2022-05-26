import datetime as dt


def year(now):
    now = dt.datetime.now()
    return {'year': now.year}
