import matplotlib.pyplot as plt

# Original dataset
preferences = [300, 200, 150, 100, 150, 100]
colors = ['#FF9999', '#FFD700', '#FF69B4', '#FFDAB9', '#FFA500', '#9ACD32']

# New additional data series or groups
additional_preferences = [180, 220, 160]
additional_colors = ['#8A2BE2', '#5F9EA0', '#D2691E']

# Combine original and additional data
all_preferences = preferences + additional_preferences
all_colors = colors + additional_colors

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(all_preferences, colors=all_colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10, 'color': 'purple'})

plt.tight_layout()
plt.show()