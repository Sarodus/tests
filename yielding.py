
def source(i):
    print 'SOURCE CALL', i
    return i

# # # # # #

def cache_team_getter():
    results = {}
    def _get(i):
        if i not in results:
            results[i] = source(i) if i else None
        return results[i]
    def _getter(i=None):
        while 1:
            i = yield _get(i)
    g = _getter();g.next()
    return g


g = cache_team_getter()
print g.send(1)
print g.send(1)
print g.send(5)
print g.send(1)
print g.send(1)


print '----------'
print '----------'


def cache_team_getter():
    results = {}
    def get(i):
        if i not in results:
            results[i] = source(i) if i else None
        return results[i]
    return get


team_getter = cache_team_getter()
print team_getter(1)
print team_getter(2)
print team_getter(3)
print team_getter(1)
print team_getter(1)



def hola(a=''):
    while 1:
        a = yield a+'!!'

g = hola();g.next()
print g.send('Jordi')
print g.send('ASDASD')
print g.send('ASDASD')
print g.send('Jordi')
print g.send('QWE')
print g.send('Jordi')

