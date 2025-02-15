a = {
    'a': 1,
    'b': 2,
    'c': None,
    'd': [1, 2, 3],
    'e': {
        'a': 1,
        'b': 2,
        'c': None,
        'd': [1, 2, 3],
    },
    "f": 'This is a string',
    'g': [True, False, None],
    'h': False
}

import json

_j = json.dumps(a)
_a = json.loads(_j)

for k, v in a.items():
    assert a[k] == _a[k]

for k, v in _a.items():
    assert a[k] == _a[k]

b = [1, 2, True, None, False]

_j = json.dumps(b)
_b = json.loads(_j)

assert b == _b

c = 1.0
_j = json.dumps(c)
_c = json.loads(_j)
assert c == _c

d = True
_j = json.dumps(d)
_d = json.loads(_j)
assert d == _d