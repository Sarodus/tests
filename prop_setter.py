
class Cosa(object):
    @property
    def foo(self):
        if not hasattr(self, '_foo'):
            self._foo = 1
        return self._foo
    @foo.setter
    def foo(self, value):
        print 'Value changed!'
        self._foo = value

    @foo.deleter
    def foo(self):
        print 'Value deleted!'
        del self._foo

c = Cosa()
print c.foo
c.foo = 5
print c.foo
del c.foo
print c.foo
