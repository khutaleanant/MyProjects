import matplotlib
matplotlib.use('Agg') # this code is use for to save particular out put file in particular location.

# If only show the output then use following code

import matplotlib.pyplot as plt
import numpy as np

Data=np.random.randn(1000)
plt.hist(Data,bins=30,color="blue",edgecolor="black",alpha=0.7)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
# plt.show()

plt.savefig("Histogram.png")

