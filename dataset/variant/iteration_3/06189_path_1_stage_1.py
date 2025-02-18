import matplotlib.pyplot as plt
import numpy as np

temperature = np.array([15, 18, 20, 25, 28, 30, 32, 35, 37, 40])
humidity = np.array([80, 75, 70, 65, 62, 60, 55, 50, 48, 45])
crop_yield = np.array([4.5, 4.7, 5.0, 5.5, 6.2, 6.0, 5.8, 5.3, 4.8, 4.0])

# Normalize crop yield for bubble size
crop_yield_normalized = (crop_yield - crop_yield.min()) / (crop_yield.ptp() / 100)

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

scatter = ax.scatter(temperature, humidity, s=crop_yield_normalized*100, c=crop_yield, cmap='plasma', alpha=0.8, edgecolor='blue', marker='D')

# Title and labels
ax.set_title("Impact of Temperature & Humidity on Crop Yield", fontsize=14, fontweight='normal', style='italic')
ax.set_xlabel("Avg Temperature (°C)", fontsize=10, style='italic')
ax.set_ylabel("Humidity (%)", fontsize=10, style='italic')

# Adjust grid and borders
ax.grid(visible=True, linestyle='-', color='grey', alpha=0.8, linewidth=1)
ax.spines['top'].set_linewidth(0.5)
ax.spines['right'].set_linewidth(0.5)

# Color bar to reflect crop yield
cbar = plt.colorbar(scatter)
cbar.set_label('Crop Yield (tons/hectare)', fontsize=10, style='italic')

# Annotate specific points
for temp, hum, yield_val in zip(temperature, humidity, crop_yield):
    ax.text(temp, hum, f"{yield_val:.1f}", fontsize=8, ha='left', color='darkred')

plt.tight_layout()
plt.show()