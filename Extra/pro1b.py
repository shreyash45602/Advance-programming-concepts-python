
a = 100
print("Value:", a)
print("Type :", type(a))
print("ID   :", id(a))
a = a + 10
print("ID   :", id(a))

print() 

b = 45.67
print("--- Float ---")
print("Value:", b)
print("Type :", type(b))
print("ID   :", id(b))
b = b + 88.8
print("ID :", id(b))
print()

c = 3 + 4j
print("Value:", c)
print("Type :", type(c))
print("ID   :", id(c))
c = c + 9
print("ID :", id(c))
print()

d = "Python"
print("Value:", d)
print("Type :", type(d))
print("ID   :", id(d))
d = d + "string"
print()

e = True
print("Value:", e)
print("Type :", type(e))
print("ID   :", id(e))
print()

f = [10, 20, 30]
print("--- List ---")
print("Value:", f)
print("Type :", type(f))
print("ID   :", id(f))
print()

g = (1, 2, 3)
print("Value:", g)
print("Type :", type(g))
print("ID   :", id(g))
print()

h = {"name": "Alice", "age": 25}
print("Value:", h)
print("Type :", type(h))
print("ID   :", id(h))
print()

i = {1, 2, 3}
print("Value:", i)
print("Type :", type(i))
print("ID   :", id(i))
print()

a_list = [10, 20, 30]
a_list.append(40)
print("Updated list:", a_list)
print(" list is mutable")
d = "Python"
print("ID:", id(d)) 
d = d + " Language" 
print( "ID :", id(d))




