import matplotlib.pyplot as plt

departments = ['Phys', 'Bio', 'Chem', 'CS', 'Math']
funding_data = {
    'Phys': [500, 520, 480, 550, 570, 600, 620, 610, 640, 630, 650],
    'Bio': [300, 320, 310, 330, 340, 360, 380, 390, 400, 410, 420],
    'Chem': [400, 410, 415, 420, 430, 440, 450, 460, 470, 480, 490],
    'CS': [600, 610, 620, 630, 640, 660, 670, 680, 690, 700, 710],
    'Math': [200, 210, 205, 220, 225, 230, 240, 250, 255, 260, 270],
}

funding_list = [funding_data[dept] for dept in departments]

fig, ax = plt.subplots(figsize=(12, 8))

box = ax.boxplot(funding_list, vert=False, patch_artist=True, labels=departments, notch=True)

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.setp(box['medians'], color='black')

ax.set_title('Yearly Funding Distribution (2015-2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Funding ($1000s)', fontsize=12)
ax.set_ylabel('Dept', fontsize=12)

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.set_facecolor('#f9f9f9')

plt.tight_layout()
plt.show()