import random

attempts = 0 

random = random.randint(1,9)

while attempts < 5:
    number = int(input("Type your guess:"))
    attempts =attempts+1
    print("attempts left :",5-attempts)
    if (attempts == 0 ):
        print("You lose")
    if (number<random):
        print("The number was too low try something higher")
    if (number>random):
        print("This number was too high try something lower")
    if (number == random):
        print("Congratulations! You got it ")
    
    
