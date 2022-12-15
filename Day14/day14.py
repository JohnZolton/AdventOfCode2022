data=[]
with open('test.txt') as f:
    lines = f.readlines()
    for line in lines:
        data.append([x.strip() for x in line.split('->')])
data.append(['500,0'])

x_vals = []
y_vals = []
for line in data:
    for item in line:
        x, y = [int(x) for x in item.split(',')]
        x_vals.append(x)
        y_vals.append(y)
dimensions = [max(x_vals)-min(x_vals), max(y_vals)-min(y_vals)]

grid = [['.'] * (dimensions[0]+1) for _ in range(dimensions[1]+1)]
def printgrid():
    for lien in grid:
        print(''.join(lien))
    print()
# shifting
min_x = min(x_vals)

for i in range(len(data)):
    for j in range(len(data[i])-1):
        x1, y1 = [int(x) for x in data[i][j].split(',')]
        x2, y2 = [int(x) for x in data[i][j+1].split(',')]
        x = min(x1, x2)
        y = min(y1, y2)
        while x < max(x1, x2):
            grid[y][x-min_x] = '#'
            x+=1

        while y < max(y1, y2+1):
            grid[y][x-min_x] = '#'
            y+=1

# adding sand spawn
x, y = data[-1][0].split(',')
spawn = (int(x)-min_x, int(y))
grid[spawn[1]][spawn[0]] = '+'
printgrid()
print(len(grid))


# now model pouring sand from 500,0
sand = 0
global OVERFLOW
OVERFLOW = False



def sandfall(loc):
    x, y = loc
    # down, left, right
    global OVERFLOW
    if y >= len(grid)-1 or x < 0 or x >= len(grid[0]):
        OVERFLOW = True
        return

    if grid[y+1][x] == '.':
        sandfall((x, y+1))

    elif grid[y+1][x] == 'o' or grid[y+1][x]=='#':
        if x-1 < 0: 
            OVERFLOW = True
            
        elif grid[y+1][x-1] == '.':
            sandfall((x-1, y+1))
        elif x+1 >= len(grid[0]): 
            OVERFLOW = True
        
        elif grid[y+1][x+1] == '.':
            sandfall((x+1, y+1))
        
        else:
            grid[y][x] = 'o'
            
        
while not OVERFLOW:
    sand += 1
    sandfall(spawn)
printgrid()
print(sand-1)