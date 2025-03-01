
**Problem 7.11**  

A square loop is cut out of a thick sheet of aluminum. 

It is then placed so that the top portion is in a uniform magnetic field **B**, and is allowed to fall under gravity (Fig. 7.20). 

(In the diagram, shading indicates the field region; **B** points into the page.) 

If the magnetic field is **1 T** (a pretty standard laboratory field), find the **terminal velocity** of the loop (in m/s). 

Find the **velocity of the loop as a function of time**. 

How long does it take (in seconds) to reach, say, **90% of the terminal velocity**? 

What would happen if you cut a tiny slit in the ring, breaking the circuit?  

**[Note: The dimensions of the loop cancel out; determine the actual numbers, in the units indicated.]**

解：

$$
\mathcal{E} = vBl
$$

$$
i = \frac{vBl}{R}
$$

$$
F_{\text{磁}} = ilB = \frac{vB^2l^2}{R}
$$

$$
F = ma
$$

$$
mg-\frac{vB^2l^2}{R} = m \frac{dv}{dt}
$$

$$
\frac{dv}{dt} + \frac{B^2l^2}{mR}v = g
$$

令
$$
\frac{B^2l^2}{mR} = \frac{1}{\tau}
$$

$$
\frac{dv}{dt} + \frac{v}{\tau} = g
$$

$$
\tau\frac{dv}{dt} + v = g\tau
$$

$$
\tau\frac{dv}{dt} = g\tau - v
$$

$$
\frac{dv}{g\tau - v} =\frac{dt}{\tau}   
$$

$$
ln(v - g\tau) = \frac{-t}{\tau} + C
$$

$$
v - g\tau = A e^{-t/\tau }
$$

$$
v = g\tau  + A e^{-t/\tau }
$$

$v(0) =  g\tau  + A = 0$

$A = - g\tau$

$$
v(t) = g\tau\left[1 - e^{-t/\tau }\right]
$$

$$
v(t) = g\tau - g\tau e^{-t/\tau }
$$

$$
e^{-t/\tau } = 1 - \frac{v(t)}{g\tau}
$$

$$
-t/\tau=  ln \left[ 1 - \frac{v(t)}{g\tau} \right]
$$

$$
t=  -\tau \times ln \left[ 1 - \frac{v(t)}{g\tau} \right]
$$

把實際參數帶入，鋁的密度 $\rho = 2700\, kg/m^3$，$A$ 是迴路截面積，$l$ 方形的邊長

$$
m = 4\rho Al
$$

鋁的導電度 $\sigma = 3.5 \times 10^7\, S/m$

$$
R = \frac{4l}{\sigma A}
$$

$$
mR = 4\rho Al \frac{4l}{\sigma A} = \frac{16l^2\rho }{\sigma}
$$

$$
\tau = \frac{mR }{B^2l^2} = \frac{16l^2\rho}{B^2l^2\sigma} = \frac{16\rho}{B^2\sigma}
$$

$$
v(t)  = g\tau\left[1 - e^{-t/\tau }\right]
$$

$$
v(t) = \frac{16\rho g }{B^2\sigma}\left[ 1-  e^{-t/\frac{16\rho}{B^2\sigma}} \right]
$$

```python

import numpy as np
import matplotlib.pyplot as plt

# 參數設定（鋁的物性）
rho_al = 2700      # kg/m³
sigma_al = 3.5e7   # S/m
g = 9.81           # m/s²
B = 1.0            # T

# 計算時間常數
time_constant = ((16 * rho_al) /(B**2 * sigma_al) )

print(f"時間常數 = {time_constant:.4e} s")

# 計算終端速度
v_terminal = g*time_constant

print(f"終端速度 = {v_terminal:.4e} m/s")

def v(t):
    return v_terminal * (1 - np.exp(-t/time_constant))

# 計算達到90%終端速度的時間

def time_to_reach_velocity(v_t):
    return -time_constant* np.log(1 - v_t / (g * time_constant))

t_90 = time_to_reach_velocity(0.9*v_terminal)

print(f"達到終端速度90%所需要的時間為{t_90:.4e} s")


# 計算 t = 0 到 10倍時間常數的速度
t_values = np.linspace(0, 10*time_constant, 100)  # 100 個時間點
v_values = v(t_values)

# 繪製速度隨時間變化的圖

plt.plot(t_values, v_values, label=r'$v(t)$')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs. Time')
plt.legend()
plt.grid()
plt.show()

```

```
時間常數 = 1.2343e-03 s
終端速度 = 1.2108e-02 m/s
達到終端速度90%所需要的時間為2.8420e-03 s
```