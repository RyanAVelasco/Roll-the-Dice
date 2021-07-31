import random


def roll(cycle):
    while not cycle == 0:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_count[dice_1] = dice_count.get(dice_1, 0) + 1
        dice_count[dice_2] = dice_count.get(dice_2, 0) + 1
        cycle -= 1
    print('[ROLL]', dice_1, '/', dice_2)


dice_count = {} # Keeps count of rolls
start_cycle = int(input('How many times (start)? '))
end_cycle = int(input('How many times (end)? '))

while True:
    play = input('Roll? (Y/N) ').lower().strip()
    if play == 'y' or play == 'yes':
        roll_time = random.randint(start_cycle, end_cycle)
        roll(roll_time)
        for key, value in dice_count.items() : print('#:', key, 'times', value)
    elif play == 'n' or play == 'no' : 
        print('Thanks for playing')
        quit()
    else : quit()