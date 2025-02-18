import numpy as np
import matplotlib.pyplot as plt

# Backstory: 
# The chart represents the fictional growth of various fruit-type plantations in the "Tropical Bay" over the years from 2000 to 2020. Each type of fruit plantation's growth is depicted to understand the trend in total plantation area (in hectares).

# Define the years from 2000 to 2020
years = np.arange(2000, 2021)

# Plantation area (in hectares) for different fruits
mango = np.array([5, 7, 8, 10, 14, 18, 22, 30, 40, 52, 65, 80, 98, 115, 135, 150, 170, 195, 220, 245, 270])
pineapple = np.array([4, 5, 6, 7, 9, 10, 12, 15, 18, 22, 27, 32, 40, 45, 50, 55, 62, 70, 78, 85, 92])
banana = np.array([6, 8, 10, 14, 18, 22, 28, 35, 42, 50, 60, 70, 85, 95, 110, 125, 140, 160, 182, 200, 225])
coconut = np.array([2, 3, 4, 5, 6, 7, 9, 11, 14, 17, 21, 25, 30, 35, 42, 50, 58, 68, 78, 88, 100])
papaya = np.array([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 18, 22, 25, 30, 35, 40, 45, 50, 55, 60, 66])

# Stack the data
plantation_data = np.vstack([mango, pineapple, banana, coconut, papaya])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(16, 10))

fruit_labels = ['Mango', 'Pineapple', 'Banana', 'Coconut', 'Papaya']
fruit_colors = ['#FFD700', '#FF6347', '#FFDAB9', '#8FBC8F', '#FFB6C1']

# Use stackplot for the area chart
ax.stackplot(years, plantation_data, labels=fruit_labels, colors=fruit_colors, alpha=0.85)

# Title and labels with necessary backstory context
ax.set_title("Growth of Fruit Plantations in Tropical Bay (2000-2020)", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Total Plantation Area (Hectares)', fontsize=14)

# Customize plot aesthetics
ax.legend(loc='upper left', fontsize=12, title='Fruit Type', frameon=False)
ax.grid(linestyle='--', alpha=0.5)

# Highlight some interesting points with annotations
ax.annotate('Mango Boom', xy=(2015, 150), xytext=(2010, 420),
            arrowprops=dict(facecolor='gold', arrowstyle='->', lw=2),
            fontsize=12, color='darkorange')

ax.annotate('Banana Surge', xy=(2018, 370), xytext=(2015, 600),
            arrowprops=dict(facecolor='yellowgreen', arrowstyle='->', lw=2),
            fontsize=12, color='olive')

# Text box for extra context
props = dict(boxstyle='round', facecolor='#DDDDDD', alpha=0.5)
additional_info = (
    "Over the years, Tropical Bay witnessed\n"
    "a significant surge in fruit plantations.\n"
    "The prominence of Mango and Banana cultivation\n"
    "led to a flourishing agricultural sector."
)
ax.text(0.02, 0.95, additional_info, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=props)

# Better readability for x-axis labels
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 701, 100))

# Highlight start and end values for each fruit type
for idx, fruit in enumerate(fruit_labels):
    ax.annotate(f'{plantation_data[idx, 0]}', (2000, plantation_data[idx, 0]), textcoords="offset points", xytext=(-15,5), ha='center')
    ax.annotate(f'{plantation_data[idx, -1]}', (2020, plantation_data[idx, -1] + np.sum(plantation_data[:idx, -1])), textcoords="offset points", xytext=(-15,-10), ha='center')

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()