import numpy as np
import matplotlib.pyplot as plt
import glob
import os

dir_path = os.path.abspath(os.getcwd())
txt_path = glob.glob('data/*.txt')                          # getting path of all data
txt_path = [dir_path + '\\' + txt for txt in txt_path]


data = np.genfromtxt(txt_path[0], dtype=float)
X = data[:,0:1]
Y0 = data[:,1:2]    # parse data
Y1 =data[:,2:3]
Y2 =data[:,3:4]
plt.plot(X, Y0, label="2. Column")
plt.plot(X, Y1, label="3. Column")  #plotting
plt.plot(X, Y2, label="4. Column")
plt.legend(loc="upper left")
plt.grid(linestyle='-')
plt.show()

for index in range(1, 6):
    data = np.genfromtxt(txt_path[index], dtype=float)
    X = data[:, 1:]
    Y = data[:, 0:1]
    plt.plot(X, Y, label=str(index + 1) + ".txt")
plt.grid(linestyle='-')
plt.legend(loc="upper left")
plt.show()