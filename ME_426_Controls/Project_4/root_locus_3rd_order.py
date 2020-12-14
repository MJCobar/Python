import control as ctl
import numpy as np
import matplotlib.pyplot as plt

plt.grid()
tout = np.linspace(0,50,1000)
for k_1,k_2 in zip(range(49,50),range(49,50)):
    den = [1,3.51,(0.878+0.25*k_2),(0.0547+0.109*k_2+0.25*k_1),0.109*k_1]
    s = np.roots(den)
    plt.plot(np.real(s),np.imag(s),'b*')
    #print(s)
    print(k_1)
    print(k_2)
    G = ctl.tf([0.25*k_1,0.109*k_1],den)
    tout,yout = ctl.step_response(G,tout)
    #print(G)
    #plt.plot(tout,yout)
    plt.pause(0.1)