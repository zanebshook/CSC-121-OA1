motorcycles = ['honda', 'yamaha', 'kawasaki', 'suzuki', 'ktm']
# (0-honda)(1-yamaha)(2-kawasaki)(3-suzuki)(4-ktm)
print(f'About {motorcycles[0].title()}:')
message_0 = f"Chase Sexton broke the 21 year long '{motorcycles[0].title()}'\
 curse when he won his first Supercross Championship in 2023."
print(message_0)
print(f'About {motorcycles[1].title()}:')
message_1 = f"Cooper Webb won the Supercross Championship aboard a\
 {motorcycles[1].title()} in 2025, he has now won the series on 2 brands;\
 {motorcycles[1].title()} and {motorcycles[4].upper()}."
print(message_1)
print(f'About {motorcycles[2].title()}:')
message_2 = f"Sexton finished second in the series in 2025 riding a\
 {motorcycles[4].upper()}, this season he is riding a {motorcycles[2].title()}\
 and believes this is the machine he needs to win his second Supercross\
 Championship."
print(message_2)
print(f'About {motorcycles[3].title()}:')
message_3 = f"{motorcycles[3].title()} has not won the Supercross Championship\
 since 2010, when Ryan Dungey won his first of 4 Supercross Championships."
print(message_3)
print(f'About {motorcycles[4].upper()}:')
message_4 = f"In 2017, Canton, NC native Shane McElrath won his first ever\
 Supercross race at the season opener in the 250 class aboard a\
 {motorcycles[4].upper()}. Throughout his professional career, Shane has raced\
 for every OEM except for {motorcycles[2].title()}."
print(message_4)