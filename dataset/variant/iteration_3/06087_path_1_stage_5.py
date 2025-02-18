import matplotlib.pyplot as plt

data = [1800, 1900, 1600, 1800, 2000, 1700, 1650, 1750, 1800, 1550,
        2250, 2350, 2500, 2400, 2300, 2600, 2200, 2300, 2700, 2800,
        2100, 2200, 2500, 2000, 2100, 2300, 2150, 2400, 2100, 2200,
        2000, 1900, 1800, 2100, 1850, 2200, 2000, 1950, 1750, 1900,
        1550, 1700, 1600, 1650, 2000, 1500, 1750, 1700, 1800, 1900]

fig, ax = plt.subplots(figsize=(8, 6))

ax.boxplot(
    data, 
    vert=True, 
    patch_artist=True, 
    boxprops=dict(facecolor='#87CEEB', color='#4682B4'),  # New sky blue face and steel blue border
    whiskerprops=dict(color='#4682B4'),  # Steel blue whiskers
    capprops=dict(color='#4682B4'),      # Steel blue caps
    medianprops=dict(color='#FF4500', linestyle='--')  # Orange red median line
)

ax.set_title('Single Group Caloric Intake - 2023', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Caloric Intake (kcal)', fontsize=12)
ax.set_xticks([])

ax.grid(axis='x', linestyle='-', linewidth=0.5)

plt.tight_layout()
plt.show()