#Positive Numbers
n = int(input("Enter the number of elements: "))
a = list()
print("Enter the values: ")
for i in range(n):
    p = int(input())
    a.append(p)
b = list()
for i in a:
    if i > 0:
        b.append(i)
print(b)
