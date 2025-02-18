import matplotlib.pyplot as plt
import numpy as np

# Age groups and beverage preferences data
age_groups = ['18-25', '26-35', '36-45', '46-60', '60+']
beverages = ['Coffee', 'Tea']

# Beverage consumption data in percentage
coffee_preference = [40, 35, 30, 25, 15]
tea_preference = [-20, -25, -30, -35, -40]  # Represent tea as negative for diverging effect

# Create the figure and the axis
fig, ax = plt.subplots(figsize=(10, 7))

# Define bar width
bar_width = 0.6

# Generate bar positions
bar_positions = np.arange(len(age_groups))

# Create a diverging bar chart
ax.bar(bar_positions, coffee_preference, bar_width, color='#CD853F', label='Coffee (Positive)', align='center')
ax.bar(bar_positions, tea_preference, bar_width, color='#FBC02D', label='Tea (Negative)', align='center')

# Annotating each segment with the appropriate percentage value
for i, coffee in enumerate(coffee_preference):
    ax.annotate(f'{coffee}%', 
                xy=(bar_positions[i], coffee / 2), 
                ha='center', va='center', fontsize=10, color='black')

for i, tea in enumerate(tea_preference):
    ax.annotate(f'{-tea}%',  # Convert back to positive for annotation
                xy=(bar_positions[i], tea / 2), 
                ha='center', va='center', fontsize=10, color='black')

# Configure the plot
ax.axhline(0, color='black', linewidth=0.8)  # Central axis line
ax.set_xlabel('Age Groups', fontsize=14)
ax.set_ylabel('Percentage Preference', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(age_groups)
ax.legend()

# Use tight_layout for clarity
plt.tight_layout()

# Show the plot
plt.show()