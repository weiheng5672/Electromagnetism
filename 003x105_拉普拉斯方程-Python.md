
---

## **Python 解拉普拉斯方程的步驟**
### **1. 離散化網格**
   - 把區域劃分成 $N \times N$ 的網格。
   - 內部點滿足拉普拉斯方程：
     $$
     V_{i,j} = \frac{V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1}}{4}
     $$
   - 邊界點設定為已知的固定值（Dirichlet 邊界條件）。

### **2. 迭代法求解**
   - 逐步更新每個內部點的值，直到結果收斂（變化量很小）。
   - 兩種常用方法：
     - **Jacobi 方法（同步更新）**：新值不影響本輪其他計算。
     - **Gauss-Seidel 方法（逐步更新）**：新值立即用於計算下一個點（收斂更快）。

### **3. 迭代停止條件**
   - 設定容差值 $\epsilon$，當所有點的變化量小於 $\epsilon$ 時停止。

---

## **Python 程式碼**
這裡使用 **NumPy** 來處理矩陣運算，並用 **Matplotlib** 來視覺化結果。

```python
import numpy as np
import matplotlib.pyplot as plt

# 參數設置
N = 50  # 網格大小 (50x50)
max_iter = 1000  # 最大迭代次數
tolerance = 1e-4  # 收斂條件

# 創建 NxN 網格，初始值為 0
V = np.zeros((N, N))

# 設定邊界條件
x = np.linspace(0, np.pi, N)
V[0, :] = np.sin(x)  # 頂部邊界值 sin(x), x從0到pi
V[-1, :] = 0  # 底部邊界值 0
V[:, 0] = 0  # 左邊界值 0
V[:, -1] = 0  # 右邊界值 0

# 迭代計算 (Jacobi Method)
for iteration in range(max_iter):
    V_new = V.copy()  # 創建副本來存放新值
    for i in range(1, N-1):
        for j in range(1, N-1):
            V_new[i, j] = (V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1]) / 4
    
    # 檢查是否收斂
    if np.max(np.abs(V_new - V)) < tolerance:
        print(f"收斂於 {iteration} 次迭代")
        break
    V = V_new  # 更新網格值

# 生成 3D 圖形
x = np.linspace(0, N-1, N)
y = np.linspace(0, N-1, N)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V, cmap='coolwarm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential V')
ax.set_title("Laplace's Equation Solution (3D)")
plt.show()

```

---

## **程式碼解釋**
1. **建立數值網格**
   - `V = np.zeros((N, N))` 建立一個 $N \times N$ 的零矩陣作為初始值。
   - 設定邊界條件，例如頂部固定為 1，其他邊界為 0。

2. **迭代更新**
   - 每個內部點更新為 **周圍四個點的平均值**。
   - `V_new = V.copy()` 確保本輪計算不影響原值（Jacobi 方法）。

3. **檢查收斂**
   - 如果所有點的變化量 **小於容差值**，則結束迭代。

4. **視覺化**
   - 數值解繪製為 3D 表面圖，其中 X 和 Y 是網格座標，而 V 是電位高度。

---

## **優化與變體**
1. **改用 Gauss-Seidel 方法（更快收斂）**
   - 直接更新 `V[i, j]` 而非 `V_new[i, j]`。
   - 不需要 `V.copy()`，但會影響並行計算能力。

2. **使用 NumPy 向量化提高效能**
   - 用 `V[1:-1, 1:-1] = (V[:-2, 1:-1] + V[2:, 1:-1] + V[1:-1, :-2] + V[1:-1, 2:]) / 4` 取代 for 迴圈。

3. **考慮 Neumann 邊界條件（導數為 0）**
   - 在某些物理問題中，邊界的斜率為零，而不是固定值。

