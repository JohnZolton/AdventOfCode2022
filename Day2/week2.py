import csv

data = []
with open('input.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    for line in reader:
        data.append(line)

outs = { # ax = rock, by = paper, cz = scissors
# win = 6, draw = 3, lose = 0
# rock = 1, paper = 2, scissors = 3
    ('A','Z'): 6+2,
    ('A','Y'): 3+1,
    ('A','X'): 0+3,
    ('B','Z'): 6+3,
    ('B','Y'): 3+2,
    ('B','X'): 0+1,
    ('C','Z'): 6+1,
    ('C','Y'): 3+3,
    ('C','X'): 0+2  
}

factors = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

score = 0
for hand in data:
    them, outcome = hand[0], hand[1]
    score += outs[(them, outcome)]
print(score)