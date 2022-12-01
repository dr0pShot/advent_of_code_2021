file = open('input.txt', 'r')
lines = file.readlines()
prev = lines[0]
counter = 0
for line in lines[1:]:
    if int(line) > int(prev):
        counter += 1
    prev = line
print(counter)
