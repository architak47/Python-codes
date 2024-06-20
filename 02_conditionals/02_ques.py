age = 20
day = "Wednesday"

price = 12 if age >= 18 else 8

if(day == "Wednesday"):
    price = price - 2
    print("It's Wednesday! You get a discount!")

print("Ticket price for you is", price)