import dis

g = 100

def func():
    print(g)
    g = 1
    print(g)


dis.dis(func)
func()