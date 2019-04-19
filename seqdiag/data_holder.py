import time
from collections import defaultdict, deque, namedtuple
from functools import partial


_data = defaultdict(partial(deque, maxlen=4096))
_keys = []

def get_data():
    return _data


def get_keys():
    return _keys


def post(**kwargs):
    # print(kwargs) # for debug
    who = kwargs.get('who', 'anonymous')
    if who not in _keys:
        _keys.append(who)
    
    _data['who'].append(who)

    t_end_ms = time.time() * 1000
    elapsed_ms = float(kwargs.get('elapsed', 1)) * 1000
    t_start_ms = t_end_ms - elapsed_ms

    _data['t_start_ms'].append(t_start_ms)
    _data['t_end_ms'].append(t_end_ms)

    _func = str(kwargs.get('func','?'))
    _in = str(kwargs.get('in',''))
    _out = str(kwargs.get('out',''))
    
    
    _data['func'].append(_func)
    _data['in'].append(_in)
    _data['out'].append(_out)
    
    _data['msg'].append(str(kwargs))
    
# example
post(who='LogServer',func='initialize')
