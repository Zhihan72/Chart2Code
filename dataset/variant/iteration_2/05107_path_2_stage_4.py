import matplotlib.pyplot as plt

kids_data = [5, 7, 6, 4, 5, 6, 8, 9, 10, 7, 5, 6, 4, 6, 5, 7, 8, 11, 12]
teens_data = [6, 8, 9, 7, 7, 6, 8, 10, 12, 11, 10, 9, 7, 9, 8, 10, 8, 13, 14]
adults_data = [9, 10, 12, 11, 12, 14, 13, 12, 14, 15, 14, 13, 12, 14, 15, 17, 18, 19, 20]
seniors_data = [8, 10, 9, 7, 8, 9, 11, 12, 10, 11, 9, 8, 7, 10, 9, 8, 10, 11, 12]

data = [kids_data, teens_data, adults_data, seniors_data]

plt.figure(figsize=(12, 7))

box = plt.boxplot(data, patch_artist=True, notch=False, vert=True)

# Apply a new set of colors
colors = ['#008080', '#FF6347', '#4682B4', '#B22222']  # Teal, Tomato, SteelBlue, and Firebrick
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['whiskers'], color='grey', linewidth=1)
plt.setp(box['caps'], color='grey', linewidth=1)
plt.setp(box['medians'], color='darkred', linewidth=3)
plt.setp(box['fliers'], marker='s', color='purple', alpha=0.7)

plt.grid(axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()