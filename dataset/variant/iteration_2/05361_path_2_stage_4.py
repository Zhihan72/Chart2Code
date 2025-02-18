import matplotlib.pyplot as plt
import numpy as np

companies = ['AlphaCorp', 'BetaTech', 'Gamma Innovations', 'Delta Systems']
years = ['2030', '2021', '2019']  # Randomly altered years
categories = ['Quantum Computation', 'AI', 'IoT', 'Cyber Defense', 'Robot Tech']  # Altered category labels

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

fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

single_color = '#4682B4'

for original_index, new_index in zip([0, 1, 2], [2, 1, 0]):
    year_data = innovations[new_index * len(companies):(new_index + 1) * len(companies)]
    x = np.arange(len(categories))

    for j in range(len(companies)):
        axes[original_index].bar(x + j * 0.15, year_data[j], width=0.1, color=single_color, align='center', label=companies[j] if original_index == 0 else "")

    axes[original_index].set_title(f"Innovations in Year {years[new_index]}", fontsize=14)  # Altered title text
    axes[original_index].set_xlabel("Tech Divisions", fontsize=12)  # Altered x-axis label text
    axes[original_index].set_xticks(x + 0.225)
    axes[original_index].set_xticklabels(categories, rotation=45, ha='right')
    axes[original_index].grid(True, linestyle='--', linewidth=0.5)

axes[0].set_ylabel("Innovations Count", fontsize=12)  # Altered y-axis label
axes[0].legend(loc='upper left', fontsize=10, title='Corporations')  # Altered legend title text

fig.suptitle("Innovation Summit: Top Tech Firms Analysis (2019-2030)", fontsize=16, fontweight='bold')  # Altered super title text
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()