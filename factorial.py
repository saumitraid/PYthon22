def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

print("The factorial is ",factorial(10))