file = open('data.txt', 'r')

lines = file.readlines()

prev = 999999
increases = 0
sliding_increases = 0
past = []

for line in lines:
    curr = int(line)
    if curr > prev:
        increases += 1
    prev = curr
    if len(past) == 3:
        if sum(past) < (sum(past[1:]) + curr):
            sliding_increases += 1
        past = past[1:]
        past.append(curr)
    else:
        past.append(curr)

print(increases)
print(sliding_increases)
