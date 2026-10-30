s = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    elif ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z'
        consonants = consonants + 1
    elif ch >= '0' and ch <= '10'
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special characters =", special)