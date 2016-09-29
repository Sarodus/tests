from timeit import timeit

print timeit( "p = '1234567654321';p == p[::-1]" )
print timeit( "p = '1234567654321';x = len(p) / 2;p[:x] == p[:x:-1]" )
print timeit( "p = '1234567654321';''.join(reversed(p)) == p" )
