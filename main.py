import random
from matplotlib import pyplot as plt
import numpy as np

generations = int(input('# of generations: '))
parents = 10
offspring = 0
populationSize = [parents]
headsOrTails = ['heads', 'tails']
coinOrder = []

#Function for flipping coins
def flipCoins(flips):
  coinOrder = []
  heads = 0
  tails = 0
  for i in range(flips):
    coin = random.choice(headsOrTails)
    if(coin == 'heads'):
      heads +=1
      coinOrder.append('heads')
    else:
      tails+=1
      coinOrder.append('tails')
  return heads

#Function for getting the order of coins
def flipCoins2(flips):
  coinOrder = []
  heads = 0
  tails = 0
  for i in range(flips):
    coin = random.choice(headsOrTails)
    if(coin == 'heads'):
      heads +=1
      coinOrder.append('heads')
    else:
      tails+=1
      coinOrder.append('tails')
  return coinOrder

#Part 1
for i in range(generations):
  while(parents > 0):
    numHeads = flipCoins(2)
    if(numHeads == 0):
      parents-=1
    elif(numHeads == 1):
      parents-=1
      offspring+=2
  parents = offspring
  offspring = 0
  populationSize.append(parents)
part1List = np.array(populationSize)
print('Part 1 Values: ' + str(part1List))

#Setup for part 2
parents = 10
offspring = 0
populationSize = [parents]

#Part 2
for i in range(generations):
  while(parents > 0):
    coinOrder = flipCoins2(2)
    if(coinOrder[0] == 'tails' and coinOrder[1] == 'tails'):
      parents-=1
    elif(coinOrder[0] == 'heads' and coinOrder[1] == 'tails'):
      parents-=1
      offspring+=2
    elif(coinOrder[0] == 'tails' and coinOrder[1] == 'heads'):
      parents-=1
      offspring+=1
  parents = offspring
  offspring = 0
  populationSize.append(parents)
part2List = np.array(populationSize)
print('Part 2 Values' + str(part2List))

GenerationsNum = np.array([])
for i in range(generations + 1):
  GenerationsNum = np.append(GenerationsNum, i)

#Graph data
plt.plot(GenerationsNum, part1List, label = "Part 1") 
plt.plot(GenerationsNum, part2List, label = "Part 2")
plt.xlabel('Generations') 
plt.ylabel('Population Size') 
plt.xlim([0,generations])
plt.title('Generations vs Population Size')
plt.legend()
plt.yscale('log', basey=2)
plt.show()