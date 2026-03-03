favorite_places = {
    'hank' : ['charlotte', 'myrtle beach', 'florida'],
    'brett' : ['alaska', 'argentina', 'tennessee'],
    'rachael' : ['greece', 'italy', 'london'],
}
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")