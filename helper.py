#!/usr/bin/env python3

def datafiles_info():
    res = {}
    with open('./datafiles/info.txt', encoding='utf8') as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith('AssetInfo'):
                continue
            p1 = line.find('{')
            p2 = line.find(',', p1+1)
            p3 = line.find(',', p2+1)
            code = line[p1+1:p2]
            name = line[p2+2:p3]
            res[code] = name
    return res