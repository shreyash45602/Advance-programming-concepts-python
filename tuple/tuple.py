tuple = (1,2,1,3,2,2,4,5,6,3,6,2,6,4,5,9,9)
print(tuple)
print(type(tuple))
print(id(tuple))

cu = tuple.count(9)
print("no of count :",cu)

res = tuple.index(2)
print("index of first occurrance of 3:",res)

ind = tuple.index(2,3)
print("index of 1st occurrence of 2 after the position :",ind)
