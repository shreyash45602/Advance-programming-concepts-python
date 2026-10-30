story=("""A boy playing there,
There is a playground,
An aeroplane is in the sky,
The sky is pink,
Alphabets and numbers are allowed in the passwords,""")
count = 0
for line in story.split(","):  
   if story line and not line.startswith("T") :
     count += 1
print("lines without starting with alphabet T : ",count)
