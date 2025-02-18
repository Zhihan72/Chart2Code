import matplotlib.pyplot as plt

# Manually shuffled growth data within the original structure
growth_data = [
    [65, 60, 68, 67, 62, 61, 64, 58, 66, 63, 60, 65],  # Shuffled group 1
    [38, 39, 34, 42, 35, 39, 41, 36, 37, 40, 43, 38],  # Shuffled group 2
    [11, 10, 8, 14, 12, 10, 12, 15, 11, 9, 13, 9],     # Shuffled group 3
    [4, 5, 5, 3, 4, 6, 5, 4, 6, 3, 4, 5]               # Shuffled group 4
]

plt.figure(figsize=(10, 6))
box = plt.boxplot(growth_data, patch_artist=True, notch=True, medianprops={'color': 'red'})

colors = ['skyblue', 'lightgreen', 'lightcoral', 'plum']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()