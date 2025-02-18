import matplotlib.pyplot as plt
import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

steps_friend_1 = [4000, 4200, 3780, 5000, 5300, 6000, 6200]
steps_friend_2 = [3500, 3650, 3200, 4100, 4300, 4600, 4900]
steps_friend_3 = [4500, 4700, 4900, 5300, 5500, 5800, 6000]
steps_friend_4 = [3000, 3100, 2900, 3500, 3800, 4000, 4100]
steps_friend_5 = [5000, 5200, 5100, 4900, 4800, 5500, 5700]
steps_friend_6 = [2000, 2300, 2100, 2600, 2800, 3000, 3100]

steps_data = np.array([steps_friend_1, steps_friend_2, steps_friend_3, steps_friend_4, steps_friend_5, steps_friend_6])

fig, ax = plt.subplots(figsize=(12, 8))

new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#FFC300', '#581845']

for i, steps in enumerate(steps_data):
    ax.plot(days, steps, marker='o', linestyle='-', color=new_colors[i], label=f'F{i + 1}')

ax.set_title("Weekly Steps", fontsize=16, fontweight='bold')
ax.set_xlabel("Days", fontsize=14)
ax.set_ylabel("Steps", fontsize=14)

ax.legend(title="Friends", loc='upper left', fontsize=12, title_fontsize='13')

ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xticks(days)
ax.set_yticks(range(0, 7000, 500))
plt.xticks(rotation=45)
plt.tight_layout()

annotations = [
    ("F1 and F3 most active Sat.", 5.5, 6000),
    ("F4 increased activity.", 6, 4100),
    ("F5 consistent.", 3, 5100)
]
for text, x, y in annotations:
    ax.annotate(text, (x, y), xytext=(15, 25), textcoords='offset points',
                arrowprops=dict(arrowstyle="->", color='black'), fontsize=12, bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="wheat"))

plt.show()