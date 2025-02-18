import matplotlib.pyplot as plt

creatures = ['Dragons', 'Unicorns', 'Phoenixes', 'Mermaids']
popularity = [40, 25, 20, 10]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(popularity, labels=creatures, colors=colors, startangle=90, autopct='%1.1f%%')

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()