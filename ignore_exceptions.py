# TODO, also act as decorator

class IgnoreExceptions:
    def __init__(self, *exceptions):
        self.exceptions = exceptions or Exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return isinstance(exc_value, self.exceptions)


with IgnoreExceptions():
    print 'Ignore Exceptions'
    raise IndexError('nope :v')

print 'yap, IndexError ignored'

with IgnoreExceptions(ValueError):
    print 'Ignore ValueError'
    raise ValueError('nope :v')

print 'yap, ValueError Ignored'

with IgnoreExceptions(IndexError, ValueError):
    print 'Ignore (IndexError, ValueError), but its TypeError, CRASH!!'
    raise TypeError('Crash, haha!')

# Realistic usage:
# def find_any_abc():
#     with IgnoreExceptions(Query.NotFound):
#         return Query.a
#     with IgnoreExceptions(Query.NotFound):
#         return Query.b
#     with IgnoreExceptions(Query.NotFound):
#         return Query.c
