def max_of_two_num(n,m):
    if n>m:
        return n
    else:
        return m

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

x=max_of_two_num(a,b)

print("Maximum of",a,"and",b,"is",x)