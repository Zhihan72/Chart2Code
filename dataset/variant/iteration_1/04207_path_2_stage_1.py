import matplotlib.pyplot as plt
import numpy as np

tribes = ['Elves', 'Dwarves', 'Orcs', 'Humans', 'Halflings', 'Goblins']
# Shuffled and modified average age of adulthood and average years of education
average_age_adulthood = np.array([18, 25, 14, 33, 120, 70])  # in years
average_years_education = np.array([12, 15, 6, 20, 80, 50])  # in years

fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(average_age_adulthood, average_years_education, 
                     c=average_years_education, cmap='plasma', s=200, 
                     edgecolors='black', alpha=0.8)

ax.set_title('Fantastical Education Journey: Age of Adulthood vs. Years of Education\nAcross Various Tribes', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Average Age of Adulthood (Years)', fontsize=13)
ax.set_ylabel('Average Years of Education', fontsize=13)

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Years of Education', fontsize=13, fontweight='bold')

for i, tribe in enumerate(tribes):
    ax.annotate(tribe, (average_age_adulthood[i], average_years_education[i]), 
                fontsize=11, ha='right', va='bottom', color='white', weight='bold', 
                bbox=dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0.3'))

ax.grid(True, linestyle='--', alpha=0.5)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlim(10, 130)
ax.set_ylim(0, 90)

plt.tight_layout()
plt.show()