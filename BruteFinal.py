from random import *
import sys
import timeit
import csv

A_operators = ['&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//', '~+', '**']

#Range of test values:
INITIAL_TEST_VALUE1 = 2
INITIAL_TEST_VALUE2 = 3

uglyCSV = False 

debug = False

def Main():
    '''Manages the computation and output of results'''
    if debug == True:
        confirmRun = input("Are you sure [yes/no]?\n")
        if confirmRun == "yes":
            GetIterativeResults()
    else:
        GetIterativeResults()

def GetIterativeResults():
    '''Gets output by iterating through all possible combinations of operators.'''
    if debug == True:
        print("Getting Results...")
    SetStep("Step 1/5:")
    results = GetResults()
    if debug == True:
        print("DONE")
        print("Filtering Duplicates...")
    SetStep("Step: 2/5:")
    results = FilterDuplicates(results)
    if debug == True:
        print("DONE")
        print("Removing Commutatively Identical Results...")
    SetStep("Step 3/5:")
    results = NetCommuteFilter(results)
    if debug == True:
        print("DONE")
        print("Verifying Results...")
    SetStep("Step 4/5:")
    results = VerifyResults(results)
    if debug == True:
        print("DONE")
        print("Classifying Results...")
    SetStep("Step 5/5:")
    results = SeparateTrivial(results)
    if debug == True:
        print("DONE!")
        print("Total Number of Results:", len(results[0]) + len(results[1]))
        print("Number of Trivial Results:", len(results[0]))
        print("Number of Non-Trivial Results:", len(results[1]))

    if saveAs.lower() == "csv":
        SaveResultsAsCSV(results[0] + results[1], "Final")
    elif saveAs.lower() == "txt":
        SaveResultsAsTXT(results, "Final")

def SetExport(s):
    ''' Defines the output file type'''
    saveAs = s
    global saveAs

def SetOperatorList(S):
    ''' Defines the bitwise list to be tested'''
    A_operators = eval(S)
    global A_operators

def GetStep():
    ''' DOCSTRING '''
    return step

def SetStep(s):
    ''' DOCSTRING '''
    step = s
    global step

def GetProgress():
    ''' Current progress of the evaluate function'''
    Current = counter
    Total = ResLen
    return Current/Total

def SaveResultsAsCSV(L, fileName):
    ''' Exports the results of the program into a CSV file'''
    resultsFile = open("brutewiseOpsResults" + str(fileName) + ".csv", "w", newline='')
    resultsFileWriter = csv.writer(resultsFile, delimiter=',')
    for row in L:
        resultsFileWriter.writerow(row)
    resultsFile.close()

def SaveResultsAsTXT(Results, fileName):
    '''EXports the results of the program as a txt file'''
    TotalAmount = 5
    text_file = open("BruteWiseResults" + str(fileName)+ ".txt", "w", newline='')
    text_file.write("Trivial Results:\n")
    text_file.write("====================\n")
    for row in Results[0]:
        text_file.write(str(row)+"\n")
    text_file.write("Non-Trivial Results:\n")
    text_file.write("====================\n")
    for row in Results[1]:
        text_file.write(str(row)+"\n")
    text_file.close()

def GetResults():
    '''Finds all candidate (possible) results.'''
    results = []
    numOne = INITIAL_TEST_VALUE1
    numTwo = INITIAL_TEST_VALUE2
    for op1 in range(len(A_operators)):
        for op2 in range(len(A_operators)):
            for op3 in range(len(A_operators)):
                for op4 in range(len(A_operators)):
                    answer = Evaluate(str(numOne),str(numTwo),op1,op2,op3,op4)
                    if answer != False:
                        results += [answer]
    return results

def VerifyResults(Results):
    ''' Verifies all results
    '''
    counter = 0
    VerRes = []
    ResLen = len(Results)
    global ResLen
    if debug == True:
        print("Number of Results Under Review:", len(Results))
    for i in Results:
        counter += 1
        global counter
        if Bit_8(i) == True:
            VerRes += [i]
        #TODO: fix
        #if counter % 500 == 0:
        #    SaveResultsAsCSV(VerRes, str(counter // 500))
    return VerRes

def VerifyExpression(expression, timesToCheck=1):
    ''' Input list in form ['op1', 'op2', 'op3', 'op4'] and a number timesToCheck
    Output: Runs '(A [op1] B) [op2] (A [op3] B) = A [op4] B' timesToCheck times.
    Returns True if this expression is True for all cases. '''
    for i in range(timesToCheck):
        if Bit_8(expression) == False:
            return False
    return True

def Evaluate(a,b,w,x,y,z):
    '''Takes two positive integers as strings and 4 operators and checks if (a op1 b) op2 (a op3 b) = a op4 b'''
    try:
        if eval(str(eval(a+A_operators[w]+b))+A_operators[x]+str(eval(a+A_operators[y]+b)))== eval(a+A_operators[z]+b):
            return [ A_operators[w],A_operators[x],A_operators[y],A_operators[z] ]
        else:
            return False
    except:
        return False

def FilterDuplicates(results):
    '''Filters out duplicates from a list.'''
    uniqueResults = []
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
    ''' Checks if any commutatively identical bitwise lists exist in Results
    '''
    CommuteResults = []
    n = []
    for i in range(len(Results)):
        for j in range(i + 1, len(Results)):
            if CommuteFilter(Results[i], Results[j]) == True:
                n += [i]
                break
    for k in range(len(Results)):
        if k not in n:
            CommuteResults += [ Results[k] ]
    return CommuteResults

def Bit_8(L):
    ''' Takes in a list of operators for a Type One expression and returns True if the expression is a valid bitwise expression up to an 8 bit number
    '''
    for i in range(256):
        for j in range(256):
            try:
                if eval(str(eval(str(i)+L[0]+str(j))) + L[1] + str(eval(str(i)+L[2]+str(j)))) == eval(str(i)+L[3]+str(j)):
                    continue
                else:
                    return False
            except:
                return False
    return True

def Bit_Big(L):
    ''' Takes in a list of operators for a Type One expression and returns True if the expression is a valid bitwise expression up to an 8 bit number
    '''
    for i in range(500):
        for j in range(500):
            try:
                if eval(str(eval(str(i)+L[0]+str(j))) + L[1] + str(eval(str(i)+L[2]+str(j)))) == eval(str(i)+L[3]+str(j)):
                    continue
                else:
                    return False
            except:
                return False
    return True

def SeparateTrivial(Results):
    ''' Separates result into Type 1 and Type 2 bitwise operates
    '''
    Type_1 = []
    Type_2 = []
    for i in Results:
        if i[0] == i[2] and i[2] == i[3]:
            Type_1 += [i]
        else:
            Type_2 += [i]
    return [Type_1, Type_2]

if __name__  == "__main__":
    Main()
