def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def main():
    while True:
        print("\n--- เมนูเครื่องคิดเลข ---")
        print("1. บวกเลขสองจำนวน")
        print("2. ลบเลขสองจำนวน")
        print("3. คูณเลขสองจำนวน")
        print("4. ออก")

        choice = input("เลือกเมนู: ")

        if choice == "4":
            print("จบโปรแกรม")
            break
        elif choice in ["1", "2", "3"]:
            a = float(input("ใส่ตัวเลขที่ 1: "))
            b = float(input("ใส่ตัวเลขที่ 2: "))

            if choice == "1":
                print(f"ผลลัพธ์: {add(a, b)}")
            elif choice == "2":
                print(f"ผลลัพธ์: {sub(a, b)}")
            elif choice == "3":
                print(f"ผลลัพธ์: {mul(a, b)}")
        else:
            print("กรุณาเลือกเมนู 1-4 เท่านั้น")

if __name__ == "__main__":
    main()