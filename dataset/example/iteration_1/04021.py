import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart showcases the annual tech involvement of individuals in various age groups, 
# displaying the increasing trend in tech usage by each age category over a decade.

# Data definition for each age group
years = np.arange(2010, 2021)
age_18_24 = np.array([20, 30, 45, 60, 70, 85, 90, 95, 100, 110, 120])
age_25_34 = np.array([30, 40, 55, 70, 80, 95, 110, 130, 150, 170, 190])
age_35_44 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
age_45_54 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
age_55_plus = np.array([1, 2, 3, 5, 7, 9, 12, 15, 18, 22, 25])

# Creating the area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area chart to show tech involvement
ax.stackplot(years, age_18_24, age_25_34, age_35_44, age_45_54, age_55_plus,
             labels=['18-24', '25-34', '35-44', '45-54', '55+'],
             colors=['#FFD700', '#ADFF2F', '#1E90FF', '#FF69B4', '#DAA520'], alpha=0.8)

# Adding titles and labels
ax.set_title("Annual Tech Involvement Across Various Age Groups (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Tech-Involved Individuals (Thousands)", fontsize=12)

# Configuring the legend
ax.legend(loc='upper left', title='Age Groups', fontsize=10, frameon=False)

# Enhancing grid readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adjusting the x-axis to prevent labels from overlapping
plt.xticks(rotation=45)

# Ensuring a tight layout to avoid clipping
plt.tight_layout()

# Displaying the plot
plt.show()