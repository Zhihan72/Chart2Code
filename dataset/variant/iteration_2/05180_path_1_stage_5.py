import matplotlib.pyplot as plt

sales_percentage = [30, 20, 15, 10, 15]

# Colors for each segment
colors = ['#99ff99', '#ffb3e6', '#c2c2f0', '#66b3ff', '#ff9999']

explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(sales_percentage, autopct='%1.1f%%', startangle=180,
                                  colors=colors, explode=explode, textprops=dict(color="black", fontsize=12))

# Change pie chart to donut by drawing a white circle at the center with radius 0.70
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis('equal')

plt.tight_layout()
plt.show()