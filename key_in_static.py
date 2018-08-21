from timeit import timeit

setup = '''
from string import ascii_letters
key = 'X'
array = %s(ascii_letters)
'''

stmt = '''
key in array
'''

for array_type in (list, tuple, set, frozenset):
    print array_type.__name__,
    print timeit(
        setup=setup % array_type.__name__,
        stmt=stmt,
        number=10000000
    )
