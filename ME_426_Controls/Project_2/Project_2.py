import numpy as np
import matplotlib.pyplot as plt
import control as ctl

plt.close("all")

ydata = [0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
0,
4.55,
0,
0,
0,
5.44,
4.73,
0,
6.31,
4.68,
5.06,
5.22,
0,
0,
5.37,
5.1,
5.41,
5.59,
0,
5.48,
5.48,
5.94,
5.59,
0,
6.98,
4.59,
4.55,
5.52,
4.73,
6.31,
5.06,
5.29,
6.34,
5.63,
5.33,
0,
5.37,
4.98,
6.34,
4.77,
5.22,
4.81,
5.63,
5.41,
5.77,
5.41,
7.51,
0,
5.98,
5.1,
5.06,
0,
4.81,
6.89,
6.43,
6.59,
6.08,
5.77,
5.14,
5.06,
0,
0,
5.7,
6.8,
5.8,
5.06,
5.14,
4.55,
4.59,
4.73,
4.89,
5.22,
5.7,
5.25,
0,
6.21,
4.64,
6.59,
0,
5.41,
5.02,
5.73,
4.81,
0,
5.18,
5.41,
5.06,
5.66,
0,
5.7,
7.01,
6.92,
5.66,
5.25,
6.31,
7.51,
5.66,
6.18,
5.44,
6.04,
5.91,
5.63,
6.08,
6.4,
5.22,
5.66,
6.37,
7.07,
5.25,
0,
5.8,
0,
4.89,
5.02,
5.22,
4.85,
5.52,
6.4,
5.98,
6.11,
6.18,
7.12,
7.72,
6.92,
5.91]

xdata = np.asarray([0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
46,
47,
48,
49,
50,
51,
52,
53,
54,
55,
56,
57,
58,
59,
60,
61,
62,
63,
64,
65,
66,
67,
68,
69,
70,
71,
72,
73,
74,
75,
76,
77,
78,
79,
80,
81,
82,
83,
84,
85,
86,
87,
88,
89,
90,
91,
92,
93,
94,
95,
96,
97,
98,
99,
100,
101,
102,
103,
104,
105,
106,
107,
108,
109,
110,
111,
112,
113,
114,
115,
116,
117,
118,
119,
120,
121,
122,
123,
124,
125,
126,
127,
128,
129,
130,
131,
132,
133,
134,
135,
136,
137])


plt.plot(xdata,ydata,'b*',label='Experimental Data')

tau = 10.0

sig = 1.0/tau

G = ctl.tf([6*sig],[1,sig])

time = np.linspace(0,200,100)

time,yout = ctl.step_response(G,time)

plt.plot(time,yout)

plt.xlabel('Time (sec)')
plt.ylabel('Measured Windspeed (m/s)')
plt.legend()
plt.grid()
plt.show()