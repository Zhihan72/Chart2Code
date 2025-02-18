import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

africa_internet = [10, 13, 17, 22, 28, 33, 39, 45, 52, 59, 65]
asia_internet = [20, 25, 30, 37, 44, 50, 58, 65, 72, 78, 84]
europe_internet = [60, 63, 66, 69, 72, 76, 79, 83, 86, 88, 91]
north_america_internet = [70, 73, 75, 78, 80, 82, 84, 86, 88, 89, 90]
south_america_internet = [40, 44, 48, 53, 59, 64, 68, 73, 78, 82, 86]
oceania_internet = [50, 52, 55, 58, 61, 63, 66, 70, 73, 75, 77]

internet_usage = np.array([
    africa_internet, 
    asia_internet, 
    europe_internet, 
    north_america_internet, 
    south_america_internet,
    oceania_internet
])

fig, ax = plt.subplots(figsize=(12, 8))

# Shuffle colors without random module
colors = ['lightseagreen', 'thistle', 'lightgreen', 'lightblue', 'lightcoral', 'gold']

ax.stackplot(years, internet_usage, colors=colors, alpha=0.8)

ax.set_title("Internet Growth by Continent (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Users (% Pop)", fontsize=12)

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()