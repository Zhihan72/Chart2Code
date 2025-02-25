import matplotlib.pyplot as plt
import numpy as np

sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydro', 'Solar', 'Wind']
countries = ['USA', 'China', 'Germany', 'India', 'Brazil']

energy_data = [
    [1000, 1200, 800, 500, 300, 400],  
    [1500, 2000, 1000, 800, 600, 700],  
    [300, 450, 900, 700, 500, 600],     
    [1400, 1200, 200, 600, 400, 300],   
    [200, 300, 100, 900, 800, 700]      
]

average_production = np.mean(energy_data, axis=0)
deviation_data = energy_data - average_production

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), gridspec_kw={'height_ratios': [3, 2]})

bar_width = 0.7
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
bottoms_pos = np.zeros(len(countries))
bottoms_neg = np.zeros(len(countries))

for source_idx, (source, color) in enumerate(zip(sources, colors)):
    source_data = deviation_data[:, source_idx]
    pos_data = np.where(source_data >= 0, source_data, 0)
    neg_data = np.where(source_data < 0, source_data, 0)
    
    ax1.bar(countries, pos_data, width=bar_width, bottom=bottoms_pos, color=color)
    ax1.bar(countries, neg_data, width=bar_width, bottom=bottoms_neg, color=color)
    
    bottoms_pos += pos_data
    bottoms_neg += neg_data

ax1.set_ylabel('Deviation from Avg. Energy Production (TWh)', fontsize=12)
ax1.set_title('Diverging Energy Production by Source in Different Countries, 2023', fontsize=16, fontweight='bold', pad=20)

ax2.bar(sources, average_production, color=['#61a4b2'], width=bar_width)
ax2.set_ylabel('Avg. Global Production (TWh)', fontsize=12)
ax2.set_title('Average Global Energy Production by Source, 2023', fontsize=16, pad=20)
ax2.set_xticklabels(sources, rotation=45, ha='right')

plt.tight_layout()
plt.show()