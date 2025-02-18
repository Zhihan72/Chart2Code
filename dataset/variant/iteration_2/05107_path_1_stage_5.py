import matplotlib.pyplot as plt

kids_data = [5, 7, 6, 4, 5, 6, 8, 9, 10, 7, 5, 6, 4, 6, 5, 7, 8, 11, 12]
teens_data = [6, 8, 9, 7, 7, 6, 8, 10, 12, 11, 10, 9, 7, 9, 8, 10, 8, 13, 14]
adults_data = [9, 10, 12, 11, 12, 14, 13, 12, 14, 15, 14, 13, 12, 14, 15, 17, 18, 19, 20]

data = [kids_data, teens_data, adults_data]

plt.figure(figsize=(12, 7))
box = plt.boxplot(data, patch_artist=True, notch=True, vert=False)

colors = ['#FF5733', '#900C3F', '#C70039']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['whiskers'], color='black', linewidth=1.5)
plt.setp(box['caps'], color='black', linewidth=1.5)
plt.setp(box['medians'], color='blue', linewidth=2)
plt.setp(box['fliers'], marker='o', color='green', alpha=0.5)

plt.box(False)
plt.tight_layout()
plt.show()