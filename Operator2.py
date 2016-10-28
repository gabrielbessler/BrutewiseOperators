# Two digits:
from random import *
import sys
import timeit
import csv

#Dangerous
sys.setrecursionlimit = 1500
#If timing is enabled, python will use timeit() to output the time of each
#process in Main()
timeFunctions = False
displayingResults = False
#Results will be exported in a CSV file
exportResults = True

Z = ['&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//']
#Z with most elements removed. Used for testing without crashing due to recursion max depth reached.
#Z = ['&', '|', '+']

#Values exploited in code:
initial_test_value = 100
MIN_TEST_VAL = 10000
MAX_TEST_VAL = 1
LOW_LOW_TEST_VAL = 1
HIGH_LOW_TEST_VAL = 100

def Main():
    '''DOCSTRING'''
    #Timeit Test Results:
    # ***** uniqueTime is causing the max recurs depth error, even though it
    # uses <1% of processing time ******
    # uniqueTime uses about 1/3
    # verify uses 2/3
    # BUG: getResults takes 10x as long every ~1/5 times

    #Optimization:
    #1) Use iteration instead of recursion? Check (see unique below).
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
            results = NetCommuteFilter(results)
            results = verifyResults(results)
            results = tempR[0]
            n = tempR[1]                        # is this necessary?
            if exportResults == True:
                saveResultsAsCSV(results)

def saveResultsAsCSV(L):
    #We will be using a CSV (comma separated values) file to save results.
    #This file-type is supported in python and can be used in excel/various programs.

    #filename, mode = writing,
    #with open("brutewiseOpsResults.csv", "w", newline='') as csv_file:
    #    writer = csv.writer(csv_file, delimiter=',')
    #    for line in L:
    #        writer.writerow(line)

    #need to set newline='' otherwise it will add a \n after every line
    resultsFile = open("brutewiseOpsResults.csv", "w", newline='')
    resultsFileWriter = csv.writer(resultsFile, delimiter=',')

    #Alternative?
    #resultsFileWriter.writerows(L)

    for i in L:
        resultsFileWriter.writerow(i)
    resultsFile.close()

def getResults(Results):
    '''DOCSTRING'''
    test = initial_test_value
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
    '''verifyResults() iterates through the list of possible results and
    checks each one several times using calculate().
    Returns the updated list of results.'''
    n = 0
    tempRes = []
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
                tempRes += [i]
                n+=1
    return (tempRes, n)

def test(L, N=2):
    """Input list in form ['op1', 'op2', 'op3', 'op4'] and a number N.
    Output: Runs '(A [op1] B) [op2] (A [op3] B) = A [op4] B' N times.
    Returns True if this expression is True all N times. """
    for j in range(N):
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

def unique(Results):
    '''Filters out duplicates from a list.'''
    UniRes = []
    for i in range(len(Results)):
        if Results[i] not in Results[i+1:]:
            UniRes += Results[i:i+1]
    return UniRes  
#TODO: Functions in between the lines below need work. They are not currently operating correctly! 
#There are two because one may be better than the other.
# ------------------------------------------------------------------------------
def NetCommuteFilter1(Results):
    '''Filters out commutatively identical lists'''
    ComRes = []
    for i in range(len(Results)):
        for j in range( i+1, len(Results) ):
            ComRes += CommuteFilter1(Results[i], Results[j])
    ComRes = unique(ComRes)
    return ComRes


def CommuteFilter1(L1, L2):
    '''Checks if two lists are commutatively identical'''
    if L1[1] == '+' and L2[1] == '+' and L1[3] == L2[3]:
        if L1[0] == L2[2] and L1[2] == L2[0]:
            return L1
    elif L1[1] == '*' and L2[1] == '*' and L1[3] == L2[3]:
        if L1[0] == L2[2] and L1[2] == L2[0]:
            return L1
    return [L1]+[L2]

def CommuteFilter(L1, L2):
    '''Checks if two lists are commutatively identical'''
    if L1[0] == L2[2] and L1[2] == L2[0]:
        if L1[3] == L2[3]:
            if L1[1] == '+' and L2[1] == '+':
                return True
            elif L1[1] == '*' and L2[1] == '*':
                return True
    else:
        return False

def NetCommuteFilter(Results):
    '''Filters out commutatively identical lists'''
    ComRes = []
    for i in range(len(Results)):
        for j in range( i+1, len(Results) ):
            if CommuteFilter(Results[i], Results[j]) == False:
                ComRes += [ Results[i] ]
    return ComRes
# --------------------------------------------------------------------
def calculate(L):
    '''Takes a list of operators for a Type One expression and returns True if the expression is valid.'''
    a = choice(range(MIN_TEST_VAL,MAX_TEST_VAL))
    b = choice(range(MIN_TEST_VAL,MAX_TEST_VAL))
    c = choice(range(LOW_LOW_TEST_VAL,HIGH_LOW_TEST_VAL))
    try:
        if eval( str(eval('a'+L[0]+'b')) + L[1] + str(eval('a'+L[2]+'b')) ) == eval('a'+L[3]+'b'):
            if eval( str(eval('a'+L[0]+'c')) + L[1] + str(eval('a'+L[2]+'c')) ) == eval('a'+L[3]+'c'):
                if eval( str(eval('c'+L[0]+'b')) + L[1] + str(eval('c'+L[2]+'b')) ) == eval('c'+L[3]+'b'):
                    if eval( str(eval('a'+L[0]+'a')) + L[1] + str(eval('a'+L[2]+'a')) ) == eval('a'+L[3]+'a'):
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
