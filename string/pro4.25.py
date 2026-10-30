text = input("Enter string: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

values = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(values) > 1:
    print("Second most frequent:", values[1][0])
else:
    print("No second character")