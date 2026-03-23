countries = ["UK", "China", "Italy", "Brazil", "USA"]
pop2020 = [66.7, 1426, 59.4, 208.6, 331.6]
pop2024 = [69.2, 1410, 58.9, 212.0, 340.1]
changes = []
for i in range(5):
    x = (pop2024[i] - pop2020[i]) / pop2020[i] * 100
    changes.append(x)
print("Population change of each country:")
for i in range(5):
    print(countries[i], ":", round(changes[i], 2), "%")
info = []
for i in range(5):
    info.append([countries[i], changes[i]])
info.sort(key=lambda x: x[1], reverse=True)
print()
print("From largest increase to largest decrease:")
for i in info:
    print(i[0], ":", round(i[1], 2), "%")
print()
print("Largest increase:", info[0][0])
print("Largest decrease:", info[-1][0])
import matplotlib.pyplot as plt
plt.bar(countries, changes)
plt.xlabel("Country")
plt.ylabel("Change %")
plt.title("Population Change")
plt.show()