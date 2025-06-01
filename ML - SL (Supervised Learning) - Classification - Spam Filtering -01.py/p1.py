import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([2,4,6,8])
ypoints=np.array([5,7,9,11])

plt.plot(xpoints,ypoints,label="Line Plot",color="g",marker="o")
plt.legend()
plt.title("Simple Graph")
plt.grid(True)
plt.show()
