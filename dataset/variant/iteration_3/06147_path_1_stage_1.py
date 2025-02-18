import matplotlib.pyplot as plt
import numpy as np

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
ax.bar(bar_positions, coffee_preference, bar_width, color='#8B4513', label='Coffee')
ax.bar(bar_positions, tea_preference, bar_width, bottom=coffee_preference, color='#CD853F', label='Tea')
ax.bar(bar_positions, juice_preference, bar_width, bottom=np.array(coffee_preference) + np.array(tea_preference), color='#FBC02D', label='Juice')

# Annotating each segment with the percentage value
for i, (coffee, tea, juice) in enumerate(zip(coffee_preference, tea_preference, juice_preference)):
    # Annotating Coffee
    ax.annotate(f'{coffee}%', 
                xy=(bar_positions[i], coffee / 2), 
                ha='center', va='center', fontsize=10, color='black')
    
    # Annotating Tea
    ax.annotate(f'{tea}%', 
                xy=(bar_positions[i], coffee + tea / 2), 
                ha='center', va='center', fontsize=10, color='black')

    # Annotating Juice
    ax.annotate(f'{juice}%', 
                xy=(bar_positions[i], coffee + tea + juice / 2), 
                ha='center', va='center', fontsize=10, color='black')

# Configure the plot
ax.set_xlabel('Age Groups', fontsize=14)
ax.set_ylabel('Percentage Preference', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(age_groups)

# Add legend
ax.legend()

# Use tight_layout to prevent overlap and truncation
plt.tight_layout()

# Show the plot
plt.show()
