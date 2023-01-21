print("welcome to my quiz game")
playing = input("Do you want to play?")

if playing.lower()!="yes":
    quit()

print("okay! Lets play:")
score=0

answer = input("what does CPU stand for?")
if answer.lower() == "central processing unit":
    print('correct!')
    score+=1
else:
    print("Incorrect!")

answer = input("what is gpu stand for?")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score+=1
else:
    print("Incorrect!")
    
answer = input("What is RAM stand for?")
if answer.lower() == "random access memory":
    print('correct!')
    score+=1
else:
    print("Incorrect!")
    
answer = input("what does psu stand for??")
if answer.lower() == "power supply":
    print('correct!')
    score+=1
else:
    print("Incorrect!")

print("You got" + str(score)+" question correct!")
print("You got" + str((score/4)*100)+"%.")



