import time
from collections import defaultdict, deque, namedtuple
from functools import partial


_data = defaultdict(partial(deque, maxlen=1024))
_keys = []

def get_data():
    return _data


def get_keys():
    return _keys


def post(**kwargs):

    who = kwargs.get('who', 'anonymous')
    if who not in _keys:
        _keys.append(who)
    
    _data['who'].append(who)

    t_start_ms = time.time() * 1000
    _data['t_start_ms'].append(t_start_ms)
    _data['t_end_ms'].append(t_start_ms+500)

    _data['msg'].append(repr(kwargs))
    
# example
post(who='LogServer',msg='initialized')
