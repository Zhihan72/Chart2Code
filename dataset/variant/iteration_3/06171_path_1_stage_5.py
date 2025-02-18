import matplotlib.pyplot as plt
import numpy as np

shelters = ['Bright Paw', 'Furry Friends', 'Happy Tails', 'Paws Claws', 'Loving Paws', 'Safe Haven', 'Animal Angels']
adoptable_pets = [150, 230, 190, 210, 170, 180, 160]

pet_types = ['Dogs', 'Cats', 'Others']
pet_counts_1 = [130, 80, 20]

x_positions = np.arange(len(shelters))
bar_width = 0.6

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [3, 2]})
fig.suptitle('Adoptable Pets Statistics in Shelters - 2022', fontsize=16, fontweight='bold', y=1.02)

# Donut chart with new colors
explode = (0.1, 0.2, 0)
ax1.pie(pet_counts_1, labels=pet_types, explode=explode, colors=['#FF6347', '#4682B4', '#32CD32'],
        autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 11}, 
        wedgeprops={'width': 0.3})
ax1.set_title('Pet Types in "Furry Friends" Shelter', fontsize=12)

# Bar chart with new colors
bars = ax2.bar(x_positions, adoptable_pets, color=['#FF6347', '#4682B4', '#32CD32', '#D2691E', '#8B008B', '#FF69B4', '#BDB76B'],
               width=bar_width, edgecolor='black', linestyle='-.')

for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=9)

ax2.set_xticks(x_positions)
ax2.set_xticklabels(shelters, rotation=30, ha='right', fontsize=11)
ax2.set_title("Adoptable Pets in Shelters", fontsize=14)
ax2.set_ylabel("Number of Pets", fontsize=11)
ax2.yaxis.grid(True, linestyle='-', linewidth=1, alpha=0.5)

plt.tight_layout()
plt.show()