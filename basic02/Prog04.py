#menu driven program in python

#defining addition function

def add(a,b):
    sum = a+b
    print(a, '+', b, '=', sum)

def subtract(a,b):
    difference = a-b
    print(a, '-', b, '=', difference)

a = int(input("Enter first number:"))
b = int(input("Enter Second number:"))

while True:                                 # infinte loop using True keyword
    print("\nMenu\n\t1.Sum\t2.Subrtract\t3.Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        add(a,b)
    elif choice == 2:         
        subtract(a,b)
    elif choice ==3:                            # elif is alternate of switch
       break                         
    else:
        print("Please enter a valid choice")