import matplotlib.pyplot as plt
import numpy as np

libraries = np.array([5, 10, 15, 20, 25])
literacy_rates = np.array([60, 65, 70, 75, 78])

fig, ax = plt.subplots(figsize=(12, 8))

scatter = ax.scatter(libraries, literacy_rates, color='royalblue', edgecolor='black', s=150, alpha=0.6)

def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

params = np.polyfit(libraries, literacy_rates, 2, full=False, cov=False)
x_smooth = np.linspace(min(libraries), max(libraries), 300)
y_smooth = quadratic(x_smooth, *params)

ax.plot(x_smooth, y_smooth, linestyle='--', color='orange', linewidth=2)

plt.title('Impact of Community Libraries on Literacy Rates\nAn Insightful Look at District-wise Data', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Number of Community Libraries', fontsize=14)
plt.ylabel('Literacy Rates (%)', fontsize=14)

highlight_libraries = [10, 25]
highlight_labels = ['Small Town A', 'Old Town']
for lib, label in zip(highlight_libraries, highlight_labels):
    index = np.where(libraries == lib)[0][0]
    ax.annotate(label, (libraries[index], literacy_rates[index]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=10, arrowprops=dict(arrowstyle='->', color='gray'))

plt.tight_layout()

plt.show()