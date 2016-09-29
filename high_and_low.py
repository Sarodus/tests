from timeit import timeit

"""Given space separated numbers, return biggest and lower"""


print timeit(
setup='''
def high_and_low(numbers):
    nn = [int(s) for s in numbers.split()]
    return "%i %i" % (max(nn),min(nn))
''',
stmt='''
high_and_low('20 30 40 50 60 70 80 90 100 -10 -20 -30 -40')
''',
number=100000
)


print timeit(
setup='''
def high_and_low(numbers):
    n = sorted(map(int, numbers.split()))
    return '%s %s' % (n[-1], n[0])
''',
stmt='''
high_and_low('20 30 40 50 60 70 80 90 100 -10 -20 -30 -40')
''',
number=100000
)
