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

# Calculate the average production per fruit over the years
average_production = np.mean(fruit_production, axis=1)

# Bar width for grouped bar chart
bar_width = 0.15
x = np.arange(len(years))

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 1]})
colors = ['#FF6666', '#FFCC66', '#99CCFF', '#66FF99', '#C299FF']

# First subplot: Grouped Bar Chart for yearly fruit production
for i, fruit in enumerate(fruits):
    axs[0].bar(x + i * bar_width, fruit_production[i], width=bar_width, label=fruit, color=colors[i])

axs[0].set_title('Annual Fruit Production at Granary Farms\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Production in Tonnes', fontsize=14)
axs[0].set_xticks(x + bar_width * 2)
axs[0].set_xticklabels(years)
axs[0].legend(title='Fruits', fontsize=12, title_fontsize='12')
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Add text annotations for bar chart
for i in range(len(fruits)):
    for j in range(len(years)):
        axs[0].text(x[j] + i * bar_width, fruit_production[i, j] + 3, str(fruit_production[i, j]), ha='center', va='bottom', fontsize=10)

# Second subplot: Pie Chart for average fruit production
axs[1].pie(average_production, labels=fruits, colors=colors, autopct='%.1f%%', startangle=140, pctdistance=0.85)
axs[1].set_title('Average Fruit Production Share at Granary Farms\n(2018-2022)', fontsize=16, fontweight='bold', pad=20)

# Draw circle and set ratio to make pie chart look like a donut
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)
axs[1].axis('equal')

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()