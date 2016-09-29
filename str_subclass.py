
class STR(str):

    translations = {
        'asd' : 'A ese de',
    }

    def __add__(self, other):
        return STR('%s%s' % (self, other))

    def __pos__(self):
        return STR(self.upper())

    def __neg__(self):
        return STR(self.lower())

    def __invert__(self):
        return STR(self.translations.get(-self, self))


print +STR('ASD')
print -STR('ASD')
print +STR('asd') + -STR('QWE')
print ~STR('ASD')
