from collections import namedtuple

class Color():
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return 'Color(red={s.red}, green={s.green}, blue={s.blue})'.format(s = self)

    def __add__(self, other):
        if isinstance(other, Color):
            return Color(self.red + other.red, self.green + other.green, self.blue + other.blue)
        return Color(0,0,0)


# CLASS
c = Color(240, 230, 50) + Color(5, 1, 2)
print c
print c.red
print c.green
print c.blue

# namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])
c = Color(240, 230, 50)
print c
print c.red, c[0]
print c.green, c[1]
print c.blue, c[2]

# tuple
c = (240, 230, 50)
print c
print c[0]
print c[1]
print c[2]
