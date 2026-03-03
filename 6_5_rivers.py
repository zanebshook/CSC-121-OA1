rivers = {
    'french broad river': 'america',
    'river thames': 'england',
    'ganges river': 'india'
}

for river, location in rivers.items():
    print(f"The {river.title()} River is located in {location.title()}")