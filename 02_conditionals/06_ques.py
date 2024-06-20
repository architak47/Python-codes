distance = 5

if distance < 3:
    transport = "walk"
elif distance < 10:
    transport = "bike"
else:
    transport = "car"

print("your recommended mode of transport is", transport)