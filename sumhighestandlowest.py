def getHighestFreq(l, d):
    result = float("-inf")
    maximum_frequency = 0

    for i in d.keys():
        if d[i]> maximum_frequency:
            maximum_frequency = d[i]
            result = i

    return result

def getLowestFreq(l, d):
    result2 = float("inf")
    minimum_frequency = float("inf")

    for i in d.keys():
        if d[i] < minimum_frequency:
            minimum_frequency = d[i]
            result2 = i

    return result2





n = int(input("Enter the number of elements"))
l = []

for i in range(0, n):
    num = int(input(f"Enter a number: "))
    l.append(num)

print(l)

d ={}

for i in range(0, len(l)):
    if l[i] in d:
        d[l[i]] += 1
    if l[i] not in d:
        d[l[i]] = 1

    

    



higher = getHighestFreq(l, d)
lower = getLowestFreq(l, d)
print(higher, lower)


print(higher + lower)