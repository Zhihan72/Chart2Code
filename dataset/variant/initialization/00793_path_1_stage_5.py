import matplotlib.pyplot as plt

art_movements = ['Renaiss.', 'Baroque', 'Romant.', 'Impress.', 'Contemp.']
color_usage = [22, 18, 25, 15, 20]

fig, ax = plt.subplots(figsize=(10, 7))
ax.pie(color_usage, labels=art_movements, autopct='%1.1f%%', startangle=140, explode=(0.05,) * 5)

plt.setp(ax.texts, size=9, weight='bold', color='white')

ax.axis('equal')

plt.show()