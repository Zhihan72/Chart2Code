import matplotlib.pyplot as plt
import numpy as np

# Backstory: A survey was conducted to measure the preferences of different types of beverages (coffee, tea, and juice) among various age groups. 
# This data is to be visualized to observe consumption trends across different age demographics.

# Age groups and beverage preferences data
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
beverages = ['Coffee', 'Tea', 'Juice']

# Beverage consumption data in percentage
coffee_preference = [40, 35, 30, 25, 15]
tea_preference = [20, 25, 30, 35, 40]
juice_preference = [40, 40, 40, 40, 45]

# Create the figure and the axis
fig, ax = plt.subplots(figsize=(10, 7))

# Define bar width
bar_width = 0.6

# Generate bar positions
bar_positions = np.arange(len(age_groups))

# Create a stacked bar chart
bars1 = ax.bar(bar_positions, coffee_preference, bar_width, label=beverages[0], color='#8B4513')
bars2 = ax.bar(bar_positions, tea_preference, bar_width, bottom=coffee_preference, label=beverages[1], color='#CD853F')
bars3 = ax.bar(bar_positions, juice_preference, bar_width, bottom=np.array(coffee_preference)+np.array(tea_preference), label=beverages[2], color='#FBC02D')

# Annotating each segment with the percentage value
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%',
                    xy=(bar.get_x() + bar.get_width() / 2, bar.get_y() + height / 2),
                    xytext=(0, 0), 
                    textcoords='offset points',
                    ha='center', va='center', fontsize=10, color='black')

# Configure the plot
ax.set_title('Beverage Preference Among Different Age Groups', fontsize=16, fontweight='bold')
ax.set_xlabel('Age Groups', fontsize=14)
ax.set_ylabel('Percentage Preference', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(age_groups)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add legend
ax.legend(loc='best', title='Beverage Type', fontsize=12)

# Use tight_layout to prevent overlap and truncation
plt.tight_layout()

# Show the plot
plt.show()