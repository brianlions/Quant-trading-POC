#!/usr/bin/env python3
import collections
import time

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
            abbr   = fields[2][:-1]
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

class StopWatch(object):
    def __init__(self):
        self._start_time = time.time()
        self._stop_time = None
        self._last_check_time = None

    def start(self):
        self._start_time = time.time()
        self._stop_time = None
        self._last_check_time = None

    def stop(self):
        self._stop_time = time.time()

    def elapse_time(self):
        '''Note: return value will not change if stopped.'''

        if not self._stop_time:
            return time.time() - self._start_time
        else:
            return self._stop_time - self._start_time

    def delta_time(self):
        '''Note: return value will not change if stopped.'''

        if not self._stop_time:
            now = time.time()
            if not self._last_check_time:
                delta = now - self._start_time
            else:
                delta = now - self._last_check_time
            self._last_check_time = now
            return delta
        elif self._last_check_time:
            return self._stop_time - self._last_check_time
        else:
            return self._stop_time - self._start_time