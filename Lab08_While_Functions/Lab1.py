def main():
    total = 0
    while True:
        x = int(input())
        if x == 0:
            break
        total += x
    print(f"ผลรวม: {total}")

if __name__ == "__main__":
    main()