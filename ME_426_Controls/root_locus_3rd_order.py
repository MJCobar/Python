import control as ctl
import numpy as np
import matplotlib.pyplot as plt

plt.grid()
tout = np.linspace(0,50,1000)
for k in range(0,1000):
    den = [1,10,0,k]
    s = np.roots(den)
    plt.plot(np.real(s),np.imag(s),'b*')
    #print(s)
    print(k)
    G = ctl.tf([k],den)
    tout,yout = ctl.step_response(G,tout)
    print(G)
    #plt.plot(tout,yout)
    plt.pause(0.1)
    #plt.show()