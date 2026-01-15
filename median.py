n = int(input("Enter the number of elements"))

lst = []

for i in range(n):
    num = int(input(f"Enter the number {i+1} " ))
    lst.append(num)
    
lst.sort()


if n%2 == 1:
    median = lst[n//2]
else:
    median = ((lst[n//2] + lst[n//2 -1])/2)
    
print(median)
