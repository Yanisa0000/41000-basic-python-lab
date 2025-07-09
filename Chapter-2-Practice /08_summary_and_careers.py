bill, tip, people = input("Enter bill, tip%, and number of people: ").split()

bill = float(bill)
tip = float(tip)
people = int(people)

total = bill + (bill * tip / 100)

amount = total / people

print(f"Each person pays: {round(amount, 2)}")