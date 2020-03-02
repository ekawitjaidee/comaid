import random

password = ''

def fitness(key):
    global password
    sum_fit=0
    if len(key) != len(password):
        # print('error')
        pass
    else:
        for i in range(len(password)):
            if key[i] == password[i]:
                sum_fit=sum_fit+1
    return sum_fit

def createPass():
    global password
    for i in range(20):
        password+=str(random.randint(0, 9))

def createPop(num):
    mylist = []
    for j in range(num):
        pa=''
        for i in range(20):
            pa+=str(random.randint(0, 9))
        mylist.append({'gene':(pa), 'fitness':(fitness(pa))})
    return mylist

def sortFunc(e):
      return e['fitness']

def mutation(strtemp):
    MR = 1/20*100
    old_temp = strtemp
    for i in range(len(strtemp)):
        if (random.randint(0, 100) <= MR):
            strtemp = strtemp[:i]+str(random.randint(0, 9))+strtemp[i+1:]
    return strtemp

def Xover(myList, num):
    index1 = random.randint(0, num)
    index2 = random.randint(0, num)
    fsplit = random.randint(1, 19)
    tempList1 = myList[index1].get('gene')
    tempList2 = myList[index2].get('gene')
    a = tempList1[:fsplit]+tempList2[fsplit:]
    b = tempList2[:fsplit]+tempList1[fsplit:]
    a = mutation(a)
    b = mutation(b)
    return [{'gene':(a), 'fitness':(fitness(a))}, 
    {'gene':(b), 'fitness':(fitness(b))}]

if __name__ == '__main__':
    createPass()
    while(True):
        populations = input('Enter number of population: ')
        if (populations.isdigit() and int(populations) > 1):
            populations = int(populations)
            parent = createPop(populations)
            break
        else:
            print('\tInvalid input!!\n')

    count = 0
    child = []
    while(True):
        print('\nCommand : | p = print population || q = exit || run = start || s = sort population |')
        val = input('Enter command: ')
        print('')
        if (val == 'p'):
            print(*parent, sep='\n')
            print('')
        if (val == 's'):
            parent.sort(reverse=True,  key=sortFunc)
            print(*parent, sep='\n')
            print('')
        elif (val == 'run'):
            while(True):
                val2 = input('Insert number of gen (insert 0 to exit): ')
                print('')
                if (val2.isdigit() and int(val2) > 0):
                    gen = count+int(val2)
                    while(count < gen and max(parent, key = lambda k : k['fitness'])['fitness'] < 20):
                        for i in range(int(populations/5), int(populations/2)):
                            child = child+(Xover(parent, (populations-1)))
                        
                        parent.sort(reverse=True,  key=sortFunc)
                        num_other_child = populations-len(child)
                        for k in range(0, num_other_child):
                            child.append(parent[k])

                        parent.clear()
                        parent = child
                        child = []
                        count += 1
                    print('\tFINISH!! \n\tgen = '+str(count))
                    print(max(parent, key = lambda k : k['fitness']))
                    print('')
                    if (max(parent, key = lambda k : k['fitness'])['fitness'] >= 20):
                        break
                elif(val2.isdigit() and int(val2) == 0):
                    break
                else:
                    print('\tInvalid input!!\n')

        elif (val == 'q'):
            break
        else :
            print('\tInvalid command')
        