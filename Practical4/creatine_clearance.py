# pseudocode step 1: save the person's information
age = 25
weight = 60
gender = "female"
cr = 80

# pseudocode step 2: check whether the input values are valid
if age >= 100:
    print("age is wrong")
elif weight <= 20 or weight >= 80:
    print("weight is wrong")
elif cr <= 0 or cr >= 100:
    print("cr is wrong")
elif gender != "male" and gender != "female":
    print("gender is wrong")
else:
    # pseudocode step 3: calculate creatinine clearance using the formula
    answer = ((140 - age) * weight) / (72 * cr)

    # pseudocode step 4: adjust the result if the person is female
    if gender == "female":
        answer = answer * 0.85

    # pseudocode step 5: print the final result
    print("CrCl =", answer)