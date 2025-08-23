def show_table(n, limit):
    i = 1
    while i <= limit:
        print(f"{n} × {i} = {n * i}")
        i += 1

def main():
    n = int(input("ใส่ค่าของ n: "))
    limit = int(input("ใส่ค่าของ limit: "))
    show_table(n, limit)

if __name__ == "__main__":
    main()