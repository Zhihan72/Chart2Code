import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# In the fantastical realm of Lyretia, the capital city allocates its budget across various aspects of daily life. 
# The pie chart will illustrate the allocation for the year 3050. The additional subplot will show the trend 
# of technology advancement over the past five decades to support this futuristic context.

# Define budget categories
budget_categories = [
    'Urban Development',
    'Healthcare Initiatives',
    'Technological Advancements',
    'Education Programs',
    'Public Safety',
    'Environmental Sustainability',
    'Arts & Culture',
    'Transportation Infrastructure'
]

# Corresponding budget allocation percentages
budget_allocation = [25, 20, 18, 15, 10, 6, 4, 2]

# Ensure the sum of allocation percentages is 100
assert sum(budget_allocation) == 100, "The budget allocations must sum up to 100."

# Define colors for each budget category
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD433', '#FF6666', '#66CCCC', '#93FF33']

# Define explode array
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(1, 2, figsize=(18, 9))

# Plot the pie chart
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

# Define data for technological advancements over the past five decades
years = np.arange(3000, 3051, 10)
tech_advancement = {
    'AI and Robotics': np.array([10, 15, 20, 25, 35, 40]),
    'Sustainable Energy': np.array([5, 10, 15, 20, 30, 38]),
    'Biotechnology': np.array([8, 12, 18, 23, 27, 33]),
}

# Plot the line chart for technological advancements
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