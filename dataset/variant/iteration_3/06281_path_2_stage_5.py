import matplotlib.pyplot as plt

# Data
fruit_types = ['Blueberries', 'Mangoes', 'Strawberries', 'Peaches']
percentages = [20, 30, 25, 10]
colors = ['#4B0082', '#FFA500', '#FF6347', '#FFD700']

# Subplots in a 2x1 arrangement
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 14))

# Donut Pie Chart
explode = (0.1, 0.15, 0.2, 0.05)
wedges, texts, autotexts = ax1.pie(
    percentages, labels=None, autopct='%1.1f%%', startangle=60,
    colors=colors, explode=explode, shadow=False, textprops=dict(color="navy"),
    wedgeprops=dict(width=0.4))  # Width argument added here

plt.setp(texts, size=11, weight="normal")
plt.setp(autotexts, size=11, weight="normal")
ax1.set_title('Random Fruit Distribution', fontsize=15, fontweight='normal', pad=10)

ax1.axis('equal')
ax1.legend(wedges, fruit_types, title="Random Fruits", loc="upper right", fontsize=11)

# Horizontal Bar Chart
bars = ax2.barh(fruit_types, percentages, color=colors, edgecolor='grey', hatch="/")
ax2.set_title('Random Fruit Trends', fontsize=15, fontweight='normal', pad=10)
ax2.set_xlabel("Preference (%)", fontsize=11)
ax2.set_xlim(0, 35)
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))
ax2.xaxis.grid(True, linestyle='-', alpha=0.9)
ax2.yaxis.grid(True, linestyle=':', alpha=0.5)

# Bar labels
for bar, percentage in zip(bars, percentages):
    ax2.text(bar.get_width() - 5.5, bar.get_y() + bar.get_height() / 2, f'{percentage}%', 
             va='center', ha='left', color='white', fontsize=10, fontweight='normal')

plt.tight_layout()
plt.show()