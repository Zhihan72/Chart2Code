import matplotlib.pyplot as plt

regions = ['Asia', 'Europe', 'Africa', 'North America', 'Latin America & Caribbean', 'Oceania']
usage_percentages = [53, 15, 12, 10, 7, 3]

# Applying random stylistic elements
colors = ['#33FFF9', '#FF33A8', '#FF5733', '#3357FF', '#F9FF33', '#33FF57']  # shuffled colors

explode = (0, 0.1, 0, 0, 0, 0)  # changed explode position

plt.figure(figsize=(10, 7))
wedges, texts = plt.pie(usage_percentages, startangle=140, colors=colors,
                                   explode=explode, pctdistance=0.9, shadow=False)

# Varying the font style and weight for the percentages
for text in texts:
    text.set_fontsize(10)
    text.set_fontweight('light')

centre_circle = plt.Circle((0, 0), 0.70, fc='white', linestyle='--', linewidth=1.5)  # dashed line style for circle border
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Global Internet Users\nDistribution by Region (2023)', fontsize=14, fontweight='medium')  # changed font size and weight
plt.axis('equal')

# Removing the legend for a cleaner look
# Adding a grid for better visual aid
plt.grid(which='major', linestyle=':', linewidth=0.5)  # dotted grid style

plt.tight_layout()
plt.show()