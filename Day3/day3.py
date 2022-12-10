ans = 0

with open('input2.txt') as f:
    count = 0
    prospects = set()
    for line in f.read().strip().split():
        
        if count == 0:
            for letter in line:
                prospects.add(letter)
        else:
            toremove = []
            for item in prospects:
                if item not in line:
                    toremove.append(item)
            for x in toremove:
                prospects.remove(x)
        count += 1
        if count == 3:
            for i in prospects:
                if i.islower():
                    ans += ord(i) - ord('a') + 1
                else:
                    ans += ord(i) - ord('A') + 27
            count = 0
            prospects = set()
print(ans)
"""    for line in f.read().strip().split():

        a = len(line.strip())//2
        left= line[:a]
        right = line[a:]
        used = []
        for letter in left:
            if letter in right and letter not in used:
                if letter.islower():
                    ans += ord(letter) - ord('a') + 1
                else:
                    ans += ord(letter) - ord('A') + 27
                used.append(letter)"""
    #print(ans)

