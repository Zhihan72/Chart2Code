import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2021)
sector_names = ['AI & Machine Learning', 'Cybersecurity', 'Blockchain', 'Cloud Computing']

# Revenue data to be split into positive/negative growth
ai_revenue = [6, 9, -15, 18, -9, 40]
cybersecurity_revenue = [15, -18, 20, -23, 25, 12]
blockchain_revenue = [1, -2, 3, -30, 30, -12]
cloud_revenue = [5, -8, 15, -22, 12, 50]

# Create figure and axis objects
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting diverging bar chart for each sector
ax.bar(years, ai_revenue, label=sector_names[0], color='#FF9999', align='center')
ax.bar(years, cybersecurity_revenue, bottom=ai_revenue, label=sector_names[1], color='#66B2FF', align='center')
new_bars = np.add(ai_revenue, cybersecurity_revenue).tolist()
ax.bar(years, blockchain_revenue, bottom=new_bars, label=sector_names[2], color='#99FF99', align='center')
new_bars = np.add(new_bars, blockchain_revenue).tolist()
ax.bar(years, cloud_revenue, bottom=new_bars, label=sector_names[3], color='#FFCC99', align='center')

# Add axis labeling and title
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Net Change in Revenue (billion USD)', fontsize=12, fontweight='bold')
ax.set_title('Diverging Revenue Change in Technology Sectors: 2015-2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(years)
ax.axhline(0, color='black', linewidth=0.8)  # Add central axis line
ax.legend(loc='upper left', fontsize=10)

# Add text annotation as needed (for clarity, only demonstrate one sector)
for bar in ai_revenue:
    height = bar
    ax.text(years[np.where(np.array(ai_revenue) == bar)[0][0]], height + np.sign(height)*2,
            f'{bar}', ha='center', va='bottom' if height > 0 else 'top', fontsize=9)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()