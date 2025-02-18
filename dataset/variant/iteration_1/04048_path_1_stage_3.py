import matplotlib.pyplot as plt

nodes = {
    'Solar Panels': 3,
    'Wind Turbines': 6,
    'Hydropower': 2,
    'Geothermal': 4,
    'Biomass': 5,
    'Energy Storage': 7,
    'Grid Distribution': 3,
    'Smart Grids': 6
}

# Sort nodes by weights in descending order
sorted_nodes = sorted(nodes.items(), key=lambda item: item[1], reverse=True)
labels, values = zip(*sorted_nodes)

plt.figure(figsize=(12, 8))

# Randomly alter stylistic elements
plt.bar(labels, values, color=plt.cm.plasma([val / max(values) for val in values]), edgecolor='gray', linestyle='--', hatch='/')

# Add altered labels and title
plt.xlabel('Components', fontsize=12, fontstyle='italic')
plt.ylabel('Importance', fontsize=12, fontstyle='italic')
plt.title('Random Importance of Renewable Energy Components', fontsize=18, fontweight='heavy')

# Add values on top of bars with altered fonts
for i, v in enumerate(values):
    plt.text(i, v + 0.2, str(v), ha='center', va='bottom', fontstyle='italic', color='darkred', fontsize=10)

# Different tick and grid styles
plt.xticks(rotation=30, ha='right', fontsize=10, color='darkblue')
plt.yticks(fontsize=10, color='darkblue')
plt.grid(axis='y', linestyle='-', linewidth=0.5, color='black')

# Alter legend
plt.legend(['Energy Components'], loc='upper right', frameon=False, fontsize=10)

plt.tight_layout()
plt.show()