import random

print("\n\033[1m\033[93m Dice Roller Alpha\033[0m")
print("\033[3mThe rolling of the dice is the unfolding of fate.\033[0m\n")

while True:

    roll = (input("roll: ")).replace(' ', '').split('d')
    count, sides = int(roll[0]) if roll[0] else 1, int(roll[1])

    Dices = [random.randint(1, sides) for _ in range(count)]

    print(f"Dices: {Dices}")
    print(f"Total: {sum(Dices)}\n")
