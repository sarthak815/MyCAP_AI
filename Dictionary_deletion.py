a = {"India":"Delhi",
    "France":"Paris",
    "United Kingdom":"London",
    "USA":"Washington DC"}
print(a)
c = "y"
while c == "y":
    b  = input("Enter country to be deleted: ")
    del a[b]
    c  = input("Would you like to delete another element(y/n):")
print(f"The updated dictionary is\n{a}")
