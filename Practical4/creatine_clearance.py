# save person's information
age = 25
weight = 60
gender = "female"
cr = 80
# check if the values are okay first
if age >= 100:
    print("age is wrong")
elif weight <= 20 or weight >= 80:
    print("weight is wrong")
elif cr <= 0 or cr >= 100:
    print("cr is wrong")
elif gender != "male" and gender != "female":
    print("gender is wrong")
else:
    # do the formula
    answer = ((140 - age) * weight) / (72 * cr)
    # female needs 0.85
    if gender == "female":
        answer = answer * 0.85
    print("CrCl =", answer)