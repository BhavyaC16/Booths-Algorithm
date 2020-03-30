# Booths-Algorithm
Implementing Booth's Algorithm for multiplication and division

Developed by Bhavya Chopra and Sonali Singhal

## Booth’s Multiplication Algorithm

[STEP 1]

 - Assign the multiplicand (x) to M.
 - Assign the multiplier (y) to Q.
 - Initialize q0 to 0.
 - Initialize q1 to the lowest bit of Q.
 - Assign the two’s complement of M to negM.
 - Initialize n to the maximum of bits required for the representation of M and Q.
 - Initialize A to 0.
 
[STEP 2]

 - Check if n>0.
 - If YES, move to step 3.
 - If NO, terminate the operation with AQ as the result of the multiplication.
 
[STEP 3]

 - Check the value of q1q0 .
 - If q1q0 is 01, perform A = A+M.
 - If q1q0 is 10, perform A = A-M = A+negM.
 - If q1q0 is 00 or 11, proceed to next step.
 
[STEP 4]

 - Right Shift AQ.
 - The most significant bit is retained when shifting. (For Example: 1101 ➝ 1110, and 0110 ➝ 0011)
 
[STEP 5]
 - Decrement the value of n (Perform n = n-1).
 - Go back to Step 2.

## Booth’s Division Algorithm

[STEP 1]

 - Assign the dividend (x) to Q.
 - Assign the divisor (y) to M.
 - Initialize q1 to the lowest bit of Q.
 - Assign the two’s complement of M to negM.
 - Initialize n to the maximum of bits required for representation of M and Q.
 - Initialize A to 0.

[STEP 2]

 - Check if A<0.
 - If YES, Left Shift AQ, and perform A = A+M.
 - If NO, Left Shift AQ, and perform A = A-M = A+negM.

[STEP 3]

 - Check if A<0. 
 - If YES, set q1 to 0.
 - If NO, set q1 to 1.

[STEP 4]

 - Decrement n by 1 (Perform n = n-1).
 
[STEP 5]

 - Check if n=0.
 - If NO, go to Step 2
 - If YES, proceed to the next step.
 
[STEP 6]

 - Check if A<0.
 - If YES, perform A = A+M.
 - Assign the value of Q to the quotient.
 - Assign the value of A to the remainder.
 
[STEP 7]

 - If x and y have opposite signs, take two’s complement of quotient.
 - If x is negative, take two’s complement of remainder.


## Complexity Analysis

### Multiplication Algorithm: 

n represents the maximum number of bits required to represent x (multiplicand) and y (multiplier). 

Then, 

n = max(bits(x), bits(y)) = max( log<sub>2</sub>x, log<sub>2</sub>y) = log n

The algorithm loops over the constant time complexity steps (O(1)) (comparison and shift operations), or O(n) steps (addition operation), for as many number of times as the number of bits required to represent the larger number amongst the multiplier and the multiplicand.

Hence, time complexity of operation = O(n2).

Also, the memory required for the operation is dependent on the space required for A, Q and M, and negM, which is n bits respectively. Thus, space complexity of operation = O(n).

### Division Algorithm: 

n represents the maximum number of bits required to represent x (dividend) and y (divisor).

Then, n = max(bits(x), bits(y)) = max( log2x, log2y). =log n 

The algorithm loops over the constant time complexity steps (O(1)) (comparison and shift operations), or O(n) steps (addition operation), for as many number of times as the number of bits required to represent the larger number amongst the divisor and dividend.

Hence, time complexity of operation = O(n2).

Also, the memory required for the operation is dependent on the space required for A, Q and M, and negM, which is n bits respectively. Thus, space complexity of operation = O(n).



## Test cases

## Flow Diagrams
