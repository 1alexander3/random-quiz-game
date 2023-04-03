print("Welcome to my random questions quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Okay, see you later!")
    quit()

print("Okay! Let's play!")
score = 0

answer = input("Where would you be if you were standing on the Spanish Steps? ").lower()
if answer == "rome":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What disease commonly spread on pirate ships? ").lower()
if answer == "scurvy":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("How many minutes are in a full week? ").replace(",", "")
if answer == "10080":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Roald Amundsen was the first man to reach the South Pole, but where was he from? ").lower()
if answer == "norway":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What software company is headquartered in Redmond, Washington? ").lower()
if answer == "microsoft":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the world's fastest bird? ").lower()
if answer == "peregrine falcon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the most awesome person in the world? ")
if score > 5:
    print("It's you! :)")
else:
    print("Not you! :(")


print("You got " + str(score) + " questions correct!")
print("You got " + str(round((score / 6) * 100)) + "%.")