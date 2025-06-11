n=int(input())
c,d=divmod(n,5)

def asdf(a,b):
    if b%3 == 0:
        print(a+(b//3))
    elif a == 0:
        print(-1)
    else:
        asdf(a-1, b+5)

asdf(c,d)