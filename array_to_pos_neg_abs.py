from timeit import timeit

"""Given set (also list in last) with positive and negative, return [ POSITIVES, abs(NEGATIVES) ]"""

a = set([1,2,3,4,5])
b = set([-74, -78])
c = set([])
d = set([4, 6, 8, -4, -10])

def get_where(arr):
    _in = set(i for i in arr if i > 0)
    return _in, map(abs, _in ^ arr)

print get_where(a)
print get_where(b)
print get_where(c)
print get_where(d)



print timeit(
setup='''
a = set([1,2,3,4,5])
b = set([-74, -78])
c = set([])
d = set([4, 6, 8, -4, -10])

def get_where(arr):
    _in = set(i for i in arr if i > 0)
    _ni = set(abs(i) for i in arr if i < 0)
    return _in, _ni
''',
stmt='''
get_where(a)
get_where(b)
get_where(c)
get_where(d)
''',
number=10000
)

print timeit(
setup='''
a = set([1,2,3,4,5])
b = set([-74, -78])
c = set([])
d = set([4, 6, 8, -4, -10])

def get_where(arr):
    _in = set(i for i in arr if i > 0)
    return _in, map(abs, _in ^ arr)
''',
stmt='''
get_where(a)
get_where(b)
get_where(c)
get_where(d)
''',
number=10000
)

print timeit(
setup='''
a = set([1,2,3,4,5])
b = set([-74, -78])
c = set([])
d = set([4, 6, 8, -4, -10])

def get_where(arr):
    _in  = set()
    _out = set()
    for i in arr:
        if i > 0:
            _in.add(i)
        else:
            _out.add(abs(i))
    return _in, _out
''',
stmt='''
get_where(a)
get_where(b)
get_where(c)
get_where(d)
''',
number=10000
)
