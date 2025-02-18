import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1970, 2021, 10)

recycling_boomers = [10, 30, 45, 50, 55, 60]
volunteering_boomers = [10, 15, 25, 30, 40, 50]
fitness_boomers = [20, 30, 35, 40, 50, 55]

recycling_genx = [5, 15, 25, 35, 45, 55]
volunteering_genx = [5, 10, 20, 25, 35, 40]
fitness_genx = [10, 25, 30, 35, 45, 50]

fig, axs = plt.subplots(2, 2, figsize=(14, 12), constrained_layout=True)

colors = ['blue', 'green', 'red']

axs[1, 1].plot(years, recycling_boomers, marker='o', color=colors[1])
axs[1, 1].plot(years, volunteering_boomers, marker='o', color=colors[2])
axs[1, 1].plot(years, fitness_boomers, marker='o', color=colors[0])
axs[1, 1].set_title('Elderly Boomers (1946 - 1964)')
axs[1, 1].set_xlabel('Time Period')
axs[1, 1].set_ylabel('Active Rate (%)')

axs[0, 1].plot(years, recycling_genx, marker='o', color=colors[2])
axs[0, 1].plot(years, volunteering_genx, marker='o', color=colors[0])
axs[0, 1].plot(years, fitness_genx, marker='o', color=colors[1])
axs[0, 1].set_title('Decade Gen X (1965 - 1980)')
axs[0, 1].set_xlabel('Time Period')
axs[0, 1].set_ylabel('Active Rate (%)')

axs[0, 0].plot(years, np.array(recycling_boomers) + np.array(recycling_genx), marker='o', color=colors[1])
axs[0, 0].plot(years, np.array(volunteering_boomers) + np.array(volunteering_genx), marker='o', color=colors[2])
axs[0, 0].plot(years, np.array(fitness_boomers) + np.array(fitness_genx), marker='o', color=colors[0])
axs[0, 0].set_title('Collective Snapshot of Generations')
axs[0, 0].set_xlabel('Time Period')
axs[0, 0].set_ylabel('Cumulative Active Rate (%)')

fig.suptitle('Exploring Awareness through the Ages\nGenerational Activities (1970 - 2020)', weight='bold', size=16)

plt.show()