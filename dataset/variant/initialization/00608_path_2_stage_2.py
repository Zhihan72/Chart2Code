import matplotlib.pyplot as plt
import numpy as np

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

python_popularity = np.array([35, 36, 37, 39, 38, 39, 40, 42, 43, 44, 45, 46])
javascript_popularity = np.array([30, 29, 29, 30, 32, 31, 32, 33, 35, 36, 35, 34])
java_popularity = np.array([15, 15, 16, 16, 17, 17, 17, 16, 15, 14, 14, 13])
csharp_popularity = np.array([10, 10, 10, 9, 8, 9, 10, 10, 11, 12, 13, 14])
rust_popularity = np.array([5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 10])

fig, ax = plt.subplots(figsize=(12, 8))

# Changed colors to a new set of colors
ax.stackplot(
    months, 
    python_popularity, 
    javascript_popularity, 
    java_popularity, 
    csharp_popularity, 
    rust_popularity, 
    labels=['Python', 'JavaScript', 'Java', 'C#', 'Rust'],
    colors=['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a'],
    alpha=0.8
)

ax.set_title("Rising Tides:\nProgramming Language Popularity in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Popularity (%)", fontsize=14)

ax.grid(True, linestyle='-.', alpha=0.6)
ax.legend(loc='lower right', fontsize=12)
plt.xticks(rotation=45, fontsize=10, style='italic')
plt.yticks(fontsize=10, style='italic')
plt.tight_layout()

plt.gcf().set_facecolor('#f5f5f5')
plt.show()