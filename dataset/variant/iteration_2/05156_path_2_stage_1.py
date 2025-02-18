import matplotlib.pyplot as plt
import numpy as np

# Years for x-axis
years = np.arange(2010, 2021)

# Search interest for different languages (fictional data, % of total search interest)
python_interest = [10, 15, 20, 30, 40, 50, 60, 70, 75, 80, 85]
java_interest = [40, 38, 35, 33, 30, 28, 25, 23, 22, 20, 18]
javascript_interest = [20, 22, 25, 30, 35, 40, 45, 48, 50, 53, 55]
csharp_interest = [15, 17, 19, 17, 15, 14, 12, 11, 12, 13, 12]
ruby_interest = [15, 13, 11, 10, 9, 8, 7, 6, 6, 6, 5]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the line chart for each programming language
ax.plot(years, python_interest, marker='o', linestyle='-', color='blue', linewidth=2)
ax.plot(years, java_interest, marker='s', linestyle='-', color='green', linewidth=2)
ax.plot(years, javascript_interest, marker='^', linestyle='-', color='orange', linewidth=2)
ax.plot(years, csharp_interest, marker='d', linestyle='-', color='purple', linewidth=2)
ax.plot(years, ruby_interest, marker='x', linestyle='-', color='red', linewidth=2)

# Remove annotations, legend, title, and labels
ax.grid(True, linestyle='--', alpha=0.7)

# Ensuring x-tick labels are readable by rotating them
plt.xticks(years, rotation=45)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()