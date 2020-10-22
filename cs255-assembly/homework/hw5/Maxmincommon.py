A = [2,45,6,4]
B = [3,6,5,7,8]

max = A[0]
min = A[0]
sum = 0
for i in A:
    sum += i
    if max < i:
        max = i
    if min > i:
        min = i

for i in B:
    sum += i
    if max < i:
        max = i
    if min > i:
        min = i

count = 0
for i in A:
    for j in B:
        if i == j:
            count += 1

print(max)
print(min)
print(sum)
print(count)