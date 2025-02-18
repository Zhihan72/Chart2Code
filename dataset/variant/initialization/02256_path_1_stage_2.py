import matplotlib.pyplot as plt
import numpy as np

# Updated sectors list with new additions
sectors = ['AI - Software', 'AI - Hardware', 'Cyber - Network', 'Cyber - Application', 
           'Fintech - Payments', 'Fintech - InsureTech', 'EdTech - K-12', 'EdTech - Higher Education',
           'HealthTech - Devices', 'HealthTech - Software', 'Web3 - Blockchain', 'Web3 - NFTs']

# Synthetic growth data for each sector
ai_software_growth = [22, 24, 23, 25, 27, 30, 28, 25, 27, 26, 29, 31,
                      28, 32, 29, 30, 31, 33, 30, 31, 35, 29, 34, 37, 36, 35, 33, 32, 36, 37, 38, 39]
ai_hardware_growth = [18, 19, 22, 20, 21, 25, 24, 22, 23, 24, 20, 26,
                      27, 29, 22, 28, 30, 26, 28, 25, 27, 29, 31, 30, 32, 29, 31, 28, 30, 33, 29, 27]

cyber_network_growth = [10, 12, 11, 15, 18, 17, 16, 20, 22, 25, 27, 28,
                        26, 23, 22, 24, 26, 25, 23, 21, 25, 28, 29, 30, 31, 29, 32, 30, 31, 28, 26, 27]
cyber_app_growth = [9, 11, 13, 14, 16, 20, 17, 18, 20, 21, 24, 26,
                    27, 28, 29, 30, 28, 27, 26, 29, 32, 31, 33, 30, 29, 31, 32, 33, 30, 28, 29, 27]

fintech_payments_growth = [36, 34, 32, 40, 45, 43, 47, 44, 48, 45, 46, 49,
                           42, 44, 46, 48, 50, 47, 45, 49, 51, 53, 50, 48, 52, 55, 57, 54, 56, 52, 49, 48]
fintech_insuretech_growth = [38, 39, 35, 32, 34, 37, 40, 42, 45, 48, 44, 43,
                             46, 45, 47, 50, 53, 55, 52, 54, 56, 53, 57, 56, 55, 51, 50, 48, 47, 46, 48, 50]

edtech_k12_growth = [8, 10, 12, 15, 18, 16, 13, 17, 19, 22, 20, 21,
                     23, 25, 24, 26, 28, 30, 27, 25, 29, 31, 34, 32, 28, 30, 29, 33, 31, 35, 33, 32]
edtech_higher_growth = [7, 11, 14, 16, 19, 21, 23, 18, 20, 24, 27, 25,
                        22, 28, 29, 30, 32, 34, 33, 35, 37, 36, 31, 33, 38, 39, 34, 31, 30, 29, 32, 35]

healthtech_devices_growth = [25, 26, 24, 28, 29, 30, 27, 31, 34, 32, 30, 33,
                             36, 37, 35, 34, 38, 40, 39, 37, 35, 36, 31, 33, 32, 37, 39, 38, 36, 34, 32, 33]
healthtech_software_growth = [27, 29, 30, 28, 31, 32, 33, 35, 37, 36, 35, 38,
                              39, 37, 36, 35, 34, 33, 32, 31, 30, 29, 34, 32, 35, 37, 38, 39, 36, 35, 33, 31]

# New made-up data series
web3_blockchain_growth = [15, 17, 19, 21, 24, 23, 26, 29, 33, 32, 31, 30,
                          29, 34, 32, 35, 37, 36, 39, 38, 40, 42, 45, 43, 44, 46, 41, 39, 38, 37, 42, 40]
web3_nfts_growth = [10, 13, 14, 17, 19, 18, 20, 22, 26, 25, 24, 23,
                    28, 27, 29, 32, 31, 30, 28, 27, 30, 33, 34, 36, 38, 37, 35, 33, 32, 31, 34, 36]

# Compile all data for plotting
growth_data = [
    ai_software_growth, ai_hardware_growth,
    cyber_network_growth, cyber_app_growth,
    fintech_payments_growth, fintech_insuretech_growth,
    edtech_k12_growth, edtech_higher_growth,
    healthtech_devices_growth, healthtech_software_growth,
    web3_blockchain_growth, web3_nfts_growth
]

fig, ax = plt.subplots(figsize=(14, 10))

# Plot adjustments to accommodate new data
bp = ax.boxplot(growth_data, vert=True, notch=True, patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='blue'),
                whiskerprops=dict(color='blue'),
                capprops=dict(color='blue'),
                medianprops=dict(color='red', linewidth=2),
                flierprops=dict(marker='o', color='blue', markersize=8, alpha=0.5))

parts = ax.violinplot(growth_data, showmeans=False, showmedians=False, widths=0.7)
for pc in parts['bodies']:
    pc.set_facecolor('lightgrey')
    pc.set_edgecolor('black')
    pc.set_alpha(0.4)

means = [np.mean(data) for data in growth_data]
ax.scatter(range(1, len(means) + 1), means, color='green', zorder=3)

ax.yaxis.grid(True, linestyle='--', which='major', color='lightgrey', alpha=0.7)

# Update x-ticks to accommodate new groups
ax.set_xticks(range(1, len(sectors) + 1))
ax.set_xticklabels(sectors, rotation=45, ha='right')

plt.tight_layout()
plt.show()