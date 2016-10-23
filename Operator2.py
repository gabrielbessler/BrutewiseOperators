# Two digits:
from random import *
import sys

#Dangerous
sys.setrecursionlimit = 1500

# Z = ['&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//']
Z = ['&', '|', '+']

def Main():
    confirmRun = input("Are you sure [y/n]?\n")
    if confirmRun == "y":
        results = []
        results = getResults(results)
        results = unique(results)
        tempR = verifyResults(results)
        results = tempR[0]
        n = tempR[1]

def getResults(Results):
    test = 100
    i = choice(range(test))
    i2 = choice(range(test))
    for w in range(len(Z)):
        for x in range(len(Z)):
            for y in range(len(Z)):
                for z in range(len(Z)):
                    answer = evaluation(str(i),str(i2),w,x,y,z)
                    if answer!= None:
                        Results += [answer]
    return Results

def verifyResults(Results):
    n = 0
    for i in Results:
        if calculate(i) == True:
            correct = True
            j = 20
            while j > 0:
                if calculate(i) == False:
                    correct = False
                j -= 1
            if correct == True:
                print(i)
                n+=1
    return (Results, n)

def test(L):
    for j in range(2):
        if calculate(L) == False:
            return False
    return True

def evaluation(a,b,w,x,y,z):
    try:
        if eval(str(eval(a+Z[w]+b))+Z[x]+str(eval(a+Z[y]+b)))== eval(a+Z[z]+b):
            return [ Z[w],Z[x],Z[y],Z[z] ]
    except:
        pass

def unique(L):
    if len(L) <= 1:
        return L
    if L[0] in L[1:]:
        return unique(L[1:])
    return L[0:1] + unique(L[1:])

def calculate(L):
    a = choice(range(1,10000))
    b = choice(range(1,10000))
    try:
        if eval( str(eval('a'+L[0]+'b')) + L[1] + str(eval('a'+L[2]+'b')) ) == eval('a'+L[3]+'b'):
            return True
        else:
            return False
    except:
        pass


#correct = True
#j = 0
#while j > 0:
#if calculate(i) == False:
#correct = False
#j -= 1
#if correct == True:
#print(i)

if __name__  == "__main__":
    Main()
