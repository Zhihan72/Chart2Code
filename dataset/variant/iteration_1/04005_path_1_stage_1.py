import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = ['Win', 'Spr', 'Sum', 'Fal']

# Energy consumption (kWh)
heating = [450, 120, 30, 180]
cooling = [20, 80, 300, 100]
lighting = [150, 120, 150, 160]
appliances = [200, 210, 230, 220]

# Aggregated data
data = [heating, cooling, lighting, appliances]

# Appliance labels
appliance_labels = ['Heat', 'Cool', 'Light', 'Apps']

# Calculating percentage
def calculate_percentage_share(data):
    percentages = []
    total_consumption = [sum(x) for x in zip(*data)]
    for series in data:
        percentages.append([((val / total) * 100) if total != 0 else 0 for val, total in zip(series, total_consumption)])
    return percentages

percentage_data = calculate_percentage_share(data)

# Setting up plots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Stacked histogram
axs[0].hist([np.arange(len(seasons))] * len(data), bins=np.arange(len(seasons) + 1), weights=data, 
            label=appliance_labels, histtype='barstacked', alpha=0.8, edgecolor='black')

axs[0].set_title("Energy Consumption\nby Season", fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel("Season", fontsize=11)
axs[0].set_ylabel("Energy (kWh)", fontsize=11)
axs[0].set_xticks(np.arange(len(seasons)))
axs[0].set_xticklabels(seasons, rotation=0)
axs[0].legend(title="Devices", fontsize=10, title_fontsize='11', loc='upper left')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Percentage share line plot
for idx, percentage in enumerate(percentage_data):
    axs[1].plot(seasons, percentage, marker='o', label=appliance_labels[idx], linewidth=2)

axs[1].set_title("Energy Share by Device", fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel("Season", fontsize=11)
axs[1].set_ylabel("Share (%)", fontsize=11)
axs[1].legend(title="Devices", fontsize=10, title_fontsize='11', loc='best')
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Layout adjustment
plt.tight_layout()

# Show plots
plt.show()