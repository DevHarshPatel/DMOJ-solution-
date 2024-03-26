N = int(input())
hat_numbers = [int(input()) for _ in range(N)]
count = 0

for i in range(N):   
    opposite_index = (i + N // 2) % N

    if hat_numbers[i] == hat_numbers[opposite_index]:
        count += 1

print(count)
