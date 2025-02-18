import matplotlib.pyplot as plt

percentages = [25, 20, 15, 18, 12, 10]

single_color = ['#66c2a5' for _ in range(len(percentages))]
explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(
    percentages, 
    labels=None,  # No labels for the pie segments
    autopct=None,  # Remove percentage display
    startangle=90, 
    colors=single_color,
    explode=explode
)

ax.axis('equal')
plt.show()