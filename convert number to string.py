d = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

num = int(input())

answer = []


while num > 0:
    last_digit = num % 10
    answer.append(d[last_digit])
    num = num//10


answer.reverse()

print(" ".join(answer))

