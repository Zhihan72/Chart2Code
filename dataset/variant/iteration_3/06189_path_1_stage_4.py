import matplotlib.pyplot as plt
import numpy as np

temperature = np.array([15, 18, 20, 25, 28, 30, 32, 35, 37, 40])
# humidity removed
crop_yield = np.array([4.5, 4.7, 5.0, 5.5, 6.2, 6.0, 5.8, 5.3, 4.8, 4.0])

# Normalize crop yield for bubble size
crop_yield_normalized = (crop_yield - crop_yield.min()) / (crop_yield.ptp() / 100)

# Manually shuffled crop yield for colors
shuffled_yield = np.array([5.0, 6.2, 4.7, 5.3, 4.0, 4.8, 6.0, 4.5, 5.8, 5.5])

fig, ax = plt.subplots(figsize=(12, 8))

# Plot only temperature vs shuffled_yield using crop yield for bubble size
scatter = ax.scatter(temperature, np.arange(len(temperature)), s=crop_yield_normalized*100, c=shuffled_yield, cmap='plasma', alpha=0.8, edgecolor='blue', marker='D')

ax.set_title("Temperature Effect on Yield", fontsize=14, fontweight='normal', style='italic')
ax.set_xlabel("Temperature in Celsius", fontsize=10, style='italic')
ax.set_ylabel("Index", fontsize=10, style='italic') # Changed to Index as humidity is removed

ax.grid(visible=True, linestyle='-', color='grey', alpha=0.8, linewidth=1)
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linewidth(0.5)

cbar = plt.colorbar(scatter)
cbar.set_label('Yield (tons/ha)', fontsize=10, style='italic')

# Update annotations
for temp, yield_val in zip(temperature, shuffled_yield):
    ax.text(temp, temperature.tolist().index(temp), f"{yield_val:.1f}", fontsize=8, ha='left', color='darkgreen')

plt.tight_layout()
plt.show()