import matplotlib.pyplot as plt

# Backstory: Imaginary Budget Distribution for a Fantasy Adventure Guild
# Title: "Annual Budget Allocation of the Wizards' Guild (2023)"

# Categories and their budget percentages
categories = ['Research and Development', 'Recruitment', 'Training', 'Resources', 'Field Missions', 'Miscellaneous']
budgets = [25, 15, 20, 10, 25, 5]

# Define colors for each slice
colors = ['#6b8e23', '#20b2aa', '#ff6347', '#ffa07a', '#ba55d3', '#ffd700']

# Create the main figure
fig, ax = plt.subplots(figsize=(10, 7))

# Basic Pie Chart with enhanced features
wedges, texts, autotexts = ax.pie(
    budgets,
    labels=categories,
    colors=colors,
    autopct='%1.1f%%',
    pctdistance=0.85,
    startangle=140,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Adding a circle to make the pie chart look like a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensuring the pie chart's aspect ratio is equal
ax.axis('equal')

# Customizing the appearance of texts
plt.setp(autotexts, size=10, weight="bold", color="white")
plt.setp(texts, size=11, weight="bold")

# Setting the title with additional formatting
ax.set_title("Annual Budget Allocation of the Wizards' Guild (2023)", fontsize=15, fontweight='bold', pad=20, color='#4b0082')

# Adding an outer legend for a clean look
ax.legend(wedges, categories, title="Budget Categories", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=10, title_fontsize='12')

# Applying tight layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()