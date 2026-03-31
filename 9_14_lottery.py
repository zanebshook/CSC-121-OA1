from random import choice
loto_characters = ['8', '6', '7', '5', '3', '0', '9', '12', '16', '24', 'p', 
                   'h', 'o', 'n', 'e']
winning_ticket = ['8', '5', '3', '9', 'h']

purchased_ticket = []
chosen_number = input("Enter any number below 100:")
purchased_ticket.append(chosen_number)
chosen_number = input("Enter any number below 100:")
purchased_ticket.append(chosen_number)
chosen_number = input("Enter any number below 100:")
purchased_ticket.append(chosen_number)
chosen_number = input("Enter any number below 100:")
purchased_ticket.append(chosen_number)
chosen_letter = input("Enter a letter:")
purchased_ticket.append(chosen_letter)

if purchased_ticket == winning_ticket:
    print("You are the winner!")
else: print("Sorry, better luck next time.")