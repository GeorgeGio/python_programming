x= 1 # global variable

def first():
    x = 2
    print(x)

def second():
    global x
    print(x)
    x=5



first()
print(x)
second()
print(x)
