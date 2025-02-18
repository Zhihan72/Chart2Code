import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

campaign_A = np.array([2, 3, 5, 7, 11, 13, 15, 20, 23, 30, 35])
campaign_B = np.array([1, 2, 3, 5, 8, 12, 17, 25, 31, 38, 45])
campaign_C = np.array([0, 1, 2, 4, 7, 10, 13, 18, 22, 29, 33])
campaign_D = np.array([1, 3, 4, 6, 9, 14, 19, 27, 32, 40, 47])
campaign_E = np.array([2, 4, 4, 5, 9, 11, 16, 22, 29, 35, 39])

cumulative_A = np.cumsum(campaign_A)
cumulative_B = np.cumsum(campaign_B)
cumulative_C = np.cumsum(campaign_C)
cumulative_D = np.cumsum(campaign_D)
cumulative_E = np.cumsum(campaign_E)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

ax1.plot(years, campaign_A, marker='o', linestyle='-', color='darkorange', label='Camp A', linewidth=2)
ax1.plot(years, campaign_B, marker='s', linestyle='-', color='purple', label='Sector B', linewidth=2)
ax1.plot(years, campaign_C, marker='^', linestyle='-', color='deepskyblue', label='Initiative C', linewidth=2)
ax1.plot(years, campaign_D, marker='d', linestyle='-', color='green', label='Team D', linewidth=2)
ax1.plot(years, campaign_E, marker='*', linestyle='-', color='red', label='Drive E', linewidth=2)

ax1.set_title('Yearly Planting in EcoVille (2010-2020)\nFighting Urban Smog', fontsize=16, fontweight='bold', pad=15)
ax1.set_ylabel('Planted Trees (K)', fontsize=14)
ax1.legend(title='Groups', loc='upper left', fontsize=12, title_fontsize=13)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.plot(years, cumulative_A, marker='o', linestyle='-', color='darkorange', label='Accumulated A', linewidth=2)
ax2.plot(years, cumulative_B, marker='s', linestyle='-', color='purple', label='Total B', linewidth=2)
ax2.plot(years, cumulative_C, marker='^', linestyle='-', color='deepskyblue', label='Sum C', linewidth=2)
ax2.plot(years, cumulative_D, marker='d', linestyle='-', color='green', label='Compiled D', linewidth=2)
ax2.plot(years, cumulative_E, marker='*', linestyle='-', color='red', label='Aggregate E', linewidth=2)

ax2.set_title('Overall Tree Count by Group (2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Total Planted Trees (K)', fontsize=14)
ax2.legend(title='Total Groups', loc='upper left', fontsize=12, title_fontsize=13)
ax2.grid(True, linestyle='--', alpha=0.6)

for year, value in zip(years, cumulative_A):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='darkorange')
for year, value in zip(years, cumulative_B):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='purple')
for year, value in zip(years, cumulative_C):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='deepskyblue')
for year, value in zip(years, cumulative_D):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='green')
for year, value in zip(years, cumulative_E):
    ax2.annotate(f'{value}', xy=(year, value), xytext=(0, 10), textcoords='offset points', ha='center', fontsize=9, color='red')

plt.tight_layout()
plt.show()