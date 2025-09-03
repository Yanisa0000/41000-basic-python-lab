n = int(input())   
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

filtered = [x for x in numbers if 10 <= x <= 50]

print("ค่าที่อยู่ในช่วง 10-50:", filtered)