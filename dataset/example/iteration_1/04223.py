import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart visualizes the annual contribution of different book genres to a public library's check-out rates
# in the year 2022, with an emphasis on the fluctuating popularity ranking each quarter.

# Data for the chart
genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Science Fiction', 'Biographies', 'Children']
quarterly_checkouts = [
    [120, 80, 95, 130],   # Fiction
    [100, 110, 105, 90],  # Non-Fiction
    [60, 70, 75, 65],     # Mystery
    [50, 65, 60, 70],     # Science Fiction
    [40, 45, 40, 55],     # Biographies
    [30, 35, 40, 60]      # Children
]

# Average yearly checkouts for each genre
yearly_checkouts = [np.mean(q) for q in quarterly_checkouts]

# Colors for the bars
colors = plt.cm.nipy_spectral(np.linspace(0, 1, len(genres)))

# Create a figure and axis for the bar chart
fig, ax1 = plt.subplots(figsize=(12, 8))

# Create the bar chart
bars = ax1.bar(genres, yearly_checkouts, color=colors, edgecolor='black', alpha=0.7)

# Annotate bars with the average yearly check-outs
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height:.0f}', xy=(bar.get_x() + bar.get_width() / 2, height), 
                 xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=10, color='black')

# Set limits and labels
ax1.set_ylim(0, max(yearly_checkouts) + 20)
ax1.set_title('Annual Contribution of Book Genres to Library Check-Out Rates\n(Year 2022)', fontsize=14, pad=15)
ax1.set_xlabel('Book Genres', fontsize=12)
ax1.set_ylabel('Average Yearly Check-Outs', fontsize=12)

# Add gridlines for better readability
ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

# Create a subplot to show the quarterly breakdown using line plots
ax2 = ax1.twinx()

# Plot quarterly data for each genre
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
for index, (genre, quarterly_data) in enumerate(zip(genres, quarterly_checkouts)):
    ax2.plot(quarters, quarterly_data, 'o-', color=colors[index], label=genre, linewidth=2)

# Configure labels and legend for the line plot
ax2.set_ylabel('Quarterly Check-Outs', fontsize=12)
ax2.legend(loc='upper right', fontsize=10, title='Genres')

# Enhance visual consistency
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_color('grey')
ax2.tick_params(axis='y', colors='grey')

# Automatically adjust the layout to prevent overlaps
plt.tight_layout()

# Show the plot
plt.show()