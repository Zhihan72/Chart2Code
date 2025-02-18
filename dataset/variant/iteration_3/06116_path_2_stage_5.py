import matplotlib.pyplot as plt
import numpy as np

# Define data
heroes = ["The Silent Knight", "Thunder Hornet", "Crimson Tornado", "Midnight Leopard"]
timeframe = ["Year 2018", "Year 2019", "Year 2020", "Year 2021", "Year 2022"]

# Combine data into a diverging structure
data = {
    'Positive': np.array([
        [125, 135, 155, 145, 165],  # Rescues
        [100, 105, 115, 110, 130],  # Rescues
        [85, 90, 100, 95, 115],     # Rescues
        [115, 120, 125, 135, 140]   # Rescues
    ]),
    'Negative': np.array([
        [85, 100, 110, 90, 105],    # Battles
        [65, 75, 85, 80, 80],       # Battles
        [80, 85, 95, 90, 100],      # Battles
        [95, 90, 105, 100, 120]     # Battles
    ])
}

# Adjust the width of the bars and x-axis positions
width = 0.35
x = np.arange(len(timeframe))

fig, axs = plt.subplots(1, 1, figsize=(14, 8))

# Iterate over heroes to plot diverging bars
for i, hero in enumerate(heroes):
    axs.bar(x - width * i, data['Positive'][i], width, label=f'{hero} Rescues', bottom=data['Negative'][i], color='#2E86C1', edgecolor='black')
    axs.bar(x - width * i, -data['Negative'][i], width, label=f'{hero} Battles', color='#E74C3C', edgecolor='black')

# Customize the plot
axs.set_title('Superheroes Achievements Diverging Bar (Years 2018-2022)', fontsize=16, fontweight='bold', pad=20)
axs.set_xlabel('Time Periods', fontsize=12)
axs.set_ylabel('Mission Counts', fontsize=12)

axs.set_xticks(x)
axs.set_xticklabels(timeframe, rotation=45)
axs.axhline(0, color='black', linewidth=0.8)

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()