def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1

print('Enter Number')

while True:
    try:
        number = int(input())
        break
    except ValueError:
        print('enter an integer above zero')

while number != 1:
    number = collatz(number)
    print(number)
