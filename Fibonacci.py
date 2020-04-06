#Fibonacci Numbers
n = int(input("How many fibonacci numbers are to be found? "))
a = 0
b = 1
c = 0
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
