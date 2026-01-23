d = {"Nitya": 9, "Pranav": 8, "Navya": 4, "Sam":7, "Ria": 10}


largest = float('-inf')
second = float('-inf')

for i in d.values():
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print(largest)
print(second)
