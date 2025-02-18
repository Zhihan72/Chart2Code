import matplotlib.pyplot as plt

aggregate_spending = [
    500, 450, 400, 150, 200, 450, 320, 100, 350, 420, 280, 370,
    520, 460, 390, 160, 210, 460, 310, 90, 340, 430, 270, 365,
    495, 445, 395, 145, 195, 455, 325, 95, 345, 415, 275, 360
]

fig, ax = plt.subplots(figsize=(8, 6))
box = ax.boxplot(aggregate_spending, vert=True, patch_artist=True, 
                 notch=True, whis=1.5)

colors = ['#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

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