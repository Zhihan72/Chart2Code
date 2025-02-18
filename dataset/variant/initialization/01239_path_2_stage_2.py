import matplotlib.pyplot as plt

# Satisfaction scores for each department
satisfaction_scores = {
    'Computer Science': [8, 7, 9, 6, 8, 7, 9, 10, 9, 5, 7, 6, 8, 9, 7, 9],
    'Humanities': [6, 5, 7, 8, 6, 5, 6, 7, 5, 5, 6, 7, 5, 8, 4, 5],
    'Business': [7, 8, 6, 8, 7, 7, 9, 6, 6, 7, 7, 6, 7, 8, 9, 7],
    'Engineering': [9, 8, 7, 9, 10, 8, 7, 9, 8, 9, 8, 8, 9, 9, 8, 7],
    'Sciences': [7, 8, 7, 8, 7, 8, 6, 7, 7, 8, 8, 9, 7, 8, 6, 7]
}

# Prepare data
data = list(satisfaction_scores.values())

# Create the box plot
plt.figure(figsize=(10, 6))
box = plt.boxplot(data, notch=False, vert=False, patch_artist=True)

# Define colors and styling
colors = ['#C1FFD7', '#C1E1FF', '#FFE4C1', '#FFDDC1', '#FFD1DC']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Customize elements
plt.grid(axis='x', linestyle=':', linewidth=0.5, alpha=0.8)

for whisker in box['whiskers']:
    whisker.set(color='blue', linewidth=1)

for cap in box['caps']:
    cap.set(color='orange', linewidth=1)

for median in box['medians']:
    median.set(color='red', linewidth=1.5)

plt.tight_layout()
plt.show()