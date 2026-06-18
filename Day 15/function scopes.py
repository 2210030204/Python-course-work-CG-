'''#LOCAL SCOPE'''
def display():
    n=10
    print("Inside:",n)
display()

'''#GLOBAL SCOPE'''
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)


def display():
    global n
    n=10
    print("Inside:",n)
display()
print("Outside:",n)


def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)


def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Innerr function:",n)
    inner()
    print("Outer function:",n)
outer()

def update(n):
    n+=10
    print("Inside:",n)
n=10
update(n)
print("Outside:",n)


def update(n):
    n+=10
    print("Inside:",n)
n=10.4
update(n)
print("Outside:",n)


def update(n):
    n+=10
    print("Inside:",n)
n=3+4j
update(n)
print("Outside:",n)


def update(n):
    n+="lang"
    print("Inside:",n)
n="python"
update(n)
print("Outside:",n)


def update(n):
    n=(10)
    print("Inside:",n)
n=(1,2,3,4,5)
update(n)
print("Outside:",n)



def update(n):
    n.append(10)
    print("Inside:",n)
n=[1,2,3,4,5]
update(n)
print("Outside:",n)

def update(n):
    n[4]=10
    print("Inside:",n)
n={1:1,2:2,3:3}
update(n)
print("Outside:",n)


def update(n):
    n=False
    print("Inside:",n)
n=True
update(n)
print("Outside:",n)
