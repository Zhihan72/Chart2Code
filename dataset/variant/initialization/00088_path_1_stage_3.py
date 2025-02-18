import matplotlib.pyplot as plt
import numpy as np

# Data for 2050
sources = ['Solar', 'Wind', 'Hydro', 'Nuclear', 'Coal', 'Gas', 'Other Ren.']
percent_2050 = [20, 25, 15, 5, 15, 10, 10]

# Sort data for 2050
sorted_idx = np.argsort(percent_2050)
sorted_sources = [sources[i] for i in sorted_idx]
sorted_percent_2050 = [percent_2050[i] for i in sorted_idx]

# Data for 2020
percent_2020 = [6, 3, 27, 5, 15, 10, 34]

# Create plots
fig, axs = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [1.5, 1]})

# Bar chart for 2050
bars = axs[0].barh(sorted_sources, sorted_percent_2050, color=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])
axs[0].xaxis.grid(True, linestyle='--', color='grey', alpha=0.5)
axs[0].bar_label(bars, fmt='%.1f%%')
axs[0].set_title('2050 Energy Mix', fontsize=16, pad=20)
axs[0].set_xlabel('% of Total', fontsize=12)
axs[0].set_xlim(0, 30)
axs[0].set_yticklabels(sorted_sources, fontsize=11)

# Pie chart for 2020
axs[1].pie(percent_2020, labels=sources, autopct='%1.1f%%',
           startangle=90, colors=['#FFD700', '#1E90FF', '#32CD32', '#FFA07A', '#A9A9A9', '#FF4500', '#9370DB'])
axs[1].set_title('2020 Energy Mix', fontsize=14, pad=20)

plt.tight_layout()
plt.show()