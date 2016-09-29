class Factory(type):
    def __getattr__(cls, key):
        return getattr(cls(), key)

    def __call__(cls):
        return cls._get_cls(cls._get_brand())

    @staticmethod
    def _get_brand():
        return 'km'
        return 'bb'

    def __repr__(self):
        return '<PromoFactory brand=%s>' % self._get_brand()


class Promo:
    __metaclass__ = Factory

    @staticmethod
    def _get_cls(brand):
        return {
            'km': PromoKM
        }.get(brand, PromoBB)




class PromoBB(object):
    asd = 1

    @classmethod
    def func(cls, id):
        return '%s%s' % (cls, id)



class PromoKM(object):
    asd = 2

    @classmethod
    def func(cls, id):
        return '%s%s' % (cls, id)



print Promo
print Promo()
print Promo.asd
print Promo.func(5)
