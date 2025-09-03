a = input()
b = input()

a_lower = a.lower()
b_lower = b.lower()

if a_lower < b_lower:
    print("A comes before B")
elif a_lower > b_lower:
    print("A comes after B")
else:
    print("A equals B")