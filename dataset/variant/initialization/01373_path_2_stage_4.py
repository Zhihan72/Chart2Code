import matplotlib.pyplot as plt

departments = ['Phys', 'Bio', 'Chem', 'CS', 'Math', 'Eng', 'Econ']

funding_data = {
    'Physics': [500, 520, 480, 550, 570, 600, 620, 610, 640, 630, 650],
    'Biology': [300, 320, 310, 330, 340, 360, 380, 390, 400, 410, 420],
    'Chemistry': [400, 410, 415, 420, 430, 440, 450, 460, 470, 480, 490],
    'Computer Science': [600, 610, 620, 630, 640, 660, 670, 680, 690, 700, 710],
    'Mathematics': [200, 210, 205, 220, 225, 230, 240, 250, 255, 260, 270],
    'Engineering': [550, 560, 580, 590, 610, 620, 630, 660, 670, 680, 700],
    'Economics': [250, 260, 270, 280, 290, 310, 330, 340, 350, 355, 360],
}

funding_list = [funding_data[dept] for dept in funding_data.keys()]

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(funding_list, vert=True, patch_artist=True, labels=departments, notch=True)

uniform_color = '#66B3FF'
for patch in box['boxes']:
    patch.set_facecolor(uniform_color)

plt.setp(box['medians'], color='black')

ax.set_title('Research Funding by Dept (2015-2025)', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Funding ($1000s)', fontsize=12)
ax.set_xlabel('Dept', fontsize=12)

plt.tight_layout()
plt.show()