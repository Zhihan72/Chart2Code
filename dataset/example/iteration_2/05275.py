import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart displays the data from a fictional study on the average number of books read per person per year in different regions over the first decade of the 21st century.
# The goal is to understand reading habits and their evolution in different geographical areas. Subplots will be used to compare data between regions and show growth rates.

# Define the years for the data
years = np.arange(2001, 2011)

# Manually crafted data for average books read per person per year in different regions
north_america_books = np.array([5, 5.5, 6, 6.2, 6.5, 7, 7.5, 8, 8.3, 8.7])
europe_books = np.array([4, 4.5, 5, 5.5, 5.8, 6, 6.3, 6.7, 7, 7.3])
asia_books = np.array([2, 2.5, 3, 3.5, 3.8, 4.2, 4.5, 5, 5.3, 5.8])

# Calculate growth rates (year-over-year growth percentages)
north_america_growth = np.diff(north_america_books) / north_america_books[:-1] * 100 
europe_growth = np.diff(europe_books) / europe_books[:-1] * 100
asia_growth = np.diff(asia_books) / asia_books[:-1] * 100

# Initialize the figure and the two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Plotting the bar chart for average books read
x = np.arange(len(years))  # the label locations
width = 0.25  # the width of the bars

ax1.bar(x - width, north_america_books, width, label='North America', color='skyblue')
ax1.bar(x, europe_books, width, label='Europe', color='lightgreen')
ax1.bar(x + width, asia_books, width, label='Asia', color='lightcoral')

ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Books Read per Person', fontsize=12)
ax1.set_title('Average Books Read per Person per Year by Region (2001-2010)', fontsize=14, weight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)

# Plotting the bar chart for growth rates
ax2.bar(x[1:] - width, north_america_growth, width, label='North America', color='skyblue')
ax2.bar(x[1:], europe_growth, width, label='Europe', color='lightgreen')
ax2.bar(x[1:] + width, asia_growth, width, label='Asia', color='lightcoral')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (%)', fontsize=12)
ax2.set_title('Year-over-Year Growth Rate in Books Read per Person', fontsize=14, weight='bold', pad=15)
ax2.set_xticks(x[1:])
ax2.set_xticklabels(years[1:], rotation=45)
ax2.legend(loc='upper left', fontsize=10, title='Regions', title_fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)

# Adding text annotations to highlight significant changes
ax1.annotate('Steady Growth', xy=(8, 8.7), xytext=(6, 9.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='navy', weight='bold')
ax1.annotate('Rapid Improvement', xy=(8, 5.8), xytext=(6, 6.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1), fontsize=10, color='darkred', weight='bold')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()