# Two digits:
from random import *
import sys
import timeit
import csv

#If enabled, outputs runtime of key functions
timeFunctions = False
#If enabled, prints results in CMD
displayingResults = False
#Results will be exported in a CSV file
exportResults = True

B_operators = ['<<', '>>', '&', '|' ] #basic biwise ops
T_operators = ['+', '-', '*', '/', '%'] #basic real ops
A_operators = ['&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//'] #larger set of both bitwise and real ops

#Range of test values:
INITIAL_TEST_VALUE_MAX = 100 #potential results range
MIN_TEST_VAL = 1
MAX_TEST_VAL = 10000
LOW_LOW_TEST_VAL = 1
HIGH_LOW_TEST_VAL = 100

#Method 1 = Sampling
#Method 2 = Iteration (Exhaustive)
COMP_METHOD = 2
REPEAT_NUM = 100 # number of iterations for sampling

def Main():
    '''Manages the computation and output of results'''
    confirmRun = input("Are you sure [y/n]?\n")
    if confirmRun == "y":
        if timeFunctions == True:
            TimeFuncs()
        if timeFunctions == False:
            if COMP_METHOD == 1:
                #TODO: This
                print("Work in progress...")
            elif COMP_METHOD == 2:
                GetIterativeResults()

def GetIterativeResults():
    '''Gets output by iterating through all possible combinations of operators.'''
    results = GetResults()
    results = FilterDuplicates(results)
    results = VerifyResults(results)
    results = NetCommuteFilter(results)
    results = tempR[0]
    n = tempR[1]
    if exportResults == True:
        #TODO: output this at the top of the CSV
        SaveResultsAsCSV(results)

def TimeFuncs():
    '''Finds the time it takes to run each of the functions in the program
    (for debugging/optimization).'''

    getResultsTime = []
    filterDuplicatesTime = []
    netCommuteFilterTime = []
    verifyResultsTime = []

    for i in range(3):
        results = []
        getResultsTime += [timeit.timeit(lambda: GetResults(results), number = 1)]
        filterDuplicatesTime += [timeit.timeit(lambda: FilterDuplicates(results), number=1)]
        netCommuteFilterTime += [timeit.timeit(lambda: NetCommuteFilter(results), number = 1)]
        verifyResultsTime += [timeit.timeit(lambda: VerifyResults(results)[0], number = 1)]

    print("Function getResults() time: " + str(getResultsTime) + "seconds")
    print("Function FilterDuplicates(): " + str(filterDuplicatesTime) + "seconds")
    print("Function NetCommuteFilter() time: " + str(netCommuteFilterTime) + "seconds")
    print("Function VerifyResults() time: " + str(VerifyResultsTime) +"seconds")

def SaveResultsAsCSV(L):
    ''' Exports the results of the program into a CSV file'''

    resultsFile = open("brutewiseOpsResults.csv", "w", newline='')
    resultsFileWriter = csv.writer(resultsFile, delimiter=',')

    for row in L:
        resultsFileWriter.writerow(row)
    resultsFile.close()

def GetResults():
    '''Finds all candidate (possible) results.'''
    results = []

    #Picks two values to test expressions (in the smaller INITIAL_TEST_VALUE_MAX range)
    numOne = choice(range(INITIAL_TEST_VALUE_MAX))
    numTwo = choice(range(INITIAL_TEST_VALUE_MAX))

    #Iterates through all possible permutations of A_ops for 4 operators.
    for op1 in range(len(A_operators)):
        for op2 in range(len(A_operators)):
            for op3 in range(len(A_operators)):
                for op4 in range(len(A_operators)):
                    answer = Evaluate(str(numOne),str(numTwo),op1,op2,op3,op4)
                    if answer != False:
                        results += [answer]
    return results

def VerifyResults(Results):
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

def VerifyExpression(expression, timesToCheck=2):
    ''' Input list in form ['op1', 'op2', 'op3', 'op4'] and a number timesToCheck
    Output: Runs '(A [op1] B) [op2] (A [op3] B) = A [op4] B' timesToCheck times.
    Returns True if this expression is True for all cases. '''
    for i in range(timesToCheck):
        if calculate(expression) == False:
            return False
    return True

def Evaluate(a,b,w,x,y,z):
    '''Takes two positive integers as strings and 4 operators and checks if (a op1 b) op2 (a op3 b) = a op4 b'''
    try:
        if eval(str(eval(a+A_operators[w]+b))+A_operators[x]+str(eval(a+A_operators[y]+b)))== eval(a+A_operators[z]+b):
            return [ A_operators[w],A_operators[x],A_operators[y],A_operators[z] ]
    except:
        return False

def FilterDuplicates(results):
    '''Filters out duplicates from a list.'''
    uniqueResults = []
    
    #For each item in Results, it checks if that same item is in the rest of the list
    for i in range(len(results)):
        if results[i] not in results[i+1:]:
            uniqueResults += results[i:i+1]
    return uniqueResults

def CommuteFilter(L1, L2):
    '''Checks if two lists are commutatively identical'''
    if L1[0] == L2[2] and L1[2] == L2[0]:
        if L1[3] == L2[3]:
            if L1[1] == '+' and L2[1] == '+':
                return True
            elif L1[1] == '*' and L2[1] == '*':
                return True
    return False

def NetCommuteFilter(Results):
    '''Filters out commutatively identical lists'''
    ComRes = []
    for i in range(len(Results)):
        if i == len(Results) - 1:
            ComRes += [Results[i]]
        for j in range( i+1, len(Results) ):
            if CommuteFilter(Results[i], Results[j]) == True:
                break
            else: 
                ComRes += [ Results[i] ]
    return ComRes 

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
        return False
    except:
        return False

if __name__  == "__main__":
    Main()
