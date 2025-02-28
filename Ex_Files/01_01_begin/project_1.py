import random

print(random.randint(1, 10))

print(random.random())
      
answer = random.randint(1,8)
if answer==1:
  print("Yes")
if answer == 2:
  print("No")
if answer == 3:
  print("Maybe")

lucky_number = random.randint(1, 100)

fortune_number = random.randint(1, 3)

fortune_text=""
if fortune_number == 1:
  fortune_text = "you will have a great day"
elif fortune_number == 2:
  fortune_text = "you will have a bad day"
else:
  fortune_text = "you will have an ok day"

print(f"youwillhaveagreatday,goodlucknumberis:{lucky_number}{fortune_text}")
