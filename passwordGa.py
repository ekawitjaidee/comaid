import random

pop = [] #poppulation size = 20
popsize = input('Enter population size = ')
Ps = input('Binary tournament enter 1 | Roulette wheel enter 2 = ')
indi = [0]*popsize #individual size = 20
Eliterate = 10 #10%

target = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]

def randomindi():
  get = [0]*20
  for i in range(popsize):
    for j in range(20):
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
    
def sortSecond(val): 
    return val[1]   

def sortfit(p):
  p.sort(key = sortSecond ,reverse = True)
  return p

def bitour(p): #binarytournament
  a = random.randint(0,len(p)-1)
  b = random.randint(0,len(p)-1)
  if a == b :
    b = b-1

  pr1 = []
  pr2 = []
  prf1 = 0
  prf2 = 0
  for i in range(len(p)):
    if i == a :
      pr1 = p[i][0]
      prf1 = p[i][1]
    if i == b :  
      pr2 = p[i][0]
      prf2 = p[i][1]
  if prf1 > prf2 :    
   return pr1
  else:
    return pr2   

def rourettewheel(p):
  sumfitness = 0
  prob = [0]*len(p)

  for i in range(len(p)):
    sumfitness += p[i][1] 

  for i in range(len(p)):
    prob[i] = float(p[i][1])/float(sumfitness)

  fp = prob[0] #frist probability
  lp = prob[len(prob)-1] # last probability
  rp = random.uniform(lp,fp) #range of probability

  for i in range(len(prob)):
    if(prob[i]>=rp and rp>=prob[i+1]):
      return p[i][0]


def xover(p1,p2): #Crossover
  percent = random.randint(0,19)
  p1fh = [0]*len(p1)
  p1sh = [0]*len(p1)
  p2fh = [0]*len(p1)
  p2sh = [0]*len(p1)
  for i in range(len(p1)):
    if i < percent:
      p1fh[i] = p1[i]
      p2fh[i] = p2[i]
    else:
      p1sh[i] = p1[i]
      p2sh[i] = p2[i]
  p1 = p1fh[:percent] + p2sh[percent:]
  p2 = p2fh[:percent] + p1sh[percent:]
  return p1,p2

def mutation(o):
  Mutarate = 0.05*100 # mutation rate = (1/individual size) * 100 

  for i in range(len(o)):
    if random.randint(0,100) <= int(Mutarate):
      o[i] = random.randint(0,9)
  return o


poppulation = []
poppulation = randomindi() #Add random number into population

poppulation = fitnesscal(poppulation,target) #Find fitness first generation
poppulation = sortfit(poppulation)#sorting fitness
gen = 1 
print("gen"+str(gen)+" Max fitness = "+str(poppulation[0][1])+" "+str(poppulation[0][0])+" ("+str((poppulation[0][1]/20.0)*100)+")%") 
gen = 2 # print 1st generation alredy

while poppulation[0][1] != 20:
  newpop = []

  for i in range((len(poppulation)*Eliterate)/100): #Elite append 10% of parent to offspring
    newpop.append(poppulation[i][0])


  while len(newpop) < popsize:
    # Parent selection Binary tournament or roulette wheel
    if Ps == 1: 
      parent1 = bitour(poppulation)
      parent2 = bitour(poppulation)
    elif Ps == 2:
      parent1 = rourettewheel(poppulation)
      parent2 = rourettewheel(poppulation)
    while parent1 == parent2:
      if Ps == 1:
        parent2 = bitour(poppulation)
      elif Ps == 2 :
        parent2 = rourettewheel(poppulation)
    
    #Crossover of parents
    child=xover(parent1,parent2)
    #Mutation child 
    o1 = mutation(child[0])
    o2 = mutation(child[1])
    #Add offspring
    newpop.append(o1)
    newpop.append(o2)
  poppulation = []  
  for i in range(len(newpop)):
    poppulation.append((newpop[i],0)) 
  poppulation = fitnesscal(poppulation,target)
  poppulation = sortfit(poppulation)
  print("gen"+str(gen)+" Max fitness = "+str(poppulation[0][1])+" "+str(poppulation[0][0])+" ("+str((poppulation[0][1]/20.0)*100)+")%")  
  gen +=1  
