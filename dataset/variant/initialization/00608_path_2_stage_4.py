import matplotlib.pyplot as plt
import numpy as np

# Altering textual content for this task
months = [
    'Ja', 'Febr', 'Mrch', 'Ap', 'Ma', 'Jn',
    'Jly', 'Agt', 'Septr', 'Octbr', 'Nv', 'Decrm'
]

# Manually shuffled popularity values while maintaining the same dimensional structure
python_popularity = np.array([37, 36, 35, 39, 38, 40, 39, 42, 44, 43, 46, 45])
javascript_popularity = np.array([29, 30, 29, 30, 31, 32, 32, 35, 33, 36, 34, 35])
java_popularity = np.array([16, 15, 16, 17, 15, 17, 17, 16, 14, 15, 13, 14])
csharp_popularity = np.array([10, 9, 10, 10, 8, 9, 10, 11, 10, 12, 14, 13])
rust_popularity = np.array([6, 5, 6, 7, 6, 7, 7, 8, 7, 9, 8, 10])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(
    months, 
    python_popularity, 
    javascript_popularity, 
    java_popularity, 
    csharp_popularity, 
    rust_popularity, 
    labels=['Pythn', 'JS', 'Jv', 'C-Shrp', 'Rustlng'],
    colors=['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00', '#6a3d9a'],
    alpha=0.8
)

ax.set_title("Unpredictable Swells:\nLanguage Fame in '23", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Month Timeframes", fontsize=14)
ax.set_ylabel("Admiration Share (%)", fontsize=14)

ax.grid(True, linestyle='-.', alpha=0.6)
ax.legend(loc='lower right', fontsize=12)
plt.xticks(rotation=45, fontsize=10, style='italic')
plt.yticks(fontsize=10, style='italic')
plt.tight_layout()

plt.gcf().set_facecolor('#f5f5f5')
plt.show()