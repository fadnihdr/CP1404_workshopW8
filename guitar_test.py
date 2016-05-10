from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
fender = Guitar("Fender Stratocaster", 2014, 13054.23)


print(gibson.get_age())
print(fender.get_age())

print(gibson.is_vintage())
print(fender.is_vintage())

guitars = []

while True:
    name = str(input("Name:"))
    if name == "":
        break
    year = int(input("Year:"))
    cost = float(input("Cost:"))
    print("{} ({}) {} added".format(name,year,cost))
    guitars.append(Guitar(name,year,cost))
for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))