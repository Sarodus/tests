from timeit import timeit

print timeit( "any((False, False, False, False, True, False))", number=10000000)
print timeit( "False or False or False or False or True or False", number=10000000)
