def factorial(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

def main():
    n = int(input("กรอกค่า n: "))
    print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()