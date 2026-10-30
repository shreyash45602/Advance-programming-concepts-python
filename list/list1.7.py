list = []

for i in range(10):
    num = int(input("Enter number: "))
    list.append(num)

total = sum(list)
average = total / 10
print(type(list))
print(id(list))
print("Numbers:", list)
print("Sum:", total)
print("Average:", average)