with open('input8.txt') as f:
#with open('test8.txt') as f:
    lines = f.read().split('\n')

trees = [[int(x) for x in line] for line in lines]
trees.pop()

visibles = set()


base = 2 * len(trees) + 2* len(trees[0]) -4


for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        if trees[i][j] > max(trees[i][:j]) or trees[i][j] > max(trees[i][j+1:]):  
            visibles.add((i,j))
        
        above = [row[j] for row in trees[:i]]
        below = [row[j] for row in trees[i+1:]]
        
        if trees[i][j] > max(above) or trees[i][j] > max(below):
            visibles.add((i,j))
            
print(len(visibles) + base)

score = 0
for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        left, right, up, down = 0,0,0,0
        for k in range(j-1, -1, -1):
            left += 1
            if trees[i][k] >= trees[i][j]:
                break
            
        for k in range(j+1, len(trees[0])):
            right += 1
            if trees[i][k] >= trees[i][j]:
                break
        
        for k in range(i-1, -1, -1):
            up += 1
            if trees[k][j] >= trees[i][j]:
                break
        
        for k in range(i+1, len(trees)):
            down += 1
            if trees[k][j] >= trees[i][j]:
                break
        
        score = max(score, left * right * up * down)
print(score)
        
    
        
