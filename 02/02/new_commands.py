file = open('input.txt', 'r')
horizontal = 0
depth = 0
aim = 0
for line in file.readlines():
    command, number = line.split(' ')
    if 'forward' in command:
        horizontal += int(number)
        depth += aim * int(number)
    if 'down' in command:
        aim += int(number)
    if 'up' in command:
        aim -= int(number)
print(horizontal*depth)
