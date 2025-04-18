import matplotlib.pyplot as plt

# Updated data with an additional food category and its production size
labels_food = ['Fruits', 'Vegetables', 'Grains', 'Proteins', 'Dairy', 'Spices']
production_sizes = [30, 25, 20, 15, 10, 5]
colors_food = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2F0', '#FFB6C1']

# Added a new colony and its sweet consumption data
colonies = ["Zeta-1", "Xenon-13", "Omaha-8", "Beta-3", "Lyra-22", "Gamma-6"]
sweet_consumption = [100, 150, 90, 110, 130, 120]

fig, ax = plt.subplots(2, 1, figsize=(10, 12))

# Update the pie chart to display the extra category
ax[0].pie(
    production_sizes, 
    labels=labels_food, 
    autopct='%1.1f%%', 
    startangle=45,  
    colors=colors_food, 
    textprops=dict(color="navy", fontsize=9, weight='light')
)
ax[0].set_title('Galactic Food Resource Split', fontsize=16, fontweight='bold', pad=25)
ax[0].axis('equal')

# Update the bar chart to display the extra colony and sweet consumption
ax[1].bar(colonies, sweet_consumption, color='#8EC0E4', edgecolor='darkblue', hatch='//')
ax[1].set_title('Colony Sweet Consumption', fontsize=14, fontweight='bold')
ax[1].set_ylabel('Sweet Items per Month', fontsize=12)
ax[1].set_xlabel('Planetary Colonies', fontsize=12)

for i, value in enumerate(sweet_consumption):
    ax[1].text(i, value + 3, str(value), ha='center', va='bottom', fontweight='light', fontsize=10, color='darkgreen')

ax[1].grid(True, linestyle='--', linewidth=0.6, color='grey', alpha=0.7)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()