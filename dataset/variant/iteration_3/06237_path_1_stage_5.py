import matplotlib.pyplot as plt

vegetables = ['Lettuce', 'Beans', 'Spinach', 'Carrots', 'Peppers', 'Tomatoes']
gardeners = [60, 55, 65, 85, 95, 120]
growth = [5, 8, 3, 10, 12, 15]
colors = ['#81C784', '#9575CD', '#4DD0E1', '#FFD54F', '#FF8A65', '#E57373']

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].barh(vegetables, gardeners, color=colors, alpha=0.8)
ax[0].tick_params(axis='y', labelsize=12)
ax[0].tick_params(axis='x', labelsize=12)

growth_colors = ['#76FF03' if g > 0 else '#F44336' for g in growth]
ax[1].barh(vegetables, growth, color=growth_colors, alpha=0.8)
ax[1].tick_params(axis='y', labelsize=12)
ax[1].tick_params(axis='x', labelsize=12)

for i, v in enumerate(growth):
    ax[1].text(v + (1 if v > 0 else -1), i, f"{v}", va='center', ha='left' if v > 0 else 'right', fontsize=12, color='black')

plt.tight_layout()
plt.show()