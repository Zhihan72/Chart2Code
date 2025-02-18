import matplotlib.pyplot as plt

budgets = [22, 12, 18, 11, 20, 4, 13]
colors = ['#ffd700', '#4682b4', '#20b2aa', '#ff6347', '#6b8e23', '#ba55d3', '#ffa07a']

fig, ax = plt.subplots(figsize=(10, 7))

# Modify the pie chart styles
ax.pie(
    budgets,
    colors=colors,
    autopct='%1.1f%%',  # percentage display
    startangle=90,      # different start angle
    wedgeprops=dict(edgecolor='navy', linewidth=2, linestyle='--')  # customize wedge border
)

# Add a legend with a different location and shadow effect
ax.legend(
    loc='upper right',  # place legend at the upper right corner
    shadow=True,        # add shadow effect for the legend
    fontsize='large'    # change the font size of the legend
)

# Modify grid and ticks
ax.set_xticks([])  # remove x-axis ticks
ax.set_yticks([])  # remove y-axis ticks
ax.grid(visible=False)  # turn off grid

plt.tight_layout()
plt.show()