import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2010, 2021)

# Manually created data showing subscription numbers (in millions)
netflix_subs = np.array([20, 24, 30, 37, 45, 53, 62, 72, 82, 92, 107])
hulu_subs = np.array([7, 8, 10, 13, 16, 20, 25, 29, 31, 33, 36])
prime_subs = np.array([15, 17, 20, 24, 27, 32, 36, 42, 48, 53, 60])
disney_subs = np.array([0, 0, 0, 0, 0, 0, 0, 10, 28, 50, 73])

# Initialize figure and axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting streaming service data
ax1.plot(years, netflix_subs, marker='o', color='red', linewidth=2)
ax1.plot(years, hulu_subs, marker='s', color='green', linewidth=2)
ax1.plot(years, prime_subs, marker='^', color='blue', linewidth=2)
ax1.plot(years, disney_subs, marker='d', color='purple', linewidth=2)

# Titles and labels
ax1.set_title('Decade of Growth in Streaming Services (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of Subscribers (millions)', fontsize=14)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Display the plot
plt.show()