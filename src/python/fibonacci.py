def fibonacci(n):
    if n >= 2:
        return(fibonacci(n-1) + fibonacci(n-2))
    else:
        return(n)

if __name__ == '__main__':
    x = int(input("Enter number: "))
    print("{}th term in fibonacci series is {}".format(x, fibonacci(x)))
    for i in range(x+1):
        print(fibonacci(i), end=", ")


