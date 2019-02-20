def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
def main():
    a=int(input("enter a "))
    b=int(input("enter b "))
    c=int(input("enter c "))
    d=greatest(a,b,c)
    print(d)
main()
