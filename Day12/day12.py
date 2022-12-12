# day 12, Hill Climbing Algorithm
data = []
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        dataline = [x for x in line.strip()]
        data.append(dataline)

# find start, end, and possible starting points 'a'
starts = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            start = (i,j)
        if data[i][j] == 'E':
            end = (i,j)
        if data[i][j] =='a':
            starts.append((i,j))
starts.append(start)

vals = {}
for i in range(26):
    vals[chr(i+97)] = i+1
vals['S'] = 0
vals['E'] = 27

def firstsolution(start):
    stack = [(start, 0)]
    steps = 0
    visited = set()
    while stack:
        (x, y), dist = stack.pop(0)

        if (x, y) == end: return dist

        if (x,y) in visited: continue
        else: visited.add((x,y))
        # right down left up
        DIR = [1, 0, -1, 0, 1]
        options = []
        for i in range(len(DIR)-1):
            if x+DIR[i] >= 0 and x+DIR[i] < len(data) and y+DIR[i+1] >= 0 and y+DIR[i+1] < len(data[0]):
                options.append((x+DIR[i], y+DIR[i+1]))

        for z,w  in options:
            if (z,w) in visited: continue
            if vals[data[z][w]] - vals[data[x][y]] <=1:
                stack.append(((z,w), dist+1))
    # failure case, end not found
    return float('inf')

def secondsolution():
    ans = []
    for start in starts:
        ans.append(firstsolution(start))
    return min(ans)


print('found in:', firstsolution(start))
print('found in:', secondsolution())