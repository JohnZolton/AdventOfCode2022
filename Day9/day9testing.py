import csv

def parttwo():
    moves = []
    with open('day9.txt') as f:
        lines = csv.reader(f, delimiter=' ')

        for line in lines:
            moves.append(line)

    visited = set()


    #knot_coords = {x: (12,16) for x in range(10)}
    knot_coords = {x: (0,0) for x in range(10)}
    knot_pairs = [(x, x+1) for x in range(9)]

    #head, tail = (0,4), (0,4)
    #visited.add(tail)
    #visited.add((12, 16))
    visited.add((0,0))

    #example = [['_'] * 30 for _ in range(30)]


    def distance(head,tail):
        x, y = head
        z, w = tail
        return ((z - x)**2 + (w - y)**2)**.5

    def deltadist(a, b):
        if a-b == 0:
            return 0
        if a-b > 0: return 1
        if a-b < 0: return -1

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
            example = [['_'] * 27 for _ in range(27)]
            for knots in knot_pairs:
                head, tail = knots[0], knots[1]
                head_coord = knot_coords[head]
                tail_coord = knot_coords[tail]
                if distance(head_coord, tail_coord) > 2**.5:
                    dx = deltadist(head_coord[0],tail_coord[0])
                    dy = deltadist(head_coord[1],tail_coord[1])
                    tail_coord = (tail_coord[0] + dx, tail_coord[1]+dy)
                    knot_coords[tail] = tail_coord
                    
            
                #example[tail_coord[1]][tail_coord[0]] = str(tail)
            #x, y = knot_coords[0]
            visited.add(knot_coords[9])
            """example[y][x] = 'H'
            for line in example:
                print("".join(line))
            print()"""
            num -= 1
            

    print(len(visited))

parttwo()