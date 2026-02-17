guest = ['davie allison', 'alan kulwicki', 'dale earnhardt']
#
message_da28 = f'Hey, {guest[0].title()}, we would love to hear all about the 1988 Daytona 500. Come have dinner with us tomorrow.'
print(message_da28)
message_ak7 = f'Hey {guest[1].title()}, we would love to hear about the 1992 Hoooters 500 race in Atlanta. Come have dinner with us tomorrow'
print(message_ak7)
message_de3 = f'Hey {guest[2].title()} come have dinner with us tommorow and tell us all about the 1998 Dayona 500.'
print(message_de3)
print("Hey guys, I found a bigger table, I'm going to invite a few more people.")
guest.insert(0, 'adam petty')
guest.append('jimmy means')
guest.insert(3, 'neil bonnett')
guest.sort()
# (0-adam petty)(1-alan kulwicki)(2-dale earnhardt)(3-davie allison)(4-jimmy means)(5-neil bonnett)
print(message_da28)
print(message_ak7)
print(message_de3)
message_ap45 = f'Hey {guest[0].title()}, it would be an honor if you would come have dinner with us tomorrow.'
print(message_ap45)
message_nb51 = f'Hey {guest[5].title()}, it would be an honor if you would come have dinner with us tomorrow.'
print(message_nb51)
message_jm52 = f'Hey {guest[4].title()}, you are my favorite driver of the owner/driver era in NASCAR. Please come have dinner with us tomorrow.'
print(message_jm52)
print(f"The first three drivers in the list are {guest[:3]}")
print(f"Three drivers from the middle of the list are {guest[2:4]}")
print(f"Three drivers from the end of the list are {guest[-3:]}")