s = input("enter a string :")
upper = 0
lower = 0
for ch in s:
     if ch>='A' and ch<='Z': 
      upper += 1
     elif ch>='a' and ch<='z':
      lower += 1
print("Uppercase =", upper)
print("Lowercase =", lower)