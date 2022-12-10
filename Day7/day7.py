with open('input7.txt') as f:
#with open('test7.txt') as f:
    lines = f.readlines()

directories = []
cur_dir = 0
path = []
fs = {('/',):0}
for line in lines:
    res = line.split()
    match res:
        case['$', 'ls']: pass
        case['$', 'cd', '..']:
            path = path[:-1]
        case['$', 'cd', directory]:
            path += [directory]
        case['dir', directory]:
            fs.setdefault(tuple(path+[directory]), 0)
        case[size, filename]:
            for i in range(1, len(path)+1):
                fs[tuple(path[:i])] += int(size)

over10k = [x for x in fs.values() if x <= 100000]

total = fs[('/',)]
print(total)
space= 70000000
freespace = (space - total)

required = 30000000 - freespace 
print(required)

options = [x for x in fs.values() if x >= required]
print(sorted(options)[0])
