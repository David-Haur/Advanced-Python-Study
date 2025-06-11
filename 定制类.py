class Student():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'name: %s' % self.name
    
    __repr__ = __str__  # repr用于调试时输出

    def __getattr__(self, attr):    # 动态返回一个属性
        if attr == 'score':
            return 87
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    
    def __call__(self): # call魔术方法用于直接调用对象
        print('my name is %s' %self.name)
    

class Fib():
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self): # 让该类可以被序列化
        return self
    
    def __next__(self): # for循环遍历该类对象时，会不断调用__next__方法
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a
    
    def __getitem__(self, n):   #支持索引、切片、未来还得添加负值等功能
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a+b
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            L = []
            a, b = 1, 1
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a+b
            return L

s = Student('Mike')
# print(s)

# for n in Fib():
#     print(n, end=' ')

# f = Fib()
# print(f[2:10])

s()
print(callable(s))
print(callable(2))