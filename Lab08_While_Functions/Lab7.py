def main():
    numbers = []

    while True:
        data = input()
        if data == "end":
            break
        try:
            num = float(data)  
            numbers.append(num)
        except ValueError:
            print("กรุณากรอกตัวเลขหรือ end")

    if len(numbers) == 0:
        print("ไม่มีข้อมูล")
    else:
        print(f"ค่าสูงสุด: {max(numbers)}")
        print(f"ค่าต่ำสุด: {min(numbers)}")

if __name__ == "__main__":
    main()