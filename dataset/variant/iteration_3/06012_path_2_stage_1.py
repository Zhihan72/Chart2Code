import numpy as np
import matplotlib.pyplot as plt

# Data Preparation:
brightness = np.array([5.1, 5.4, 5.7, 6.0, 6.3, 6.5, 7.0, 7.5, 8.0, 4.2, 4.5, 4.8, 3.1, 3.3,
                       3.9, 2.7, 2.5, 1.0, -1.5, 0.8, -1.0, -2.4, -2.3])
temperature = np.array([3000, 3200, 3500, 3700, 4000, 4300, 5000, 5200, 6000, 7000, 8000,
                        9000, 12000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 
                        50000, 55000, 60000])

# Plotting the scatter chart
fig, ax = plt.subplots(figsize=(12, 7))

# Scatter plot with a single color
ax.scatter(temperature, brightness, color='royalblue', alpha=0.75, edgecolors='w', s=100)

# Adding titles and labels
ax.set_title('Hertzsprung-Russell Diagram: Stellar Classification by Brightness and Temperature', fontsize=16, fontweight='bold', wrap=True)
ax.set_xlabel('Surface Temperature (K)', fontsize=12)
ax.set_ylabel('Absolute Magnitude (Brightness)', fontsize=12)
ax.invert_yaxis()  # inverting y-axis for brightness

# Adding grid lines
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Ensuring no overlapping of text or elements
plt.tight_layout()

# Display the plot
plt.show()