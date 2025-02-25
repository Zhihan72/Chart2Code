import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Randomly altered data for bacterial strains
e_coli = np.array([40, 25, 15, 35, 5, 50, 45, 60, 15, 30, 20])
staph = np.array([20, 75, 85, 80, 10, 40, 55, 25, 60, 70, 65])
salmonella = np.array([18, 80, 75, 12, 22, 65, 8, 45, 30, 55, 38])

total_concentration = e_coli + staph + salmonella

fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Styling elements changed
ax1.stackplot(years, e_coli, staph, salmonella, labels=['E. coli', 'Staph', 'Salmonella'], 
              colors=['#ffcccc','#99ccff','#c2f0c2'], alpha=0.6)

ax2.plot(years, total_concentration, label='Total Conc.', color='orange', lw=2, linestyle='-', marker='s')

ax1.set_title('Bacterial Concentrations (2010-2020)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Bacterial Conc. (CFU/mL)', fontsize=14, color='darkred')
ax2.set_ylabel('Total Conc. (CFU/mL)', fontsize=14, color='darkblue')

# Modified grid and legend styles
ax1.grid(True, linestyle='-.', alpha=0.8, color='black')
ax1.legend(loc='upper right', fontsize=10, title='Bacterium')
ax2.legend(loc='upper left', fontsize=10, title='Overall')

# Borders (spines) randomly altered
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_color('green')
ax1.spines['left'].set_color('purple')

events = [(2012, 'Plant Opened'), (2018, 'Regulation Applied')]
for year, event in events:
    ax1.axvline(x=year, color='blue', linestyle='-.', linewidth=2, ymin=0.05, ymax=0.9)
    ax1.annotate(event, xy=(year, 140), xytext=(year, 150),
                 arrowprops=dict(facecolor='red', shrink=0.1, width=1.5),
                 fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightblue', alpha=0.7))

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()