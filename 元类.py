Hello = type('Hello', (object,), dict(lala=print))

h = Hello()
h.lala('hhh')

print(type(h))