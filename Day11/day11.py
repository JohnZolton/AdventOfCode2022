import csv, math
data = []

with open('input.txt') as f:
    for line in f.read().split('\n'):
        data.append(line.strip())

class Monkey:
    def __init__(self, number, items, operation, test, true, false):
        self.number = number
        self.items = items
        self.operation = operation
        self.test=test
        self.iftrue=true
        self.iffalse=false 

    def __str__(self):
        return f"#{self.number}, {self.items}, {self.operation}, {self.test}, TRUE: to {self.iftrue}, FALSE: to {self.iffalse}"

def loadmonkeys():
    monkeys = []

    for i in range(len(data)):
        if data[i].startswith("Monkey"):
            number = int(data[i][-2])
            idx = data[i+1].find(':')
            items = data[i+1][idx+1:].split(',')
            items = [int(x) for x in items]
            idx = data[i+2].find(':')
            operation = ''.join(data[i+2][idx+1:].split()[-3:])
            idx = data[i+3].find(':')
            test = int(data[i+3][idx+1:][-2:])
            iftrue = int(data[i+4].split()[-1])
            iffalse = int(data[i+5].split()[-1])
            newmonkey = Monkey(
                number, # number
                items, # items
                operation, # operation
                test, # test
                iftrue, # if true
                iffalse # if false
            )
            monkeys.append(newmonkey)
    return monkeys
    

def firstsolution():
    monkeys = loadmonkeys()
    inspections = [0] * len(monkeys)
    for i in range(20):
        for monkey in monkeys:
            #print(monkey.items)
            for item in monkey.items:
                old = item
                res = eval(monkey.operation)
                #print(res)
                res = res//3
                #print('decreased to ', res)
                if res % monkey.test == 0:
                    monkeys[monkey.iftrue].items.append(res)
                    #print(res, 'thrown to monkey ', monkey.iftrue)
                else:
                    monkeys[monkey.iffalse].items.append(res)
                    #print(res, 'thrown to monkey ', monkey.iffalse)
                inspections[monkey.number] += 1
            monkey.items = []
        #for monkey in monkeys:
            #print(monkey)

    #print(sorted(inspections))
    print(sorted(inspections)[-1]*sorted(inspections)[-2])

def secondsolution():
    monkeys = loadmonkeys()
    inspections = [0] * len(monkeys)
    tests = []
    for monkey in monkeys:
        tests.append(monkey.test)
    factor = math.lcm(*tests)
    print('Modulus: ', factor)

    inspections = [0] * len(monkeys)
    for i in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                old = item
                res = int(eval(monkey.operation))
                res = res % factor
                if res % monkey.test == 0:
                    monkeys[monkey.iftrue].items.append(res)
                    #print(res, 'thrown to monkey ', monkey.iftrue)
                else:
                    monkeys[monkey.iffalse].items.append(res)
                    #print(res, 'thrown to monkey ', monkey.iffalse)
                inspections[monkey.number] += 1
            monkey.items = []

        #for monkey in monkeys:
            #print(monkey)
        if (i+1) % 1000 ==0 or i == 19:
            print(inspections)

    print(sorted(inspections))
    print('Total monkey business: ', sorted(inspections)[-1]*sorted(inspections)[-2])

firstsolution()
secondsolution()