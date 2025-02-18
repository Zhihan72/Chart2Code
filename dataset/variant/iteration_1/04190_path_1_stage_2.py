import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

python_popularity = np.array([35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
javascript_popularity = np.array([40, 42, 44, 46, 48, 50, 52, 55, 57, 59, 62])
java_popularity = np.array([50, 52, 54, 56, 58, 59, 60, 61, 62, 63, 64])
csharp_popularity = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])
ruby_popularity = np.array([20, 22, 24, 26, 28, 30, 32, 34, 35, 36, 38])

fig, axes = plt.subplots(2, 1, figsize=(12, 10))

axes[0].plot(years, python_popularity, color='#FF5733', marker='o', linestyle='-', linewidth=2)
axes[0].plot(years, javascript_popularity, color='#33FF57', marker='s', linestyle='--', linewidth=2)
axes[0].plot(years, java_popularity, color='#3357FF', marker='^', linestyle='-.', linewidth=2)
axes[0].plot(years, csharp_popularity, color='#F7DC6F', marker='D', linestyle=':', linewidth=2)
axes[0].plot(years, ruby_popularity, color='#AF7AC5', marker='*', linestyle='-', linewidth=2)

axes[0].set_title('Popularity Trends of Various Programming Languages (2010-2020)', fontsize=16, fontweight='bold')
axes[0].set_xlabel('Year', fontsize=12)
axes[0].set_ylabel('Popularity Index', fontsize=12)

python_diff = np.diff(python_popularity, prepend=python_popularity[0])
javascript_diff = np.diff(javascript_popularity, prepend=javascript_popularity[0])
java_diff = np.diff(java_popularity, prepend=java_popularity[0])
csharp_diff = np.diff(csharp_popularity, prepend=csharp_popularity[0])
ruby_diff = np.diff(ruby_popularity, prepend=ruby_popularity[0])

axes[1].bar(years, python_diff, color='#FF5733', alpha=0.6)
axes[1].bar(years, javascript_diff, color='#33FF57', alpha=0.6, bottom=python_diff)
axes[1].bar(years, java_diff, color='#3357FF', alpha=0.6, bottom=python_diff + javascript_diff)
axes[1].bar(years, csharp_diff, color='#F7DC6F', alpha=0.6, bottom=python_diff + javascript_diff + java_diff)
axes[1].bar(years, ruby_diff, color='#AF7AC5', alpha=0.6, bottom=python_diff + javascript_diff + java_diff + csharp_diff)

axes[1].set_title('Year-On-Year Changes in Popularity Index (2010-2020)', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Year', fontsize=12)
axes[1].set_ylabel('Change in Popularity Index', fontsize=12)

plt.tight_layout()
plt.show()