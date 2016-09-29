def select(query, structure):
    selector = structure
    for q in query.split('.'):

        if q.isdigit() and '__iter__' in dir(structure):
            try:
                structure = selector = structure[int(q)]
            except KeyError as e:
                structure = None

        elif 'get' in dir(structure):
            structure = selector = structure.get(q)

        else:
            structure = selector = None

        if structure is None:
            break

    return selector


print 'A)', select('a.x.456', {'a': {'x': 1}})
print 'B)', select('a.x', {'a': {'x': 1}})
print 'C)', select('a.z', {'a': {'x': 1}})
print 'D)', select('a.0', {'a': [1, 2, 3]})
print 'E)', select('a.2', {'a': [1, 2, 3]})
print 'F)', select('a', {'a': [1, 2, 3]})
