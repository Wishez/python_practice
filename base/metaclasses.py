

class autoprop(type):
    def __init__(cls, name, bases, dict):
        super(autoprop, cls).__init__(name, bases, dict)
        props = {}
        print('init metaclass')
        for member in dict.keys():
            if member.startswith("_get_") or member.startswith("_set_"):
                print(props)
                print(props[member[5:]])
                print(member)
                props[member[5:]] = 1
        for prop in props.keys():
            fget = getattr(cls, "_get_%s" % prop, None)
            fset = getattr(cls, "_set_%s" % prop, None)
            setattr(cls, prop, property(fget, fset))

class autosuper(type):
    def __init__(cls, name, bases, dict):
        super(autosuper, cls).__init__(name, bases, dict)
        setattr(cls, "_%s__super" % name, super(cls))


class A():
    __metaclass__ = autosuper
    def meth(self):
        return "A"
class B(A):
    def meth(self):
        return "B" + self.__super.meth()
class C(A):
    def meth(self):
        return "C" + self.__super.meth()
class D(C, B):
    def meth(self):
        return "D" + self.__super.meth()

assert D().meth() == "DCBA"

import time
def now():
    return time.ctime(time.time())

class myclass:
    __metaclass__ = autoprop
    def _get_x(self):
        print('Get_x on %s' % now())
        return -self.__x
    def _set_x(self, x):
        print('Get_x on %s' % now())
        self.__x = -x

n = myclass()
assert not hasattr(n, 'x')
n.x = 12
# ap = autoprop
print( n.__dict__)
assert n.x == 12
# assert n._myclass__x == -12
