import matplotlib.pyplot as plt

bodies = ['Saturn', 'Jupiter', 'Mercury', 'Venus', 'Mars', 'Moon']
counts = [12, 15, 8, 40, 55, 65]
new_colors = ['#3498db', '#2ecc71', '#f1c40f', '#9b59b6', '#34495e', '#16a085']

fig, ax = plt.subplots(figsize=(12, 7))
bars = ax.bar(bodies, counts, color=new_colors, width=0.6)

for bar, count in zip(bars, counts):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, str(count), ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_xticks(range(len(bodies)))
ax.set_xticklabels(bodies, rotation=45, ha='right')

plt.tight_layout()
plt.show()