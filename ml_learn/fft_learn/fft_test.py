#%%
# test jupyter notebook extenstion
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 


#%%
# test fft
from scipy.fftpack import fft
# Number of sample points
N = 600
# sample spacing, period
T = 1.0/800.0
# time axis, period*Number = end time
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0*2.0*np.pi*x) + 0.5*np.sin(80.0*2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1/(2.0*T), N//2)
plt.plot(xf, 2.0/N*np.abs(yf[0:N//2]))
plt.grid()
plt.show()

#%%
# show raw data
path = "./fft_learn/data.txt"
file = open(path, "r")
data_list = list()
str_val = file.readline()
while len(str_val):
    data_list.append(float(str_val))
    str_val = file.readline()
file.close()
y = np.array(data_list)
x = np.linspace(0, len(data_list), len(data_list))
plt.plot(x, y)
plt.grid()
plt.show()

#%%
# fft transfer
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
path = "./fft_learn/data.txt"
file = open(path, "r")
data_list = list()
str_val = file.readline()
while len(str_val):
    data_list.append(float(str_val))
    str_val = file.readline()
file.close()
y = np.array(data_list)
N = len(data_list)
T = 1/25600
d = 100
xf = np.linspace(0.0, 1/(d*T), N//d)
yf = fft(y)
plt.plot(xf, 2.0/N*np.abs(yf[0:N//d]))
plt.grid()
plt.show()
