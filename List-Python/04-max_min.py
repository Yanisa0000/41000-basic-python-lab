n = int(input())          # จำนวนข้อมูล
numbers = []
for _ in range(n):
    num = int(input())    # อ่านค่าทีละตัว
    numbers.append(num)

print("มากที่สุด:", max(numbers))
print("น้อยที่สุด:", min(numbers))