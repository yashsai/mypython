def greatest(a,b,c):
    x=a if (a>b and a>c) else b
    if(c>a and c>b):
        x=c
    return x
def main():
    a=99
    b=534
    c=531
    d=greatest(a,b,c)
    print(d)
main()
