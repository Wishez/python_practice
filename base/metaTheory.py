MetaTest = type('M', (), {})
class M(type):
    pass

class Complex(metaclass=M):
    pass
print(M.__class__, Complex.__class__)