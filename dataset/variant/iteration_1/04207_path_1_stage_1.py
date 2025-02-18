import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
tribes = ['Elves', 'Dwarves', 'Orcs', 'Humans', 'Halflings', 'Goblins']
average_age_adulthood = np.array([120, 70, 25, 18, 33, 14])  # in years
average_years_education = np.array([80, 50, 15, 12, 20, 6])  # in years

# Scatter plot with a single consistent color for all points
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(average_age_adulthood, average_years_education, 
                     c='royalblue', s=200, 
                     edgecolors='black', alpha=0.8)

# Title and labels
ax.set_title('Fantastical Education Journey: Age of Adulthood vs. Years of Education\nAcross Various Tribes', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Average Age of Adulthood (Years)', fontsize=13)
ax.set_ylabel('Average Years of Education', fontsize=13)

# Annotate each point with tribe name
for i, tribe in enumerate(tribes):
    ax.annotate(tribe, (average_age_adulthood[i], average_years_education[i]), 
                fontsize=11, ha='right', va='bottom', color='white', weight='bold', 
                bbox=dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0.3'))

# Enhancements
ax.grid(True, linestyle='--', alpha=0.5)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xlim(10, 130)
ax.set_ylim(0, 90)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()