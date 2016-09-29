from itertools import cycle, islice

c = cycle(('odd', 'even', 'moar'))
c = cycle('\\/')

for _ in range(0, 10):
    for r in islice(c, 20):
        print r,
    print

print

for r in islice(c, 10):
    print ('%s ' % r) * 20
