sandwichOrders = ['ham', 'turkey', 'roast beef', 'italian']
finishedSandwiches = []

while sandwichOrders:
    orderUp = sandwichOrders.pop()
    print(f"The {orderUp.title()} Sandwich is now ready.")
    finishedSandwiches.append(orderUp)
print("The following sandwiches are now ready:")
for order in finishedSandwiches:
    print(f"{order.title()}")