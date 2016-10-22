# Random operator generator
import sys
from random import *
L = ['<<', '>>', '&', '|' ]
P = ['+', '-', '*', '/', '%', '**']
#Z = ['<<', '>>', '&', '|', '+', '-', '*', '/', '%', '**']

def Main():
    '''DOCSTRING'''
    #Stores all of the results
    Results = []
    NumberPairs = []    
    #Number of iterations (Caution: runs NUM^2 times)
    REPEAT_NUM = 10
    
    for i in list(range(REPEAT_NUM)):
        for i2 in list(range(REPEAT_NUM)):
            answer = r(str(i), str(i2))
            if answer != None:
                Results += [answer[0:4]]
                NumberPairs += [answer[4:]] 
    
    #lenResults is used for seeing number of duplicates
    #lenResultsBeforeFiltering = len(Results)
    Results = filter(Results)
    #lenResultsAfterFiltering = len(Results)
    
    for i in Results:
        #print(i)
        #print(calculate(i))
        if calculate(i) == True:
            correct = True
            j = 0
            while j > 0: 
                if calculate(i) == False:
                    correct = False
                j -= 1
            if correct == True:
                print(i)

def filter(L):
    '''DOCSTRING'''
    if len(L) <= 1:
        return L
    if L[0] in L[1:]: 
        return filter(L[1:])
    return L[0:1] + filter(L[1:])
    
def calculate(L):
    '''DOCSTRING'''
    a = choice(range(1,10))
    b = choice(range(1,10))
    try:
        if eval( str(eval('a'+L[0]+'b')) + L[1] + str(eval('a'+L[2]+'b')) ) == eval('a'+L[3]+'b'):
            return True
        else:
            return False
    except: 
        pass

def r(a, b):
    '''DOCSTRING'''
    try:
        c = choice(range(len(L)))
        e = choice(range(len(L)))
        d = choice(range(len(P)))
        f = choice(range(len(P)))
        if eval(str(eval(a+L[c]+b))+P[d]+str(eval(a+L[e]+b)))== eval(a+P[f]+b):
            return([L[c],P[d],L[e],P[f],a,b])
    except:
        pass

# if eval(str(eval(a+Z[c]+b))+Z[d]+str(eval(a+Z[e]+b)))== eval(a+Z[f]+b):
# return([Z[c],Z[d],Z[e],Z[f],a,b])