email = input("Enter email: ")

if "@" in email and "." in email.split("@")[-1]:
    print("Valid Email")
else:
    print("Invalid Email")