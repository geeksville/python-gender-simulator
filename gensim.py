
import random

choices = ['m', 'f']

def nextPool(curPool):
    """decide to keep having children if not male child"""
    newPool = []
    for p in curPool:
        if p == 'f': # if female, keep trying to have kids
            newPool.append(random.choice(choices))
    return newPool

def genPool(numKids):
    pool = []
    for i in range(numKids):
        pool.append(random.choice(choices))
    return pool

totalMales = 0
totalFemales = 0
genNum = 0

def countKids(pool):
    """Update global kid count based on current pool, return true if we found only males"""
    global totalMales, totalFemales, genNum
    numMales = 0
    numFemales = 0
    for p in pool:
        if p == 'm':
            numMales += 1
        else:
            numFemales += 1

    genNum += 1
    print(f"Gen {genNum} had {numMales} males and {numFemales} females")
    totalMales += numMales
    totalFemales += numFemales
    return numMales == len(pool)

numFirst = 1000
curPool = genPool(numFirst)

while not countKids(curPool):
    curPool = nextPool(curPool)

print(f"total males {totalMales} and females {totalFemales}")