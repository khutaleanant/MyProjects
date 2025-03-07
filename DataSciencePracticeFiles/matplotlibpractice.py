'''
import matplotlib
matplotlib.use("Agg")
'''
import matplotlib.pyplot as plt
import numpy as np

Xpoints=np.array([2,4])
Ypoints=np.array([7,9])

plt.plot(Xpoints,Ypoints,label="LinePlot",color="r",marker="o")
plt.legend()
plt.grid(True)
plt.title("Graph")

plt.show()
'''
plt.savefig("Graph1.jpeg")
'''
