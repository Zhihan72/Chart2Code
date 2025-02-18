import matplotlib.pyplot as plt

percentages = [25, 20, 18, 15, 12, 7]

fig, ax = plt.subplots(figsize=(10, 8))
explode = (0.05, 0.05, 0, 0, 0, 0)

# Use a single color for all wedges
single_color = '#66B3FF'

ax.pie(percentages, startangle=140, colors=[single_color]*len(percentages), pctdistance=0.85,
       wedgeprops=dict(width=0.3), explode=explode)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()

plt.show()