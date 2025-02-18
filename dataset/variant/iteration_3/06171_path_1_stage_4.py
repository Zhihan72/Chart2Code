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

# Donut chart
explode = (0.1, 0.2, 0)  # changed explode for the first two slices
ax1.pie(pet_counts_1, labels=pet_types, explode=explode, colors=['#FFA07A', '#8A2BE2', '#3CB371'],
        autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 11}, 
        wedgeprops={'width': 0.3})  # added a border to wedges
ax1.set_title('Pet Types in "Furry Friends" Shelter', fontsize=12)

# Bar chart
bars = ax2.bar(x_positions, adoptable_pets, color=['#FFA07A', '#8A2BE2', '#3CB371', '#DAA520', '#FF4500', '#20B2AA', '#9370DB'],
               width=bar_width, edgecolor='black', linestyle='-.')  # altered edge/border style

for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=9)

ax2.set_xticks(x_positions)
ax2.set_xticklabels(shelters, rotation=30, ha='right', fontsize=11)  # adjusted rotation
ax2.set_title("Adoptable Pets in Shelters", fontsize=14)
ax2.set_ylabel("Number of Pets", fontsize=11)
ax2.yaxis.grid(True, linestyle='-', linewidth=1, alpha=0.5)  # changed grid line style

plt.tight_layout()
plt.show()