import matplotlib.pyplot as plt
import numpy as np

months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]

python_pop = np.array([35, 36, 37, 39, 38, 39, 40, 42, 43, 44, 45, 46])
js_pop = np.array([30, 29, 29, 30, 32, 31, 32, 33, 35, 36, 35, 34])
java_pop = np.array([15, 15, 16, 16, 17, 17, 17, 16, 15, 14, 14, 13])
rust_pop = np.array([5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 10])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(
    months, 
    python_pop, 
    js_pop, 
    java_pop, 
    rust_pop,
    colors=['#4daf4a'],  # Applying a single color consistently
    alpha=0.8
)

ax.set_title("Lang Pop in 2023", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Months", fontsize=14)
ax.set_ylabel("Pop (%)", fontsize=14)

plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)

plt.tight_layout()

plt.show()