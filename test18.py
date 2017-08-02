# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10,100)
y=np.sin(x)+1
z=np.cos(x**2)+1

plt.figure(figsize=(8,4))
plt.plot(x,y,label='$\sin x+1$',color='red',linewidth=20)
plt.plot(x,z,'b--',label='$\cos x^2+1$',color='green')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('A simple Example')
plt.ylim(0,2.2)
plt.legend()
plt.show()