file = open('input.txt', 'r')
lines = file.readlines()
count = 0
for i in range(len(lines)-3):
    a = int(lines[i])
    b = int(lines[i+1])
    c = int(lines[i+2])
    d = int(lines[i+3])

    curr = a + b + c
    next = b + c + d
    if next > curr:
        count += 1
print(count)

