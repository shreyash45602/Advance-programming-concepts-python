def countalphabet(sen):
  res = sen.split(",")
  count = 0
  for i in res:
    i = i.strip()
    if i and not i.startswith('T'):
      count += 1
  print("Total count:",count)

sen = ("A boy is playing their, Their is a play ground, An aeroplane is in the sky, The sky is pink, alphabets and numbers are allowed in the password")
countalphabet(sen)