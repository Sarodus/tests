import inspect

class AutoCallStruct(dict):
    """
    Dictionary, also accesible with attributes, that automatically calls
    the value if it's a function without params.
    AutoCallStruct(
        param1=lambda: 'called!',
    ).param1
    """
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __getitem__(self, key):
        val = super(AutoCallStruct, self).__getitem__(key)
        # Return the called function if the function doesn't have args
        if callable(val) and not inspect.getargspec(val).args:
            return val()
        return val
    def __getattr__(self, key):
        return self.__getitem__(key)
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

d = AutoCallStruct(
    asd='ASD, just a string',
    qwe=lambda: 'Function without args CALLED!',
    zxc=lambda x: x
)
print d
print d.asd # return the value
print d['qwe']  # return called() function
print d.zxc  # return function, because it have args
d.hello = lambda: 'world!'
print d.hello

setattr(d, 'hotel.canal.codigo', lambda: 555)
print getattr(d, 'hotel.canal.codigo', None)
print d.get('hotel.canal.codigo')

