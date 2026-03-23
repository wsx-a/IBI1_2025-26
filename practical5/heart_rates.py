heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
total_patients = len(heart_rates)
average_heart_rate = sum(heart_rates) / len(heart_rates)
low = 0
normal = 0
high = 0
for rate in heart_rates:
    if rate < 60:
        low = low + 1
    elif rate <= 120:
        normal = normal + 1
    else:
        high = high + 1
print("Low:", low)
print("Normal:", normal)
print("High:", high)
if low > normal and low > high:
    print("Most patients are in low category.")
elif normal > low and normal > high:
    print("Most patients are in normal category.")
else:
    print("Most patients are in high category.")
import matplotlib.pyplot as plt
plt.pie([low, normal, high], labels=["LOW", "Normal", "High"])
plt.title("Heart Rate Categories")
plt.show()