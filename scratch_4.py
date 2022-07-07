n=int(input("enter the number:"))
if n%2==0:
    if n%3==0:
        print("divisible by both 2 and 3")
    else:
        print("divisible by 2 not 3")
else:
    if n%3==0:
        print("divisible by 3")
    else:
        print("not div by 2 and 3")