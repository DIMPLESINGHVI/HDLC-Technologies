# fibonacci series

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range (0,n) :
        f = a + b
        a = b
        print(f)
        b = f

print("Enter upto which term you want to print the series: ")
n = int(input())
fib(n)

