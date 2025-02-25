import matplotlib.pyplot as plt
import numpy as np

fruits = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
years = ["2018", "2019", "2020", "2021", "2022"]

fruit_production = np.array([
    [150, 180, 200, 220, 240],  # Apples
    [100, 120, 140, 160, 180],  # Bananas
    [60, 80, 100, 120, 140],    # Cherries
    [20, 40, 60, 80, 100],      # Dates
    [10, 30, 50, 70, 90]        # Elderberries
])

average_production = np.mean(fruit_production, axis=1)

bar_width = 0.15
x = np.arange(len(years))

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
colors = ['#FFCC66', '#66FF99', '#C299FF', '#99CCFF', '#FF6666']

# Bar chart for yearly production
for i, fruit in enumerate(fruits):
    axs[0].bar(x + i * bar_width, fruit_production[i], width=bar_width, color=colors[i])

axs[0].set_title('Fruit Production (2018-22)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Tonnes', fontsize=14)
axs[0].set_xticks(x + bar_width * 2)
axs[0].set_xticklabels(years)

# Adding values on top of bars
for i in range(len(fruits)):
    for j in range(len(years)):
        axs[0].text(x[j] + i * bar_width, fruit_production[i, j] + 3, str(fruit_production[i, j]), ha='center', va='bottom', fontsize=10)

# Standard pie chart for average production share
axs[1].pie(average_production, labels=fruits, colors=colors, autopct='%.1f%%', startangle=140)
axs[1].set_title('Avg. Production Share (2018-22)', fontsize=16, fontweight='bold', pad=20)
axs[1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.show()