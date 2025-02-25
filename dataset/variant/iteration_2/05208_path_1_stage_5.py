import matplotlib.pyplot as plt

percentages = [30, 25, 15, 5]
single_color = '#7b3f00'  # Brown color used consistently
explode = (0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    percentages,
    startangle=140,
    colors=[single_color] * len(percentages),  # Applying the single color to all wedges
    explode=explode,
    shadow=True,
    wedgeprops=dict(width=0.3)
)

ax.axis('equal')
plt.show()