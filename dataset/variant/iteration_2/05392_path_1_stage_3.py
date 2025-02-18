import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
e_coli = np.array([15, 5, 45, 30, 50, 60, 25, 35, 20, 40, 15])
staph = np.array([55, 10, 60, 25, 40, 20, 85, 65, 75, 70, 80])
salmonella = np.array([12, 22, 18, 8, 65, 75, 38, 45, 30, 80, 55])
total_concentration = e_coli + staph + salmonella

fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Color order has been shuffled
ax1.stackplot(years, e_coli, staph, salmonella, labels=['E. coli', 'Staph', 'Salmonella'], 
              colors=['#99ff99','#66b3ff','#ff9999'], alpha=0.7)
ax2.plot(years, total_concentration, label='Total Conc.', color='black', lw=2, linestyle='--', marker='o')

ax1.set_title('Bacterial Conc. (2010-20)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Indiv. Conc. (CFU/mL)', fontsize=14, color='dimgray')
ax2.set_ylabel('Total Conc. (CFU/mL)', fontsize=14, color='dimgray')

ax1.grid(True, linestyle='--', alpha=0.5, color='gray')
ax1.legend(loc='upper left', fontsize=12, title='Strain')
ax2.legend(loc='upper right', fontsize=12, title='Total')

events = [(2012, 'Plant Opens'), (2018, 'Waste Regulation')]
for year, event in events:
    ax1.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, ymin=0.05, ymax=0.9)
    ax1.annotate(event, xy=(year, 140), xytext=(year, 150),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1),
                 fontsize=10, ha='center', bbox=dict(boxstyle="round,pad=0.3", edgecolor='none', facecolor='lightgrey', alpha=0.5))

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()