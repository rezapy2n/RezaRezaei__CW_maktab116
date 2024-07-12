x = 'I love maktab(-:'

def f1():
    s = 'I love GeeksforGeeks'
    global m
    m = 'hello'
    def f2():
        s = 'Me too'
        print(s)
        
    f2()
    print(s)
    print(x)


f1()
print(m)

