import numpy as np
import matplotlib.pyplot as plt

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
ax.plot(decades, coal, color='black', marker='o', linestyle='-', linewidth=2)
ax.plot(decades, oil, color='brown', marker='s', linestyle='--', linewidth=2)
ax.plot(decades, natural_gas, color='blue', marker='^', linestyle='-.', linewidth=2)
ax.plot(decades, nuclear, color='purple', marker='D', linestyle=':', linewidth=2)
ax.plot(decades, renewables, color='green', marker='*', linestyle='-', linewidth=2)

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Customize x-ticks and y-ticks
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 701, 100))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the line chart
plt.show()