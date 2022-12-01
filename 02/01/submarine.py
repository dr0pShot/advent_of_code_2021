file = open('input.txt', 'r')
horizontal = 0
depth = 0
for line in file.readlines():
    command, number = line.split(' ')
    if 'forward' in command:
        horizontal += int(number)
    if 'down' in command:
        depth += int(number)
    if 'up' in command:
        depth -= int(number)
print(horizontal, depth)
print(horizontal * depth)
