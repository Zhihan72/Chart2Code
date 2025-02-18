import matplotlib.pyplot as plt

# Manually shuffled content within the data group while maintaining the 6 groups of 6 data points
altered_spending = [
    450, 500, 400, 150, 320, 450, 200, 100, 350, 420, 280, 370,
    460, 520, 390, 310, 460, 160, 95, 445, 390, 525, 350, 210,
    220, 520, 395, 145, 195, 425, 325, 95, 340, 365, 275, 450
]

fig, ax = plt.subplots(figsize=(8, 6))
box = ax.boxplot(altered_spending, vert=True, patch_artist=True, 
                 notch=True, whis=1.5)

single_color = '#FFD700'
for patch in box['boxes']:
    patch.set_facecolor(single_color)

ax.set_title('Household Expenditure Overview', fontsize=14, fontweight='medium')
ax.set_ylabel('Expenditure (USD)', fontsize=10)
ax.grid(axis='x', linestyle='-.', alpha=0.5)

for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='darkred', linewidth=2)
    cap.set(color='darkred', linestyle='-', linewidth=2)

for median in box['medians']:
    median.set(color='green', linewidth=3)

ax.legend(['Spending Distribution'], loc='upper right', frameon=False)

plt.tight_layout()
plt.show()