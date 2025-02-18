import matplotlib.pyplot as plt
import numpy as np

tomatoes = np.array([60, 55, 58, 65, 62, 64, 50, 70, 75, 80])
carrots = np.array([49, 42, 50, 47, 40, 52, 45, 55, 58, 60])
cucumbers = np.array([37, 32, 35, 30, 38, 40, 42, 45, 48, 50])
lettuce = np.array([20, 28, 24, 26, 32, 30, 22, 34, 36, 38])

total_yields = {
    'Tomatoes': np.sum(tomatoes),
    'Carrots': np.sum(carrots),
    'Cucumbers': np.sum(cucumbers),
    'Lettuce': np.sum(lettuce)
}

sorted_vegetables = sorted(total_yields.items(), key=lambda item: item[1], reverse=True)
vegetable_names, sorted_totals = zip(*sorted_vegetables)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(vegetable_names, sorted_totals, color=['#FF6347', '#FFA500', '#32CD32', '#9ACD32'])

ax.set_title('Total Yields of Vegetables (2011-2020)', fontsize=16, fontweight='bold')
ax.set_ylabel('Total Yield (kg)', fontsize=12)

plt.tight_layout()
plt.show()