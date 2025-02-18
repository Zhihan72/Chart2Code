import matplotlib.pyplot as plt
import numpy as np

# Modified age groups and beverage preferences data
age_brackets = ['25-18', '35-26', '45-36', '60-46', '60+']
drink_types = ['Espresso', 'Green Tea']

# Beverage consumption data in percentage
espresso_preference = [40, 35, 30, 25, 15]
green_tea_preference = [-20, -25, -30, -35, -40]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Define bar width
bar_width = 0.6
bar_positions = np.arange(len(age_brackets))

# Create a diverging bar chart
ax.bar(bar_positions, espresso_preference, bar_width, color='#CD853F', label='Espresso (Positive)', align='center')
ax.bar(bar_positions, green_tea_preference, bar_width, color='#FBC02D', label='Green Tea (Negative)', align='center')

# Annotate each segment with the appropriate percentage value
for i, espresso in enumerate(espresso_preference):
    ax.annotate(f'{espresso}%', 
                xy=(bar_positions[i], espresso / 2), 
                ha='center', va='center', fontsize=10, color='black')

for i, tea in enumerate(green_tea_preference):
    ax.annotate(f'{-tea}%',  
                xy=(bar_positions[i], tea / 2), 
                ha='center', va='center', fontsize=10, color='black')

# Configure the plot
ax.axhline(0, color='black', linewidth=0.8)
ax.set_xlabel('Demographics', fontsize=14)
ax.set_ylabel('Preference Rate', fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(age_brackets)
ax.legend()

plt.tight_layout()

plt.show()