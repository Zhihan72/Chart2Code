import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

africa_internet = [10, 13, 17, 22, 28, 33, 39, 45, 52, 59, 65]
asia_internet = [20, 25, 30, 37, 44, 50, 58, 65, 72, 78, 84]
europe_internet = [60, 63, 66, 69, 72, 76, 79, 83, 86, 88, 91]
north_america_internet = [70, 73, 75, 78, 80, 82, 84, 86, 88, 89, 90]
south_america_internet = [40, 44, 48, 53, 59, 64, 68, 73, 78, 82, 86]

internet_usage = np.array([
    africa_internet, 
    asia_internet, 
    europe_internet, 
    north_america_internet, 
    south_america_internet
])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, internet_usage, labels=['NA', 'SA', 'Eur', 'Afr', 'Asi'], 
             colors=['lightcoral', 'gold', 'lightskyblue', 'lightgreen', 'violet'], alpha=0.6,
             linewidth=1.5)

ax.set_title("Internet Growth:\nContinents (2010-2020)", fontsize=18, style='italic')
ax.set_xlabel("Year", fontsize=14, style='italic')
ax.set_ylabel("Users (% Pop.)", fontsize=14, style='italic')
ax.legend(loc='upper right', title='Continents', fontsize=10)
ax.grid(visible=False)  # No grid lines
ax.spines['top'].set_visible(False)  # Top border disabled
ax.spines['right'].set_visible(False)  # Right border disabled
plt.xticks(years, rotation=30)  # Custom tick labels
plt.tight_layout()

plt.show()