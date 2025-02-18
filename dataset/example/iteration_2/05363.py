import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart illustrates the popularity of different genres of books over a decade (2010-2019) in a fictional city library. 
# Additionally, it includes a subplot showing the cumulative year-wise donation of books during the same period.

# Define the years of the study
years = np.arange(2010, 2020)

# Define the genres
genres = ['Fiction', 'Non-Fiction', 'Science', 'History', 'Fantasy']

# Constructing book popularity data over the years
fiction = [30, 35, 40, 45, 50, 55, 65, 70, 75, 80]
non_fiction = [20, 25, 22, 30, 35, 38, 40, 42, 45, 48]
science = [10, 12, 15, 17, 20, 22, 25, 28, 30, 32]
history = [15, 18, 20, 22, 25, 26, 28, 30, 32, 35]
fantasy = [25, 28, 29, 32, 35, 38, 40, 42, 45, 50]

# Cumulative book donation data over the years
cumulative_donations = [100, 200, 350, 500, 700, 900, 1150, 1400, 1700, 2000]

# Prepare data for bar plotting
bar_width = 0.15
index = np.arange(len(years))

plt.figure(figsize=(14, 8))

# Main bar chart for genres popularity
plt.subplot(2, 1, 1)
plt.bar(index - 2*bar_width, fiction, bar_width, label='Fiction')
plt.bar(index - bar_width, non_fiction, bar_width, label='Non-Fiction')
plt.bar(index, science, bar_width, label='Science')
plt.bar(index + bar_width, history, bar_width, label='History')
plt.bar(index + 2*bar_width, fantasy, bar_width, label='Fantasy')

plt.title('Library Book Popularity Over a Decade', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Books Borrowed', fontsize=12)
plt.xticks(index, years, rotation=45)
plt.legend(title='Genres', loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Subplot: Cumulative donations line graph
plt.subplot(2, 1, 2)
plt.plot(years, cumulative_donations, marker='o', color='b', linewidth=2, alpha=0.8)
plt.fill_between(years, cumulative_donations, color='blue', alpha=0.1)

plt.title('Cumulative Book Donations (2010-2019)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Donations', fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(visible=True, linestyle='--', alpha=0.7)

# Optimize the layout
plt.tight_layout()

# Display the chart
plt.show()