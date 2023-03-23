from matplotlib import pyplot as plt
import numpy as np

N = 1000000
x = np.random.uniform(low = 0, high = 14, size = int(N/6))
y = np.random.normal(20,3,int(N))

z = np.concatenate((x,y))

plt.tick_params(labelleft=False, left=False)
plt.tick_params(labelbottom=False, bottom=False)
plt.hist(z, bins = 100, density = True, histtype = 'step',  label = 'signal', color = 'black')
plt.vlines(x = 22, ymin = -0.01, ymax = 0.15, colors = 'black', linestyle = '--', label = "threshold")
plt.xlabel("signal pulse height [mV]")
plt.ylabel("Signal distribution proability [noise + signal]")
plt.legend()
plt.savefig('distribution.pdf')
plt.show()
