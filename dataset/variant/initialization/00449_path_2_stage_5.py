import matplotlib.pyplot as plt

meanings = [40, 20, 15, 15, 10, 25, 5]
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#EE82EE', '#8A2BE2', '#5F9EA0']  # Different colors for each section
explode = (0.1, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(meanings, startangle=100, colors=colors, explode=explode,
                       shadow=False, wedgeprops={'edgecolor': 'gray', 'linestyle': '--', 'linewidth': 2})

centre_circle = plt.Circle((0,0),0.65,fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')
ax.grid(True, linestyle=':', linewidth=1)  # Adding a grid

ax.legend(wedges, [f'Part {i}' for i in range(len(meanings))], loc='upper right')  # Adding legend with labels

plt.show()