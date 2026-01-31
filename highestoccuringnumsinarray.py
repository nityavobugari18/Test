
n = int(input("Enter the number of elements"))
l = []

for i in range(0, n):
    num = int(input(f"Enter a number: "))
    l.append(num)

print(l)

d = {}

for i in range(0, len(l)):
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1


answer = float("-inf")
maximum_frequency = 0


for i in d.keys():
    if d[i] > maximum_frequency:
        maximum_frequency = d[i]
        answer = i

print(answer)