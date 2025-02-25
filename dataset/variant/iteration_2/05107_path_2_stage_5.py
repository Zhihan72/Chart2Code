import matplotlib.pyplot as plt

# Manually shuffled data to randomly alter content
kids_data = [7, 5, 6, 9, 5, 6, 8, 5, 10, 7, 4, 6, 4, 8, 5, 7, 7, 11, 12]
teens_data = [8, 6, 9, 7, 9, 7, 8, 10, 12, 11, 7, 9, 8, 10, 10, 6, 8, 13, 14]
adults_data = [15, 10, 12, 11, 12, 14, 13, 12, 14, 9, 14, 13, 12, 14, 15, 17, 18, 19, 20]
seniors_data = [9, 8, 10, 7, 11, 9, 11, 12, 10, 8, 9, 8, 7, 10, 9, 8, 10, 11, 12]

data = [kids_data, teens_data, adults_data, seniors_data]

plt.figure(figsize=(12, 7))

box = plt.boxplot(data, patch_artist=True, notch=False, vert=True)

colors = ['#008080', '#FF6347', '#4682B4', '#B22222']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['whiskers'], color='grey', linewidth=1)
plt.setp(box['caps'], color='grey', linewidth=1)
plt.setp(box['medians'], color='darkred', linewidth=3)
plt.setp(box['fliers'], marker='s', color='purple', alpha=0.7)

plt.grid(axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()