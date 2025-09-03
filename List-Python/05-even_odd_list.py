n = int(input())      
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("เลขคู่:", even)
print("เลขคี่:", odd)