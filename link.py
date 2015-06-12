# -*- coding:koi8-r -*-



# class Link:
#     def __init__(self):
#         pass

class SingletonDecorator:
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance == None:
            self.instance = self.klass(*args, **kwds)
        return self.instance


class foo:
    def __init__(self, a):
        self.a = a


a = SingletonDecorator(foo)

x = a('r')
y = a('f')
y.a = 'q'
z = a('e')
# x.val = 'sausage'
# y.val = 'eggs'
# z.val = 'spam'
print(x.a)
print(y.a)
print(z.a)
print(x is y is z)
