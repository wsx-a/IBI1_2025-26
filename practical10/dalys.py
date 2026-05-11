import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"E:\IBI1\IBI1_2025-26\practical10")
print("Current working directory:")
print(os.getcwd())
print("\nFiles in this directory:")
print(os.listdir())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print("\nFirst 5 rows:")
print(dalys_data.head(5))
print("\nDataframe info:")
dalys_data.info()
print("\nSummary statistics:")
print(dalys_data.describe())
print("\nMaximum DALYs in whole dataset:", dalys_data["DALYs"].max())
print("Minimum DALYs in whole dataset:", dalys_data["DALYs"].min())
print("First year in dataset:", dalys_data["Year"].min())
print("Most recent year in dataset:", dalys_data["Year"].max())

# Afghanistan: first 10 rows, third and fourth columns
# comment: the maximum DALYs in the first 10 Afghanistan rows was reported in 1998

afghanistan_data = dalys_data.loc[dalys_data["Entity"] == "Afghanistan", :]
afghanistan_first_10 = afghanistan_data.iloc[0:10, 2:4]
print("\nAfghanistan first 10 rows, third and fourth columns:")
print(afghanistan_first_10)
max_afghan_row = afghanistan_first_10.loc[afghanistan_first_10["DALYs"].idxmax()]
print("\nYear with maximum DALYs across the first 10 Afghanistan rows:")
print(max_afghan_row["Year"])

# Zimbabwe: all years using a Boolean
# comment: DALYs for Zimbabwe were recorded from 1990 to 2019

zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]

print("\nAll years recorded for Zimbabwe:")
print(zimbabwe_years)
print("\nFirst year for Zimbabwe:", zimbabwe_years.min())
print("Last year for Zimbabwe:", zimbabwe_years.max())

# Countries with maximum and minimum DALYs in 2019
# comment: the country with the maximum and minimum DALYs in 2019 is printed below

recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
max_row_2019 = recent_data.loc[recent_data["DALYs"].idxmax()]
min_row_2019 = recent_data.loc[recent_data["DALYs"].idxmin()]
print("\nCountry with maximum DALYs in 2019:")
print(max_row_2019)
print("\nCountry with minimum DALYs in 2019:")
print(min_row_2019)

# Plot DALYs over time for one of those countries
# here I use the country with maximum DALYs in 2019

country_max = max_row_2019["Entity"]
country_max_data = dalys_data.loc[dalys_data["Entity"] == country_max, ["Year", "DALYs"]]
plt.figure(figsize=(8, 5), dpi=150)
plt.plot(country_max_data["Year"], country_max_data["DALYs"], "bo-")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time in " + country_max)
plt.xticks(country_max_data["Year"], rotation=-90)
plt.tight_layout()
plt.savefig("dalys_over_time_" + country_max.replace(" ", "_") + ".png")
plt.show()

# My extra question
# Question: How has the relationship between the DALYs in China and the UK changed over time?

china_data = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]]
uk_data = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["Year", "DALYs"]]
china_uk = pd.merge(china_data, uk_data, on="Year", suffixes=("_China", "_UK"))
china_uk["Difference"] = china_uk["DALYs_China"] - china_uk["DALYs_UK"]
print("\nChina and UK DALYs comparison:")
print(china_uk.head())
plt.figure(figsize=(8, 5), dpi=150)
plt.plot(china_uk["Year"], china_uk["DALYs_China"], "r-", label="China")
plt.plot(china_uk["Year"], china_uk["DALYs_UK"], "b-", label="United Kingdom")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in China and the United Kingdom over time")
plt.legend()
plt.xticks(china_uk["Year"], rotation=-90)
plt.tight_layout()
plt.savefig("china_uk_dalys_comparison.png")
plt.show()

plt.figure(figsize=(8, 5), dpi=150)
plt.plot(china_uk["Year"], china_uk["Difference"], "g-")
plt.xlabel("Year")
plt.ylabel("DALYs difference (China - UK)")
plt.title("Difference in DALYs between China and the United Kingdom")
plt.xticks(china_uk["Year"], rotation=-90)
plt.tight_layout()
plt.savefig("china_uk_dalys_difference.png")
plt.show()

print("\nAverage difference between China and UK DALYs:")
print(china_uk["Difference"].mean())