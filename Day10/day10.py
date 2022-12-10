import csv

data = []
with open('input.txt') as f:
    lines = csv.reader(f, delimiter=' ')

    for line in lines:
        if len(line) > 1:
            data.append([line[0], int(line[1])])
        else:
            data.append(line)

# noop = run one cycle, do nothing
# addx = run two cycles, then add N

def firstsolution():
    cycle = 1
    val = 1
    i = 0
    nextadd = 1
    signal_strength = []

    while i < len(data):
        if data[i][0] == 'addx':
            if nextadd > 0:
                nextadd -= 1
            else:
                val += data[i][1]
                i += 1
                nextadd=1
        else:
            i+=1
        cycle += 1
        if (cycle-20)%40==0 or cycle ==20:
            signal_strength.append(cycle*val)

    print(sum(signal_strength))

def secondsolution():
    register = [['.']*40 for _ in range(6)]
    cycle = 1
    val = 1
    i = 0
    nextadd = 1
    register[0][0] = '#'

    while i < len(data):
        if data[i][0] == 'addx':
            if nextadd > 0:
                nextadd -= 1
            else:
                val += data[i][1]
                i += 1
                nextadd=1
        else:
            i+=1
        cycle += 1
        
        row, column = divmod(cycle-1, 40)
        if val-1 <= column <= val+1:
            register[row][column] = '#'
        for line in register:
            print(''.join(line))
        print()

firstsolution()
secondsolution()