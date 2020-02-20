import datetime
import os

d = {}

path = "./"

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)
        dir(entry)
        d[entry.name] = {'filesize': entry.stat().st_size,
                         'lastmodified': datetime.datetime.fromtimestamp(entry.stat().st_mtime).strftime('%c')}

    for value, key in d.items():
        print(value)
        for a, b in key.items():
            print(a, b)

            #  entry.is_file()
            #  entry.name
            #  entry.stat()
            #  import datetime
            #  datetime.datetime.fromtimestamp()
