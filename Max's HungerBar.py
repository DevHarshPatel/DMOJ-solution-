hunger = int(input())
apples = int(input())
seconds = int(input())

if hunger <= apples:
    apples = hunger
left = apples-seconds
if left < 0:
    left = 0
print(left)
