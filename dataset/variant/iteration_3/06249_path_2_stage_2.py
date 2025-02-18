import matplotlib.pyplot as plt
import numpy as np

# Data: Years and corresponding values for internet users
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
internet_users = np.array([2.7, 2.9, 3.2, 3.5, 3.8, 4.2, 4.5, 4.8, 5.1, 5.3])  # in billions

# Plotting the data on line chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot internet users
ax1.plot(years, internet_users, marker='o', linestyle='-', linewidth=2, color='green', label='Internet Users (Billions)')
for i, txt in enumerate(internet_users):
    ax1.annotate(f'{txt}B', (years[i], internet_users[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# Setting titles and labels
plt.title("Digital Evolution: Internet User Growth", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Internet Users (Billions)", fontsize=14, color='green')

# Legend
ax1.legend(loc='upper left')

# Grids for readability
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Ticks for x-axis and y-axis
ax1.set_xticks(years)
ax1.set_yticks(np.arange(0, 6.5, 0.5))

# Layout adjustments
plt.tight_layout()

# Show plot
plt.show()