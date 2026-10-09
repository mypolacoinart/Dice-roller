import random

roll = (input("roll: ")).replace(' ', '').split('d')
count, sides = int(roll[0]) if roll[0] else 1, int(roll[1])

Dices = [random.randint(1, sides) for _ in range(count)]

print(f"Dices: {Dices}")
print(f"Total: {sum(Dices)}")