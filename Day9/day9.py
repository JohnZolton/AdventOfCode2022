import csv

moves = []
with open('day9.txt') as f:
    lines = csv.reader(f, delimiter=' ')

    for line in lines:
        moves.append(line)

def distance(head,tail):
        x, y = head
        z, w = tail
        return ((z - x)**2 + (w - y)**2)**.5

def deltadist(a, b):
    if a-b == 0:
        return 0
    if a-b > 0: return 1
    if a-b < 0: return -1

def partone():
    visited = set()
    head, tail = (0,0), (0,0)
    visited.add(tail)
    
    for move in moves:
        direct, num = move[0], int(move[1])
        while num > 0:
            if direct == 'R':
                head = (head[0]+1, head[1])
            if direct == 'L':
                head = (head[0]-1, head[1])
            if direct == 'U':
                head = (head[0], head[1]-1)
            if direct == 'D':
                head = (head[0], head[1]+1)
            if distance(head, tail) > 2**.5:
                dx = deltadist(head[0],tail[0])
                dy = deltadist(head[1],tail[1])
                tail = (tail[0] + dx, tail[1]+dy)
                visited.add(tail)

            num -= 1
    print(len(visited))

def parttwo():
    visited = set()

    knot_coords = {x: (0,0) for x in range(10)}
    knot_pairs = [(x, x+1) for x in range(9)]

    visited.add((0,0))

    for move in moves:
        direct, num = move[0], int(move[1])
        while num > 0:
            if direct == 'R':
                knot_coords[0] = (knot_coords[0][0]+1, knot_coords[0][1])
            if direct == 'L':
                knot_coords[0] = (knot_coords[0][0]-1, knot_coords[0][1])
            if direct == 'U':
                knot_coords[0] = (knot_coords[0][0], knot_coords[0][1]-1)
            if direct == 'D':
                knot_coords[0] = (knot_coords[0][0], knot_coords[0][1]+1)
            
            for knots in knot_pairs:
                head, tail = knots[0], knots[1]
                head_coord = knot_coords[head]
                tail_coord = knot_coords[tail]
                if distance(head_coord, tail_coord) > 2**.5:
                    dx = deltadist(head_coord[0],tail_coord[0])
                    dy = deltadist(head_coord[1],tail_coord[1])
                    tail_coord = (tail_coord[0] + dx, tail_coord[1]+dy)
                    knot_coords[tail] = tail_coord

            visited.add(knot_coords[9])
            num -= 1
    print(len(visited))

partone()
parttwo()