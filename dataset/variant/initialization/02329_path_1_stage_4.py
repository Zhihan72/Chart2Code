import matplotlib.pyplot as plt
import numpy as np

decad3s = ['1980', '1990', '2000', '2010', '2020']
coal_fp = [50, 45, 40, 30, 20]
natGas = [20, 20, 25, 30, 25]
hydropower = [15, 12, 10, 10, 10]
re_newables = [5, 8, 5, 10, 30]

data = np.array([coal_fp, natGas, hydropower, re_newables])

plt.figure(figsize=(12, 8))
plt.stackplot(decad3s, coal_fp, natGas, hydropower, re_newables,
              colors=['#FF6347', '#9ACD32', '#DAA520', '#40E0D0'], 
              alpha=0.8)

plt.xlabel('Era', fontsize=12)
plt.ylabel('Share (%)', fontsize=12)

plt.title('Energy Source Mix Over Time', fontsize=14)

plt.show()