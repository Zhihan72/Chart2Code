import matplotlib.pyplot as plt

# Backstory
# The Galactic Food Council manages the distribution of food resources across five distinct planetary colonies. 
# Each colony specializes in producing certain types of food, which are crucial for the survival and cultural richness
# of the galactic community. The council regularly evaluates and displays food production data to ensure balanced distribution 
# and sustainability.

# Title: "Galactic Food Production Distribution and Sweet Consumption Overview"

# Data for food production (as percentages)
labels_food = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy']
production_sizes = [30, 25, 20, 15, 10]
colors_food = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Data for sweet consumption by colony (number of sweet items eaten per month)
colonies = ["Zeta-1", "Xenon-13", "Omaha-8", "Beta-3", "Lyra-22"]
sweet_consumption = [100, 150, 90, 110, 130]

# Create the figure and axes
fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Donut pie chart for food production
wedges, texts, autotexts = ax[0].pie(
    production_sizes, 
    labels=labels_food, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85, 
    colors=colors_food, 
    wedgeprops={'width': 0.4, 'edgecolor': 'w', 'alpha': 0.85},
    textprops=dict(color="black", fontsize=10, weight='bold')
)

# Center circle to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax[0].add_artist(centre_circle)
ax[0].set_title('Galactic Food Production Distribution', fontsize=14, fontweight='bold', pad=20)
ax[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Bar chart for sweet consumption
ax[1].bar(colonies, sweet_consumption, color='#FFDA79', edgecolor='black')
ax[1].set_title('Monthly Sweet Consumption by Colony', fontsize=14, fontweight='bold')
ax[1].set_ylabel('Number of Sweet Items', fontsize=12)
ax[1].set_xlabel('Colonies', fontsize=12)

# Annotate values on bar chart
for i, value in enumerate(sweet_consumption):
    ax[1].text(i, value + 3, str(value), ha='center', va='bottom', fontweight='bold')

# Optimize layout
plt.tight_layout()

# Show the plot
plt.show()