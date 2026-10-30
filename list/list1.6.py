num = [11,3,55,24,9,10,76,94]
print(type(num))
print(id(num))
print("list",num)
largest = num[0]
smallest = num[0]

for num in num:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
