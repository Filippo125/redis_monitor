intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),    # 60 * 1
    ('seconds', 1),
    )

def seconds_to_human_readable(seconds):
    result = []
    if seconds == 0:
        return "0"
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result)


suffixes = ['B', 'kB', 'MB', 'GB', 'TB', 'PB']
def bytes_to_human_readable(nb):
    i = 0
    while nb >= 1024 and i < len(suffixes)-1:
        nb /= 1024.
        i += 1
    f = ('%.2f' % nb).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])