# Start with the initial number of infected students
infected = 5
# Set the daily growth rate
growth_rate = 0.4
# Store the class size
class_size = 91
# Start counting days
day = 1
# Display the number of infected students on day 1
print("Day", day, ":", infected, "students infected")
# Keep calculating until the whole class is infected
while infected < class_size:
    # Move to the next day
    day = day + 1
     # Increase infected students by the growth rate
    infected = infected + infected * growth_rate
    # If infected goes above class size, set it to class size
    if infected > class_size:
        infected = class_size
        # Display the result for that day
    print("Day", day, ":", infected, "students infected")
# Report the total number of days taken
print("It took", day, "days to infect the whole class.")
