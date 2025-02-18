import matplotlib.pyplot as plt
import numpy as np

seasons = ['Winter', 'Spring', 'Summer', 'Fall']
heating = [450, 120, 30, 180]
cooling = [20, 80, 300, 100]
lighting = [150, 120, 150, 160]
appliances = [200, 210, 230, 220]
entertainment = [100, 130, 90, 120]
water_heating = [180, 160, 110, 190]
data = [heating, cooling, lighting, appliances, entertainment, water_heating]
appliance_labels = ['Heating', 'Cooling', 'Lighting', 'Appliances', 'Entertainment', 'Water Heating']

colors = ['#FF6347', '#32CD32', '#8A2BE2', '#FFD700', '#FF4500', '#4682B4']
hatch_patterns = ['/', '\\', '-', '|', '+', '.']

fig, ax = plt.subplots(figsize=(7, 7))

for i in range(len(data)):
    ax.hist(np.arange(len(seasons)), bins=np.arange(len(seasons) + 1), weights=data[i],
            label=appliance_labels[i], alpha=0.7, edgecolor='grey', color=colors[i], hatch=hatch_patterns[i])

ax.set_title("Energy Usage in a Home by Season", fontsize=14, pad=15)
ax.set_xlabel("Season", fontsize=11)
ax.set_ylabel("Energy (kWh)", fontsize=11)
ax.set_xticks(np.arange(len(seasons)))
ax.set_xticklabels(seasons, rotation=0)
ax.legend(title="Appliances", fontsize=9, title_fontsize='10', loc='upper right')
ax.yaxis.grid(True, linestyle='-.', alpha=0.9)

plt.tight_layout()
plt.show()