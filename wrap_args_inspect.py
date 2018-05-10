import inspect
from itertools import izip, chain


def ins(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper


@ins
def function(a, b=2, c=3):
    print 'LOCALS    ', locals()


args = (1, 5)

function(*args)

i = inspect.getargspec(function)

if i.defaults:
    result = dict(
        chain(
            izip(reversed(i.args), reversed(i.defaults)),
            izip(i.args, args)
        )
    )
else:
    result = dict(izip(i.args, args))

print 'CALCULATED', result


