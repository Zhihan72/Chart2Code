import matplotlib.pyplot as plt

species_count = [90, 12, 150, 45, 25, 15]
colors = ['#ff6f69', '#ffcc5c', '#88d8b0', '#4d648d', '#8b4513', '#ffb6c1']  # New set of colors

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(species_count, colors=colors, startangle=140)

plt.show()