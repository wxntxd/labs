def comparison (n,m):
    if n>m:
        return n
    else:
        return m

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

x = comparison (a,b)

print("Maximum of",a,"and",b,"is",x)