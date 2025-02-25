import matplotlib.pyplot as plt
import numpy as np

# Define the years and disciplines
years = np.arange(2015, 2026)
disciplines = ['CS', 'Biz', 'Sci', 'Art', 'Hum']

# Enrollment data (in thousands)
cs_enrollments = [50, 70, 90, 130, 160, 200, 250, 310, 380, 460, 550]
business_enrollments = [40, 55, 75, 95, 120, 150, 190, 230, 280, 340, 400]
science_enrollments = [30, 40, 55, 70, 85, 105, 130, 160, 200, 240, 290]
arts_enrollments = [20, 25, 35, 50, 60, 80, 95, 115, 140, 170, 200]
humanities_enrollments = [10, 15, 20, 27, 33, 40, 50, 60, 75, 90, 110]

# Stack the data for plotting the area chart
enrollment_data = np.vstack([cs_enrollments, business_enrollments, science_enrollments, arts_enrollments, humanities_enrollments])

# Calculate total enrollments
total_enrollments = np.sum(enrollment_data, axis=0)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart
ax.stackplot(years, enrollment_data, labels=disciplines, colors=['#4169E1', '#FF6347', '#3CB371', '#FFD700', '#8A2BE2'], alpha=0.7)

# Overlay line plot for the total enrollments
ax.plot(years, total_enrollments, label='Total Enroll', color='black', linewidth=2.5, marker='o')

# Set titles and labels
ax.set_title('Online Edu Growth (2015-25)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Enrollments (k)', fontsize=12)

# Adding legend
ax.legend(loc='upper left', title='Subjects', fontsize=10)

# Enhance readability
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 901, 100))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()