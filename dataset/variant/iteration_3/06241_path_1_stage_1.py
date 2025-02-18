import matplotlib.pyplot as plt
import numpy as np

# Define budget categories with additional fictitious data
budget_categories = [
    'Urban Development',
    'Healthcare Initiatives',
    'Technological Advancements',
    'Education Programs',
    'Public Safety',
    'Environmental Sustainability',
    'Arts & Culture',
    'Transportation Infrastructure',
    'Space Exploration',
    'Quantum Computing Research'
]

# Corresponding budget allocation percentages with additional categories
budget_allocation = [20, 18, 15, 12, 10, 6, 4, 2, 8, 5]

# Define colors for each budget category, adding more colors
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD433', '#FF6666', '#66CCCC', '#93FF33', '#CC99FF', '#33FFCC']

# Define explode array for emphasis on certain categories
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(1, 2, figsize=(18, 9))

# Plot the pie chart with added categories
wedges, texts, autotexts = ax[0].pie(
    budget_allocation, explode=explode, labels=budget_categories, colors=colors,
    autopct='%1.1f%%', startangle=140, pctdistance=0.85, shadow=True, wedgeprops=dict(edgecolor='k')
)

# Customize text properties
for text in texts:
    text.set_fontsize(11)
    text.set_color('navy')

for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('darkred')

# Draw a circle at the center to transform the pie into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title and additional styling
ax[0].set_title("Lyretia Capital Budget Allocation (3050)", fontsize=16, fontweight='bold', pad=20)

# Define data for technological advancements over the past five decades with additional sectors
years = np.arange(3000, 3051, 10)
tech_advancement = {
    'AI and Robotics': np.array([10, 15, 20, 25, 35, 40]),
    'Sustainable Energy': np.array([5, 10, 15, 20, 30, 38]),
    'Biotechnology': np.array([8, 12, 18, 23, 27, 33]),
    'Quantum Computing': np.array([2, 7, 12, 18, 25, 32]),
    'Space Technologies': np.array([3, 6, 10, 15, 22, 28])
}

# Plot the line chart for technological advancements with new data series
for tech, improvements in tech_advancement.items():
    ax[1].plot(years, improvements, label=tech, marker='o', linewidth=2.5)

# Customize line chart 
ax[1].set_title('Technological Advancements (3000-3050)', fontsize=16, fontweight='bold', pad=20)
ax[1].set_xlabel('Year', fontsize=12, fontweight='bold')
ax[1].set_ylabel('Advancement Index', fontsize=12, fontweight='bold')
ax[1].legend(title="Technology Sectors", fontsize='medium', loc='best')
ax[1].grid(True, which='both', linestyle='--', linewidth=0.5)

# Layout and display
plt.tight_layout()
plt.show()