import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    iteration = []
    previousFlip = 2
    streak = 0
    for flip in range(100):
        iteration.append(random.randint(0,1))
    for flip in iteration:
        if flip==previousFlip:
            streak+=1
        else:
            streak = 0
        previousFlip = flip
        if streak ==6:
            numberOfStreaks+=1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
