import datetime


def utc_rfc3339_string(dt):
    '''转化 datetime(UTC) 为 rfc3339 格式字符串'''

    if isinstance(dt, datetime.datetime):
        return dt.isoformat('T') + 'Z'

    return ''


def utc_rfc3339_parse(s):
    '''转化 rfc3339 (UTC) 格式字符串为 datetime'''

    if not s:
        return
    if s[-1].upper() != 'Z':
        return
    return datetime.datetime.strptime(s.rstrip('Zz'), '%Y-%m-%dT%H:%M:%S.%f')
