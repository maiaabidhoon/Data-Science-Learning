def sum(a,b):
    return a + b

def minus(a,b):
    return a - b

def multiply(a,b):
    return a * b

def fac(a):
    if (a == 0):
        return 1
    else:
        return (a - 1) * a

def main():
    a = int(input("Enter Value of a : "))
    op = input("Enter the Operator : ")
    if (op != "fac"):
        b = int(input("Enter Value of b : "))

    if(op == "+"):
        print(sum(a,b))
    elif(op == "-"):
        print(minus(a,b))
    elif (op == "*"):
        print(multiply(a,b))
    elif (op == "fac"):
        print(fac(a))
    else:
        print("Enter Correct Operator")

if __name__ == '__main__':
    main()