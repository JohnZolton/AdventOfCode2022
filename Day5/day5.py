import csv

stacks = []
moves = []
piles = [
    ['D','T','W','F','J','S','H','N'],
    ['H	R	P	Q	T	N	B	G'],
    ['L	Q	V'],
    ['N	B	S	W	R	Q'],
    ['N	D	F	T	V	M	B'],
    ['M	D	B	V	H	T	R'],
    ['D	B	Q	J'],
    ['D	N	J	V	R	Z	H	Q'],
    ['B	N	H	M	S']
]

for i in range(1, len(piles)):
    
    piles[i] = piles[i][0].split('\t')
piles.insert(0,[])
#piles = [[],['Z','N'],['M','C','D'],['P']]

with open('input5.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    i=0
    for line in reader:
        if i >9:
            moves.append(line)
        i+=1

    for move in moves:
        start = int(move[3])
        end = int(move[-1])
        amount = int(move[1])
        package = piles[start][-amount:]
        
        piles[end] += (package)

        #piles[start] = piles[start][:-amount]
        while amount > 0:
            piles[start].pop()
            
            amount -= 1
            
for pile in piles[1:]:
    print(pile[-1])


