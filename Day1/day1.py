
data = []

count = 0
with open('input.txt') as f:
    
    for line in f:
        if line == '\n':
            data.append(count)
            count = 0
        else:
            count += int(line)
print(sum(sorted(data)[-3:]))
       