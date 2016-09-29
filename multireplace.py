import re
from timeit import timeit

print timeit(
setup='''
def _multiple_replace(string, **kwargs):
    return reduce(lambda a, kv: a.replace(*kv), kwargs.iteritems(), string)
''',
stmt='''
_multiple_replace('hello, world', hello = 'goodbye', world = 'earth')
''',
number=100000
)

def _multiple_replace(string, **kwargs):
    return reduce(lambda a, kv: a.replace(*kv), kwargs.iteritems(), string)
print _multiple_replace('hello, world', hello = 'goodbye', world = 'earth')

print '===================='
# # # # # # # # # #
print timeit(
stmt='''
'hello, world'.replace('hello', 'goodbye').replace('world', 'earth')
''',
number=100000
)

print 'hello, world'.replace('hello', 'goodbye').replace('world', 'earth')

print '===================='
# # # # # # # # # #
print timeit(
setup='''
import re
def _rereplace(string, **kwargs):
    rep = dict((re.escape(k), v) for k, v in kwargs.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], string)
''',
stmt='''
_rereplace('hello, world', hello = 'goodbye', world = 'earth')
''',
number=100000
)

def _rereplace(string, **kwargs):
    rep = dict((re.escape(k), v) for k, v in kwargs.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    return pattern.sub(lambda m: rep[re.escape(m.group(0))], string)

print _rereplace('hello, world', hello = 'goodbye', world = 'earth')


print '===================='
print timeit(
setup='''
def _rrrr(string, **kwargs):
    for k,v in kwargs.iteritems():
        string = string.replace(k, v)
    return string
''',
stmt='''
_rrrr('hello, world', hello = 'goodbye', world = 'earth')
''',
number=100000
)

def _rrrr(string, **kwargs):
    for k, v in kwargs.iteritems():
        string = string.replace(k, v)
    return string

print _rrrr('hello, world', hello = 'goodbye', world = 'earth')

