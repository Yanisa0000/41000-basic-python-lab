n = int(input())         
numbers = []
for _ in range(n):
    num = int(input())   
    numbers.append(num)

print("ลิสต์เดิม:", numbers)
numbers.sort()           
print("ลิสต์ที่เรียงแล้ว:", numbers)