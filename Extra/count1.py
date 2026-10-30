def countlines(sen):
    count = 0
    for l in sen.split(","):
        if l and not l.startswith("T"):
            count += 1
    print("lines not starting with T:", count)
story =("""A boy playing there,There is a playground,An aeroplane is in the sky,The sky is pink,Alphabets and numbers are allowed in the passwords,""")
countlines(sen)