import matplotlib.pyplot as plt

time_spent = [10, 15, 20, 25, 20, 10]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']
explode = (0, 0, 0.2, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    time_spent, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True,
    wedgeprops=dict(edgecolor='black', linestyle='--')
)

# Create the donut shape by adding a circle at the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.tight_layout()

plt.show()