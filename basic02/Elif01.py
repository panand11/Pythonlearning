#elif stmnt works just like else if in C

def login(choice):
    if choice == 1:
        print("python")
    elif choice == 2:
        print("java")    
    elif choice == 3:
        print("HTML")

var = int(input("enter your choice"))
login(var)