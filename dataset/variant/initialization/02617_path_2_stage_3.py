import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_title('Agricultural Output Range', fontsize=14, weight='bold', pad=20)
ax.set_ylabel('Output (units)', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()