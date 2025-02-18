import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2030, 2041)

school_programs = np.array([500, 520, 530, 540, 560, 580, 610, 630, 660, 680, 700])
environmental_projects = np.array([300, 310, 320, 330, 350, 370, 390, 420, 450, 470, 490])
# neighborhood_watch removed
healthcare_support = np.array([100, 110, 120, 130, 150, 170, 180, 200, 220, 240, 260])
food_drives = np.array([150, 160, 170, 180, 190, 200, 210, 230, 250, 270, 290])

plt.figure(figsize=(14, 8))
plt.stackplot(years, school_programs, environmental_projects, healthcare_support, food_drives,
              labels=['School Events', 'Green Projects', 'Medical Aid', 'Food Campaigns'],
              colors=['#FFD700', '#228B22', '#4682B4', '#FFA500'], alpha=0.8)

plt.title('Volunteer Time Development across Different Sectors (2030-2040)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Hours Dedicated', fontsize=14)

plt.legend(loc='upper left', title='Sectors', bbox_to_anchor=(1, 1), fontsize=10)

plt.grid(alpha=0.3, linestyle='--')
plt.xticks(rotation=45)
plt.tight_layout()

milestones = {
    2032: 'Key School Partnership',
    2035: 'Green Initiative Surge',
    2037: 'Health Surge',
    2040: 'Big Food Drive'
}

for year, text in milestones.items():
    hour_total = sum([school_programs[year-2030], environmental_projects[year-2030], healthcare_support[year-2030], food_drives[year-2030]])
    plt.annotate(text, xy=(year, hour_total*0.8), xytext=(year, hour_total + 100),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='center', color='black', backgroundcolor='white')

plt.show()