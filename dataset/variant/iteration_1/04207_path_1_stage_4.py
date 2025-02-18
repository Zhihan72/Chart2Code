import matplotlib.pyplot as plt
import numpy as np

# Data for the plot, including new tribes
tribes = ['Elves', 'Dwarves', 'Orcs', 'Humans', 'Halflings', 'Goblins', 'Gnomes', 'Trolls', 'Fairies']
average_years_education = np.array([80, 50, 15, 12, 20, 6, 60, 10, 70])  # additional data added

# Horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.barh(tribes, average_years_education, color='skyblue', edgecolor='black', alpha=0.8)

# Title and labels
ax.set_title('Fantastical Education Journey: Years of Education Across Various Tribes', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Average Years of Education', fontsize=13)
ax.set_ylabel('Tribes', fontsize=13)

# Remove borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Remove grid
ax.grid(False)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()