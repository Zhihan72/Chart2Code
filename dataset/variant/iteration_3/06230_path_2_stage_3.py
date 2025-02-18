import matplotlib.pyplot as plt

preferences = [300, 200, 150, 100, 150, 100]
colors = ['#FF9999', '#FFD700', '#FF69B4', '#FFDAB9', '#FFA500', '#9ACD32']

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(preferences, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10, 'color': 'purple'})

plt.tight_layout()
plt.show()