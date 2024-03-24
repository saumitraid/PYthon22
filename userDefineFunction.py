# Function without return and without parameter
def add():
    a=10
    b=15
    a=a+b
    print("Addition is ",a)

add()

# Function without return and with parameter
def mult(a,b):
    c=a*b
    print("The multiplication is",c)

mult(50,5)


# Function with return and with parameter
def sub(a,b):
    c=a-b
    return c

print("Subtraction is",sub(35,10))


