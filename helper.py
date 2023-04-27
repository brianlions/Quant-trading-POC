#!/usr/bin/env python3
import collections

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

def datafiles_info_v2():
    by_code = {}
    by_abbr = {}
    InfoCls = collections.namedtuple('DataInfo', 'code name abbr path first last'.split())
    with open('./datafiles/info.txt', encoding='utf8') as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith('AssetInfo'):
                continue
            fields = line.split()
            code   = fields[0][fields[0].find('{')+1:-1]
            name   = fields[1][:-1]
            abbr   = fields[2]
            first  = fields[-2]
            last   = fields[-1]
            file   = './datafiles/{}_{}_{}.xlsx'.format(code, first, last)
            by_code[code] = InfoCls(code, name, abbr, file, first, last)
            by_abbr[abbr] = InfoCls(code, name, abbr, file, first, last)
    return by_code, by_abbr

def chinese_font_setup():
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    plt.rcParams['axes.unicode_minus'] = False