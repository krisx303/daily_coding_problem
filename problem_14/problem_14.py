import random

x = 10
y = 10
r = 10
points = 0


for _ in range(2000000):
    xp = random.uniform(-x, x)
    yp = random.uniform(-y, y)
    if xp**2 + yp**2 <= r**2:
        points += 1

print(4*points/2000000)

