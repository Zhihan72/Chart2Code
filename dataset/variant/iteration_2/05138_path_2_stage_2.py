import matplotlib.pyplot as plt

# Aggregate data for single-group vertical box plot
aggregate_spending = [
    500, 450, 400, 150, 200, 450, 320, 100, 350, 420, 280, 370,
    520, 460, 390, 160, 210, 460, 310, 90, 340, 430, 270, 365,
    495, 445, 395, 145, 195, 455, 325, 95, 345, 415, 275, 360
]

# Create a vertical box plot for a single group
fig, ax = plt.subplots(figsize=(8, 6))
box = ax.boxplot(aggregate_spending, vert=True, patch_artist=True, 
                 notch=True, whis=1.5)

# Set custom color for the single group box
colors = ['#87CEEB']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Set title and labels
ax.set_title('Aggregate Household Spending', fontsize=16, fontweight='bold')
ax.set_ylabel('Amount Spent (USD)', fontsize=12)

# Add grid for better readability
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Customize whiskers and caps
for whisker, cap in zip(box['whiskers'], box['caps']):
    whisker.set(color='gray', linewidth=1.5)
    cap.set(color='gray', linewidth=1.5)

# Customize medians
for median in box['medians']:
    median.set(color='blue', linewidth=2)

# Avoid overlapping and ensure the layout is tight
plt.tight_layout()

# Display the plot
plt.show()