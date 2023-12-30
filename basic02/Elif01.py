#elif stmnt works just like else if in C

def login(choice):               #def keyword is used to define functions in python
    if choice == 1:
        print("python")
    elif choice == 2:
        print("java")    
    elif choice == 3:
        print("HTML")
    else:
        print("invalid choice given")

var = int(input("enter your choice"))
login(var)