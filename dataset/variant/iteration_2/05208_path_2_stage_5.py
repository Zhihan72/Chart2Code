import matplotlib.pyplot as plt

percentages = [30, 25, 15, 10, 5]
single_color = '#7b3f00'  # Applying a consistent single color
explode = (0.05, 0.1, 0, 0, 0.1)

fig, ax = plt.subplots(figsize=(10, 8))

# Draw a donut pie chart by adjusting wedgeprops
wedges, _ = ax.pie(
    percentages, 
    startangle=90,
    colors=[single_color] * len(percentages),  # Use the single color for all wedges
    explode=explode,
    wedgeprops=dict(width=0.3, edgecolor='w', lw=2)
)

ax.axis('equal')

plt.tight_layout()
plt.show()