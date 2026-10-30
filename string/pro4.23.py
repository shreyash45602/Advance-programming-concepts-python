text = input("Enter string: ")

compressed = ""
count = 1

for i in range(len(text)):
    if i + 1 < len(text) and text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

if len(compressed) < len(text):
    print(compressed)
else:
    print(text)