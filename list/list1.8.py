list = [11,32,34,56,89,90,57,36,19,23,17,88,93,54,59]
even = 0
odd = 0

for num in list:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(type(list))
print(id(list))
print("Even numbers:", even)
print("Odd numbers:", odd)