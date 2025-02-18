import matplotlib.pyplot as plt
import numpy as np

# Backstory: In a fictional city, Techville, there is an annual competition called "Tech Innovators Championship" where tech companies show their yearly progress in different tech sectors. The categories include Artificial Intelligence (AI), Robotics, Internet of Things (IoT), Cybersecurity, and Quantum Computing. The bar chart presents the number of innovations from five companies over the past three years (2020-2022).

# Define the data for the chart
companies = ['AlphaCorp', 'BetaTech', 'Gamma Innovations', 'Delta Systems', 'Epsilon Ventures']
years = ['2020', '2021', '2022']
categories = ['AI', 'Robotics', 'IoT', 'Cybersecurity', 'Quantum Computing']

innovations = np.array([
    # 2020 innovations
    [12, 9, 15, 10, 5],    # AlphaCorp
    [8, 11, 13, 9, 4],     # BetaTech
    [9, 8, 12, 11, 3],     # Gamma Innovations
    [10, 7, 14, 10, 2],    # Delta Systems
    [9, 8, 13, 8, 1],      # Epsilon Ventures
    # 2021 innovations
    [14, 11, 18, 12, 6],   # AlphaCorp
    [9, 12, 14, 10, 5],    # BetaTech
    [11, 10, 13, 12, 4],   # Gamma Innovations
    [12, 9, 16, 11, 3],    # Delta Systems
    [11, 9, 14, 9, 2],     # Epsilon Ventures
    # 2022 innovations
    [16, 13, 20, 13, 7],   # AlphaCorp
    [10, 13, 15, 11, 6],   # BetaTech
    [12, 11, 15, 13, 5],   # Gamma Innovations
    [14, 10, 17, 12, 4],   # Delta Systems
    [13, 10, 16, 10, 3]    # Epsilon Ventures
])

# Create a figure for the bar charts
fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

colors = ['#FF6347', '#3CB371', '#4682B4', '#FFD700', '#FF69B4']

# Plot each year's data
for i, ax in enumerate(axes):
    year_data = innovations[i * len(companies):(i + 1) * len(companies)]
    x = np.arange(len(categories))
    
    for j in range(len(companies)):
        ax.bar(x + j * 0.15, year_data[j], width=0.1, color=colors[j], align='center', label=companies[j] if i == 0 else "")
    
    ax.set_title(f"Innovations in {years[i]}", fontsize=14)
    ax.set_xlabel("Categories", fontsize=12)
    ax.set_xticks(x + 0.3)
    ax.set_xticklabels(categories, rotation=45, ha='right')
    ax.grid(True, linestyle='--', linewidth=0.5)

# Setting the ylabel only on the first plot for clarity
axes[0].set_ylabel("Number of Innovations", fontsize=12)

# Add a legend to the first axes
axes[0].legend(loc='upper left', fontsize=10, title='Companies')

# Main title for the whole figure
fig.suptitle("Tech Innovators Championship: Innovations by Tech Companies (2020-2022)", fontsize=16, fontweight='bold')

# Automatically adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the plots
plt.show()