import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2015, 2026)

# Define the disciplines and their enrollment data (in thousands)
disciplines = ['Computer Science', 'Business', 'Science', 'Arts', 'Humanities']

# Manually altered data for each discipline over the years, while preserving the structure
cs_enrollments = [50, 68, 85, 135, 150, 195, 260, 315, 375, 455, 560]
business_enrollments = [35, 60, 78, 98, 115, 145, 185, 235, 270, 330, 390]
science_enrollments = [33, 37, 57, 68, 87, 103, 135, 155, 205, 235, 295]
arts_enrollments = [23, 30, 38, 55, 57, 85, 90, 120, 130, 175, 195]
humanities_enrollments = [12, 17, 23, 29, 31, 42, 55, 58, 78, 92, 115]

# Stack the data for plotting
enrollment_data = np.vstack([cs_enrollments, business_enrollments, science_enrollments, arts_enrollments, humanities_enrollments])

# Calculate total enrollments for the overlay line plot
total_enrollments = np.sum(enrollment_data, axis=0)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Plot the stacked area chart
ax.stackplot(years, enrollment_data, labels=disciplines, colors=['#4169E1', '#FF6347', '#3CB371', '#FFD700', '#8A2BE2'], alpha=0.7)

# Overlay line plot for the total enrollments
ax.plot(years, total_enrollments, label='Total Enrollments', color='black', linewidth=2.5, marker='o')

# Set titles and labels
ax.set_title('Tracking Increases in Online Education Enrollment (2015-2025)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Enrollments (in thousands)', fontsize=12)

# Adding legend
ax.legend(loc='upper left', title='Disciplines', fontsize=10)

# Enhance readability
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 901, 100))

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()