quantity = int(input("Enter the number of tickets you will need to purchase: "))
tickets = [] #prices of tickets as ages are input
while quantity > 0:
    age = int(input("Enter the age of the ticket holder: "))
    if 2 < age < 13:
        childCost = 10
        tickets.append(childCost)
        quantity -= 1
    elif age > 12:
        adultCost = 15
        tickets.append(adultCost) 
        quantity -= 1
    else:
        quantity -= 1
print(f"Your total for today will be ${sum(tickets)}")









