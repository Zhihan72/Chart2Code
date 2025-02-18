import matplotlib.pyplot as plt
import numpy as np

countries = ['JavaNation', 'Brazil', 'Belgium', 'Iceland', 'Imaginaryland', 
             'Netherlands', 'Canada', 'Finland', 'CoffeeTopia', 'Switzerland',
             'Norway', 'Sweden', 'Denmark']
consumption_kg = [9.5, 6.1, 6.8, 9, 10.5, 
                  8.4, 6.5, 12, 11.2, 7.9,
                  9.9, 8.2, 8.7]

sorted_indices = np.argsort(consumption_kg)[::-1]
countries_sorted = [countries[i] for i in sorted_indices]
consumption_sorted = [consumption_kg[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#B0C4DE', '#32CD32', '#FF8C00', '#8A2BE2', '#DC143C', 
          '#9370DB', '#FF69B4', '#ADFF2F', '#20B2AA', '#1E90FF',
          '#FF6347', '#FFD700', '#00CED1']

ax.barh(countries_sorted, consumption_sorted, color=colors, edgecolor='darkslategray')

# Randomly alter the title:
ax.set_title('Caffeine Excursion:\nLeading Coffee Consumers of 2023', fontsize=16, fontweight='bold', pad=15)

# Randomly alter the x-axis label:
ax.set_xlabel('Annual Coffee Intake (kg per person)', fontsize=12)

# Randomly annotate the bars, swap consumption values and units
for bar in ax.containers[0]:
    width = bar.get_width()
    ax.annotate(f'{width} /kg', xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0), textcoords='offset points',
                ha='left', va='center', fontsize=10, color='black')

ax.tick_params(axis='y', which='major', labelsize=10)

plt.tight_layout()
plt.show()