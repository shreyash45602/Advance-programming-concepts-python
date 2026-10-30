numbers = [10, 20, 30]
print(type(numbers))
print(id(numbers))
print("old list",numbers)
numbers.append(40)
numbers.insert(0, 5)
numbers.insert(2, 15)

print("Updated list:", numbers)