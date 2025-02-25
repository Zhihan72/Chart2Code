import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

bills = np.array([
    [60, 65, 70, 55, 80, 85, 75, 50, 105, 100, 90, 95], 
    [31, 22, 25, 40, 33, 24, 28, 38, 35, 36, 30, 20], 
    [36, 38, 40, 25, 33, 30, 26, 39, 35, 32, 31, 27]
]) - np.array([
    [100, 130, 125, 90, 85, 125, 110, 95, 135, 80, 115, 120], 
    [45, 50, 32, 37, 43, 41, 48, 30, 34, 35, 47, 39], 
    [40, 47, 54, 38, 50, 44, 49, 52, 35, 42, 45, 36]
])

x = np.arange(len(months))
bar_width = 0.25
colors = ['#FF5733', '#33FFBD', '#3380FF']
fig, ax = plt.subplots(figsize=(12, 8))

for idx in range(bills.shape[0]):
    positive_idxs = bills[idx] > 0
    negative_idxs = ~positive_idxs
    
    ax.bar(x[positive_idxs] + idx*bar_width, bills[idx, positive_idxs], width=bar_width, color=colors[idx], label=f'Set {idx+1} +')
    ax.bar(x[negative_idxs] + idx*bar_width, bills[idx, negative_idxs], width=bar_width, color=colors[idx], label=f'Set {idx+1} -')

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_title("Diverging Utility Bills", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Mon", fontsize=12)
ax.set_ylabel("Bill Difference", fontsize=12)
ax.set_xticks(x + bar_width)
ax.set_xticklabels(months)

plt.legend()
plt.tight_layout()
plt.show()