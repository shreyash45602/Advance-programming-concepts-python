marital_status = input("Enter marital status (married/unmarried): ")

if marital_status == "married":
    print("Driver is Insured")
else:
    gender = input("Enter gender (male/female): ")
    age = int(input("Enter age: "))

    if (gender == "male" and age > 30) :
        print("Driver is Insured")
    elif (gender == "female" and age > 25):
         print("Driver is Insured") 
    else:
        print("Driver is Not Insured")