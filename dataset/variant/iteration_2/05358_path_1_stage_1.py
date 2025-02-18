import matplotlib.pyplot as plt
import numpy as np

# Define fruit types and years
fruits = ["Apples", "Bananas", "Cherries", "Dates", "Elderberries"]
years = ["2018", "2019", "2020", "2021", "2022"]

# Data: Annual fruit production in tonnes
fruit_production = np.array([
    [150, 180, 200, 220, 240],  # Apples
    [100, 120, 140, 160, 180],  # Bananas
    [60, 80, 100, 120, 140],    # Cherries
    [20, 40, 60, 80, 100],      # Dates
    [10, 30, 50, 70, 90]        # Elderberries
])

# Calculate deviations from the average for each fruit
deviations = fruit_production - fruit_production.mean(axis=1, keepdims=True)

# Bar width for diverging bar chart
bar_width = 0.25
x = np.arange(len(years))

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
colors = ['#FF6666', '#FFCC66', '#99CCFF', '#66FF99', '#C299FF']

# First subplot: Diverging Bar Chart for deviations in fruit production
for i, fruit in enumerate(fruits):
    axs[0].bar(x + i * bar_width, deviations[i], width=bar_width, label=fruit, color=colors[i])

axs[0].set_title('Deviation from Average Production at Granary Farms\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Production Deviation in Tonnes', fontsize=14)
axs[0].set_xticks(x + bar_width * 2)
axs[0].set_xticklabels(years)
axs[0].axhline(0, color='black', linewidth=0.8)
axs[0].legend(title='Fruits', fontsize=12, title_fontsize='12')
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations for bar chart
for i in range(len(fruits)):
    for j in range(len(years)):
        axs[0].text(x[j] + i * bar_width, deviations[i, j] + (3 if deviations[i, j] >= 0 else -6), f'{deviations[i, j]:.0f}', ha='center', va='bottom' if deviations[i, j] >= 0 else 'top', fontsize=10)

# Second subplot remains unchanged: Pie Chart for average fruit production
average_production = np.mean(fruit_production, axis=1)
axs[1].pie(average_production, labels=fruits, colors=colors, autopct='%.1f%%', startangle=140, pctdistance=0.85)
axs[1].set_title('Average Fruit Production Share at Granary Farms\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)
axs[1].axis('equal')

plt.tight_layout()
plt.show()