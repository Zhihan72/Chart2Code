import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2011, 2021)
tomatoes = np.array([62, 60, 70, 55, 50, 75, 65, 64, 58, 80])
carrots = np.array([52, 49, 42, 60, 40, 50, 58, 55, 47, 45])
cucumbers = np.array([35, 48, 30, 42, 32, 37, 50, 45, 40, 38])
lettuce = np.array([32, 38, 22, 34, 20, 24, 26, 28, 36, 30])

# Sort data for each vegetable
sorted_indices_tomatoes = np.argsort(tomatoes)
sorted_indices_carrots = np.argsort(carrots)
sorted_indices_cucumbers = np.argsort(cucumbers)
sorted_indices_lettuce = np.argsort(lettuce)

# Apply sorting to vegetable yields and corresponding years
sorted_years_tomatoes = years[sorted_indices_tomatoes]
sorted_tomatoes = tomatoes[sorted_indices_tomatoes]

sorted_years_carrots = years[sorted_indices_carrots]
sorted_carrots = carrots[sorted_indices_carrots]

sorted_years_cucumbers = years[sorted_indices_cucumbers]
sorted_cucumbers = cucumbers[sorted_indices_cucumbers]

sorted_years_lettuce = years[sorted_indices_lettuce]
sorted_lettuce = lettuce[sorted_indices_lettuce]

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.2

# Plot sorted bar charts for each vegetable
ax.bar(sorted_years_tomatoes - width * 1.5, sorted_tomatoes, width, label='Tomatoes', color='tomato', hatch='x')
ax.bar(sorted_years_carrots - width / 2, sorted_carrots, width, label='Carrots', color='orange', hatch='o')
ax.bar(sorted_years_cucumbers + width / 2, sorted_cucumbers, width, label='Cucumbers', color='green', hatch='//')
ax.bar(sorted_years_lettuce + width * 1.5, sorted_lettuce, width, label='Lettuce', color='lightgreen', hatch='\\')

ax.set_title('Community Garden Vegetable Yields (2011-2020)', fontsize=18, fontweight='normal', pad=20)
ax.set_xlabel('Year', fontsize=12, color='blue')
ax.set_ylabel('Yield (kg)', fontsize=12, color='blue')
ax.set_xticks(np.arange(2011, 2021))
ax.set_yticks(np.arange(0, 100, 10))
ax.grid(True, linestyle='-', alpha=0.7)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='lower right', fontsize=12, edgecolor='grey', title='Vegetables', title_fontsize=12)

plt.tight_layout()
plt.show()