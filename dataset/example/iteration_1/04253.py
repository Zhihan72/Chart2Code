import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart shows the monthly temperature trends for three fictional cities (Alpha, Bravo, and Charlie) over the span of a year. The cities experience diverse climates with different seasonal temperature variations.

# Months and corresponding temperature data for each city
months = np.arange(1, 13)
city_alpha_temp = np.array([30, 32, 35, 40, 45, 50, 55, 54, 48, 42, 35, 31])  # City Alpha: Hot summers, mild winters
city_bravo_temp = np.array([20, 25, 30, 40, 50, 60, 65, 64, 55, 45, 30, 22])  # City Bravo: Warm summers, cold winters
city_charlie_temp = np.array([10, 15, 20, 25, 30, 35, 40, 38, 32, 26, 20, 15]) # City Charlie: Cool climate

# Plot
plt.figure(figsize=(14, 8))

# Plot the line charts for each city
plt.plot(months, city_alpha_temp, label='City Alpha', marker='o', color='coral', linewidth=2)
plt.plot(months, city_bravo_temp, label='City Bravo', marker='s', color='dodgerblue', linewidth=2)
plt.plot(months, city_charlie_temp, label='City Charlie', marker='^', color='limegreen', linewidth=2)

# Enhance readability with grid
plt.grid(True, linestyle='--', alpha=0.5)

# Set titles and labels
plt.title("Monthly Temperature Trends for Fictional Cities: Alpha, Bravo, and Charlie\n(Comparison Over One Year)", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)

# Annotate specific data points for further insights
plt.annotate('Peak Summer in City Alpha', xy=(6, city_alpha_temp[5]), xytext=(7, 55),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, fontweight='bold')

plt.annotate('Cold Winter in City Bravo', xy=(12, city_bravo_temp[11]), xytext=(10, 20),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, fontweight='bold')

plt.annotate('Steady Climate in City Charlie', xy=(8, city_charlie_temp[7]), xytext=(9, 38),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, fontweight='bold')

# Set limits for y-axis to ensure the data points are well within the frame
plt.ylim(0, 70)
plt.xlim(1, 12)

# Set the x-ticks to display months correctly
plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Include a legend to clarify plot elements
plt.legend(loc='upper right', fontsize=12)

# Optimize layout to avoid clipping of text and labels
plt.tight_layout()

# Display the plot
plt.show()