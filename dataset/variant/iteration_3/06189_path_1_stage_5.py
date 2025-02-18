import matplotlib.pyplot as plt
import numpy as np

temperature = np.array([15, 18, 20, 25, 28, 30, 32, 35, 37, 40])
crop_yield = np.array([4.5, 4.7, 5.0, 5.5, 6.2, 6.0, 5.8, 5.3, 4.8, 4.0])
crop_yield_normalized = (crop_yield - crop_yield.min()) / (crop_yield.ptp() / 100)

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(y=temperature, width=crop_yield_normalized, color='skyblue', edgecolor='blue', alpha=0.8)

ax.set_title("Temperature Effect on Yield", fontsize=14, fontweight='normal', style='italic')
ax.set_xlabel("Normalized Yield (scale)", fontsize=10, style='italic')
ax.set_ylabel("Temperature in Celsius", fontsize=10, style='italic')

ax.grid(visible=True, linestyle='-', color='grey', alpha=0.8, linewidth=1)
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linewidth(0.5)

# Update annotations
for temp, yield_val in zip(temperature, crop_yield_normalized):
    ax.text(yield_val, temp, f"{yield_val:.1f}", fontsize=8, va='center', color='darkgreen')

plt.tight_layout()
plt.show()