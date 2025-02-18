import matplotlib.pyplot as plt
import numpy as np

shelters = ['B. Paw', 'F. Friends', 'H. Tails', 'P. Claws', 'L. Paws']
adoptable_pets = [180, 210, 200, 170, 230]  # Randomly altered values

pet_types = ['Dogs', 'Cats', 'Other']
pet_counts = [100, 90, 40]  # Randomly altered values

x_positions = np.arange(len(shelters))
bar_width = 0.6

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
fig.suptitle('Pets in Shelters - 2022', fontsize=16, fontweight='bold', y=1.02)

# Bar chart
bars = ax1.bar(x_positions, adoptable_pets, color=['#FF9999','#66B2FF','#99FF99','#FFCC99','#FFD700'], width=bar_width)

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 5, f'{yval}', ha='center', va='bottom', fontsize=10, fontweight='bold')

ax1.set_xticks(x_positions)
ax1.set_xticklabels(shelters, rotation=45, ha='right', fontsize=12)

ax1.set_title("Adoptable Pets", fontsize=14, fontweight='bold')
ax1.set_ylabel("Number", fontsize=12)

colors = ['#FF9999', '#66B2FF', '#99FF99']
explode = (0.1, 0, 0)

ax2.pie(pet_counts, labels=pet_types, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=140, textprops={'fontsize': 12, 'fontweight':'bold'})

centre_circle = plt.Circle((0,0),0.70,fc='white')
ax2.add_artist(centre_circle)

ax2.set_title('Types in "F. Friends"', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()