text = input("Enter string: ")

most = max(text, key=text.count)

print("Most frequent:", most)