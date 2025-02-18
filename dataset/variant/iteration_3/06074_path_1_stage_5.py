import matplotlib.pyplot as plt
import numpy as np

branches = ['Downtown', 'Uptown', 'Suburb', 'Airport', 'University', 'Mall']
months = np.arange(1, 13)

all_consumption = [
    [240, 200, 210, 220, 230, 240, 245, 250, 240, 230, 220, 215],
    [180, 190, 200, 195, 205, 200, 205, 210, 200, 190, 185, 195],
    [150, 145, 140, 150, 155, 160, 165, 170, 165, 160, 155, 150],
    [300, 310, 320, 300, 290, 280, 285, 290, 295, 300, 310, 320],
    [100, 110, 120, 115, 125, 130, 135, 140, 130, 120, 110, 105],
    [220, 225, 230, 235, 220, 210, 215, 225, 230, 235, 240, 245]
]

fig, axes = plt.subplots(1, 2, figsize=(18, 8), constrained_layout=True)
global_mean = np.mean([np.mean(consumption) for consumption in all_consumption])

x_indices = np.arange(len(months))
for i, consumption in enumerate(all_consumption):
    deviations = np.array(consumption) - global_mean
    pos_devs = np.where(deviations > 0, deviations, 0)
    neg_devs = np.where(deviations < 0, deviations, 0)
    axes[0].bar(x_indices, pos_devs, width=0.4, align='center', label=branches[i] if i % 2 == 0 else "", hatch='/' if i % 2 == 0 else '\\')
    axes[0].bar(x_indices, neg_devs, width=0.4, align='center', hatch='/' if i % 2 == 0 else '\\')

axes[0].set_title("Diverging Monthly Coffee Consumption", fontsize=16, fontweight='bold', pad=20)
axes[0].set_xlabel("Month", fontsize=14,)
axes[0].set_ylabel("Deviation from Mean (kg)", fontsize=14,)
axes[0].legend(loc='lower left')
axes[0].grid(False)

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
x_indices_2 = np.arange(len(quarters))

for i, consumptions in enumerate(all_consumption):
    quarterly_avg = [np.mean(consumptions[i*3:i*3+3]) for i in range(4)]
    deviations = np.array(quarterly_avg) - global_mean
    pos_devs = np.where(deviations > 0, deviations, 0)
    neg_devs = np.where(deviations < 0, deviations, 0)
    axes[1].bar(x_indices_2, pos_devs, width=0.4, align='center', label=branches[i] if i % 2 == 0 else "", hatch='/' if i % 2 == 0 else '\\')
    axes[1].bar(x_indices_2, neg_devs, width=0.4, align='center', hatch='/' if i % 2 == 0 else '\\')

axes[1].set_title("Diverging Quarterly Coffee Consumption", fontsize=16, fontweight='bold', pad=20)
axes[1].set_xlabel("Quarter", fontsize=14,)
axes[1].set_ylabel("Deviation from Mean (kg)", fontsize=14,)
axes[1].legend(loc='lower left')
axes[1].grid(False)

plt.show()