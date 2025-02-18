import matplotlib.pyplot as plt
import numpy as np

# Extended countries and coffee consumption data
countries = ['Finland', 'Norway', 'Iceland', 'Denmark', 'Netherlands', 
             'Sweden', 'Switzerland', 'Belgium', 'Canada', 'Brazil',
             'Imaginaryland', 'CoffeeTopia', 'JavaNation']
consumption_kg = [12, 9.9, 9, 8.7, 8.4, 8.2, 7.9, 6.8, 6.5, 6.1, 
                  10.5, 11.2, 9.5]

# Sort data in descending order of consumption
sorted_indices = np.argsort(consumption_kg)[::-1]
countries_sorted = [countries[i] for i in sorted_indices]
consumption_sorted = [consumption_kg[i] for i in sorted_indices]

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
colors = plt.cm.cividis(np.linspace(0.2, 0.8, len(countries)))

# Plotting horizontal bars
bars = ax.barh(countries_sorted, consumption_sorted, color=colors, edgecolor='darkslategray')

# Titles and labels
ax.set_title('Global Caffeine Rush:\nTop Coffee Consuming Countries in 2023', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Average Annual Coffee Consumption (kg per capita)', fontsize=12)

# Annotate each bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width} kg', xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0), textcoords='offset points',
                ha='left', va='center', fontsize=10, color='black')

# Enhancing the layout
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.tick_params(axis='y', which='major', labelsize=10)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()