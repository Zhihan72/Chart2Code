import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# The chart illustrates the energy consumption of different energy sources in a fictional country over the decades. The chart aims to highlight how consumption patterns have evolved and the rise of renewable energy sources in recent times.

# Decades for the timeline
decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']

# Energy consumption in TW (terawatt-hours) for each source per decade
coal = [300, 400, 500, 600, 550, 400, 300]
oil = [200, 250, 300, 350, 400, 350, 200]
natural_gas = [100, 150, 200, 250, 300, 400, 500]
nuclear = [0, 50, 100, 150, 200, 250, 300]
renewables = [10, 20, 50, 100, 200, 400, 600]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 7))

# Plot each energy source with distinct styles
ax.plot(decades, coal, label='Coal', color='black', marker='o', linestyle='-', linewidth=2)
ax.plot(decades, oil, label='Oil', color='brown', marker='s', linestyle='--', linewidth=2)
ax.plot(decades, natural_gas, label='Natural Gas', color='blue', marker='^', linestyle='-.', linewidth=2)
ax.plot(decades, nuclear, label='Nuclear', color='purple', marker='D', linestyle=':', linewidth=2)
ax.plot(decades, renewables, label='Renewables', color='green', marker='*', linestyle='-', linewidth=2)

# Annotate significant milestones
ax.annotate('Oil Crisis', xy=('1970s', 250), xytext=('1980s', 350),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkred')
ax.annotate('Rise of Renewables', xy=('2010s', 400), xytext=('2000s', 300),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=9, color='darkgreen')

# Adding titles and labels
ax.set_title('Energy Consumption Trends:\nThe Evolution of Energy Sources in a Fictional Country', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Energy Consumption (TW)', fontsize=12)
ax.legend(loc='upper left', fontsize=10, title='Energy Sources', frameon=False)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Customize x-ticks and y-ticks for better appearance
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 701, 100))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the line chart
plt.show()