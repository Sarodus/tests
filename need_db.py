def need_db(f):
    def wrapper(self, *args, **kwargs):
        self.db = True
        print f, self, args, kwargs
        return f(self, *args, **kwargs)
    return wrapper

class A(object):
    def __init__(self):
        self.db = False


    def connect(self):
        self.db = True

    @need_db
    def query(self):
        print 'QUERY', self.db


    @need_db
    def params(self, param1):
        print 'PARAMS', self.db
a = A()
a.query()
a.params(5)
a.connect()
a.query()
a.params(5)
