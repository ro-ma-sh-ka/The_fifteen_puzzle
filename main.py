from game_mechanic import mechanic


print("Let's start:")
mixed_field = mechanic.List15().mixer()
print(*mixed_field, sep='\n')
new_field = mixed_field

sample = mechanic.List15().new_list()

counter = 0
while sample != new_field:
    print(f"Movements: {counter}")
    move_to = int(input('Choose zero to move: 1 - zero to up, 2 - zero to down, 3 - zero to right, 4 - zero to left: '))
    new_field = mechanic.List15().movement(mixed_field, move_to)
    print(*new_field, sep='\n')
    counter += 1

print(f"Congratulations! You've done it after {counter} movements!")
