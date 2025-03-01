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
