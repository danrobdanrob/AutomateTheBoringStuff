import random
guess = 0
number = random.randint(1,20)
print('Guess my number')
response = int(input())
while response != number:
    guess = guess + 1
    if response > number:
        print('Your guess is too high')
        response = int(input())
    elif response < number:
        print('Your guess is too low')
        response = int(input())
print('Good job! You guessed my number in ' + str(guess) + ' guesses')
