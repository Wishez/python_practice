class defaultdict(dict):
    def __init__(self, default=None):
        self.default = default
        super().__init__()

    def __getitem__(self, item):
        if item in self:
            return dict.__getitem__(self, item)
        else:
            return self.default
    def get(self, key, *args):
        if not args:
            args = (self.default,)
        return dict.get(self, key, *args)
    def merge(self, other):
        for key in other:
            if key not in self:
                self[key] = other[key ]

class defaultdict2(dict):
    __slots__ = ['default',]
    def __init__(self, default=None):
        self.default = default
        super().__init__()

    def __getitem__(self, item):
        if item in self:
            return dict.__getitem__(self, item)
        else:
            return self.default
    def get(self, key, *args):
        if not args:
            args = (self.default,)
        return dict.get(self, key, *args)
    def merge(self, other):
        super().merge(self, other)

class defaultdict3(defaultdict2):
    __slots__ = ['x', 'default']

    def __init__(self, default=None, x=None):
        self.x = x
        super().__init__(default)


if __name__ == "__main__":
    smp_d = {
        'batman': 'Bruce Wane',
        'superman': 'Clark Kent',
        'developer': 'Philipp Zhuravlev'
    }
    d = defaultdict('Default')
    d.merge(smp_d)

    print(d.keys())
    d.x1 = 100
    d.x2 = 300
    print('first dict ===>\n', d.__dict__.keys(), d.__dict__)

    # I've set __slot__ property, but i can initial classes.
    d_1 = defaultdict2('-1')
    d_2 = defaultdict3('hello', 'x')

    d_b = defaultdict('Old boy')
    print('__getattribute__', d_b.__getattribute__('default'))

    print('dict 1 ===>\n', d_1.__slots__, d_1.default,)
    print('dict 2 ====>\n', d_2.keys(), d_2[1], d_2.x)
    print('metaclass', d_2.__class__.__class__)


