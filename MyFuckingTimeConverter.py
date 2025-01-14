from datetime import datetime
import pytz


def fuckingtimeconverterf(a):
    timestamp_ms = a
    timestamp_s = timestamp_ms / 1000
    thailand_tz = pytz.timezone('Asia/Bangkok')
    thailand_time = datetime.fromtimestamp(timestamp_s, tz=thailand_tz)
    return print(thailand_time)
