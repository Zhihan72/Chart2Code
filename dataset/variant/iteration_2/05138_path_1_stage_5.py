import matplotlib.pyplot as plt

# Household A spending data
household_a_spending = [500, 450, 400, 150, 200, 450, 320, 100, 350, 420, 280, 370]

# Create a vertical box plot for Household A
fig, ax = plt.subplots(figsize=(8, 6))
box = ax.boxplot(household_a_spending, vert=True, patch_artist=True, 
                 notch=False, widths=0.6)

# Custom color for the box
box_color = '#FF69B4'
for patch in box['boxes']:
    patch.set_facecolor(box_color)

# Customize whiskers and caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='darkred', linewidth=1)
    cap.set(color='darkred', linewidth=1)

# Customize medians
for median in box['medians']:
    median.set(color='green', linewidth=2.5)

ax.grid(axis='x', linestyle='-.', alpha=0.5)
plt.tight_layout()
plt.show()