import matplotlib.pyplot as plt
import numpy as np

# Expanded data for the chart including additional genres
genres = [
    'Fiction', 'Non-Fiction', 'Mystery', 
    'Science Fiction', 'Biographies', 'Children',
    'Fantasy', 'Historical', 'Romance'
]
quarterly_checkouts = [
    [120, 80, 95, 130],   # Fiction
    [100, 110, 105, 90],  # Non-Fiction
    [60, 70, 75, 65],     # Mystery
    [50, 65, 60, 70],     # Science Fiction
    [40, 45, 40, 55],     # Biographies
    [30, 35, 40, 60],     # Children
    [90, 100, 110, 95],   # Fantasy
    [70, 80, 60, 75],     # Historical
    [95, 85, 105, 100]    # Romance
]

# Calculate average yearly checkouts for each genre
yearly_checkouts = [np.mean(q) for q in quarterly_checkouts]

# Colors for bars
colors = plt.cm.nipy_spectral(np.linspace(0, 1, len(genres)))

# Create a figure and axis for the horizontal bar chart
fig, ax1 = plt.subplots(figsize=(14, 10))

# Create the horizontal bar chart
bars = ax1.barh(genres, yearly_checkouts, color=colors, edgecolor='black', alpha=0.7)

# Annotate bars
for bar in bars:
    width = bar.get_width()
    ax1.annotate(f'{width:.0f}', xy=(width, bar.get_y() + bar.get_height() / 2), 
                 xytext=(5, 0), textcoords='offset points', ha='left', va='center', fontsize=10, color='black')

# Set limits and labels
ax1.set_xlim(0, max(yearly_checkouts) + 20)
ax1.set_title('Annual Contribution of Book Genres to Library Check-Out Rates\n(Year 2022)', fontsize=14, pad=15)
ax1.set_ylabel('Book Genres', fontsize=12)
ax1.set_xlabel('Average Yearly Check-Outs', fontsize=12)

# Add gridlines
ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()