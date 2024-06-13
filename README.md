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
1. Total valid possibilities for T(n):

    



