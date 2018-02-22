from random import randint

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem, ttest_ind


# Generate
high_prices = [randint(1, 5) * 1000 for x in range(1, 10)]
high_means = np.mean(high_prices)
high_sem = sem(high_prices)

medium_prices = [randint(1, 5) * 500 for x in range(1, 10)]
medium_means = np.mean(medium_prices)
medium_sem = sem(medium_prices)

low_prices = [randint(1, 5) * 200 for x in range(1, 10)]
low_means = np.mean(low_prices)
low_sem = sem(low_prices)

means = [high_means, medium_means, low_means]
sems = [high_sem, medium_sem, low_sem]
labels = ["High Prices", "Medium Prices", "Low Prices"]

# Plot
fig, ax = plt.subplots()

ax.errorbar(np.arange(0, len(means)), means, yerr=sems, fmt="o")

ax.set_xlim(-0.5, 2.5)
ax.set_xticklabels(labels)
ax.set_xticks([0, 1, 2])

ax.set_ylabel("Mean House Price")

plt.show()

# t-test
(t_stat, p) = ttest_ind(high_prices, low_prices, equal_var=False)

if p < 0.05:
    print("The differences between the high and low prices are significant.")
else:
    print("The differences between high and low prices are due to chance.")
