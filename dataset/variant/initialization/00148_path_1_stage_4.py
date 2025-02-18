import matplotlib.pyplot as plt
import numpy as np

sectors = ['Res', 'Agri', 'Indus', 'Rec', 'Com']
water_usage = np.array([120, 80, 50, 30, 70])
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']  # Different colors

fig, ax = plt.subplots(figsize=(9, 9))

wedges, texts, autotexts = ax.pie(
    water_usage,
    labels=sectors,
    autopct='%1.1f%%',
    colors=colors,  # Multi-colored wedges
    startangle=45  # Changed start angle for a different orientation
)

plt.setp(autotexts, size=10, color='black', weight='light')  # Changed text properties

ax.set_title("Water Use in AquaRidge", fontsize=14, fontweight='light', loc='right')  # Changed title alignment

# Removed set_axis call for equal aspect ratio, altering plot shape
ax.legend(wedges, sectors, title="Sector", loc="upper right", fontsize=8)  # Changed location and fontsize

# Added gridlines for emphasis
ax.grid(linewidth=0.5, linestyle='--', color='gray')

plt.show()