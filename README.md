## Question:

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

 

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773


## Solution:
What needs to be calculated:
1. Total number of valid attendance sequences for N days
2. Number of sequences that results in missing the ceremony on the last day

### States:
* T(n) - Total number of valid sequences
* M(n) - Total number of missing sequences

### Steps:
A - Attend, 
M - Miss
Total valid possibilities for T(n):
* T(0) - 1 (only one possibility not attending ceremony)
* T(1) - 2 (A)
* T(2) - 4 (AA, AM, MA, MM)
* T(3) - 8 = 2*4 not (MMM possibility in T(2)) - (AAA, AAM, AMA, AMM, MAA, MAM, MMA, MMM)
* T(4) - 2*8 -1 = 15 as there would be one MMMM possibility which is not allowed

Total valid missing possibilities for M(n):
* M(0) = 0
* M(1) = 1 (M)
* M(2) = 2 (MA, MM)
* M(3) = 1*4 (MAA, MAM, MMA, MMM) i.e. Total possibility of T(2)*1
* M(4) = 1*8 -1 = 7 i.e. total possibility of T(3) - number of MMM in T(3)
* M(5) = 1*15-1 = 14 i.e. total possibility of T(4) -number of MMMA in T(4)
as we don't want to break the rule of no 4 or more consecutive missing days


This deduces the correlation - 

 T(N) = 2*T(N-1) - T(N-5)

 M(N) = T(N-1) - T(N-5)

# Requirements 
* python 3 or above

## Execution 

python .\src\attendance_solution.p.py


    



