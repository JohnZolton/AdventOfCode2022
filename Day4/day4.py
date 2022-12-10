
count = 0
with open('input4.txt') as f:
    for line in f.readlines():

        elf1, elf2 = line.split(',')
        
        e1low, e1high = elf1.split('-')
        e2low, e2high = elf2.split('-')
        elf1 = (int(e1low), int(e1high))
        elf2 = (int(e2low), int(e2high))
        # no overlap:
        if elf1[1] < elf2[0]: continue
        if elf2[1] < elf1[0]: continue
        else:
            count += 1
print(count)