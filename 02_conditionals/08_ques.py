mypass = "secure34*54"


if len(mypass) < 6:
    strength = "weak"
elif len(mypass) <= 10:
    strength = "medium"
else:
    strength = "strong"
    
print("Password strength: ", strength)