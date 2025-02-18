import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1970, 2021, 10)

recycling_boomers = [10, 30, 45, 50, 55, 60]
volunteering_boomers = [10, 15, 25, 30, 40, 50]
fitness_boomers = [20, 30, 35, 40, 50, 55]

recycling_genx = [5, 15, 25, 35, 45, 55]
volunteering_genx = [5, 10, 20, 25, 35, 40]
fitness_genx = [10, 25, 30, 35, 45, 50]

recycling_millennials = [0, 5, 10, 20, 30, 45]
volunteering_millennials = [0, 5, 10, 15, 25, 35]
fitness_millennials = [5, 10, 20, 30, 40, 50]

fig, axs = plt.subplots(2, 2, figsize=(14, 12), constrained_layout=True)

axs[0, 0].plot(years, recycling_boomers, marker='o')
axs[0, 0].plot(years, volunteering_boomers, marker='o')
axs[0, 0].plot(years, fitness_boomers, marker='o')
axs[0, 0].set_title('Baby Boomers (1946 - 1964)')
axs[0, 0].set_xlabel('Year')
axs[0, 0].set_ylabel('Participation (%)')

axs[0, 1].plot(years, recycling_genx, marker='o')
axs[0, 1].plot(years, volunteering_genx, marker='o')
axs[0, 1].plot(years, fitness_genx, marker='o')
axs[0, 1].set_title('Generation X (1965 - 1980)')
axs[0, 1].set_xlabel('Year')
axs[0, 1].set_ylabel('Participation (%)')

axs[1, 0].plot(years, recycling_millennials, marker='o')
axs[1, 0].plot(years, volunteering_millennials, marker='o')
axs[1, 0].plot(years, fitness_millennials, marker='o')
axs[1, 0].set_title('Millennials (1981 - 1996)')
axs[1, 0].set_xlabel('Year')
axs[1, 0].set_ylabel('Participation (%)')

axs[1, 1].plot(years, np.array(recycling_boomers) + np.array(recycling_genx) + np.array(recycling_millennials), 
               marker='o')
axs[1, 1].plot(years, np.array(volunteering_boomers) + np.array(volunteering_genx) + np.array(volunteering_millennials), 
               marker='o')
axs[1, 1].plot(years, np.array(fitness_boomers) + np.array(fitness_genx) + np.array(fitness_millennials), 
               marker='o')
axs[1, 1].set_title('Summary of All Generations')
axs[1, 1].set_xlabel('Year')
axs[1, 1].set_ylabel('Total Participation (%)')

fig.suptitle('Trends in Environmental and Social Awareness\nAcross Different Generations (1970 - 2020)', weight='bold', size=16)

plt.show()