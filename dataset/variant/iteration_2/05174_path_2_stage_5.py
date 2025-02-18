import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1970, 2021, 10)

recycling_boomers = [10, 28, 47, 51, 53, 58]
volunteering_boomers = [9, 16, 24, 32, 41, 48]
fitness_boomers = [19, 32, 34, 41, 49, 56]

recycling_genx = [7, 17, 22, 33, 44, 54]
volunteering_genx = [4, 11, 19, 28, 36, 38]
fitness_genx = [11, 24, 31, 34, 46, 49]

recycling_millennials = [1, 4, 11, 19, 31, 43]
volunteering_millennials = [2, 6, 9, 17, 26, 34]
fitness_millennials = [6, 12, 19, 28, 39, 48]

colors_boomers = ['red', 'green', 'blue']
colors_genx = ['purple', 'orange', 'brown']
colors_millennials = ['cyan', 'magenta', 'olive']
colors_collective = ['yellow', 'grey', 'pink']

fig, axs = plt.subplots(2, 2, figsize=(14, 12), constrained_layout=True)

# Switch Baby Boomers plot to [1, 0]
axs[1, 0].plot(years, recycling_boomers, marker='o', color=colors_boomers[0])
axs[1, 0].plot(years, volunteering_boomers, marker='o', color=colors_boomers[1])
axs[1, 0].plot(years, fitness_boomers, marker='o', color=colors_boomers[2])
axs[1, 0].set_title('The Rise of Baby Boomers')
axs[1, 0].set_xlabel('Timeline')
axs[1, 0].set_ylabel('Percentage (%)')

# Switch Millennials plot to [0, 0]
axs[0, 0].plot(years, recycling_millennials, marker='o', color=colors_millennials[0])
axs[0, 0].plot(years, volunteering_millennials, marker='o', color=colors_millennials[1])
axs[0, 0].plot(years, fitness_millennials, marker='o', color=colors_millennials[2])
axs[0, 0].set_title('Millennials in Action')
axs[0, 0].set_xlabel('Timeline')
axs[0, 0].set_ylabel('Percentage (%)')

# Switch Gen X plot to [1, 1]
axs[1, 1].plot(years, recycling_genx, marker='o', color=colors_genx[0])
axs[1, 1].plot(years, volunteering_genx, marker='o', color=colors_genx[1])
axs[1, 1].plot(years, fitness_genx, marker='o', color=colors_genx[2])
axs[1, 1].set_title('Era of Gen X')
axs[1, 1].set_xlabel('Timeline')
axs[1, 1].set_ylabel('Percentage (%)')

# Switch Collective Effort plot to [0, 1]
axs[0, 1].plot(years, np.array(recycling_boomers) + np.array(recycling_genx) + np.array(recycling_millennials), marker='o', color=colors_collective[0])
axs[0, 1].plot(years, np.array(volunteering_boomers) + np.array(volunteering_genx) + np.array(volunteering_millennials), marker='o', color=colors_collective[1])
axs[0, 1].plot(years, np.array(fitness_boomers) + np.array(fitness_genx) + np.array(fitness_millennials), marker='o', color=colors_collective[2])
axs[0, 1].set_title('Collective Effort')
axs[0, 1].set_xlabel('Timeline')
axs[0, 1].set_ylabel('Overall Participation (%)')

fig.suptitle('Changing Lifestyles Across Generations\n(1970 - 2020)', weight='bold', size=16)

plt.show()