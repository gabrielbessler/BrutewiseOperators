# Random Operator Generator
#
# Description:
# This program uses a brute force approach to finding a list of expressions
# involving bitwise operations and two numbers that are equivalent to normal
# base 10 operations between those same two numbers.
#
# Specifically:
#
# Take [x] as a bitwise operator (e.g. <<, >>, &, |)
# Take [y] as base a "base 10" operator (e.g. +, -, *, /)
# Take A, B to be two positive integers s.t. A > B
#
# Type One:
# (A [x] B) [y] (A [x] B) = A [y] B

from random import *

#List of basic bitwise operations
B_operators = ['<<', '>>', '&', '|' ]
#List of basic base 10 operations
T_operators = ['+', '-', '*', '/', '%']
#Method of finding expressions
#0 - Exhaustive Search (Interate through all posibilities for given sets of T_ops and B_ops)
#1 - Sampling (Pick random posibilities from within T_ops and B_ops)
COMP_METHOD = 1
#Number of iterations (Program will test REPEAT_NUM ^2 different expressions)
REPEAT_NUM = 10
#Range of values for which the expressions will be tested
MAX_TEST_VAL = 10000
MIN_TEST_VAL = 1
LOW_LOW_TEST_VAL = 1
HIGH_LOW_TEST_VAL = 100

def main():
    '''Manages the computation and output of results.'''
    #Valid expressions of Type One as stored as [B1, T1, B2, T2]
    Results = []
    NumberPairs = []
    #Number of iterations (Runs NUM^2 times)
    REPEAT_NUM = 10

    if COMP_METHOD == 0:
        #Exhaustive Search
        for op1 in B_operators:
            for op2 in T_operators:
                for op3 in B_operators:
                    for op4 in T_operators:
                        if calculate([str(op1), str(op2), str(op3), str(op4)]):
                            Results += [str(op1), str(op2), str(op3), str(op4)]
    elif COMP_METHOD == 1:
        #Sampling
        for n1 in range(REPEAT_NUM):
            for n2 in range(REPEAT_NUM):
                answer = r(str(n1), str(n2))
                if answer != False:
                    Results += [answer[0:4]]
                    NumberPairs += [answer[4:]]

    originalLenResults = len(Results)
    #Remove duplicates in Results
    Results = filter(Results)
    #Stores the percentage of duplicates found
    #TODO: Create function to remove commutativity duplicates (as in A+B=B+A)
    filteringEfficiency = (originalLenResults - len(Results))/originalLenResults

    #Checks if results are actually valid
    actualResults = []
    for i in Results:
        if calculate(i) == True:
            #TODO: Easier way to do this?
            correct = True
            timesToTest = 5
            while timesToTest > 0:
                if calculate(i) == False:
                    correct = False
                    break
                timesToTest -= 1
            if correct == True:
                actualResults += i
    print(actualResults)

def r(num1, num2):
    '''Input: Two integers: num1, num2
       Output: '''
    try:
        a = choice(range(len(B_operators)))
        b = choice(range(len(B_operators)))
        c = choice(range(len(T_operators)))
        d = choice(range(len(T_operators)))
        if eval(str(eval(num1+B_operators[a]+num2))+T_operators[b]+str(eval(num1+B_operators[c]+num2)))== eval(num1+T_operators[d]+num2):
            return([B_operators[a],T_operators[b],B_operators[c],T_operators[d],num1,num2])
        else:
            return False
    except:
        #Often a divide by zero error
        return False

def filter(L):
    '''Removes duplicate items from a list L'''
    if len(L) <= 1:
        return L
    if L[0] in L[1:]:
        return filter(L[1:])
    return L[0:1] + filter(L[1:])

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

#Initializer
if __name__ == "__main__":
    main()
