import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arr = [8, 8, 12, 24, 54, 54, 75, 78, 98, 102, 132]
x_xis = np.arange(0, len(arr), 1)
# Calculate the indices for the lower and upper quartiles

# Retrieve the lower and upper quartiles

# Calculate the interquartile range

# Create axes for the included and excluded data

# Create a plot displaying included and excluded data

# Report descriptions of the data
lower_quartile_index = (len(arr) + 1) // 4
upper_quartile_index = 3 * len(arr) // 4
lower_quartile = arr[lower_quartile_index]
upper_quartile = arr[upper_quartile_index]

iqr = upper_quartile - lower_quartile

included = arr[lower_quartile_index:upper_quartile_index]
included_axis = np.arange(lower_quartile_index, upper_quartile_index)

excluded_low = arr[0:lower_quartile_index]
low_axis = np.arange(0, len(excluded_low), 1)

excluded_high = arr[upper_quartile_index:len(arr)]
high_axis = np.arange(len(included) + len(excluded_high), len(arr), 1)


fig, ax = plt.subplots()
fig.suptitle("IQR example", fontsize=16, fontweight="bold")

ax.plot(included_axis, included, marker='o', color='b', label="IQR")
ax.scatter(low_axis, excluded_low, marker='o',
           color='r', label="Excluded (Low)")
ax.scatter(high_axis, excluded_high, marker='o',
           color='r', label="Excluded (High)")

plt.legend(loc="upper left", fancybox=True)
plt.show()
