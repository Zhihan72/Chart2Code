import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2041)

school_programs = np.array([500, 520, 530, 540, 560, 580, 610, 630, 660, 680, 700])
environmental_projects = np.array([300, 310, 320, 330, 350, 370, 390, 420, 450, 470, 490])
healthcare_support = np.array([100, 110, 120, 130, 150, 170, 180, 200, 220, 240, 260])
food_drives = np.array([150, 160, 170, 180, 190, 200, 210, 230, 250, 270, 290])

# Consistent single color for all data groups
single_color = '#4682B4'  

plt.figure(figsize=(14, 8))
plt.stackplot(years, school_programs, environmental_projects, healthcare_support, food_drives,
              labels=['School', 'Environment', 'Healthcare', 'Food'],
              colors=[single_color, single_color, single_color, single_color], alpha=0.75)

plt.title('Volunteer Hours (2030-2040)', fontsize=16, fontweight='bold', pad=25)
plt.xlabel('Yr', fontsize=12, fontstyle='italic')
plt.ylabel('Hours', fontsize=12, fontstyle='italic')

plt.legend(loc='lower right', title='Initiatives', fontsize=10)

plt.grid(alpha=0.5, linestyle='-.')
plt.xticks(rotation=30)
plt.tight_layout()

milestones = {
    2032: 'School Collaborate',
    2035: 'Eco Expansion',
    2037: 'Healthcare Boost',
    2040: 'Food Drive'
}

for year, text in milestones.items():
    hour_total = sum([school_programs[year-2030], environmental_projects[year-2030], healthcare_support[year-2030], food_drives[year-2030]])
    plt.annotate(text, xy=(year, hour_total*0.85), xytext=(year, hour_total + 150),
                 arrowprops=dict(facecolor='grey', arrowstyle='->'),
                 fontsize=11, ha='center', color='blue')

plt.show()