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
#

from random import *

#List of basic bitwise operations
B_operators = ['<<', '>>', '&', '|' ]
#List of basic base 10 operations
T_operators = ['+', '-', '*', '/', '%']
#Previous list including x^n
T2_operators = ['+', '-', '*', '/', '%', '**']
#List containing both bitwise and base 10 operations
All_operators = ['<<', '>>', '&', '|', '+', '-', '*', '/', '%', '**']
#Method of finding expressions
#0 - Exhaustive Search (Interate through all posibilities for given sets of T_ops and B_ops)
#1 - Sampling (Pick random posibilities from within T_ops and B_ops)
COMP_METHOD = 1
#Number of iterations (Program will test REPEAT_NUM ^2 different expressions)
REPEAT_NUM = 10

def Main():
    '''Manages the computation and output of results.'''
    #Stores all of the results
    #Valid expressions of Type One as stored as [B1, T1, B2, T2]
    Results = []
    
    #TODO: Remove? Or add as internal testing feature?
    NumberPairs = []    
    
    #Number of iterations (Caution: runs NUM^2 times)
    REPEAT_NUM = 10
        
    if COMP_METHOD == 0:
        #Exhaustive Search
        return 0
    elif COMP_METHOD == 1:
        #Sampling
        for n1 in list(range(REPEAT_NUM)):
            for n2 in list(range(REPEAT_NUM)):
                answer = r(str(n1), str(n2))
                if answer != None:
                    Results += [answer[0:4]]
                    NumberPairs += [answer[4:]] 
                    
    originalLenResults = len(Results)
    #Remove duplicates in Results
    Results = filter(Results)
    #Stores the percentage of duplicates found
    filteringEfficiency = (originalLenResults - len(Results))/len(results)
    
    #Checks if results are actually valid
    for i in Results:
        if calculate(i) == True:
            #TODO: Easier way to do this?
            correct = True
            timesToTest = 5
            while timesToTest > 0: 
                if calculate(i) == False:
                    correct = False
                    break
                j -= 1
            if correct == True:
                print(i)
                
def r(num1, num2):
    '''Input: Two integers: num1, num2
       Output: '''
    try:
        a = choice(range(len(B_operators)))
        b = choice(range(len(B_operators)))
        c = choice(range(len(T_operators)))
        d = choice(range(len(T_operators)))
        if eval(str(eval(num1+L[a]+num2))+P[b]+str(eval(num1+L[c]+num2)))== eval(num1+P[d]+num2):
            return([L[a],P[b],L[c],P[d],num1,num2])
    except:
        #Often a divide by zero error
        pass
    
def filter(L):
    '''Removes duplicate items from a list L'''
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
        return False
    except: 
        pass

#Initializer  
if __name__ == "__main__":
    main()
    
# if eval(str(eval(a+Z[c]+b))+Z[d]+str(eval(a+Z[e]+b)))== eval(a+Z[f]+b):
# return([Z[c],Z[d],Z[e],Z[f],a,b])
