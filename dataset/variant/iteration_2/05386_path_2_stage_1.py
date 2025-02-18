import matplotlib.pyplot as plt

# Data for food production (as percentages)
labels_food = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy']
production_sizes = [30, 25, 20, 15, 10]
colors_food = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0']

# Data for sweet consumption by colony (number of sweet items eaten per month)
colonies = ["Zeta-1", "Xenon-13", "Omaha-8", "Beta-3", "Lyra-22"]
sweet_consumption = [100, 150, 90, 110, 130]

fig, ax = plt.subplots(1, 2, figsize=(14, 7))

# Donut pie chart for food production
wedges, _, autotexts = ax[0].pie(
    production_sizes, 
    labels=labels_food, 
    autopct='%1.1f%%', 
    startangle=45,  # Changed start angle
    pctdistance=0.78,  # Altered percentage distance
    colors=colors_food, 
    wedgeprops={'width': 0.3, 'linewidth': 2, 'edgecolor': 'gray', 'alpha': 0.9},  # Changed edge color, width and alpha
    textprops=dict(color="navy", fontsize=9, weight='light')  # Changed text color and style
)

centre_circle = plt.Circle((0, 0), 0.62, fc='lightgrey', alpha=0.85)  # Changed center circle color and alpha
ax[0].add_artist(centre_circle)
ax[0].set_title('Galactic Food Resource Split', fontsize=16, fontweight='bold', pad=25)  # Changed title
ax[0].axis('equal')  

# Bar chart for sweet consumption
ax[1].bar(colonies, sweet_consumption, color='#8EC0E4', edgecolor='darkblue', hatch='//')  # Changed color and added hatch
ax[1].set_title('Colony Sweet Consumption', fontsize=14, fontweight='bold')  # Changed title
ax[1].set_ylabel('Sweet Items per Month', fontsize=12)
ax[1].set_xlabel('Planetary Colonies', fontsize=12)

# Annotate values on bar chart
for i, value in enumerate(sweet_consumption):
    ax[1].text(i, value + 3, str(value), ha='center', va='bottom', fontweight='light', fontsize=10, color='darkgreen')  # Changed text style

ax[1].grid(True, linestyle='--', linewidth=0.6, color='grey', alpha=0.7)  # Added a grid
ax[1].spines['top'].set_visible(False)  # Altered border by removing a spine
ax[1].spines['right'].set_visible(False)  # Altered border by removing a spine

plt.tight_layout()

plt.show()