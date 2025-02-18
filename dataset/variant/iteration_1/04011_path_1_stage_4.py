import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

cars_usage = [700, 720, 740, 760, 750, 740, 730, 720, 710, 700]
public_transit_usage = [300, 310, 320, 340, 350, 370, 400, 430, 450, 470]
walking_usage = [150, 160, 170, 180, 190, 200, 210, 220, 230, 250]

fig, ax = plt.subplots(figsize=(14, 8))

single_color = 'royalblue'
ax.plot(years, cars_usage, marker='o', linestyle='-', linewidth=2, color=single_color)
ax.plot(years, public_transit_usage, marker='^', linestyle='-', linewidth=2, color=single_color)
ax.plot(years, walking_usage, marker='d', linestyle='-', linewidth=2, color=single_color)

ax.set_xticks(years)
ax.set_ylim(0, 800)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()