steps = [1, 2]

N = 4

staircase = [0] * (N + 1)

staircase[0] = 1  # there is only one way to climb up 0 stairs (without moving)

for i in range(1, N+1):
    for step in steps:
        if i > step-1:
            staircase[i] += staircase[i-step]

print(staircase)
print(staircase[N])
