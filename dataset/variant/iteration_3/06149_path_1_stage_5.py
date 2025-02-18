import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 8))

ax.set_ylabel('Sleep Hrs', fontsize=12)
ax.set_xticklabels(['Bball'], fontsize=11, fontweight='bold')

plt.tight_layout()
plt.show()