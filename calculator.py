4a=float(input())
b=float(input())
choice=input("enter the operation")
match choice:
    case"+":
        print(a+b)
    case"-":
        print(a-b)
    case"*":
        print(a*b)
    case"/":
        print(a/b)
    case"%":
        print(a%b)
    case"**":
        print(a**b)
    case"//":
        print(a//b)
    case _:
        print("invalid")
