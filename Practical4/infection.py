# set the starting number of infected students
infected = 5
# set the growth rate for every 24 hours
growth_rate = 0.4
# total number of students in IBI1 class
total_students = 91
# start counting days
day = 1
# print the number infected on the first day
print("Day", day, ":", infected, "students infected")
# keep going until all students are infected
while infected < total_students:
    # move to next day
    day = day + 1
    # calculate new number of infected students
    infected = infected + infected * growth_rate
    # if infected number is bigger than total students, stop at 91
    if infected > total_students:
        infected = total_students
    # print infected students for this day
    print("Day", day, ":", infected, "students infected")
# print total days needed
print("It took", day, "days to infect all students.")
