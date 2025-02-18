import matplotlib.pyplot as plt
import numpy as np

seasons = ['Win', 'Spr', 'Sum', 'Fal']

heating = [450, 120, 30, 180]
cooling = [20, 80, 300, 100]
lighting = [150, 120, 150, 160]
appliances = [200, 210, 230, 220]
entertainment = [100, 90, 110, 80]
water_heating = [220, 200, 180, 240]

data = [heating, cooling, lighting, appliances, entertainment, water_heating]
appliance_labels = ['Heat', 'Cool', 'Light', 'Apps', 'Entertain', 'WaterHeat']

def calculate_percentage_share(data):
    percentages = []
    total_consumption = [sum(x) for x in zip(*data)]
    for series in data:
        percentages.append([((val / total) * 100) if total != 0 else 0 for val, total in zip(series, total_consumption)])
    return percentages

percentage_data = calculate_percentage_share(data)

fig, axs = plt.subplots(2, 1, figsize=(10, 10))  # Changed to a 2x1 arrangement

new_colors = ['#FF6347', '#4682B4', '#3CB371', '#FFD700', '#8A2BE2', '#FF4500']

axs[0].hist([np.arange(len(seasons))] * len(data), bins=np.arange(len(seasons) + 1), 
            weights=data, label=appliance_labels, histtype='barstacked', 
            alpha=0.6, edgecolor='black', color=new_colors)

axs[0].set_title("Energy Consumption by Season", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Season", fontsize=11, fontstyle='italic')
axs[0].set_ylabel("Energy (kWh)", fontsize=11)
axs[0].set_xticks(np.arange(len(seasons)))
axs[0].set_xticklabels(seasons, rotation=45)
axs[0].legend(title="Devices", fontsize=9, title_fontsize='10', loc='upper right')
axs[0].yaxis.grid(True, linestyle='-.', color='grey', alpha=0.5)

marker_styles = ['s', '^', 'd', '*', 'o', 'x']
line_styles = [':', '-', '-.', '--', '-', ':']

for idx, percentage in enumerate(percentage_data):
    axs[1].plot(seasons, percentage, marker=marker_styles[idx], label=appliance_labels[idx], 
                linewidth=2, linestyle=line_styles[idx], color=new_colors[idx])

axs[1].set_title("Energy Share by Device", fontsize=14, fontweight='bold', color='darkred')
axs[1].set_xlabel("Season", fontsize=11, fontstyle='italic')
axs[1].set_ylabel("Share (%)", fontsize=11)
axs[1].legend(title="Devices", fontsize=9, title_fontsize='10', loc='lower center')
axs[1].yaxis.grid(True, linestyle='-', color='lightgrey', alpha=0.9)

plt.tight_layout()
plt.show()