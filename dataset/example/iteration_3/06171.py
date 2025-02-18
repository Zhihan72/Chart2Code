import matplotlib.pyplot as plt
import numpy as np

# Backstory: The chart displays the annual number of adoptable pets in various shelters for the year 2022. 
# It helps to understand which shelter has the most number of pets waiting for a new home. Additionally, it includes 
# a subplot depicting the proportion of different types of pets (dog, cat, others) in the busiest shelter.

# Data Setup
shelters = ['Bright Paw', 'Furry Friends', 'Happy Tails', 'Paws Claws', 'Loving Paws']
adoptable_pets = [150, 230, 190, 210, 170]

# Detailed pet distribution for the busiest shelter 'Furry Friends'
pet_types = ['Dogs', 'Cats', 'Others']
pet_counts = [130, 80, 20]

x_positions = np.arange(len(shelters))
bar_width = 0.6

# Create the main bar chart for adoptable pets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})
fig.suptitle('Adoptable Pets Statistics in Shelters - 2022', fontsize=16, fontweight='bold', y=1.02)

# First subplot: Bar chart of adoptable pets in different shelters
bars = ax1.bar(x_positions, adoptable_pets, color=['#FF9999','#66B2FF','#99FF99','#FFCC99','#FFD700'], width=bar_width)

# Annotate each bar with the number of pets
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the x-axis
ax1.set_xticks(x_positions)
ax1.set_xticklabels(shelters, rotation=45, ha='right', fontsize=12)

# Set the title and labels
ax1.set_title("Number of Adoptable Pets in Shelters", fontsize=14, fontweight='bold')
ax1.set_ylabel("Number of Pets", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot: Pie chart for different pet types in the busiest shelter
colors = ['#FF9999', '#66B2FF', '#99FF99']
explode = (0.1, 0, 0)  # explode the first slice (dogs)

ax2.pie(pet_counts, labels=pet_types, explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 12, 'fontweight':'bold'})
ax2.set_title(f'Distribution of Pet Types in\n"Furry Friends" Shelter', fontsize=14, fontweight='bold')

# Automatically adjust layout to prevent overlap and improve spacing
plt.tight_layout()

# Show the plot
plt.show()