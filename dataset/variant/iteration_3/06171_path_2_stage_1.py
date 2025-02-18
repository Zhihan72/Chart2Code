import matplotlib.pyplot as plt
import numpy as np

# Data Setup
shelters = ['B. Paw', 'F. Friends', 'H. Tails', 'P. Claws', 'L. Paws']
adoptable_pets = [150, 230, 190, 210, 170]

# Pet distribution in the busiest shelter
pet_types = ['Dogs', 'Cats', 'Other']
pet_counts = [130, 80, 20]

x_positions = np.arange(len(shelters))
bar_width = 0.6

# Create the main bar chart
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), gridspec_kw={'width_ratios': [2, 1]})
fig.suptitle('Pets in Shelters - 2022', fontsize=16, fontweight='bold', y=1.02)

# Bar chart
bars = ax1.bar(x_positions, adoptable_pets, color=['#FF9999','#66B2FF','#99FF99','#FFCC99','#FFD700'], width=bar_width)

# Annotate each bar
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Customize the x-axis
ax1.set_xticks(x_positions)
ax1.set_xticklabels(shelters, rotation=45, ha='right', fontsize=12)

# Set the title and labels for the bar chart
ax1.set_title("Adoptable Pets", fontsize=14, fontweight='bold')
ax1.set_ylabel("Number", fontsize=12)
ax1.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Pie chart for pet types
colors = ['#FF9999', '#66B2FF', '#99FF99']
explode = (0.1, 0, 0)

ax2.pie(pet_counts, labels=pet_types, explode=explode, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 12, 'fontweight':'bold'})
ax2.set_title('Types in "F. Friends"', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()