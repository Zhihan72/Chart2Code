import matplotlib.pyplot as plt
import numpy as np

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
internet_users = np.array([2.7, 2.9, 3.2, 3.5, 3.8, 4.2, 4.5, 4.8, 5.1, 5.3])

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(years, internet_users, marker='o', linestyle='-', linewidth=2, color='green', label='Users (B)')
for i, txt in enumerate(internet_users):
    ax1.annotate(f'{txt}B', (years[i], internet_users[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

plt.title("Internet Growth", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Users (B)", fontsize=14, color='green')

ax1.legend(loc='upper left')

ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 6.5, 0.5))

plt.tight_layout()

plt.show()