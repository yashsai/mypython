def great(a,b,c):
    if(a>b):
        if(a>c):
            return a
    if(b>a):
        if(b>c):
            return b
    else:
        return c

def main():
    a=12
    b=9
    c=13
    d=great(a,b,c)
    print(d)
main()
