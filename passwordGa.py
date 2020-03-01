import random

pop = [] #poppulation size = 20
popsize = 20
indi = [0]*20 #individual size = 20

target = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

def randomindi():
  get = [0]*20
  for i in range(popsize):
    for j in range(len(indi)):
      get[j] = random.randint(0,9)  
    indi[i]=get
    get = [0]*20

  for i in range(len(indi)):
    pop.append((indi[i],0))
  return pop

def fitnesscal(p,target):
  fitness = 0
  r = []
  for i in range(len(p)):
    for j in range(len(p[0][0])):
      if p[i][0][j] == target[j]:
        fitness +=1
    r.append((p[i][0],fitness))
    fitness = 0
  return r
    

  

poppulation = []
poppulation = randomindi()
poppulation = fitnesscal(poppulation,target)
print(poppulation)