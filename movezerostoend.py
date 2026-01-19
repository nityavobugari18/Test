num = int(input("Enter the number of elements"))
l = []

for i in range(0, num):
    num = int(input(f"Enter the no {i+1} position"))
    l.append(num)
print(l)


for i in range(0, len(l)):
    if l[i] == 0:
        l.append(0)
        l.remove(0)

print(l)