import matplotlib.pyplot as plt

# Combined dataset
all_preferences = [300, 200, 150, 100, 150, 100, 180, 220, 160]
# Shuffled colors for each data group
all_colors = ['#FFD700', '#D2691E', '#5F9EA0', '#FF9999', '#FFA500', '#9ACD32', '#FFDAB9', '#FF69B4', '#8A2BE2']

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(all_preferences, colors=all_colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10, 'color': 'purple'})

plt.tight_layout()
plt.show()