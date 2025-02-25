import matplotlib.pyplot as plt
import numpy as np

# Define the data for the chart
companies = ['AlphaCorp', 'BetaTech', 'Gamma Innovations', 'Delta Systems']
years = ['2020', '2021', '2022']
categories = ['AI', 'Robotics', 'IoT', 'Cybersecurity', 'Quantum Computing']

innovations = np.array([
    [12, 9, 15, 10, 5],    # AlphaCorp 2020
    [8, 11, 13, 9, 4],     # BetaTech 2020
    [9, 8, 12, 11, 3],     # Gamma Innovations 2020
    [10, 7, 14, 10, 2],    # Delta Systems 2020
    [14, 11, 18, 12, 6],   # AlphaCorp 2021
    [9, 12, 14, 10, 5],    # BetaTech 2021
    [11, 10, 13, 12, 4],   # Gamma Innovations 2021
    [12, 9, 16, 11, 3],    # Delta Systems 2021
    [16, 13, 20, 13, 7],   # AlphaCorp 2022
    [10, 13, 15, 11, 6],   # BetaTech 2022
    [12, 11, 15, 13, 5],   # Gamma Innovations 2022
    [14, 10, 17, 12, 4]    # Delta Systems 2022
])

# Create a figure for the bar charts
fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

# Use a single color for all data groups
single_color = '#4682B4'

# Plot each year's data
for i, ax in enumerate(axes):
    year_data = innovations[i * len(companies):(i + 1) * len(companies)]
    x = np.arange(len(categories))
    
    for j in range(len(companies)):
        ax.bar(x + j * 0.15, year_data[j], width=0.1, color=single_color, align='center', label=companies[j] if i == 0 else "")
    
    ax.set_title(f"Innovations in {years[i]}", fontsize=14)
    ax.set_xlabel("Categories", fontsize=12)
    ax.set_xticks(x + 0.225)
    ax.set_xticklabels(categories, rotation=45, ha='right')
    ax.grid(True, linestyle='--', linewidth=0.5)

axes[0].set_ylabel("Number of Innovations", fontsize=12)
axes[0].legend(loc='upper left', fontsize=10, title='Companies')

fig.suptitle("Tech Innovators Championship: Innovations by Tech Companies (2020-2022)", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()