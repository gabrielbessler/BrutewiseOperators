# Two digits:
from random import *
import sys
import timeit

#Dangerous
sys.setrecursionlimit = 1500
#If timing is enabled, python will use timeit() to output the time of each
#process in Main()
timeFunctions = True
displayingResults = False

Z = ['&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//']
#Z with most elements removed. Used for testing without crashing due to recursion max depth reached.
#Z = ['&', '|', '+']

def Main():
    '''DOCSTRING'''
    #Timeit Test Results:
    # ***** uniqueTime is causing the max recurs depth error, even though it
    # uses <1% of processing time ******
    # uniqueTime uses about 1/3
    # verify uses 2/3
    # BUG: getResults takes 10x as long every ~1/5 times

    #Optimization:
    #1) Use iteration instead of recursion?
    #2) Memoization?

    confirmRun = input("Are you sure [y/n]?\n")
    if confirmRun == "y":
        if timeFunctions == True:
            getResultsTime = []
            uniqueTime = []
            verifyResultsTime = []
            for i in range(3):
                results = []
                #Alternatively, could just use time.time() twice and find the difference
                #Might be more efficient to use timeit.default_timer (saw on stackoverflow)
                getResultsTime += [timeit.timeit(lambda: getResults(results), number = 1)]
                #DISABLED
                #=================================================================
                uniqueTime += [timeit.timeit(lambda: unique(results), number = 1)]
                #=================================================================
                verifyResultsTime += [timeit.timeit(lambda: verifyResults(results)[0], number = 1)]
            #TODO: learn printf
            print("Function getResults() time: " + str(getResultsTime) + "seconds")
            print("unique(): " + str(uniqueTime) + "seconds")
            print("Function verifyResults() time: " + str(verifyResultsTime) +"seconds")

        if timeFunctions == False:
            results = []
            results = getResults(results)
            results = unique(results)
            tempR = verifyResults(results)
            results = tempR[0]
            n = tempR[1]

def getResults(Results):
    '''DOCSTRING'''
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
    '''DOCSTRING'''
    n = 0
    #TODO: make sure this is actually working (doesn't seem like it is)
    for i in Results:
        if calculate(i) == True:
            correct = True
            numberOfTests = 20
            while numberOfTests > 0:
                if calculate(i) == False:
                    correct = False
                numberOfTests -= 1
            if correct == True:
                if displayingResults == True:
                    print(i)
                n+=1
    return (Results, n)

def test(L):
    '''DOCSTRING'''
    for j in range(2):
        if calculate(L) == False:
            return False
    return True

def evaluation(a,b,w,x,y,z):
    '''DOCSTRING'''
    try:
        if eval(str(eval(a+Z[w]+b))+Z[x]+str(eval(a+Z[y]+b)))== eval(a+Z[z]+b):
            return [ Z[w],Z[x],Z[y],Z[z] ]
    except:
        pass

def unique(L):
    '''DOCSTRING'''
    usingRecursion = False
    #Using Recursion to filter duplicates
    #Times: [0.022388404642697424, 0.013230643145107024, 0.00878131772242341]
    if usingRecursion == True:
        if len(L) <= 1:
            return L
        if L[0] in L[1:]:
            return unique(L[1:])
        return L[0:1] + unique(L[1:])
    else:
        #set() does not work (unhashable list)
        return L
        #WORK IN PROGRESS
        #res = []
        #
        #for i in range(len(L)):
        #    if L[i] not in L[i+1:]:
        #        res += L[i]
        #return res

def calculate(L):
    '''DOCSTRING'''
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
