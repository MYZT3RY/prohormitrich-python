
def time_left(unix_timestamp):
    seconds = unix_timestamp % (24 * 3600)
    hours = seconds // 3600 
    seconds %= 3600 
    minutes = seconds // 60 
    seconds %= 60
    
    result = ""

    if hours >= 1:
        result += "{0} ч. ".format(hours)
    if minutes >= 1:
        result += "{0} мин. ".format(minutes)
    
    result += "{0} сек. ".format(seconds)

    return result