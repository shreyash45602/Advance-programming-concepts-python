a = input("Enter first string: ")
b = input("Enter second string: ")

if len(a) == len(b) and b in a + a:
    print("Yes")
else:
    print("No")