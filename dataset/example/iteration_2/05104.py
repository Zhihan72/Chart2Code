import matplotlib.pyplot as plt
import numpy as np

# Years of data collection related to the topic
years = np.arange(2030, 2041)

# Artificial data for volunteer hours contributed by different community initiatives
school_programs = np.array([500, 520, 530, 540, 560, 580, 610, 630, 660, 680, 700])
environmental_projects = np.array([300, 310, 320, 330, 350, 370, 390, 420, 450, 470, 490])
neighborhood_watch = np.array([200, 210, 220, 230, 240, 250, 270, 290, 310, 330, 350])
healthcare_support = np.array([100, 110, 120, 130, 150, 170, 180, 200, 220, 240, 260])
food_drives = np.array([150, 160, 170, 180, 190, 200, 210, 230, 250, 270, 290])

# Create stacked area chart
plt.figure(figsize=(14, 8))
plt.stackplot(years, school_programs, environmental_projects, neighborhood_watch, healthcare_support, food_drives,
              labels=['School Programs', 'Environmental Projects', 'Neighborhood Watch', 'Healthcare Support', 'Food Drives'],
              colors=['#FFD700', '#228B22', '#B22222', '#4682B4', '#FFA500'], alpha=0.8)

# Title and axis labels
plt.title('Growth of Volunteer Hours by Community Initiative (2030-2040)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Volunteer Hours', fontsize=14)

# Add a legend
plt.legend(loc='upper left', title='Initiatives', bbox_to_anchor=(1, 1), fontsize=10)

# Customize the grid and layout
plt.grid(alpha=0.3, linestyle='--')
plt.xticks(rotation=45)
plt.tight_layout()

# Annotate significant milestones
milestones = {
    2032: 'Major School Collaboration',
    2035: 'Eco-Project Expansion',
    2037: 'Healthcare Boost',
    2040: 'Signature Food Drive Event'
}

for year, text in milestones.items():
    hour_total = sum([school_programs[year-2030], environmental_projects[year-2030], neighborhood_watch[year-2030], healthcare_support[year-2030], food_drives[year-2030]])
    plt.annotate(text, xy=(year, hour_total*0.8), xytext=(year, hour_total + 100),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 fontsize=9, ha='center', color='black', backgroundcolor='white')

# Show plot
plt.show()