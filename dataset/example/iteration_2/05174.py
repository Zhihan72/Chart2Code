import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(1970, 2021, 10)

# Participation percentages (in %)
# Data for Baby Boomers
recycling_boomers = [10, 30, 45, 50, 55, 60]
volunteering_boomers = [10, 15, 25, 30, 40, 50]
fitness_boomers = [20, 30, 35, 40, 50, 55]

# Data for Generation X
recycling_genx = [5, 15, 25, 35, 45, 55]
volunteering_genx = [5, 10, 20, 25, 35, 40]
fitness_genx = [10, 25, 30, 35, 45, 50]

# Data for Millennials
recycling_millennials = [0, 5, 10, 20, 30, 45]
volunteering_millennials = [0, 5, 10, 15, 25, 35]
fitness_millennials = [5, 10, 20, 30, 40, 50]

fig, axs = plt.subplots(2, 2, figsize=(14, 12), constrained_layout=True)

# Line plots for each generation
axs[0, 0].plot(years, recycling_boomers, label='Recycling', marker='o')
axs[0, 0].plot(years, volunteering_boomers, label='Volunteering', marker='o')
axs[0, 0].plot(years, fitness_boomers, label='Fitness Activities', marker='o')
axs[0, 0].set_title('Baby Boomers (1946 - 1964)')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Participation (%)')
axs[0, 0].legend()
axs[0, 0].grid(True)

axs[0, 1].plot(years, recycling_genx, label='Recycling', marker='o')
axs[0, 1].plot(years, volunteering_genx, label='Volunteering', marker='o')
axs[0, 1].plot(years, fitness_genx, label='Fitness Activities', marker='o')
axs[0, 1].set_title('Generation X (1965 - 1980)')
axs[0, 1].set_xlabel('Year')
axs[0, 1].set_ylabel('Participation (%)')
axs[0, 1].legend()
axs[0, 1].grid(True)

axs[1, 0].plot(years, recycling_millennials, label='Recycling', marker='o')
axs[1, 0].plot(years, volunteering_millennials, label='Volunteering', marker='o')
axs[1, 0].plot(years, fitness_millennials, label='Fitness Activities', marker='o')
axs[1, 0].set_title('Millennials (1981 - 1996)')
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Participation (%)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Summary plot
axs[1, 1].plot(years, np.array(recycling_boomers) + np.array(recycling_genx) + np.array(recycling_millennials), 
               label='Total Recycling', marker='o')
axs[1, 1].plot(years, np.array(volunteering_boomers) + np.array(volunteering_genx) + np.array(volunteering_millennials), 
               label='Total Volunteering', marker='o')
axs[1, 1].plot(years, np.array(fitness_boomers) + np.array(fitness_genx) + np.array(fitness_millennials), 
               label='Total Fitness Activities', marker='o')
axs[1, 1].set_title('Summary of All Generations')
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Total Participation (%)')
axs[1, 1].legend()
axs[1, 1].grid(True)

# Main title
fig.suptitle('Trends in Environmental and Social Awareness\nAcross Different Generations (1970 - 2020)', weight='bold', size=16)

# Show plot
plt.show()