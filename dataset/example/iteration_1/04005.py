import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart will represent the "Energy Consumption in a Smart Home Over Different Seasons".
# The seasons are Winter, Spring, Summer, and Fall, and we will show the consumption for different appliances: Heating, Cooling, Lighting, and Appliances.

# Defining the seasons
seasons = ['Winter', 'Spring', 'Summer', 'Fall']

# Energy consumption for each appliance in each season (units in kWh)
heating = [450, 120, 30, 180]
cooling = [20, 80, 300, 100]
lighting = [150, 120, 150, 160]
appliances = [200, 210, 230, 220]

# Aggregated data
data = [heating, cooling, lighting, appliances]

# Labels for the appliances
appliance_labels = ['Heating', 'Cooling', 'Lighting', 'Appliances']

# Calculate percentage share for each appliance within a season
def calculate_percentage_share(data):
    percentages = []
    total_consumption = [sum(x) for x in zip(*data)]
    for series in data:
        percentages.append([((val / total) * 100) if total != 0 else 0 for val, total in zip(series, total_consumption)])
    return percentages

percentage_data = calculate_percentage_share(data)

# Setting up the figure and axis
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plotting the stacked histogram
axs[0].hist([np.arange(len(seasons))] * len(data), bins=np.arange(len(seasons) + 1), weights=data, 
            label=appliance_labels, histtype='barstacked', alpha=0.8, edgecolor='black')

axs[0].set_title("Energy Consumption in a Smart Home\nOver Different Seasons", fontsize=14, fontweight='bold', pad=15)
axs[0].set_xlabel("Season", fontsize=11)
axs[0].set_ylabel("Energy Consumption (kWh)", fontsize=11)
axs[0].set_xticks(np.arange(len(seasons)))
axs[0].set_xticklabels(seasons, rotation=0)
axs[0].legend(title="Appliances", fontsize=10, title_fontsize='11', loc='upper left')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Plotting the line plot for percentage share
for idx, percentage in enumerate(percentage_data):
    axs[1].plot(seasons, percentage, marker='o', label=appliance_labels[idx], linewidth=2)

axs[1].set_title("Percentage Share of Energy Consumption\nby Appliance in Each Season", fontsize=14, fontweight='bold', pad=15)
axs[1].set_xlabel("Season", fontsize=11)
axs[1].set_ylabel("Percentage Share (%)", fontsize=11)
axs[1].legend(title="Appliances", fontsize=10, title_fontsize='11', loc='best')
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()