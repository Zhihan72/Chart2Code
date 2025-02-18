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

# Changed colors and added hatch patterns
colors = ['#FF6347', '#32CD32', '#8A2BE2', '#FFD700', '#FF4500', '#4682B4']
hatch_patterns = ['/', '\\', '-', '|', '+', '.']

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

for i in range(len(data)):
    axs[0].hist(np.arange(len(seasons)), bins=np.arange(len(seasons) + 1), weights=data[i],
                label=appliance_labels[i], alpha=0.7, edgecolor='grey', color=colors[i], hatch=hatch_patterns[i])

axs[0].set_title("Energy Usage in a Home by Season", fontsize=14, pad=15)
axs[0].set_xlabel("Season", fontsize=11)
axs[0].set_ylabel("Energy (kWh)", fontsize=11)
axs[0].set_xticks(np.arange(len(seasons)))
axs[0].set_xticklabels(seasons, rotation=0)
axs[0].legend(title="Appliances", fontsize=9, title_fontsize='10', loc='upper right')  # Changed location and font size
axs[0].yaxis.grid(True, linestyle='-.', alpha=0.9)  # Altered grid style

def calculate_percentage_share(data):
    percentages = []
    total_consumption = [sum(x) for x in zip(*data)]
    for series in data:
        percentages.append([((val / total) * 100) if total != 0 else 0 for val, total in zip(series, total_consumption)])
    return percentages

percentage_data = calculate_percentage_share(data)

# Changed marker types and line styles
markers = ['o', 's', '^', 'D', '*', 'x']
line_styles = ['-', '--', '-.', ':', '-', '--']

for idx, percentage in enumerate(percentage_data):
    axs[1].plot(seasons, percentage, marker=markers[idx], linestyle=line_styles[idx], label=appliance_labels[idx], linewidth=1.5, color=colors[idx])

axs[1].set_title("Energy Usage Percentage by Appliance", fontsize=14, pad=15)
axs[1].set_xlabel("Season", fontsize=11)
axs[1].set_ylabel("Share (%)", fontsize=11)
axs[1].legend(title="Appliances", fontsize=9, title_fontsize='10', loc='upper left')  # Changed location
axs[1].yaxis.grid(True, linestyle=':', alpha=0.8)  # Altered grid style and alpha

plt.tight_layout()
plt.show()