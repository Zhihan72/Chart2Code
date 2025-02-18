import matplotlib.pyplot as plt
import numpy as np

# Data Setup with additional shelters
shelters = ['Bright Paw', 'Furry Friends', 'Happy Tails', 'Paws Claws', 'Loving Paws', 'Safe Haven', 'Animal Angels']
adoptable_pets = [150, 230, 190, 210, 170, 180, 160]

# Updated detailed pet distribution for two busiest shelters 'Furry Friends' and 'Paws Claws'
pet_types = ['Dogs', 'Cats', 'Others']
pet_counts_1 = [130, 80, 20]  # Furry Friends
pet_counts_2 = [150, 40, 20]  # Paws Claws

x_positions = np.arange(len(shelters))
bar_width = 0.6

# Create the main bar chart for adoptable pets
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})
fig.suptitle('Adoptable Pets Statistics in Shelters - 2022', fontsize=16, fontweight='bold', y=1.02)

# First subplot: Bar chart of adoptable pets in different shelters
bars = ax1.bar(x_positions, adoptable_pets, color=['#FF9999','#66B2FF','#99FF99','#FFCC99','#FFD700','#FFDEAD','#ADD8E6'], width=bar_width)

# Annotate each bar with the number of pets
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_xticks(x_positions)
ax1.set_xticklabels(shelters, rotation=45, ha='right', fontsize=12)
ax1.set_title("Number of Adoptable Pets in Shelters", fontsize=14, fontweight='bold')
ax1.set_ylabel("Number of Pets", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Second subplot: Pie charts for different pet types in two busiest shelters
explode = (0.1, 0, 0)  # explode the first slice (dogs)

ax2.pie(pet_counts_1, labels=pet_types, explode=explode, colors=['#FF9999', '#66B2FF', '#99FF99'],
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 10, 'fontweight':'bold'})
ax2.set_title('Pet Types in "Furry Friends" Shelter', fontsize=12, fontweight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

plt.show()