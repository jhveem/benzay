#We get the user's gender. We don't care about the answer though
print("are you a boy or girl?")
gender = input(">")
print(gender)

#We get the user's age here, but we only want 6 or 7 year olds, not 30 year old booty faces
print("are you 7 or 6?")
age = input(">")
if age != "6" and age != "7":
  print("WRONG ANSWER BOOTY FACE")
else:
  print("oh your a " + age + " year old " + gender)