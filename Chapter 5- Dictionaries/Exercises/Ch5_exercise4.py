Rivers = {
    'nile': 'egypt',
    ' Amazon River': 'South America',
    'Yellow River ': 'china',
    ' Niger': 'West Africa',
    'yangtze': ' Eurasia',
    }

for River, country in Rivers.items():
    print("The " + River.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for River in Rivers.keys():
    print("- " + River.title())

print("\nThe following countries are included in this data set:")
for country in Rivers.values():
    print("- " + country.title())
