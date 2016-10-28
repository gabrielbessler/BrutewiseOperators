## Brutewise Operators Program
### A Random Operator Generator

#### Goal:
Find interesting patterns in expressions involving a combination of real and bitwise operators.

#### Description
This program uses a brute force approach to finding a list of expressions
involving bitwise operations and two numbers that are equivalent to normal
base 10 operations between those same two numbers.

### Current Results

#### Type One Equation
(A *x1* B) *y1* (A *x2* B) = A *y2* B

*x1*, *x2* are elements of {'<<', '>>', '&', '|' }

*y1*, *y2* are elements of {'+', '-', '*', '/', '%', '**'}

#### Type Two Equations

(A *x1* B) *x2* (A *x3* B) = A *x4* B

*x1*, *x2*, *x3*, *x4* are elements of {'&', '|', '+', '-', '*', '/', '%', '^', '<<', '>>', '//'}

### Current Implementation

Type one equations can be found with RandomOperator.py

Type two equations can be found with Operator2.py
