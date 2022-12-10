with open('input6.txt') as f:
    lines = f.readlines()

for line in lines:
    buffer = [x for x in line[0:4]]
    found = False
    for i in range(3, len(line)):
        if not found:
            if len(set(buffer)) == 4:
                print(i)
                found = True
                
            else:
                buffer.pop(0)
                buffer.append(line[i])
        if found:
            msg = [x for x in line[i-14:i]]
            if len(set(msg))==14:
                print(i)
                quit()
            else:
                msg.pop(0)
                msg.append(line[i])
            
        