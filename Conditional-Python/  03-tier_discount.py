amount = float(input())

if amount > 2000:
    discount = 0.15
elif amount > 1000:
    discount = 0.10
elif amount > 500:
    discount = 0.05
else:
    discount = 0.0

net_price = amount * (1 - discount)

print(net_price)
