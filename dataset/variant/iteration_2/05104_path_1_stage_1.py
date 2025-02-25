import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2041)

school_programs = np.array([500, 520, 530, 540, 560, 580, 610, 630, 660, 680, 700])
environmental_projects = np.array([300, 310, 320, 330, 350, 370, 390, 420, 450, 470, 490])
neighborhood_watch = np.array([200, 210, 220, 230, 240, 250, 270, 290, 310, 330, 350])
healthcare_support = np.array([100, 110, 120, 130, 150, 170, 180, 200, 220, 240, 260])
food_drives = np.array([150, 160, 170, 180, 190, 200, 210, 230, 250, 270, 290])

plt.figure(figsize=(14, 8))
plt.stackplot(years, school_programs, environmental_projects, neighborhood_watch, healthcare_support, food_drives,
              labels=['School Programs', 'Environmental Projects', 'Neighborhood Watch', 'Healthcare Support', 'Food Drives'],
              colors=['#4682B4', '#B22222', '#228B22', '#FFD700', '#FFA500'], alpha=0.75)

plt.title('Volunteer Hours by Community Initiative (2030-2040)', fontsize=16, fontweight='bold', pad=25)
plt.xlabel('Year', fontsize=12, fontstyle='italic')
plt.ylabel('Volunteer Hours', fontsize=12, fontstyle='italic')

plt.legend(loc='lower right', title='Initiatives', fontsize=10)

plt.grid(alpha=0.5, linestyle='-.')
plt.xticks(rotation=30)
plt.tight_layout()

milestones = {
    2032: 'Major School Collaboration',
    2035: 'Eco-Project Expansion',
    2037: 'Healthcare Boost',
    2040: 'Signature Food Drive Event'
}

for year, text in milestones.items():
    hour_total = sum([school_programs[year-2030], environmental_projects[year-2030], neighborhood_watch[year-2030], healthcare_support[year-2030], food_drives[year-2030]])
    plt.annotate(text, xy=(year, hour_total*0.85), xytext=(year, hour_total + 150),
                 arrowprops=dict(facecolor='grey', arrowstyle='->'),
                 fontsize=11, ha='center', color='blue')

plt.show()