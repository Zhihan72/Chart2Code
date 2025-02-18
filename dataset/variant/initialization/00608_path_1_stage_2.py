import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

# Popularity percentages
python_pop = np.array([35, 36, 37, 39, 38, 39, 40, 42, 43, 44, 45, 46])
js_pop = np.array([30, 29, 29, 30, 32, 31, 32, 33, 35, 36, 35, 34])
java_pop = np.array([15, 15, 16, 16, 17, 17, 17, 16, 15, 14, 14, 13])
cs_pop = np.array([10, 10, 10, 9, 8, 9, 10, 10, 11, 12, 13, 14])
rust_pop = np.array([5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 10])

# Create plot
fig, ax = plt.subplots(figsize=(12, 8))

# Stack plot
ax.stackplot(
    months, 
    python_pop, 
    js_pop, 
    java_pop, 
    cs_pop, 
    rust_pop, 
    colors=['#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#e41a1c'],
    alpha=0.8
)

# Set titles and labels
ax.set_title("Lang Pop in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Pop (%)", fontsize=14)

# Adjust ticks
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

# Optimize layout
plt.tight_layout()

# Show plot
plt.show()