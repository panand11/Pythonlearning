# nested if stmnt

a =int(input("Enter value of A:"))
b =int(input("Enter value of B:"))
c =int(input("Enter value of C:"))

if a>b:
    if a>c:
        g=a
    else:
        g=c
else:
    if b>c:
        g=b
    else:
        g=c
print("Biggest number Entered =",g)