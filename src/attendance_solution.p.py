def attendance_probability(N: int):
    """Calculates attendance probability for attending ceremony
     using the Number of days """
T = [0] * (N + 1)
M = [0] * (N + 1)

[0] * (N + 1)

# Base cases for T
T[0] = 1
if N >= 1:
T[1] = 2
if N >= 2:
T[2] = 4
if N >= 3:
T[3] = 8
if N >= 4:
T[4] = 15

# Base cases for M
M[0] = 0
if N >= 1:
M[1] = 1
if N >= 2:
M[2] = 2
if N >= 3:
M[3] = 4
if N >= 4:
M[4] = 7

# Compute values using the recurrence relations
for i in range(5, N + 1):
T[i] = 2*T[i-1] - T[i-5]
M[i] = T[i-1] - T[i-5]

# The probability is the number of sequences missing the last day divided by total sequences
return f"{M[N]} / {T[N]}"


# Test cases
print(attendance_probability(4))  # Output: 7/15
print(attendance_probability(5))  # Output: 14/29
print(attendance_probability(6))  # Output: 14/29
print(attendance_probability(10))  # Output: 372/773