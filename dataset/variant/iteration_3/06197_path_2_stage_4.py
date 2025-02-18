import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

plastic_recycling = np.array([8.5, 8.7, 9.1, 9.5, 9.7, 10.0, 9.8, 9.9, 10.3, 10.5, 10.7, 11.0])
glass_recycling = np.array([5.0, 5.1, 5.2, 5.4, 5.6, 5.7, 5.8, 5.9, 6.0, 6.2, 6.3, 6.5])
paper_recycling = np.array([12.0, 12.3, 12.5, 13.0, 13.2, 13.5, 13.6, 13.8, 14.0, 14.3, 14.5, 14.8])

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(18, 8))
x_indexes = np.arange(len(months))

ax[0].barh(x_indexes, paper_recycling, color='#FFD700')
ax[0].barh(x_indexes, -plastic_recycling, color='#FF5733')
ax[0].barh(x_indexes, -glass_recycling, color='#33FF57', left=-plastic_recycling)

ax[0].set_yticks(x_indexes)

total_recycling = plastic_recycling + glass_recycling + paper_recycling
plastic_percentage = (plastic_recycling / total_recycling) * 100
glass_percentage = (glass_recycling / total_recycling) * 100
paper_percentage = (paper_recycling / total_recycling) * 100

ax[1].barh(x_indexes, paper_percentage, color='#FFD700')
ax[1].barh(x_indexes, -plastic_percentage, color='#FF5733')
ax[1].barh(x_indexes, -glass_percentage, color='#33FF57', left=-plastic_percentage)

ax[1].set_yticks(x_indexes)

plt.tight_layout()
plt.show()