n = int(input())   # จำนวนข้อมูล
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

count = 0
for num in numbers:
    if num > 50:
        count += 1

print("จำนวนที่มากกว่า 50:", count)